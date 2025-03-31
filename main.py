import my_module as mm
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import io
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import ttkbootstrap as tb
from tkinter import PhotoImage
import webbrowser


# Fetch today's APOD
apod = mm.get_apod()

# Main GUI
def GUI():
    global Date1, image_label_find, find_image_frame, photo_ref, image_label_view, explanation_text_find, explanation_text_view, APOD_name_find, explanation_text_save, Saved_APODs, image_label_save, save_image_frame, photo_ref, APOD_name_view, find_label, date_label
    global NASANOTEBOOK
    
    # Configure the style of the Notebook
    root = tb.Window(themename = "cyborg")
    root.title("NASA APOD VIEWER")
    root.geometry("900x600")

    # Create a Notebook 
    NASANOTEBOOK = ttk.Notebook(root)
    NASANOTEBOOK.pack(fill='both', expand=True)

    # Create frames for each tab
    IntroFrame = ttk.Frame(NASANOTEBOOK)
    FindFrame = ttk.Frame(NASANOTEBOOK)
    ViewFrame = ttk.Frame(NASANOTEBOOK)
    SaveFrame = ttk.Frame(NASANOTEBOOK)

    # Add tabs to the Notebook
    NASANOTEBOOK.add(IntroFrame, text = '🌌 Introduction 🌌')
    NASANOTEBOOK.add(FindFrame, text='⭐ Find an APOD! ⭐')
    NASANOTEBOOK.add(ViewFrame, text='💫 View and Save an APOD! 💫')
    NASANOTEBOOK.add(SaveFrame, text='🪐 View and Remove Saved APODS! 🪐')

    # -- IntroFrame Code --
    # Add an APOD into image to the IntroFrame
    image = PhotoImage(file="APOD image.png")
    canvas = Canvas(IntroFrame, width=300, height=200)
    canvas.pack(pady=20, padx=10)
    canvas.create_image( 0, 0, image = image,
                                 anchor = "nw")
   
    intro_label_find = Label(IntroFrame, text="Welcome to the NASA Astronomy Picture of the Day system!\n You'll be able to: \n 1. Find the Daily APOD! \n 2. View an APOD of your choice! \n 3. Save that APOD for later viewing! \n Have fun in your astronomical fantasies! \n Made by Ronen Gupta", font = ("Arial", 10))
    intro_label_find.pack(pady=10)

    # -- FindFrame Code --
    # Add frame to the FindFrame tab for the APOD image
    find_image_frame = Frame(FindFrame, bg="black")
    find_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_find = Label(find_image_frame, bg="black")
    image_label_find.pack(pady=10)

    # FindFrame Button to view the daily APOD
    View_Button = tk.Button(FindFrame, text="View the Daily APOD!", command=View_APOD_Button, fg="white", bg="black")
    View_Button.pack(pady=30)

    # FindFrame Button to view the daily APOD as a url
    View_URL_Button = tk.Button(FindFrame, text="View the Daily APOD as a URL!", command=View_APOD_URL_Button, fg="white", bg="black")
    View_URL_Button.pack(pady=30)

    # Explanation, title, url text for the chosen APOD image
    explanation_text_find = Text(FindFrame, height=15, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_find.pack(pady=10)

    # Label to explain the APOD name input
    find_label = Label(FindFrame, text="Enter a name for the Daily APOD you have viewed to save it:", bg="black", fg="white")
    find_label.pack(pady=10)

    # Entry widget for Daily APOD name
    APOD_name_find = Entry(FindFrame, bg="black", fg="white", insertbackground="white", font=("Arial", 12))
    APOD_name_find.pack(pady=10)

    # Button to save the Daily APOD
    Save_Button = tk.Button(FindFrame, text="Save the Daily APOD!", command=Save_APOD_Button, fg="white", bg="black")
    Save_Button.pack(pady=10)

    # -- ViewFrame Code --
    
    # Label to explain the date input
    date_label = Label(ViewFrame, text="Select a date from the calendar and press the Open Image button to view, or manually input with YYYY-MM-DD format!", bg="black", fg="white")
    date_label.pack(pady=10)

    # Create a Date Entry widget
    Date1 = tb.DateEntry(ViewFrame, dateformat='%Y-%m-%d', bootstyle="dark")
    Date1.pack(pady=10)

    # Button to open the View Frame image
    View_Button = tk.Button(ViewFrame, text="Open Image!", command=View_APOD_Input)
    View_Button.pack(pady=10)

    # Add frame to the ViewFrame tab for the APOD image
    view_image_frame = Frame(ViewFrame, bg="black")
    view_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_view = Label(view_image_frame, bg="black")
    image_label_view.pack(pady=10)

    # Add an explanation, title, url text for the chosen APOD image
    explanation_text_view = Text(ViewFrame, height=15, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_view.pack(pady=10)

    # Label to explain the APOD name input
    date_label = Label(ViewFrame, text="Enter a name for the APOD you have viewed to save it:", bg="black", fg="white")
    date_label.pack(pady=10)

    # Entry widget for APOD name
    APOD_name_view = Entry(ViewFrame, bg="black", fg="white", insertbackground="white", font=("Arial", 12))
    APOD_name_view.pack(pady=10) 

    # Button to save the APOD
    Save_Button = tk.Button(ViewFrame, text="Save the APOD!", command=Save_APOD, fg="white", bg="black")
    Save_Button.pack(pady=10)

    # -- SaveFrame Code --
    # Add frame to the SaveFrame tab for the APOD image
    save_image_frame = Frame(SaveFrame, bg="black")
    save_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_save = Label(save_image_frame, bg="black")
    image_label_save.pack(pady=10)

    # Add an explanation, title, url text for the chosen APOD image
    explanation_text_save = Text(SaveFrame, height=15, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_save.pack(pady=10)

    # Add a listbox to display the saved APODs
    Saved_APODs = Listbox(SaveFrame, height=15, width=80, bg="black", fg="white", font=("Arial", 10), bd=2, relief="solid")
    Saved_APODs.pack(pady=10)

    # Add a button to view the selected APOD from the saved list
    View_Button = tk.Button(SaveFrame, text="View Selected APOD!", command=View_Saved_APOD, fg="white", bg="black")
    View_Button.pack(pady=10) 

    # Add a button to remove the selected APOD from the saved list
    Remove_Button = tk.Button(SaveFrame, text="Remove Selected APOD!", command=Remove_Saved_APOD, fg="white", bg="black")
    Remove_Button.pack(pady=10)

    # Initialize photo_ref to None
    photo_ref = None  

    root.mainloop() # Start the GUI

# Function to view the daily APOD
def View_APOD_Button():
    global image_label_find, image_url, photo_ref
    if apod is None: 
        print("Failed to fetch today's APOD.")
        return
    try:
        image_url = apod['image_url']
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS) # Image.LANZOS for high-quality resampling, given by the PIL library.
        photo = ImageTk.PhotoImage(image)
        image_label_find.config(image=photo)
        image_label_find.photo = photo
        photo_ref = photo
        explanation_text_find.delete(1.0, END)
        explanation_text_find.insert(END, f"Title: {apod['title']}\n")
        explanation_text_find.insert(END, f"Date: {apod['date']}\n")
        explanation_text_find.insert(END, f"Explanation: {apod['explanation']}\n")
        explanation_text_find.insert(END, f"Image URL: {apod['image_url']}\n")
    except Exception as e: 
        print(f"Error loading image: {e}")
        image_label_find.config(image="", text=f"Error loading image: {e}", fg="red")

def View_APOD_URL_Button():
    
    if apod:
        print(f"\nTitle: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"Explanation: {apod['explanation']}")
        print(f"Image URL: {apod['image_url']}")
    try:
        webbrowser.open('https://apod.nasa.gov/apod/astropix.html')
    except Exception as e:
        print(f"Could not open browser: {e}")

def Save_APOD_Button():
    global photo_ref, Saved_APODs, APOD_name_find, explanation_text_find
    find_name = APOD_name_find.get()
    if not find_name:
        print("Please enter a name for the Daily APOD.")
        return
    if photo_ref:  
        mm.favorites[find_name] = {
            "image": photo_ref,  
            "explanation": explanation_text_find.get(1.0, END)  
        }
        print(f"Saved APOD with name '{find_name}' to favorites!")
        Saved_APODs.insert(END, find_name)
        print("No APOD image to save.")

# Function to view APOD for the specified date
def View_APOD_Input():
    global photo_ref, image_label_view, explanation_text_view, Date1
    date = Date1.entry.get()
    if date: 
        try:
            apod_data = mm.get_apod(date)
            
            if apod_data and 'image_url' in apod_data: 
                image_url = apod_data['image_url']
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                
                image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS) # Image.LANZOS for high-quality resampling, given by the PIL library.
                photo = ImageTk.PhotoImage(image)
                image_label_view.config(image=photo)
                image_label_view.photo = photo
                photo_ref = photo 
                explanation_text_view.delete(1.0, END)
                explanation_text_view.insert(END, f"Title: {apod_data['title']}\n")
                explanation_text_view.insert(END, f"Date: {apod_data['date']}\n")
                explanation_text_view.insert(END, f"Explanation: {apod_data['explanation']}\n")
                explanation_text_view.insert(END, f"Image URL: {apod_data['image_url']}\n")
            else: 
                print("No image found for this date or failed to fetch APOD.") 
        except Exception as e: 
            print(f"Error fetching APOD for date {date}: {e}")
            print(f"Transitioning to a URL viewing format...  (The APOD is a video with no thumbnail or an interactive one wowowowow)")
            webbrowser.open(image_url)
    else:
        print("Please enter a date in YYYY-MM-DD format.")
    
# Function to save the APOD
def Save_APOD(): 
    global photo_ref, APOD_name_view
    try:
        name = APOD_name_view.get()
        saved_names = Saved_APODs.get(0, END)
        if name in saved_names:
            print(f"APOD with name '{name}' already exists in favorites. Please choose a different name.")
            return
        if not name:
            print("Please enter a name for the APOD.")
            return
    except Exception as e: 
        print(f"Error saving APOD: {e}")
        return
    if photo_ref: 
        mm.favorites[name] = {
            "image": photo_ref, 
            "explanation": explanation_text_view.get(1.0, END) 
        }
        print(f"Saved APOD with name '{name}' to favorites!")
        Saved_APODs.insert(END, name)  
    else:
        print("No APOD image to save.")

# Function to remove the APOD
def Remove_Saved_APOD():
    global Saved_APODs
    try:
        selected_index = Saved_APODs.curselection()
        if selected_index:
            selected_name = Saved_APODs.get(selected_index)
            mm.favorites.pop(selected_name, None)
            Saved_APODs.delete(selected_index)
            print(f"Removed APOD '{selected_name}' from favorites!")
            explanation_text_save.delete(1.0, END)
            image_label_save.config(image="")
        else:
            print("Please select an APOD to remove.")
    except Exception as e:
        print(f"Error removing APOD: {e}")

def View_Saved_APOD():
    global Saved_APODs, photo_ref, image_label_save, explanation_text_save
    selected_index = Saved_APODs.curselection()
    if selected_index:
        selected_name = Saved_APODs.get(selected_index)
        selected_apod = mm.favorites.get(selected_name)
        if selected_apod:
            image_label_save.config(image=selected_apod["image"])
            explanation_text_save.delete(1.0, END)
            explanation_text_save.insert(END, selected_apod["explanation"])
        else:
            print(f"Error: APOD '{selected_name}' not found in favorites.")
    else:
        print("Please select an APOD to view.")
        
        
# Run the GUI
GUI()