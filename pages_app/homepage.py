import streamlit as st

# from pages.learning import main as learning_main
# from pages.cal import main as calculation_main
# from pages.autocorrection import main as auto_main

def main():
    st.title("🌟 Welcome to the Minimum Edit Distance (MED) 🌟")

    st.header("What is Minimum Edit Distance (MED)? 🤔")
    st.write(
        "Minimum Edit Distance (MED), also known as Levenshtein Distance, measures the minimum number of single-character edits (insertions, deletions, or substitutions) needed to transform one string into another. It's a crucial concept in text processing and helps in tasks like spell checking and DNA sequencing."
    )

    st.header("Why is MED Important? 💡")
    st.write(
        "1. **Autocorrection**: MED helps correct misspelled words by suggesting the closest match from a dictionary. ✍️"
    )
    st.write(
        "2. **DNA Sequencing**: MED is used to compare DNA sequences, helping in genetic research and identifying mutations. 🧬"
    )
    st.write(
        "3. **Spell Checking**: It assists in identifying and fixing spelling errors in texts and documents. 📖"
    )
    st.write(
        "4. **Fuzzy Matching**: MED is useful for finding similar records in databases, even if there are minor differences. 🔍"
    )

    st.header("Explore the App 🧭")
    st.write(
        "This web app offers several interactive pages to help you understand and use MED effectively. Navigate through the following sections:"
    )
    st.write(
        "- **Autocorrection**: Discover how MED is used to correct spelling mistakes. ✨"
    )
    st.write(
        "- **Calculation**: Dive into the details of MED calculation and see it in action. 🔢"
    )

    st.write("👉 Explore the pages from the navigation menu above and enjoy learning about MED!")

# Call the main function
if __name__ == "__main__":
    main()