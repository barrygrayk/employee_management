# Employee Management Backend

This Django project includes a `Skill` and `Employee` model. This backend handles api requests to create, update delete and employee and their skills.

## Versions

This project uses the following software versions:

- Django: 5.0.4
- Python: 3.12
- Poetry: 1.8.2

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Python](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/#installation).

## Setup

1. Install the project dependencies using Poetry:

    ```bash
    poetry install
    ```

2. Apply the migrations:

    ```bash
    poetry python manage.py migrate
    ```

3. Create  the migrations:

    ```bash
    poetry python manage.py createsuperuser
    ```

## Running Backend Locally

You can run Django commands using the `python manage.py` command. For example, to start the development server, you can use:

 ```bash
 poetry python manage.py runserver
```
 This should execute the backend serve on [serve](http://127.0.0.1:8000/)

 ### Accessing the API

 The API can be accessed at the following [URL](http://127.0.0.1:8000/api/)

 ### Admin Panel
 TThe Django admin panel can be accessed at the following [URL](http://127.0.0.1:8000/admin/)
