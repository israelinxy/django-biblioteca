# Biblioteca

## Description

Biblioteca is a web application for managing a library's book collection. It allows users to perform various actions such as adding new books, editing existing ones, deleting entries, and filtering the collection by category, publisher, title, and more.

## Features

* **User Authentication:** Securely log in to access the application and view the book list.
* **Book Management:**
    * Add new books with details like title, author, publisher, category, etc.
    * Edit existing book information.
    * Delete book entries from the database.
* **Filtering and Search:**
    * Filter the book collection by category, publisher, title, and other relevant fields.
    * Search for specific books using keywords.

## Technologies Used

* **Backend:** Django
* **Frontend:** HTML, CSS

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd biblioteca`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
    * Windows: `env\Scripts\activate`
    * macOS/Linux: `source env/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Create a superuser account: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## Usage

1. Access the application in your web browser: `http://127.0.0.1:8000/`
2. Log in using your superuser credentials.
3. Once logged in, you can start managing the library's book collection.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License.
