# Product Management API

## Overview
This project is designed to handle adding and presenting products. It is built using Django and Django REST Framework (DRF) for the backend, with Fetch API used for frontend interactions.

## Features
- Add new products
- List and view products
  
## Technologies Used
- Django
- Django REST Framework
- Fetch API
- SQlite3

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.12
- Virtual environment

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/taronghazaryan/product.git
    ```

2. Navigate to the project directory:
    ```bash
    cd product
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

## API Endpoints

### Products
- `GET /api/v1/get/` - Retrieve a list of products
- `POST /api/v1/add/` - Add a new product


