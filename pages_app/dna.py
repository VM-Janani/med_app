import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to calculate MED and return the matrix
def calculate_med_matrix(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    matrix = np.zeros((n + 1, m + 1), dtype=int)

    # Initialize the matrix
    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j

    # Fill the matrix with MED values
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,  # Deletion
                matrix[i][j - 1] + 1,  # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    return matrix

# Function to visualize the MED matrix
def visualize_med_matrix(seq1, seq2, matrix):
    fig, ax = plt.subplots()
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
    ax.set_xlabel(f"Sequence 2: {seq2}")
    ax.set_ylabel(f"Sequence 1: {seq1}")
    st.pyplot(fig)

# Load dataset function
def load_dna_dataset():
    # Load DNA sequences from the Kaggle dataset
    url = "https://raw.githubusercontent.com/VM-Janani/med_app/refs/heads/main/pages_app/images/NonPromoterSequence.csv"  # Update with the correct path to your dataset
    return pd.read_csv(url, delimiter=',')

# Streamlit app layout
def dna_sequencing_visualization():
    st.title("🧬 DNA Sequencing with Minimum Edit Distance")

    # Introduction
    st.header("🔍 Understanding DNA Sequencing and MED")
    st.write(
        "DNA sequencing determines the order of nucleotides in a DNA molecule. "
        "While Minimum Edit Distance (MED) is a foundational concept in string matching, "
        "real-world DNA sequencing techniques utilize more sophisticated algorithms that build upon MED. "
        "MED helps in understanding sequence comparison but is not directly used in actual sequencing tasks."
    )

    # Load the DNA dataset
    st.header("📂 DNA Sequences Dataset")
    dataset = load_dna_dataset()

    # Display a preview of the dataset
    st.write("Here's a preview of the DNA sequences dataset:")
    st.dataframe(dataset.head())

    # Let users select two sequences to compare
    st.header("🔍 Compare DNA Sequences Using MED")
    seq1 = st.selectbox("Select Sequence 1", dataset["Sequence"].values)
    seq2 = st.selectbox("Select Sequence 2", dataset["Sequence"].values)

    # Button to calculate MED
    if st.button("Calculate MED and Visualize"):
        med_matrix = calculate_med_matrix(seq1, seq2)
        st.write(f"Minimum Edit Distance (MED) between the two sequences is: {med_matrix[-1][-1]}")

        # Visualize the MED matrix
        st.header("📊 MED Matrix Visualization")
        visualize_med_matrix(seq1, seq2, med_matrix)

    # Additional explanation
    st.write(
        "In advanced bioinformatics, methods like Needleman-Wunsch and Smith-Waterman build upon the concepts of MED. "
        "These methods introduce penalties for gaps and mismatches to enhance the biological relevance of the alignments."
    )

def main():
    dna_sequencing_visualization()

if __name__ == "__main__":
    main()
