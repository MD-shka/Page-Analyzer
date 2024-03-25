### Hexlet tests and linter status:
[![Actions Status](https://github.com/MD-shka/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MD-shka/python-project-83/actions)

### CodeClimate and CI:
[![Python CI](https://github.com/MD-shka/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/MD-shka/python-project-83/actions/workflows/pyci.yml)
![]()
![]()
[![Maintainability](https://api.codeclimate.com/v1/badges/0e8ced7e1dd7162010e7/maintainability)](https://codeclimate.com/github/MD-shka/python-project-83/maintainability)
![]()
![]()
[![Test Coverage](https://api.codeclimate.com/v1/badges/0e8ced7e1dd7162010e7/test_coverage)](https://codeclimate.com/github/MD-shka/python-project-83/test_coverage)

### Description:

Page Analyzer is a website that analyzes specified pages for SEO suitability. 

### Website:
https://page-analyzer-7qot.onrender.com

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/MD-shka/Page-Analyzer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Page-Analyzer
    ```
3. Install dependencies using Poetry:
    ```bash
    make build
    ```

### Usage
To run the project locally, you can use the following commands:
- For development mode with Flask:
    ```bash
    make dev
    ```
- For production mode with Gunicorn:
    ```bash
    make start
    ```

### Accessing the Application
Once the server is running, you can access the application by opening a web browser and navigating to:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
