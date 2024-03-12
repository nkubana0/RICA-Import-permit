# RICA Import Permit Service

## Introduction

Welcome to the RICA Import Permit Service repository! This service allows you to submit import permit applications and receive email notifications upon successful submission.

## Getting Started

To use this service, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
git clone 

2. **Install Python**: If you don't have Python installed, download and install it from the [official website](https://www.python.org/downloads/).

3. **Install Flask**: Flask is a web framework for Python. Install it using pip, the Python package manager, by running:
```linux
pip install Flask
```

4. **Edit App Configuration**: Open the `app.py` file in the root directory of the repository. You can edit the following variables to configure the email sender and recipient:
- `sender_email`: Your email address for sending notifications.
- `receiver_email`: The recipient's email address where notifications will be sent.

```python
# App Configuration
smtp_server = 'smtp.gmail.com'  # SMTP server for sending emails
smtp_port = 587  # Port for SMTP server (Gmail uses 587)
sender_email = 'sender.email@gmail.com'  # Your email address
receiver_email = 'recipient.email@example.com'  # Recipient's email address
password = 'sender-email-password'  # Your email password
```
Replace your_email@gmail.com with your Gmail address, recipient_email@example.com with the recipient's email address, and your_email_password with your Gmail password.

Run the Application: Start the Flask server by running the following command in the terminal:

```python
python app.py
```
Access the Application: Open a web browser and go to http://localhost:5000 to access the application. You can now fill out the import permit form and submit it.
