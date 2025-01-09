import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import tkinter as tk
from tkinter import messagebox, filedialog

def start_recording():
    try:
        # Get screen dimensions
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        dim = (width, height)

        # Define codec and create VideoWriter object
        f = cv2.VideoWriter_fourcc(*"mp4v")  # Use 'mp4v' for MP4 files
        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])

        if not output_file:
            return

        output = cv2.VideoWriter(output_file, f, 30.0, dim)

        # Get recording duration
        duration = int(duration_entry.get())
        end_time = time.time() + duration

        start_button.config(state=tk.DISABLED)
        
        while True:
            # Take screenshot
            image = pyautogui.screenshot()
            frame_1 = np.array(image)
            frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
            output.write(frame)

            # Break if time exceeds the duration
            if time.time() > end_time:
                break

        # Release the video writer
        output.release()
        messagebox.showinfo("Success", "Video Captured Successfully")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        start_button.config(state=tk.NORMAL)

# GUI setup
root = tk.Tk()
root.title("Screen Recorder")
root.geometry("400x200")

# Duration label and entry
duration_label = tk.Label(root, text="Duration (seconds):")
duration_label.pack(pady=10)

duration_entry = tk.Entry(root)
duration_entry.pack(pady=10)
duration_entry.insert(0, "15")

# Start button
start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=20)

# Run the GUI
root.mainloop()
