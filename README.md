# Connect

**Connect** is a backend system designed to manage schedules, roles, and ministries within a church. It provides a robust interface to organize and optimize activities and tasks related to church management.

## Features

- **Schedule Management**  
  Create and edit schedules for various ministries and events.

- **Role Management**  
  Define and organize roles within each member.

- **Ministry Administration**  
  Register and manage information related to church ministries.

## Technologies Used

- **Django** - A Python web framework for fast and secure development.
- **Django REST Framework** - A powerful toolkit for building RESTful APIs.
- **JWT (JSON Web Token)** - Library to make authentication.

## Requirements

- Python 3.9 or higher
- Virtualenv (optional but recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/connect.git
   cd connect
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
3. Install dependencies:
   ```
   pip install -r requirements.txt
4. Configure the database in the settings.py file.
5. Apply database migrations:
   ```
   python3 manage.py migrate
6. Start the development server:
   ```
   python3 manage.py runserver
