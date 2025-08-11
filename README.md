# Government Scheme Finder

This project is a web application that helps users find government schemes in India. Users can filter schemes by category and state.

## Features

-   View a list of government schemes.
-   Filter schemes by category (e.g., Agriculture, Health, Education).
-   Filter schemes by state.

## How to Run

This application is containerized using Docker. To run the application, you will need to have Docker installed on your machine.

1.  **Build the Docker image:**
    ```bash
    docker build -t scheme-finder .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 scheme-finder
    ```
3.  **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

## Data Source

The data for the government schemes is sourced from the following Wikipedia page:

-   [List of schemes of the government of India](https://en.wikipedia.org/wiki/List_of_schemes_of_the_government_of_India)

The data is used for informational purposes only. This project is not affiliated with the Government of India.

## Note on the Scraper

The initial plan was to scrape the data from an official government website. However, due to persistent technical issues with the development environment, the scraper could not be made to work reliably. As a workaround, the application currently uses a manually curated JSON file with sample data. The scraper code is still available in the repository for reference.
