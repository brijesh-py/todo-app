# Flask ToDoList App

A simple ToDoList application built with Flask.

## Setup

1. Install the required dependencies by running the following command:
 pip install -r requirements.txt

2. Set up the database by running the following command:
 flask db upgrade
 
3. Start the application by running the following command
  flask run
  
4. Open your web browser and visit `http://localhost:5000` to access the application.

## Functionality

- The home page displays a list of existing todos.
- You can add a new todo by entering the content in the provided input field and clicking the "Add" button.
- You can delete a todo by clicking the "Delete" link next to it.
- You can update the content of a todo by clicking the "Update" link next to it, modifying the content, and clicking the "Update" button.

## Project Structure

- `run.py`: Entry point of the application.
- `app/__init__.py`: Initializes the Flask application and sets up the database.
- `app/urls.py`: Defines the URL routes and their corresponding views.
- `app/views.py`: Contains the view functions for handling different routes.
- `app/models.py`: Defines the database models for the ToDoList.
- `templates/index.html`: HTML template for the home page.
 
- In this project in use[ w3.css](https://www.w3schools.com/w3css/) framework to styling app.

## Technologies Used

- Flask: A lightweight web framework for Python.
- Flask SQLAlchemy: Provides integration between Flask and SQLAlchemy for database operations.
- Flask Migrate: Handles database migrations for Flask applications.

Contributors
Brijesh GP brijeshsoftdev@duck.com Thanks for visiting here.
