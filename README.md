# Goodreads Quotes Scraper

🤩 📖 👉 [Goodreads Quotes Scraper Live App!](https://goodreads-quotes.streamlit.app/)

📜 This is a Python program designed to scrape quotes from an author's page on Goodreads. It provides the ability to extract quotes, along with the respective authors and books, and allows users to save the scraped data as a text file.

## Take a look

<image src="./media/images/Screenshot from 2023-07-05 19-11-36.png" alt="Screenshot of Goodreads Quotes App"></image>

## Features

🔍 Scrapes quotes, authors, and books from the Goodreads author quotes page.
🔗 Supports both page URL and keyword search for retrieving quotes.
📋 Displays the scraped data in an organized and user-friendly manner.
⬇️ Provides the option to download the scraped quotes as a text file.

## Installation

To use this program locally, follow these steps:

1. Ensure you have [Python](https://www.python.org/) installed on your system (version 3.6 or higher).
2. Clone this repository or download the program file.
3. Install the required dependencies by running the following command:
   ```
   pip install streamlit requests beautifulsoup4
   ```
4. Run the program using the following command:
   ```
   streamlit run goodreads_quotes_app_0_1_3.py
   ```

## Usage

1. Go to the [web app link](https://goodreads-quotes.streamlit.app/)

2. On the sidebar, you'll find a list of suggested authors' quotes. Clicking on an author's button will prepopulate the page URL field with the respective Goodreads author quotes page.
3. Alternatively, you can manually enter the Goodreads author quotes page URL or some keywords to perform a search.
4. Click the "Scrape Quotes" button to initiate the scraping process.
5. The program will scrape the quotes, authors, and books from the provided URL or search keywords.
6. The scraped data will be displayed on the main page, showing the quotes along with their respective authors and books.
7. If the number of quotes exceeds 15, they will be separated by a horizontal line for better readability.
8. To download the scraped quotes as a text file, use the "Save Quotes as a txt file" button located in the sidebar.

## Contributing

Contributions are welcome! If you would like to enhance the functionality or fix any issues in the program, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the author:

- GitHub: [Gero Zayas](https://github.com/gerozayas)

Enjoy scraping and exploring quotes from your favorite authors! 🌟
