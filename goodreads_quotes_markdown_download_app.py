import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def scrape_quotes(page_url):
    """
    The function "scrape_quotes" is used to scrape quotes, authors, and books from a given webpage URL.
    
    :param page_url: The URL of the webpage from which you want to scrape quotes
    """
    quotes = []
    authors = []
    books = []

    def process_page(page_num):
        """
        The function `process_page` retrieves quotes, authors, and books from a web page and stores them
        in separate lists.
        
        :param page_num: The `page_num` parameter is the page number of the website you are trying to
        scrape. It is used to construct the URL for the specific page you want to scrape
        """
        response = requests.get(f"{page_url}?page={page_num}")
        soup = BeautifulSoup(response.text, "lxml")
        quotes_divs = soup.find_all("div", class_="quoteText")
        authors_span = soup.find_all("span", class_="authorOrTitle")
        books_a = soup.find_all("a", class_="authorOrTitle")

        for quote_div, author_span, book_a in zip(quotes_divs, authors_span, books_a):
            quote_text = "".join(
                elem.strip() for elem in quote_div.contents if isinstance(elem, str)
            )
            quotes.append(quote_text)
            authors.append(author_span.get_text(strip=True))
            books.append(book_a.get_text(strip=True))

    with ThreadPoolExecutor() as executor:
        [executor.submit(process_page, page_num) for page_num in range(26)]

    return quotes, authors, books


def save_quotes_to_file(quotes, authors, books, filename):
    """
    The function `save_quotes_to_file` takes in lists of quotes, authors, books, and a filename, and
    saves the quotes, authors, and books to a Markdown file.
    
    :param quotes: The `quotes` parameter is a list of strings that contains the quotes you want to save
    to the file
    :param authors: The `authors` parameter is a list that contains the names of the authors
    corresponding to each quote
    :param books: The `books` parameter is a list that contains the titles of the books corresponding to
    each quote
    :param filename: The `filename` parameter is a string that represents the name of the file you want
    to save the quotes to. It should not include the file extension
    """
    with open(f"{filename}.md", "w", encoding="utf-8") as file:
        for i in range(len(quotes)):
            file.write(f"### {quotes[i]}\n")
            file.write(f"**{authors[i]}**\n")
            file.write(f"*{books[i]}*\n")
            file.write("\n")


def main():
    page_url = input("Enter the Goodreads author quotes page URL: ")

    quotes, authors, books = scrape_quotes(page_url)
    print(f"Total Quotes: {len(quotes)}")

    save_quotes_to_file(quotes, authors, books, f"{authors[0]} quotes".replace(",", ""))
    print("Quotes saved successfully.")


if __name__ == "__main__":
    import timeit

    start_time = timeit.default_timer()

    ####### MAIN FUNCTION #########
    main()
    ####### MAIN FUNCTION #########

    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")
