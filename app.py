import streamlit as st
import random
import string

st.title("🔐 Password Generator")

length = st.number_input(
    "Enter Password Length",
    min_value=4,
    max_value=50,
    value=12
)

# ADD THESE LINES HERE
include_numbers = st.checkbox("Include Numbers", value=True)
include_symbols = st.checkbox("Include Symbols", value=True)

if st.button("Generate Password"):

    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    st.success(password)