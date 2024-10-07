# Key Logger Application

## Overview

The **Key Logger Application** is a Python-based project that records and logs keyboard activities, including key presses and releases. It is built using the `pynput` library to capture keyboard input events and store them in both text and JSON formats. This application is useful for tasks such as activity monitoring, auditing, or research on typing patterns. However, it is important to emphasize that the tool must be used ethically and legally, ensuring that consent is obtained from users whose keystrokes are being logged.

## Features

- Logs key presses, key holds, and key releases.
- Stores logs in two formats: plain text (`logs.txt`) and JSON (`logs.json`).
- Compatible with both **Windows** and **Kali Linux** operating systems.
- Includes timestamps for each keystroke for detailed analysis.
- Option for **stealth mode**, allowing the keylogger to run discreetly.
- Simple graphical user interface (GUI) built using **Tkinter** for ease of use.
- Configurable filtering mechanism to prevent logging sensitive data.

## Implementation Guide

### Requirements
1. **Python 3.x** (Make sure Python is installed and configured in your system's path)
2. **Libraries**:
   - `pynput`: For capturing keyboard events.
   - `tkinter`: For the GUI.
   - `json`: For saving logs in JSON format.

Install required libraries using pip:
```bash
pip install pynput
```

### Running the Application
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AkshayaGopalakrishnan/Key-Logger.git
   cd keylogger-project
   ```

2. **Run the Application**
   Run the keylogger script by executing the following command in your terminal:
   ```bash
   python keylogger.py
   ```

3. **Starting the Key Logger**
   - Launch the application and click on the "Start Key Logger" button to initiate the logging process.
   - All key press events will be captured and stored in `logs.txt` and `logs.json`.

### Log Files
- **logs.txt**: Contains a sequential record of keystrokes in plain text.
- **logs.json**: Stores keystroke data as JSON objects, which can be used for further analysis or parsing.

