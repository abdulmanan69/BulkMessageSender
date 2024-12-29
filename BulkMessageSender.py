import tkinter as tk
from tkinter import ttk
from threading import Thread
import time
import pyautogui
import random

class AutoMessenger:
    def __init__(self, root):
        self.root = root
        self.running = False

        self.root.title("Auto Messenger")
        self.root.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Input field for the message
        tk.Label(self.root, text="Messages (separate each message with a new line):").pack(pady=5)
        self.message_text = tk.Text(self.root, height=10, width=50)
        self.message_text.pack(pady=5)

        # Input field for the interval
        tk.Label(self.root, text="Time Interval (seconds):").pack(pady=5)
        self.interval_entry = tk.Entry(self.root, width=20)
        self.interval_entry.pack(pady=5)

        # Input field for duration
        tk.Label(self.root, text="Duration (minutes):").pack(pady=5)
        self.duration_entry = tk.Entry(self.root, width=20)
        self.duration_entry.pack(pady=5)

        # Checkbox to include time
        self.include_time_var = tk.BooleanVar()
        self.include_time_checkbox = tk.Checkbutton(self.root, text="Include countdown in messages", variable=self.include_time_var)
        self.include_time_checkbox.pack(pady=5)

        # Button to start/stop the program
        self.start_button = tk.Button(self.root, text="Start", command=self.start_program)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_program, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # Output for countdown messages
        self.output_label = tk.Label(self.root, text="", wraplength=480, justify="center")
        self.output_label.pack(pady=10)

    def start_program(self):
        try:
            self.messages = [msg.strip() for msg in self.message_text.get("1.0", tk.END).splitlines() if msg.strip()]
            self.interval = float(self.interval_entry.get())
            self.duration = float(self.duration_entry.get()) * 60  # Convert minutes to seconds
            if not self.messages or self.interval <= 0 or self.duration <= 0:
                raise ValueError

            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.thread = Thread(target=self.run_messenger)
            self.thread.start()
        except ValueError:
            self.output_label.config(text="Please enter valid input values.")

    def stop_program(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.output_label.config(text="Program stopped.")

    def run_messenger(self):
        start_time = time.time()
        elapsed = 0

        while self.running and elapsed < self.duration:
            remaining_time = self.duration - elapsed
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)

            countdown_message = f"{minutes:02d} min {seconds:02d} sec remain"
            selected_message = random.choice(self.messages)

            final_message = selected_message
            if self.include_time_var.get():
                final_message = f"{countdown_message}\n{selected_message}"

            # Type and send the message
            pyautogui.typewrite(final_message)
            pyautogui.press("enter")

            self.output_label.config(text=f"Sending:\n{final_message}")
            time.sleep(self.interval)

            elapsed = time.time() - start_time

        self.stop_program()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoMessenger(root)
    root.mainloop()
