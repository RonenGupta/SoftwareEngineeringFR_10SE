import my_module as mm
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import io
from PIL import Image, ImageTk

# Fetch today's APOD initially
apod = mm.get_apod()

# Main GUI function
def GUI():
    global View_Input, image_label_find, find_image_frame, photo_ref, image_label_view
    
    root = tk.Tk()
    root.title("NASA NERD GUIDE")
    root.geometry("900x600")
    root.config(bg="black")

    style = ttk.Style()
    
    # Configure the Notebook style
    style.theme_use("default")  #
    style.configure("TNotebook", background="black", borderwidth=0)  
    style.configure("TNotebook.Tab", background="black", foreground="white", padding=[10, 5], borderwidth=0) 
    style.map("TNotebook.Tab", background=[("selected", "#1a1a1a"), ("active", "#333333")], foreground=[("selected", "white"), ("active", "white")])  # Tab states
    style.configure("TFrame", background="black") 
    
    # Create a Notebook (tabbed interface)
    NASANOTEBOOK = ttk.Notebook(root)
    NASANOTEBOOK.pack(fill='both', expand=True)

    # Create frames for each tab
    FindFrame = ttk.Frame(NASANOTEBOOK)
    ViewFrame = ttk.Frame(NASANOTEBOOK)
    SaveFrame = ttk.Frame(NASANOTEBOOK)
    RemoveFrame = ttk.Frame(NASANOTEBOOK)

    # Add tabs to the Notebook
    NASANOTEBOOK.add(FindFrame, text='Find an APOD!')
    NASANOTEBOOK.add(ViewFrame, text='View an APOD!')
    NASANOTEBOOK.add(SaveFrame, text='Save an APOD!')
    NASANOTEBOOK.add(RemoveFrame, text='Remove an APOD!')

    # Add frame to the FindFrame tab for the APOD image
    find_image_frame = Frame(FindFrame, bg="black")
    find_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_find = Label(find_image_frame, bg="black")
    image_label_find.pack(pady=10)

    # ViewFrame Button to view the daily APOD
    View_Button = tk.Button(FindFrame, text="View the Daily APOD!", command=View_APOD_Button, fg="black", bg="black")
    View_Button.pack(pady=20)

    # Entry widget for date input
    View_Input = Entry(ViewFrame, bg="black", fg="white", insertbackground="white", font=("Arial", 12))
    View_Input.pack(pady=10)  # Add padding for spacing

    # Button to open the View Frame image
    View_Button = tk.Button(ViewFrame, text="Open Image!", command=View_APOD_Input)
    View_Button.pack(pady=10)

    # Add frame to the ViewFrame tab for the APOD image
    view_image_frame = Frame(ViewFrame, bg="black")
    view_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    #Add an image label inside the frame for the APOD image
    image_label_view = Label(view_image_frame, bg="black")
    image_label_view.pack(pady=10)

    # Initialize photo_ref to None
    photo_ref = None

    root.mainloop()

# Function to view the daily APOD
def View_APOD_Button():
    global image_label_find, image_url, photo_ref
    if apod is None:
        print("Failed to detch today's APOD.")
        image_label_find.config(image="", text="Failed to fetch APOD", fg="red")
        return
    try:
        image_url = apod['image_url']
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        # Resize image to fit within a reasonable size (e.g., 600x400 max)
        image = image.resize((min(image.width, 600), min(image.height, 400)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        # Update the image_label with the new image
        image_label_find.config(image=photo)
        image_label_find.photo = photo
        photo_ref = photo
    except Exception as e:
        print(f"Error loading image: {e}")
        image_label_find.config(image="", text=f"Error loading image: {e}", fg="red")

# Function to view APOD for the specified date
def View_APOD_Input():
    global View_Input, photo_ref, image_label_view
    date = View_Input.get()
    if date:
        try:
            apod_data = mm.get_apod(date)  # Fetch APOD for the specified date
            if apod_data and 'image_url' in apod_data:
                image_url = apod_data['image_url']
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                # Resize image to fit within a reasonable size (e.g., 600x400 max)
                image = image.resize((min(image.width, 600), min(image.height, 400)), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                image_label_view.config(image=photo)
                image_label_view.photo = photo
                photo_ref = photo
            else:
                print("No image found for this date or failed to fetch APOD.")
        except Exception as e:
            print(f"Error fetching APOD for date {date}: {e}")
    else:
        print("Please enter a date in YYYY-MM-DD format.")

# Run the GUI
GUI()