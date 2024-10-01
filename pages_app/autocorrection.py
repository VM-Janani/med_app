import streamlit as st
import nltk
from nltk.corpus import words

# Download NLTK data (ensure this is only done once)
nltk.download('words', quiet=True)
word_list = set(words.words())

# Minimum Edit Distance function
def min_edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                cost = 0
            else:
                cost = 2  # substitution cost
            dp[i][j] = min(dp[i-1][j] + 1,  # deletion
                           dp[i][j-1] + 1,  # insertion
                           dp[i-1][j-1] + cost)  # substitution
    return dp[n][m]

# Function to find the top N closest words
def get_closest_words(input_word, num_suggestions=5):
    suggestions = []
    for word in word_list:
        dist = min_edit_distance(input_word.lower(), word.lower())
        suggestions.append((word, dist))
    
    # Sort the suggestions based on distance and return top N
    suggestions = sorted(suggestions, key=lambda x: x[1])
    return suggestions[:num_suggestions]

# Main function to run the Streamlit app
def main():
    st.title("Autocorrect with Suggestions")
    st.write("Enter a word to get suggested corrections with Minimum Edit Distance:")

    user_input = st.text_input("Enter a word:")

    if user_input:
        num_suggestions = st.slider("Select number of suggestions:", 1, 10, 5)
        suggestions = get_closest_words(user_input, num_suggestions)

        st.write(f"Here are the top {num_suggestions} suggestions for the word '{user_input}':")

        for i, (word, distance) in enumerate(suggestions):
            st.write(f"{i+1}. **{word}** (Edit Distance: {distance})")

    # Footer
    st.write("Our keyboard autocorrection and suggestions are powered by a process similar to the Minimum Edit Distance algorithm. It calculates the minimal changes (insertions, deletions, or substitutions) needed to turn your input into a valid word, offering quick, smart suggestions!")

# Call the main function
if __name__ == "__main__":
    main()
