import streamlit as st
from datetime import date
import requests
from bs4 import BeautifulSoup

# Define the Web Scraper
def fetch_data(board, chosen_date):
    base_url = f"https://www.ptt.cc/bbs/{board}/index.html"
    response = requests.get(url=base_url,verify=False)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract posts
    posts = soup.find_all("div", class_="r-ent")

    filtered_data = []
    for post in posts:
        if post.find("div", class_="date").text.strip() == chosen_date:
            title = post.find("div", class_="title").text.strip()
            link = "https://www.ptt.cc" + post.find("a")["href"]
            filtered_data.append((title, link))

    return filtered_data

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