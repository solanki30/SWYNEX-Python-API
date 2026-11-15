
# Student Management REST API

## Project Overview
This project is a Student Management REST API developed using Python and Flask.

It allows users to manage student records through HTTP requests.

## Technologies Used
- Python 3.10
- Flask
- REST API
- JSON
- Postman

## Features
- View all students
- Add new students
- Update student details
- Delete student records
- Input validation
- Error handling
- JSON responses

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /students | View all students |
| POST | /students | Add a student |
| PUT | /students/<student_id> | Update a student |
| DELETE | /students/<student_id> | Delete a student |

## Installation

1. Clone the repository:

   git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder.

3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   python app.py

5. Open in browser:

   http://127.0.0.1:5000/

## Testing

The API was tested using Postman.

## Data Storage
Student records are stored in memory.
Data resets when the Flask server restarts.

## Developer
Solanki Das

## Project
SWYNEX Technologies Internship - Task 3
