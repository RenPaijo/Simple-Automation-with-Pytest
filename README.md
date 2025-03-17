<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Automation Example Using Python, Selenium, and Pytest</title>
</head>
<body>
    <h1>Simple Automation Example Using Python, Selenium, and Pytest</h1>
    <p>Welcome to this repository! 🎉</p>
    <p>
        This project demonstrates a <strong>simple example of automation</strong> utilizing 
        <strong>Python</strong>, <strong>Selenium</strong>, and <strong>Pytest</strong>. It’s 
        designed to showcase best practices for creating maintainable and organized automated 
        tests, perfect for learning or as a reference for your own projects.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Python</strong>: The programming language used for writing the automation scripts.</li>
        <li><strong>Selenium</strong>: For web automation, simulating user interactions with a web browser.</li>
        <li><strong>Pytest</strong>: A testing framework to structure, execute, and report test results.</li>
    </ul>

    <h2>Project Structure</h2>
    <pre>
.
├── tests/
│   ├── test_example.py       # Example test case
│   ├── conftest.py           # Pytest configuration file
│
├── pages/
│   ├── base_page.py          # Common functions for page interactions
│   ├── example_page.py       # Page-specific elements and actions
│
├── requirements.txt          # Required dependencies
├── README.md                 # This file!
    </pre>

    <h2>Getting Started</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre>git clone &lt;repository-url&gt;
cd &lt;repository-folder&gt;</pre>
        </li>
        <li><strong>Install dependencies:</strong>
            <pre>pip install -r requirements.txt</pre>
        </li>
        <li><strong>Run the tests:</strong>
            <pre>pytest --html=report.html --self-contained-html</pre>
        </li>
    </ol>

    <h2>Key Learning Points</h2>
    <ul>
        <li>Setting up <strong>Selenium WebDriver</strong> for automation.</li>
        <li>Writing clean, maintainable test scripts using <strong>Pytest</strong>.</li>
        <li>Organizing tests and reusable components for better scalability.</li>
        <li>Generating detailed test reports for analysis.</li>
    </ul>
</body>
</html>
