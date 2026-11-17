# Library Management System

A Library Management System backend developed using Python and FastAPI, with PostgreSQL as the database.

This project provides RESTful APIs to manage library operations, including books, authors, categories, members, borrowings, and fines.

The backend uses SQLAlchemy ORM for database operations and Pydantic for data validation.

## Features

- Book management (Create, Read, Update, Delete)
- Author management
- Category management
- Member management
- Borrowing management
- Fine management
- Database integration with PostgreSQL
- Data validation using Pydantic
- Error handling with appropriate HTTP status codes
- Interactive API documentation using Swagger UI

## Technologies Used

- **Python** – Main programming language
- **FastAPI** – Backend web framework
- **PostgreSQL** – Relational database
- **SQLAlchemy** – Object Relational Mapper (ORM)
- **Pydantic** – Data validation and serialization
- **Uvicorn** – ASGI server
- **Git & GitHub** – Version control and code hosting


## Project Structure

```text
app/
│
├── crud/
│   ├── author.py
│   ├── book.py
│   ├── borrowing.py
│   ├── category.py
│   ├── fine.py
│   └── member.py
│
├── models/
│   ├── author.py
│   ├── book.py
│   ├── borrowing.py
│   ├── category.py
│   ├── fine.py
│   └── member.py
│
├── routers/
│   ├── author.py
│   ├── book.py
│   ├── borrowing.py
│   ├── category.py
│   ├── fine.py
│   └── member.py
│
├── schemas/
│   ├── author.py
│   ├── book.py
│   ├── borrowing.py
│   ├── category.py
│   ├── fine.py
│   └── member.py
│
├── config.py
├── database.py
├── main.py
└── requirement.txt
```


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SaweraAsghar/Library_Management_System.git
```

### 2. Navigate to the project directory

```bash
cd Library_Management_System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r app/requirement.txt
```

## Environment Variables

This project uses environment variables to store PostgreSQL database configuration securely.

Create a `.env` file inside the `app` directory and add the following variables:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_NAME=library_management_system
```

Update the values according to your PostgreSQL configuration.

**Important:** Never upload your `.env` file or database credentials to GitHub.


## Running the Project

### 1. Create the PostgreSQL database

Create a database named `library_management_system` in PostgreSQL.

### 2. Start the FastAPI application

From the project root directory, run:

```bash
uvicorn app.main:app --reload
```

### 3. Open the API documentation

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to explore and test the available API endpoints.

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Future Improvements

- Develop a frontend using React.js.
- Add user authentication and authorization.
- Improve search and filtering functionality.
- Add automated testing.

## Author

**Sawera Asghar**

GitHub: https://github.com/SaweraAsghar
