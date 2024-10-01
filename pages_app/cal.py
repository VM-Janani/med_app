import streamlit as st

# Minimum Edit Distance function with step-by-step explanation of operations
def min_edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    operations = [["" for _ in range(m+1)] for _ in range(n+1)]  # To store operations

    # Initialize matrix and operations
    for i in range(1, n+1):
        dp[i][0] = i
        operations[i][0] = f"Delete '{word1[i-1]}'"
    for j in range(1, m+1):
        dp[0][j] = j
        operations[0][j] = f"Insert '{word2[j-1]}'"

    # Fill the matrix with costs and track operations
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                cost = 0
                operations[i][j] = "No change"
            else:
                cost = 1  # Substitution cost

            deletion = dp[i-1][j] + 1  # Deletion cost
            insertion = dp[i][j-1] + 1  # Insertion cost
            substitution = dp[i-1][j-1] + cost  # Substitution cost

            dp[i][j] = min(deletion, insertion, substitution)

            # Track the operation performed
            if dp[i][j] == deletion:
                operations[i][j] = f"Delete '{word1[i-1]}'"
            elif dp[i][j] == insertion:
                operations[i][j] = f"Insert '{word2[j-1]}'"
            else:
                operations[i][j] = f"Substitute '{word1[i-1]}' with '{word2[j-1]}'"

    return dp, operations, dp[n][m]

# Displaying the matrix and operations as a grid
def display_matrix(matrix, operations, word1, word2):
    st.write(f"Edit Distance Matrix and Operations for '{word1}' and '{word2}':")
    
    # Display matrix with edit distances
    st.subheader("Edit Distance Matrix")
    table = f"|   | {' | '.join(list(word2))} |\n|---|" + "---|" * len(word2) + "\n"
    for i in range(len(matrix)):
        row = '| ' + (word1[i-1] if i > 0 else ' ') + ' | ' + ' | '.join(map(str, matrix[i])) + ' |\n'
        table += row
    st.markdown(f"```\n{table}\n```")

    # Display operations matrix
    st.subheader("Operations Matrix")
    ops_table = f"|   | {' | '.join(list(word2))} |\n|---|" + "---|" * len(word2) + "\n"
    for i in range(len(operations)):
        row = '| ' + (word1[i-1] if i > 0 else ' ') + ' | ' + ' | '.join(operations[i]) + ' |\n'
        ops_table += row
    st.markdown(f"```\n{ops_table}\n```")

# Streamlit app
def main():
    st.title("📊 MED Calculation Page with Operations")

    st.write(
        "This page allows you to see how the Minimum Edit Distance (MED) algorithm calculates the edit distance between two words. "
        "You can enter two words and view the calculation steps, including which operations (insertion, deletion, substitution) were performed."
    )

    # User inputs
    word1 = st.text_input("Enter the first word:")
    word2 = st.text_input("Enter the second word:")

    if word1 and word2:
    
        matrix, operations, distance = min_edit_distance(word1, word2)

        st.write(f"Minimum Edit Distance between **'{word1}'** and **'{word2}'**: **{distance}** ✨")
        display_matrix(matrix, operations, word1, word2)

        st.write(
            "The edit distance matrix shows the costs of transforming substrings of the first word into substrings of the second word. "
            "The operations matrix shows the actual steps (insertion, deletion, substitution) taken at each stage."
        )

if __name__ == "__main__":
    main()
