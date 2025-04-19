# Boss Cafe App Using Python

This is a Python-based mobile application for a fictional cafe business. It is built using [Kivy](https://kivy.org/#home) and [KivyMD](https://kivymd.readthedocs.io/en/latest/) for the front-end, and uses **MySQL** for the backend database.

## Features

- User authentication (Sign up / Login)
- Responsive, modern UI using KivyMD
- Dark mode support
- Persistent data storage using MySQL

## Requirements

Make sure you have the following installed:

- Python 3.7+
- MySQL Server
- pip

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Database Configuration

This app uses a **MySQL** database. You need to configure your connection in the file:

```
database/db.py
```

Inside that file, you'll find the following `db_config` dictionary:

```python
DB_CONFIG = {
    "host": "192.168.x.x",   # Replace with your teacher’s local IP address
    "user": "your_username", # Replace with the MySQL username
    "password": "your_password", # Replace with the MySQL password
    "database": "bsit3b"  # Ensure the database exists
}
```

> ⚠️ **Important:** You must be connected to your teacher's WiFi network to connect to the MySQL server successfully.

### Database Setup

Ask your teacher for access credentials and ensure the `boss_cafe` database and required tables are already set up. If not, use the provided SQL schema (if available) or ask your instructor.

## Running the Application

After editing the database configuration:

```bash
python main.py
```

The app will launch with a login/signup screen.

## Screenshots

_Add your screenshots here (optional)._
