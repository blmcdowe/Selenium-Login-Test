# Selenium Login Test

Automated UI test using Selenium WebDriver to verify the login functionality of [The Internet Herokuapp](https://the-internet.herokuapp.com/login).

## Project Overview

This project demonstrates a basic Selenium test script in Python that:

    - Opens the login page
    - Inputs valid credentials
    - Submits the login form
    - Verifies successful login message

## Prerequisites

    - Python 3.7+
    - Chrome browser installed
    - ChromeDriver executable accessible via PATH or project folder

## Setup Instructions

1. Create and activate a Python virtual environment:


    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows

2. Install dependencies:


    pip install -r requirements.txt

3. Ensure chromedriver is installed and added to your PATH. Download from here.


   Running the Test Via pytest:

    pytest

   Via CLI script:

    python cli.py

## Project Structure
csharp



    ├── test_login.py      # Selenium test script

    ├── cli.py             # CLI to run tests

    ├── requirements.txt   # Python dependencies

    ├── .gitignore         # Git ignore file

    ├── conftest.py        # pytest config (warning suppression)

    └── README.md

## Notes
This test validates the presence of the login success message after submitting credentials.

Adjust URLs or selectors in test_login.py as needed for your application.

## Author
Byron McDowell — [GitHub](https://github.com/blmcdowe) | [LinkedIn](https://linkedin.com/in/byronmcdowell)






