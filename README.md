# Communication-Engineering-Bus-Project
Project Title: Networking Component for TicTacToe Game with AI using Raspberry Pi and Sense HAT Module

**Description:**

This GitHub repository contains the code for the networking component of the TicTacToe game with AI implemented using a Raspberry Pi and Sense HAT module. The project was developed as part of the Communications Engineering course (IENG 2530) and is a component of the BUS Project.

**Project Objectives:**

1. Implement an online scoreboard to store match scores or player moves in the cloud.
2. Optionally fetch the scores from the cloud and display them on the Raspberry Pi’s RGB LED matrix or a web page.
3. Design the project considering various implementation possibilities, including networking methods, cloud service providers, and display options.
4. Set up the chosen cloud service (Google Cloud Platform recommended) and integrate it with the Raspberry Pi.
5. Develop Python code to send score or move data to the cloud database.
6. Install a web server (Apache or Flask) on the Raspberry Pi and create a webpage to display the game data stored on the cloud.
7. Utilize networking tools like Wireshark to measure network parameters between the Raspberry Pi and the cloud.
8. Enable the TicTacToe game to be played over the web using a Python web framework like Flask.


**Project Structure:**

1. app.py: Python script for integrating the TicTacToe game with Google Sheets API to implement the online scoreboard.
2. main.py: Main Python script for controlling the game logic and interactions with the Sense HAT module.
3. ttsheet.json: JSON file containing configuration details for accessing the Google Sheets API.
4. webserver/: Directory containing files related to the web server setup.
5. index.html: HTML file for the webpage to display game data.
6. server.py: Python script for the web server implementation using Flask.
7. static/: Directory containing static assets (CSS, JavaScript) for the webpage.


**Usage:**

**Clone the repository to your local machine using the command:**
git clone https://github.com/your_username/tictactoe-networking.git

**Install the required dependencies:**
pip install -r requirements.txt

Configure the ttsheet.json file with your Google Sheets API credentials.

Run the main Python script to start the TicTacToe game:
python main.py

Optionally, run the web server using Flask to display game data on a webpage:
cd webserver/
python server.py


**Contributing:**
Contributions to improve the project are welcome. You can fork the repository, make your changes, and submit a pull request for review.

**License:**
This project is licensed under the MIT License. See the LICENSE file for more details.
