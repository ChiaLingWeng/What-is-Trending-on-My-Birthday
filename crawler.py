import requests
from bs4 import BeautifulSoup


# Define the Web Scraper
def fetch_data(board, chosen_date):
    base_url = f"https://www.ptt.cc/bbs/{board}/index.html"
    response = requests.get(url=base_url,verify=False)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract posts
    posts = soup.find_all("div", class_="r-ent")
    print(posts)

    filtered_data = []
    for post in posts:
        if post.find("div", class_="date").text.strip() == chosen_date:
            title = post.find("div", class_="title").text.strip()
            link = "https://www.ptt.cc" + post.find("a")["href"]
            filtered_data.append((title, link))

    return filtered_data


fetch_data("movie","2000-12-16")