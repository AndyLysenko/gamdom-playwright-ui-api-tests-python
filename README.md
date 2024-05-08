# Gamdom Playwright UI Tests (Python)

## About

This repository, `gamdom-playwright-ui-tests-python`, hosts a demo of UI tests for the [Gamdom.com](https://www.gamdom.com) gaming platform. The tests are written using Playwright with Python, showcasing automated UI testing strategies for complex web interactions.

The project aims to evaluate expertise in UI test automation, understanding of requirements, and ability to derive critical functionality from exploratory testing.

## Technologies

- [Playwright](https://playwright.dev/)
- [Python](https://www.python.org/)
- [pytest](https://pytest.org/)

## Approach

The project utilizes the Page-Object pattern to create an abstraction layer for the tested pages, enhancing test readability, maintainability, and reusability. The tests are driven by a Data-Driven approach, facilitating the easy addition of new test scenarios.

### UI Tests

UI tests have been developed based on exploratory testing of the Gamdom website. They focus on ensuring the functionality and reliability of user interactions on the platform.

## Project Structure

- `tests/`: Contains the UI tests and related files.
- `pages/`: Contains the Page Object models for various pages of the application.
- `configs/`: Stores configuration files that define settings for different environments.
- `requirements.txt`: Lists all Python package dependencies.
- `.github/`: Contains GitHub-specific metadata, such as GitHub Actions workflows for CI/CD.
- `pytest.ini`: Contains the pytest configuration settings.

## Setup

1. Clone the repository: `git clone https://github.com/AndyLysenko/gamdom-playwright-ui-api-tests-python.git`
2. Navigate to the project directory: `cd gamdom-playwright-ui-api-tests-python`
3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix or MacOS
   venv\Scripts\activate  # On Windows
   ```

4. Install the dependencies: pip install -r requirements.txt

## Running the Tests

- To run all UI tests: pytest tests/

Additional Options for Running Tests

- To run tests in a specific file: pytest tests/test_specific_file.py
- To run tests with detailed output: pytest -v tests/
- To run tests and generate an HTML report: pytest --html=report.html

## Code Quality

Code quality is maintained using formatting tools and linters such as flake8 and black. To run the linter, use the command:

bash
Copy code
flake8 .

## To Do

- Configuration Management: Set up dynamic configuration management for different environments.
- Add Reporting: Implement detailed reporting tools for test executions.
- Add Screenshots, Video, Logs: Integrate screenshot and video capturing, along with detailed logging for test runs.
- Tests in Parallel: Configure pytest to run tests in parallel to reduce execution time.
- CI/CD Pipelines: Develop GitHub Actions workflows for continuous integration and continuous deployment.
- API Testing: Extend the testing framework to include API tests.

## License

This project is licensed under the terms of the MIT license. See LICENSE for more details.
