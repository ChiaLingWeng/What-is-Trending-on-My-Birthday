import streamlit as st
from datetime import date
from crawler import fetch_data


# Streamlit UI
st.title("A")

board = st.selectbox("Choose a board:", ["Gossiping", "movie"])
chosen_date = st.date_input("Choose a date:", date.today())
if st.button("Go"):
    # Convert the date format to match the website's format
    formatted_date = chosen_date.strftime("%m/%d").lstrip("0")
    results = fetch_data(board, formatted_date)
    for title, link in results:
        st.write(f"[{title}]({link})")