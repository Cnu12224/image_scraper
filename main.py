import requests
from bs4 import BeautifulSoup
import os

def fetch_image(keyword):
    search_url = f"https://www.google.com/search?tbm=isch&q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    if img_tags:
        for img_tag in img_tags:
            img_url = img_tag['src']
            if not img_url.startswith('http'):
                img_url = 'https:' + img_url
            try:
                img_data = requests.get(img_url).content
                with open(f"{keyword}.jpg", 'wb') as handler:
                    handler.write(img_data)
                print(f"Image saved as {keyword}.jpg")
                break
            except requests.exceptions.RequestException as e:
                print(f"Error fetching image: {e}")
    else:
        print("No images found for the given keyword.")

if __name__ == "__main__":
    keyword = input("Enter the keyword to search for: ")
    fetch_image(keyword)
