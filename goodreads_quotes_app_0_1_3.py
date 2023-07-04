# Purpose of 0.1.3 -> make it faster, use asyncio and so on
# Add functionalities


import re
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

    # This code block is responsible for scraping the quotes, authors, and books
    # from the Goodreads author quotes page.
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
    #############################################################
    # SIDE BAR: Suggested Quotes
    #############################################################

    st.sidebar.title("Suggested Quotes")

    # DICTIONARY OF SUGGESTED QUOTES and their URLs
    suggested_quotes = {
        "Jordan B. Peterson": "https://www.goodreads.com/author/quotes/282885.Jordan_B_Peterson",
        "Isaac Asimov": "https://www.goodreads.com/author/quotes/16667.Isaac_Asimov",
        "Matthew Syed": "https://www.goodreads.com/author/quotes/3414480.Matthew_Syed",
    }
    help_msg = "Get the quotes from this author"

    for author, link in suggested_quotes.items():
        # if sidebar.button clicked then the value of temp_url changes to the link
        if st.sidebar.button(f"{author} ✍️", key=author, help=help_msg):
            # NOTE the use of st.session_state to store the page_url
            st.session_state.page_url = link

    if "page_url" not in st.session_state:
        st.session_state.page_url = ""

    #############################################################
    # MAIN PAGE: Goodreads Author Quotes Scraper
    #############################################################

    st.title("📚 Goodreads Quotes Scraper")
    st.markdown(
        "Enter the Goodreads **author quotes page URL** \
                or some **keywords** to search:"
    )

    # USER INPUT: Page URL ######################################
    page_url = st.text_input("Page URL", value=st.session_state.page_url)
    #############################################################

    # this is to handle the case when the user enters a keyword instead of a URL
    using_search_keyword = False

    # this is to store the quotes, authors, and books in a list
    all_quotes = []

    if st.button("Scrape Quotes"):
        # this is to handle the case when the user enters a keyword instead of a URL
        if not page_url.startswith("https://"):
            page_url = f"https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q={page_url}&commit=Search"
            using_search_keyword = True

        # this is to store the page_url in the session state
        st.session_state.page_url = page_url

        # this is to get the author's name from the page_url
        if using_search_keyword:
            the_author = re.search("(?<=q=).*?(?=&)", page_url).group(0)
        else:
            the_author = re.search("(?<=author/quotes/).*", page_url).group(0)
            # eleminate numbers and . from the author's name
            the_author = re.sub(r"[\d.]", "", the_author).replace("_", " ")

        if page_url:
            quotes, authors, books = scrape_quotes(page_url)
            st.write(f"Total Quotes: {len(quotes)} 📚", unsafe_allow_html=True)
            separator = "\n---\n"

            # this is to display the quotes, authors, and books
            for i in range(len(quotes)):
                st.markdown(f"### 💡 {quotes[i]}")

                # this is to remove the comma at the end of the author's name
                if authors[i].endswith(","):
                    authors[i] = authors[i][:-1]

                st.markdown(
                    f"<h5 style='color: darkred;display: inline;'>{authors[i]}</h5>",
                    unsafe_allow_html=True,
                )

                # this is to display the book name only
                # if the user is not using a search keyword
                if not using_search_keyword:
                    st.markdown(
                        f"<h6 style='color: #4a008f;display: inline;'> 📖 {books[i]}</h6>",  # noqa: E501,
                        unsafe_allow_html=True,
                    )
                st.markdown("<br>", unsafe_allow_html=True)
                if (i + 1) % 15 == 0 and i != len(quotes) - 1:
                    st.markdown(separator)

                # this is to store the quotes, authors, and books in a list
                all_quotes.extend([i + 1, quotes[i], authors[i], books[i], "*" * 60])

            # this is to download the quotes as a txt file
            st.sidebar.markdown(
                "<br> ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️", unsafe_allow_html=True
            )

            #####################################
            # DONWLOAD the quotes as a txt file #
            #####################################

            # FIXME: the content of the file is not being saved correctly
            st.sidebar.download_button(
                "Save Quotes as a txt file",
                file_name=f"{the_author} quotes.txt",
                data=str([str(x) for x in all_quotes]),
            )  # noqa: E501

            #########################################################
            # this automatically downloads the quotes as a txt file #
            #########################################################
            # with open(f"{the_author} quotes.txt", "w") as f:
            #     for item in all_quotes:
            #         f.write("%s\n" % item)

        else:
            st.write("Please enter a valid page URL.")


if __name__ == "__main__":
    main()
