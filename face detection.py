import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize camera
cap = cv2.VideoCapture(0)

# Create GUI window
root = tk.Tk()
root.title("😊 Face Detection GUI")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Heading label
title = tk.Label(root, text="Face Detection using OpenCV", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

# Label to show video
video_label = tk.Label(root)
video_label.pack()

# Function to update video frame
def show_frame():
    ret, frame = cap.read()
    if not ret:
        return

    # Resize and convert color
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert to ImageTk format
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)

    # Display on label
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    # Call again after 10ms
    video_label.after(10, show_frame)

# Exit button
def exit_app():
    cap.release()
    root.destroy()

exit_button = tk.Button(root, text="❌ Exit", font=("Arial", 12), bg="#e74c3c", fg="white", command=exit_app)
exit_button.pack(pady=20)

# Start showing video
show_frame()

# Start GUI loop
root.mainloop()
