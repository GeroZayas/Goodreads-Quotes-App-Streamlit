import requests
from bs4 import BeautifulSoup
import streamlit as st

@st.cache_data()
def scrape_quotes(page_url):
    quotes = []
    page_num = 1
    while page_num <= 15:
        response = requests.get(f"{page_url}?page={page_num}")
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_divs = soup.find_all('div', class_='quoteText')
        if not quotes_divs:
            break
        page_quotes = [quote.get_text(strip=True) for quote in quotes_divs]
        quotes.extend(page_quotes)
        page_num += 1
    return quotes

def main():
    st.sidebar.title("Suggested Quotes")
    suggested_quotes = {
        "Jordan B. Peterson": "https://www.goodreads.com/author/quotes/282885.Jordan_B_Peterson",
        "Isaac Asimov": "https://www.goodreads.com/author/quotes/16667.Isaac_Asimov",
        "Matthew Syed": "https://www.goodreads.com/author/quotes/3414480.Matthew_Syed"
    }
    for author, url in suggested_quotes.items():
        st.sidebar.write(author)
        st.sidebar.write(url)
        st.sidebar.write("---")

    st.title("Goodreads Author Quotes Scraper")
    st.write("Enter the Goodreads author quotes page URL:")

    page_url = st.text_input("Page URL", "")
    if st.button("Scrape Quotes"):
        if page_url:
            _extracted_from_main_19(page_url)
        else:
            st.write("Please enter a valid page URL.")


# TODO Rename this here and in `main`
def _extracted_from_main_19(page_url):
    quotes = scrape_quotes(page_url)
    st.write("Scraped Quotes:")
    st.write(f"Total Quotes: {len(quotes)}")
    
    # # FIXME: This is not working
    # if st.button("Random Quote"):
    #     random_quote = random.choice(quotes)
    #     st.markdown(f"### {random_quote}")
    
    # TODO: Add a button to save the quotes to a file markdown file and txt file

    separator = "\n---\n"
    quotes_with_separator = separator.join(quotes)
    quotes_markdown = "\n".join(f"### {quote}" for quote in quotes_with_separator.split(separator))
    st.markdown(quotes_markdown)

        
if __name__ == "__main__":
    main()
