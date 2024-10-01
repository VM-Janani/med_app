import streamlit as st

def main():
    st.title("📚Dive into Minimum Edit Distance (MED)")

    st.header("🌟 What is Minimum Edit Distance (MED)?")
    st.write(
        "Minimum Edit Distance (MED), also known as Levenshtein Distance, is a measure of how different two strings are by counting the minimum number of edits needed to convert one string into another. These edits can be insertions, deletions, or substitutions. MED is widely used in text processing for tasks like spell checking and text correction. 📝"
    )

    st.header("🔍 Example: MED Calculation for 'sitting' vs 'kitten'")
    st.write(
        "Let's explore how MED helps us find the distance between 'sitting' and 'kitten'."
    )

    st.write(
        "### Steps to Calculate MED 🔢"
    )
    st.write(
        "1. **Initialize the Matrix**: Create a matrix where each cell (i, j) represents the cost to transform the first i characters of 'sitting' into the first j characters of 'kitten'. Initialize the matrix with insertion and deletion costs."
    )
    st.write(
        "2. **Fill the Matrix**: Compute the cost for each operation (insertion, deletion, substitution) and update the matrix."
    )
    st.write(
        "3. **Find the Minimum Distance**: The value in the bottom-right cell of the matrix represents the minimum edit distance between 'sitting' and 'kitten'. 🎯"
    )

    st.header("📈 Detailed Calculation")
    st.write(
        "Let's break down the calculation step-by-step for transforming 'sitting' into 'kitten' with a **substitution cost of 1**."
    )

    st.write(
        "1. **Initialize Costs**: Set up the initial values for deletions and insertions."
    )
    st.write(
        "   - **Deletion**: The cost to delete a character. For example, deleting the first character of 'sitting' has a cost of 1."
    )
    st.write(
        "   - **Insertion**: The cost to insert a character to match 'kitten' costs 1."
    )
    
    st.write(
        "2. **Matrix Setup**: Create a matrix to represent the costs of transforming substrings of 'sitting' into substrings of 'kitten'."
    )

    st.write(
        "3. **Fill the Matrix**: Update the matrix with costs for substitutions, insertions, and deletions."
    )
    st.write(
        "   - **Substitution (cost 1)**: When characters differ, we apply a substitution cost of 1. changing 's' to 'k' has a cost of 1."
    )
    st.write(
        "   - **Substitution (cost 1)**: Now we change 'i' to 'e' has a cost of 1."
    )
    st.write(
        "   - **Deletion (cost 1)**: Now we have changed 'sitting' to 'kitting'.The final step is to remove 'g' so we perform deletion operation of cost 1. "
    )
    st.write(
        "   - **Update Matrix**: Compute the minimum cost for each cell based on whether we delete, insert, or substitute a character."
    )
    st.write(
        "4. **Result**: The final cell (bottom-right) gives the minimum edit distance. For 'sitting' to 'kitten', the MED is 3."
    )
    st.write("### Formula:")
    st.latex(r"D[i,j] = \min(D[i-1,j] + 1, D[i,j-1] + 1, D[i-1,j-1] + \text{sub-cost})")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("pages/images/med_matrix.jpg", caption="MED Matrix: Transforming 'sitting' to 'kitten'", width=300)

    st.header("🧠 Levenshtein Distance & Substitution Costs")
    st.write(
        "Levenshtein Distance is a specialized version of MED that measures how many edits are needed to transform one string into another. The substitution cost can vary depending on the application."
    )

    st.subheader("✅ Substitution Cost of 1")
    st.write(
        "In many cases, we use a substitution cost of 1, which is ideal for simple edits like fixing typos or minor errors. This makes sense for small changes that don't drastically alter the meaning."
    )
    st.write(
        "Example: Changing 'cat' to 'bat' (substitution of 'c' with 'b') is assigned a cost of 1 because it's a minor change. 🐱➡️🐶"
    )

    st.subheader("⚙️ Substitution Cost of 2")
    st.write(
        "Sometimes, a substitution cost of 2 is used when the change is more impactful or less common. This can help differentiate between minor typos and significant errors or differences."
    )
    st.write(
        "Example: Changing 'cat' to 'dog' (substitution of two different letters) could be given a cost of 2 if the changes are considered more substantial. 🐱➡️🐶"
    )

if __name__ == "__main__":
    main()
