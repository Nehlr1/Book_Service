# Book Service

Book Service is a FastAPI-based web application that provides a simple API for managing books, authors, and clients. The application uses PostgreSQL as the database and is deployed in Docker containers.

## Project Structure

The project follows a modular structure with separate directories for models, routers, and the main application. Here's an overview of the project structure:

```plaintext
book_service/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- database.py
|   |-- models/
|       |-- __init__.py
|       |-- book.py
|       |-- author.py
|       |-- client.py
|-- Dockerfile
|-- requirements.txt
|-- docker-compose.yml
```

## Technologies Used
- FastAPI: A modern, fast web framework for building APIs with Python.
- PostgreSQL: A powerful, open-source relational database system.
- Docker: A platform for automating the deployment and scaling of applications.

## Getting Started
1. Install Docker in your machine.

2. Clone the repository:

```
git clone https://github.com/Nehlr1/Book_Service.git
cd book_service
```

3. Build and run the Docker containers:

```
docker-compose up -d --build
```

## API Endpoints
The API provides the following endpoints:

* Books:
    * Add a book.
    * Edit the book's title and author.
    * Retrieve a list of books with filtering options for the first letter of the book's title and author.
    * Add multiple books by the same author.

* Authors:
    * Add an author.

* Clients:
    * Create a client.
    * Retrieve a list of books borrowed by the client.
    * Link a client to a book (client borrowed the book).
    * Unlink a client from a book (client returned the book).

## Database
The application uses PostgreSQL as the database. The database connection is managed through SQLAlchemy.

## Security
The API is secured using Bearer token authentication. Access tokens are required for protected routes.

## Contributing
Feel free to contribute to the project by opening issues or pull requests. Your feedback and contributions are highly appreciated.