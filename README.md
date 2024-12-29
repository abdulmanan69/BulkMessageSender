# Auto Messenger

Auto Messenger is a Python-based desktop application built with `tkinter`. It allows users to send automated messages on any platform by simply typing and sending messages periodically. This tool is ideal for tasks like reminders, spamming (within ethical guidelines), and scheduled messaging.

---

## Features
- Input multiple messages with each message on a new line.
- Set a customizable time interval between messages.
- Define a duration for the messaging session (in minutes).
- Optional countdown timer to display the remaining time in each message.
- Randomized message selection from the provided input.
- Easy-to-use graphical user interface (GUI).

---

## Requirements
To run this application, the following Python libraries need to be installed:

- `tkinter` (comes pre-installed with Python on most systems)
- `pyautogui`

---

## Installation
Make sure you have Python 3 installed on your system. Then, follow these steps to install the required packages:

### Install Required Libraries
Run the following command in your terminal or command prompt to install the necessary dependencies:

```bash
pip install pyautogui
```

---

## How to Use
1. Clone this repository to your local machine or download the script.
2. Run the `Auto Messenger` script by executing the following command:

```bash
python auto_messenger.py
```

3. Enter the following details in the GUI:
   - **Messages**: Input the messages you want to send (one per line).
   - **Time Interval**: Set the time interval (in seconds) between each message.
   - **Duration**: Specify the duration of the messaging session (in minutes).
   - **Include Countdown**: Check the box if you want the remaining time displayed in the messages.

4. Click **Start** to begin sending messages or **Stop** to terminate the session.

---

## Code Overview
The application uses `tkinter` for the GUI, `pyautogui` for simulating typing and sending messages, and `threading` for managing background tasks. Key functions include:

- **Input Validation**: Ensures proper values for time interval and duration.
- **Message Sending**: Types and sends messages in a loop based on the defined time interval and duration.
- **Countdown Timer**: Optionally appends a countdown message to the sent messages.

---

## Example Use Case
If you want to send periodic reminders, for instance:

1. Add messages like:
   - "Take a break!"
   - "Drink water!"
   - "Stretch your legs!"

2. Set the time interval to 300 seconds (5 minutes).
3. Set the duration to 60 minutes.

The app will send these reminders every 5 minutes for an hour.

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

---

## Acknowledgments
- [tkinter](https://docs.python.org/3/library/tkinter.html): For creating the GUI.
- [pyautogui](https://pyautogui.readthedocs.io/): For simulating keyboard input.
