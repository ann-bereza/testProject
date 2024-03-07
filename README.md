# Dataset Service

Dataset Service is a dockerized Django application that provides an API for working with a dataset of persons. It allows users to perform CRUD operations, filter data based on various criteria, and export filtered data to CSV format.

## Features

- CRUD Operations: Create, Retrieve, Update, and Delete operations for persons in the dataset.
- Filtering: Filter data by category, gender, DOB
- Export: Export filtered data to CSV format.
- Swagger UI Integration: API endpoints are documented using Swagger UI, enabling easy testing and interaction with the API.

## Installation

1. Clone the repository: git clone https://github.com/ann-bereza/testProject.git
2. Install dependencies: ```poetry install```
3. Run migrations: ```python manage.py migrate```
4. Run ```docker compose up --build```. The file <dataset.txt> will be automatically loaded into the db
5. Access Swagger UI to explore and interact with the API:
http://localhost:8000/swagger/
6. To download the results  make sure to change the `Response content type` on Swagger UI to `text/csv` before hitting 'Execute' button and click 'Download' on the response body
