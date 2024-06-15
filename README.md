# IMDB Scrapper

This application was written to pull data from imdb to use for educational purposes.

## How to Use

1. First, clone the project to your computer:

    ```bash
    git clone https://github.com/findik-faresi/IMDB_scrapper
    ```

2. Go to the project directory:

    ```bash
    cd IMDB-scrapper
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the following command to start:

    ```bash
    python main.py
    ```
    
## Features

- You can scrap differrent countries data.
- Auto save to json file.

## Example Json

```json
    "Oct 04, 2024": [
    {
        "src": "https://m.media-amazon.com/images/M/MV5BMzRjMmZkOGEtMjQ1ZC00OTI2LTg5NjItYTM0MmNjMWJlMzEzXkEyXkFqcGdeQXVyMjg2Njg1NjU@._V1_QL75_UY74_CR2,0,50,74_.jpg",
        "title": "Hay algo en el bosque (2024\u2013 )",
        "all_category": [
            "Action",
            "Adventure",
            "Comedy"
        ],
        "all_writer": [
            "Yenni Ann",
            "Zorion Eguileor",
            "Andrea Nu\u00f1ez",
            "Denis G\u00f3mez"
        ]
    }
],
"Oct 25, 2024": null,
"Nov 14, 2024": null,
"Nov 18, 2024": null,
"Dec 01, 2024": [
    {
        "src": "https://m.media-amazon.com/images/M/MV5BODIyYjMyOTQtZmMyOS00MGI2LTk0ODQtOTQ5M2Q5ZmQ4MWUyXkEyXkFqcGdeQXVyNjM2ODc4OTc@._V1_QL75_UY74_CR1,0,50,74_.jpg",
        "title": "Vice Squad: Miami (2024\u2013 )",
        "all_category": [
            "Crime"
        ],
        "all_writer": [
            "Jul Kohler",
            "Iliana Guibert",
            "Tris Marie",
            "DJ Jenkins"
        ]
    }
],
"Dec 31, 2024": [
    {
        "src": "https://m.media-amazon.com/images/M/MV5BOWVjNTlhMzAtNTczNS00ODIzLWFlZDktYTg1OWVmNjAxMjRhXkEyXkFqcGdeQXVyMjUwODU4Mzg@._V1_QL75_UX50_CR0,1,50,74_.jpg",
        "title": "Preach (2023\u2013 )",
        "all_category": [
            "Drama"
        ],
        "all_writer": [
            "Sean Derry",
            "Jo Dee Messina",
            "Ginna Claire Mason",
            "Jeremy Childs"
        ]
    }
],
```
