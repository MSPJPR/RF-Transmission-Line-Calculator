
# RF Transmission Line Calculator

This project is a web-based RF Transmission Line Calculator that computes transmission line characteristics based on input frequency and load impedance. Built using Python (Flask), HTML, and CSS, the application is designed to run on mobile devices, especially using the Termux environment on Android.

## Features
- Calculate transmission line properties for RF applications
- User-friendly web interface
- Responsive design for easy access on mobile devices

## Requirements
To run this project, you’ll need:
- Python 3.x
- Flask (for serving the website)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/MSPJPR/rf-transmission-calculator.git
   cd rf-transmission-calculator

2. Install Flask: Since Termux does not allow pip install, you can install Flask using this command:

pkg install python
pip install flask


3. Project Directory Structure: Ensure that your project directory contains the following structure:

rf-transmission-calculator/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css



Usage

1. Start the Flask server: In your Termux environment, navigate to the project directory and run:

python app.py


2. Access the Web App: Open your mobile browser and go to:

http://127.0.0.1:5000


3. Input Values:

Enter the frequency (in MHz) and load impedance (in Ohms).

Click Calculate to get the results.




Code Overview

app.py: Main server-side script for running the Flask application.

index.html: Front-end HTML layout for user interaction.

style.css: CSS file providing styling for the webpage.
