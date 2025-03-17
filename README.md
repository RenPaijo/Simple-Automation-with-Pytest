# Simple Automation Example Using Python, Selenium, and Pytest

Welcome to this repository! 🎉

This project demonstrates a **simple example of automation** utilizing **Python**, **Selenium**, and **Pytest**. It’s designed to showcase best practices for creating maintainable and organized automated tests, perfect for learning or as a reference for your own projects.

## Features

-   **Python**: The programming language used for writing the automation scripts.
-   **Selenium**: For web automation, simulating user interactions with a web browser.
-   **Pytest**: A testing framework to structure, execute, and report test results.

## Project Structure

    # Simple Automation Example Using Python, Selenium, and Pytest

Welcome to this repository! 🎉

This project demonstrates a **simple example of automation** utilizing **Python**, **Selenium**, and **Pytest**. It’s designed to showcase best practices for creating maintainable and organized automated tests, perfect for learning or as a reference for your own projects.

## Features

-   **Python**: The programming language used for writing the automation scripts.
-   **Selenium**: For web automation, simulating user interactions with a web browser.
-   **Pytest**: A testing framework to structure, execute, and report test results.

## Project Structure

    .
    ├── tests/
    │   └── test_example.py       # Example test case
    │
    ├── pages/
    │   ├── base_page.py          # Common functions for page interactions
    │   ├── example_page.py       # Page-specific elements and actions
    │
    ├── conftest.py               # Pytest configuration file (moved to root)
    ├── requirements.txt          # Required dependencies
    └── README.md                 # This file!

## Getting Started

1.  **Clone the repository:**

        git clone <repository-url>
        cd <repository-folder>

2.  **Install dependencies:**

        pip install -r requirements.txt

3.  **Run the tests:**

        pytest --html=report.html --self-contained-html

## Viewing the Test Report

After running the tests, a file named `report.html` will be generated. This file contains a detailed report of the test results. Here's how to open it:

1.  **Locate the `report.html` file:**
    *   It should be in the root directory of your project (the same directory as this `README.md` file).

2.  **Open the file in your web browser:**
    *   **Double-click** the `report.html` file. This should open it in your default web browser.
    *   Alternatively, you can **right-click** the file and select "Open with" followed by your preferred web browser (e.g., Chrome, Firefox, Safari).

3.  **View the report:**
    *   The `report.html` file will display a summary of your test results, including:
        *   The number of tests run, passed, and failed.
        *   Detailed information about each test case, including any error messages or screenshots.
        *   Environment information and other relevant details.

## Key Learning Points

-   Setting up **Selenium WebDriver** for automation.
-   Writing clean, maintainable test scripts using **Pytest**.
-   Organizing tests and reusable components for better scalability.
-   Generating detailed test reports for analysis.

## Getting Started

1.  **Clone the repository:**

        git clone <repository-url>
        cd <repository-folder>

2.  **Install dependencies:**

        pip install -r requirements.txt

3.  **Run the tests:**

        pytest --html=report.html --self-contained-html

## Viewing the Test Report

After running the tests, a file named `report.html` will be generated. This file contains a detailed report of the test results. Here's how to open it:

1.  **Locate the `report.html` file:**
    *   It should be in the root directory of your project (the same directory as this `README.md` file).

2.  **Open the file in your web browser:**
    *   **Double-click** the `report.html` file. This should open it in your default web browser.
    *   Alternatively, you can **right-click** the file and select "Open with" followed by your preferred web browser (e.g., Chrome, Firefox, Safari).

3.  **View the report:**
    *   The `report.html` file will display a summary of your test results, including:
        *   The number of tests run, passed, and failed.
        *   Detailed information about each test case, including any error messages or screenshots.
        *   Environment information and other relevant details.