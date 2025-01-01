# E-commerce API


## Description: 

This project explores the basics of backend development with FastAPI, covering topics like building web servers, managing API routes, handling query and path parameters, integrating databases with SQLModel, and organizing code into services and dependency injection.

The API serves as a learning platform and includes basic CRUD functionality, database integration, and modular API routing, laying the groundwork for more complex features like user authentication, shopping cart management, and order processing in the future.

#### Project Setup:
Configured the Python environment with dependencies for FastAPI and SQLAlchemy/SQLModel.
Set up environment variables for database connectivity.
 
#### Web Server:
Built a simple web server using FastAPI.
Started and tested the server with the FastAPI CLI (uvicorn) in development mode.

#### API Development:
Implemented endpoints with path and query parameters, including optional parameters.
Designed request bodies and headers for API operations.

#### API Organization:
Structured API paths using FastAPI routers for modularity and maintainability.

#### Database Integration:
Configured SQLAlchemy and SQLModel for async database interaction.
Designed database models and created tables using SQLModel.
Set up PostgreSQL for data persistence.
Implemented CRUD operations for interacting with the database.

#### Service Architecture:
Abstracted CRUD logic into service classes to adhere to clean code principles.
Used dependency injection to pass services into API path handlers, ensuring scalability and testability.

## Technologies/Websites Used:

FastAPI: A modern web framework for building APIs with Python, known for its speed and ease of use.

SQLAlchemy (via SQLModel): An ORM and database toolkit for defining and interacting with databases in Python.

PostgreSQL: A powerful, open-source relational database system used for persistent data storage.

Python: The programming language used to develop the project.

Restfox: cross-platform API testing and debugging tool 

Console.neon.tech: Provides an intuitive web-based UI to create, manage, and monitor PostgreSQL databases hosted on the Neon cloud platform.

## Commands For You to Use:

### Cloning Repository: 
```git clone https://github.com/rahul-vegiraju/Ecommerce.git```

cd Ecommerce

###  Create a Virtual Environment and Install Dependencies:

```python -m venv env```, ```source env/bin/activate```, ```pip install -r requirements.txt```

### Additional commands:
To Run the project: 
```fastapi dev src/```

Might need to install: 
```pip install fastapi```, ```pip install --upgrade pip```, ```pip install "fastapi[standard]"```, ```pip install psycopg2-binarypip```, ```pip install asyncpg```, ```pip install pydantic-settings```, ```pip install sqlmodel```

Make sure to use the connection string given by console.neon.tech once you make an account. You place the connection string inside of the .env file and set it inside of DATABASE_URL = "". MAKE SURE TO remove "```?sslmode=require```" at the end in order for it to work.


