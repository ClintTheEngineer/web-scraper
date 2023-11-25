import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the article titles (assuming they are in <h2> tags)
        titles = soup.find_all('h2')
        paragraphs = soup.find_all('p')

        # Extract and print the titles
        for title in titles:
            print(title.text.strip())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        # Extract and print the paragraphs
        for paragraph in paragraphs:
            print(paragraph.text.strip())
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Specify the URL of the website you want to scrape
user_input_domain = input("Enter domain: ")
url_to_scrape = user_input_domain 


# Call the function with the specified URL
simple_web_scraper(url_to_scrape)
