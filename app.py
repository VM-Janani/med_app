import streamlit as st
from pages_app.homepage import main as home_main
from pages_app.learning import main as learning_main
from pages_app.cal import main as calculation_main
from pages_app.autocorrection import main as auto_main


# Create a sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ("Home", "Learning", "Calculation", "Autocorrection"))

# Display the selected page
if options == "Home":
    home_main()  # Call the main function of home.py
elif options == "Learning":
    learning_main()  # Call the main function of learning.py
elif options == "Calculation":
    calculation_main()  # Call the main function of calculation.py
elif options == "Autocorrection":
    auto_main()  # Call the main function of autocorrection.py

