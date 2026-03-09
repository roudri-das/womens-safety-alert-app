# -------------------------------
# Women's Safety Alert App
# Author: Roudri
# Description:
# A simple desktop application that allows women to
# save emergency contacts, send an alert with location,
# and play an alarm sound in danger situations.
# -------------------------------

from tkinter import *
from tkinter import messagebox
import time
import geocoder
from playsound import playsound
import threading
import pygame


pygame.mixer.init()



# -------------------------------
# Function: Play alarm sound
# Plays a loud alarm sound to attract nearby attention
# -------------------------------
def play_alarm():
    try:
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play(-1)   # loop forever
    except Exception as e:
        print("⚠️ Could not play alarm:", e)

def stop_alarm():
    pygame.mixer.music.stop()


# -------------------------------
# Function: Save emergency contacts
# Saves up to 3 contact numbers into a text file
# -------------------------------
def save_contacts():
    contact1 = entry1.get()
    contact2 = entry2.get()
    contact3 = entry3.get()

    if contact1.strip() == "" and contact2.strip() == "" and contact3.strip() == "":
        messagebox.showerror("Error", "Please enter at least one contact before saving.")
        return

    contacts = [contact1, contact2, contact3]

    with open("contacts.txt", "w") as f:
        for number in contacts:
            if number.strip() != "":
                f.write(number + "\n")

    messagebox.showinfo("Contacts Saved", "✅ Contacts saved successfully!")


# -------------------------------
# Function: Send emergency alert
# Shows alert message with location, timestamp, and contacts
# -------------------------------
def send_alert():
    contact1 = entry1.get()
    contact2 = entry2.get()
    contact3 = entry3.get()

    if contact1.strip() == "" and contact2.strip() == "" and contact3.strip() == "":
        messagebox.showerror("Error", "Please enter at least one emergency contact.")
        return
    confirm = messagebox.askyesno(
        "Confirm Alert",
        "Are you sure you want to send the emergency alert?"
    )

    if not confirm:
        return
    # Get user's approximate location using IP
    location = geocoder.ip('me')
    location_text = f"My location: {location.latlng}"

    # Create timestamp for alert clarity
    timestamp = time.strftime("Sent on %Y-%m-%d at %I:%M %p")

    # Read saved emergency contacts
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.readlines()
        contact_text = "".join(contacts)
    except FileNotFoundError:
        contact_text = "No contacts saved!"

    # Display emergency alert message
    messagebox.showinfo(
        "🚨 Emergency Alert",
        f"⚠️ HELP NEEDED!\n\n"
        f"📍 Location: {location.latlng}\n"
        f"{timestamp}\n\n"
        f"📞 Contacts:\n{contact_text}"
    )

    # Update status label after alert
    status_label.config(text="Alert sent to emergency contacts ✅", fg="green")




# -------------------------------
# GUI Window Setup
# -------------------------------
window = Tk()
window.title("Women's Safety Alert App")
window.geometry("400x500")
window.config(bg="#f7f7f7")


# -------------------------------
# App Title
# -------------------------------
title = Label(
    window,
    text="🚨 Women's Safety Alert App",
    font=("Arial", 16, "bold"),
    bg="#f7f7f7",
    fg="#cc0000"
)
title.pack(pady=10)


# -------------------------------
# Emergency Contact Input Fields
# -------------------------------
Label(window, text="Enter up to 3 emergency contact numbers:", bg="#f7f7f7").pack()

entry1 = Entry(window, width=30)
entry1.pack(pady=5)

entry2 = Entry(window, width=30)
entry2.pack(pady=5)

entry3 = Entry(window, width=30)
entry3.pack(pady=5)

info_label = Label(
    window,
    text="⚠️ Please save contacts before sending alert.",
    bg="#f7f7f7",
    fg="blue",
    font=("Arial", 9)
)
info_label.pack(pady=5)
# -------------------------------
# Buttons Section
# -------------------------------
save_button = Button(
    window,
    text="Save Contacts",
    command=save_contacts,
    bg="orange",
    fg="white",
    font=("Arial", 12),
    width=20
)
save_button.pack(pady=10)

send_button = Button(
    window,
    text="Send Alert",
    command=send_alert,
    bg="red",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20
)
send_button.pack(pady=10)

alarm_button = Button(
    window,
    text="Play Alarm",
    command=play_alarm,
    bg="purple",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)
alarm_button.pack(pady=10)
stop_button = Button(
    window,
    text="Stop Alarm",
    command=stop_alarm,
    bg="gray",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)
stop_button.pack(pady=10)


# -------------------------------
# Status Label
# -------------------------------
status_label = Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#f7f7f7"
)
status_label.pack(pady=10)


# -------------------------------
# Footer (Author Credit)
# -------------------------------
footer = Label(
    window,
    text="Made by Roudri ❤️",
    bg="#f7f7f7",
    fg="#4B0082",
    font=("Arial", 12, "bold")
)
footer.pack(side="bottom", pady=10)


# -------------------------------
# Run the Application
# -------------------------------
window.mainloop()




