# Goodreads Quotes Scraper

(Live App!)[https://goodreads-quotes.streamlit.app/]

This is a Python program designed to scrape quotes from an author's page on Goodreads. It provides the ability to extract quotes, along with the respective authors and books, and allows users to save the scraped data as a text file.

## Features

- Scrapes quotes, authors, and books from the Goodreads author quotes page.
- Supports both page URL and keyword search for retrieving quotes.
- Displays the scraped data in an organized and user-friendly manner.
- Provides the option to download the scraped quotes as a text file.

## Installation

To use this program, follow these steps:

1. Ensure you have [Python](https://www.python.org/) installed on your system (version 3.6 or higher).
2. Clone this repository or download the program file.
3. Install the required dependencies by running the following command:
   ```
   pip install streamlit requests beautifulsoup4
   ```
4. Run the program using the following command:
   ```
   streamlit run <filename>.py
   ```
   Replace `<filename>.py` with the actual name of the file where the program is saved.

## Usage

1. Open the program in your preferred Python editor or IDE.
2. Ensure that the required modules (such as `re`, `requests`, `streamlit`, and `bs4`) are imported.
3. Locate the `VERSION` section at the top of the code and update it to reflect the current version of your program.
4. Run the program using the command mentioned in the installation steps.
5. The program will launch a Streamlit app in your default web browser.
6. On the sidebar, you'll find a list of suggested authors' quotes. Clicking on an author's button will prepopulate the page URL field with the respective Goodreads author quotes page.
7. Alternatively, you can manually enter the Goodreads author quotes page URL or some keywords to perform a search.
8. Click the "Scrape Quotes" button to initiate the scraping process.
9. The program will scrape the quotes, authors, and books from the provided URL or search keywords.
10. The scraped data will be displayed on the main page, showing the quotes along with their respective authors and books.
11. If the number of quotes exceeds 15, they will be separated by a horizontal line for better readability.
12. To download the scraped quotes as a text file, use the "Save Quotes as a txt file" button located in the sidebar.

## Contributing

Contributions are welcome! If you would like to enhance the functionality or fix any issues in the program, feel free to submit a pull request. Please ensure to follow the [contribution guidelines](CONTRIBUTING.md) when making changes.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the author:

- GitHub: [Your GitHub Username](https://github.com/YourGitHubUsername)

Enjoy scraping and exploring quotes from your favorite authors!
