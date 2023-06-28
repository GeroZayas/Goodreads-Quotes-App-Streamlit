import requests
import streamlit as st
from bs4 import BeautifulSoup

#################
# VERSION 0.1.3 #
#################

@st.cache_data()
def scrape_quotes(page_url):
    quotes = []
    authors = []
    books = []
    page_num = 1
    while page_num <= 25:
        response = requests.get(f"{page_url}?page={page_num}")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes_divs = soup.find_all("div", class_="quoteText")
        authors_span = soup.find_all("span", class_="authorOrTitle")
        books_a = soup.find_all("a", class_="authorOrTitle")

        if not quotes_divs:
            break

        for quote_div, author_span, book_a in zip(quotes_divs, authors_span, books_a):
            quote_text = ""
            for elem in quote_div.contents:
                if elem.name == "br":
                    break
                if isinstance(elem, str):
                    quote_text += elem.strip()
            quotes.append(quote_text)
            authors.append(author_span.get_text(strip=True))
            books.append(book_a.get_text(strip=True))

        page_num += 1

    return quotes, authors, books


def main():
    st.sidebar.title("Suggested Quotes")
    suggested_quotes = {
        "Jordan B. Peterson": "https://www.goodreads.com/author/quotes/282885.Jordan_B_Peterson",
        "Isaac Asimov": "https://www.goodreads.com/author/quotes/16667.Isaac_Asimov",
        "Matthew Syed": "https://www.goodreads.com/author/quotes/3414480.Matthew_Syed",
    }
    for author, url in suggested_quotes.items():
        # st.sidebar.markdown(f"Goodreads: {author}")
        st.sidebar.markdown(f"[{author}]({url})\n---")
        # st.sidebar.write("---")

    st.title("Goodreads Author Quotes Scraper")
    st.write("Enter the Goodreads author quotes page URL:")

    page_url = st.text_input("Page URL", "")
    if st.button("Scrape Quotes"):
        if page_url:
            quotes, authors, books = scrape_quotes(page_url)
            st.write(f"Total Quotes: {len(quotes)}")
            separator = "\n---\n"

            for i in range(len(quotes)):
                st.markdown(f"### {quotes[i]}")
                st.markdown(
                    f"<h5 style='color: darkred;display: inline;'>{authors[i]}</h5>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"<h6 style='color: #4a008f;display: inline;'>{books[i]}</h6>",
                    unsafe_allow_html=True,
                )
                st.markdown("<br>", unsafe_allow_html=True)
                if (i + 1) % 15 == 0 and i != len(quotes) - 1:
                    st.markdown(separator)
        else:
            st.write("Please enter a valid page URL.")


if __name__ == "__main__":
    main()
