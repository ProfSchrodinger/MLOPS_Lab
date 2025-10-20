# LAB1 - MLOps (IE-7374)

This project demonstrates a complete Continuous Integration (CI) pipeline for a Python application. It covers key MLOps practices, including virtual environment management, version control with Git, automated testing with pytest and unittest, and CI automation using GitHub Actions.

# Project Overview

1. The primary goal of this lab was to build a robust development and deployment workflow. The key concepts covered include:

2. Environment Setup: Using a Python virtual environment to manage dependencies and ensure a consistent, isolated workspace.

3. Version Control: Structuring the project in a Git repository, with source code, tests, and workflow configurations properly organized.

4. Automated Testing: Implementing comprehensive unit tests to validate the application's functionality and prevent regressions.

5. Continuous Integration (CI): Configuring a GitHub Actions workflow to automatically build the environment, install dependencies, and run tests on every push to the main branch.

# About the Program: Text Analyzer

The core application for this project is a simple command-line text analysis tool, located in src/text_analyzer.py. It provides functions to extract basic statistics from a given string of text.

The main functions are:
    count_words(text): Returns the total number of words.
    count_characters(text): Returns the total number of characters, including spaces.
    count_sentences(text): Returns the number of sentences based on punctuation.
    analyze_text(text): A summary function that returns a dictionary containing all the above metrics.

# Automated Testing and CI/CD Workflow

To ensure code quality and reliability, this project is configured with a fully automated testing and integration pipeline.

## Testing Frameworks

The application is tested using both pytest and unittest. The test suites, located in the test/ directory, verify that each function in the text_analyzer module behaves as expected with various inputs.

## GitHub Actions Workflow

A Continuous Integration workflow is defined in .github/workflows/pytest_actions.yaml. This workflow is automatically triggered on every push to the main branch and performs the following steps:

    1. Checkout Code: Clones the latest version of the repository.
    2. Set up Python: Prepares a clean Ubuntu environment with the specified Python version.
    3. Install Dependencies: Installs all required packages from the requirements.txt file.
    4. Run Pytest: Executes the entire test suite and generates a report.
    5. Report Status: The workflow reports a "success" or "failure" status, providing immediate feedback on whether the new code changes have introduced any issues.
