# NeoFi Collaborative Event Management API

A RESTful backend API for an event scheduling and collaboration system, built with **Django** and **Django REST Framework**.

## 📁 Project Structure - NeoFi Event Management Backend

This document outlines the structure and purpose of key files and directories in the project.

```
ott-movie-platform/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── .env.example
├── neofi_backend/                 # Main Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── events/                       # Django app
│   ├── __init__.py
│   ├── apps.py
│   ├── permissions.py
│   ├── models.py
│   ├── views.py
│   └── urls.py

```

## Root Directory


## Features

- **User Authentication & Authorization**
  - JWT-based token authentication
  - Role-Based Access Control: Owner, Editor, Viewer

- **Event Management**
  - Create, read, update, delete (CRUD) operations on events
  - Support for recurring events with customizable patterns
  - Conflict detection for overlapping events
  - Batch creation of events

- **Collaboration**
  - Share events with granular permissions per user
  - Track edit history with attribution and versioning
  - Rollback to previous versions
  - Changelog with diff visualization (field-level changes)

- **Security & Performance**
  - Input validation and error handling
  - Rate limiting and secure authentication
  - API documentation with Swagger UI
  - Support for JSON serialization (MessagePack optional)

---

## Tech Stack

- Python 3.9+
- Django 4.x
- Django REST Framework
- Simple JWT for token authentication
- drf-yasg for Swagger/OpenAPI documentation
- PostgreSQL (recommended) or SQLite (for dev/testing)

---

## Setup and Running Locally

### Prerequisites

- Python 3.9 or higher
- Git
- PostgreSQL (optional, you can use SQLite for quick testing)

### Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd neofi_backend
```

### 2. Create and activate a virtual environment


  ```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```
### 3. Install Dependencies


```bash
pip install -r requirements.txt
```


### 4. Configure environment variables
Create a .env file or set environment variables as needed for Django secret key, DB credentials, etc.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```


### 7. Run the development server
```bash
python manage.py runserver
```


### 8. Access the API documentation

Open your browser and go to:
http://127.0.0.1:8000/swagger/


## Usage Overview
Register new users: POST /api/auth/register

Login to get JWT token: POST /api/auth/login

Create, list, update, delete events under /api/events/

Share events with other users with specific roles

View and rollback event versions

View changelogs and diffs between versions

## Notes
All API endpoints require authentication except registration and login.

Use the JWT token in the Authorization: Bearer <token> header for protected endpoints.

Permissions are enforced at the event level based on user roles.

Recurring events support uses a JSON-based recurrence pattern (see API docs).

The changelog feature stores detailed edit history with field-level diffs.

