# Boss-Cafe-App-Using-Python

Boss Cafe App is a simple mobile application built using Python, Kivy, and KivyMD. It provides a login and signup system, allowing users to register and authenticate into the app. This project is designed to help manage user data for a fictional cafe business.

## Features

- **User Authentication**: Users can sign up, log in, and securely access their accounts.
- **SQLite Database**: Stores user information securely in a local SQLite database.
- **Modern UI**: Utilizes KivyMD to create a beautiful and responsive mobile interface with a smooth user experience.
- **Dark Mode Support**: The app is set to use dark mode by default.

## Requirements

Before running the app, ensure you have the following installed:

- Python 3.x
- Kivy (2.0.0 or later)
- KivyMD (latest version)
- SQLite3 (comes pre-installed with Python)

To install the necessary libraries, run:

```bash
pip install kivy kivymd
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/boss-cafe-app.git
    cd boss-cafe-app
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python main.py
    ```

## Usage

- Launch the app and create a new account using the signup feature.
- Log in with your credentials to access the app's features.
- The app will store your data securely in the SQLite database.

## Project Structure

```
boss-cafe-app/
│
├── main.py               # Entry point of the application
├── database/
│   ├── user_data.db      # SQLite database file
│   └── db_helper.py      # Database helper functions
├── screens/
│   ├── login_screen.py   # Login screen logic
│   ├── signup_screen.py  # Signup screen logic
│   └── home_screen.py    # Home screen logic
├── assets/
│   ├── images/           # Image assets
│   └── styles/           # Custom styles
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Kivy](https://kivy.org/) - For the amazing Python framework.
- [KivyMD](https://kivymd.readthedocs.io/) - For the Material Design components.