import my_module as mm # Getting the module for the data and the error handling
import tkinter as tk # Tkinter for the standardised GUI
from tkinter import * # Tkinter for the GUI
from tkinter import ttk # Tkinter again
import requests # Requests for getting the APOD data
import io # IO for handling image data and converting it into bytes
from PIL import Image, ImageTk # Pillow for further image handling
from tkcalendar import DateEntry # Tkcalendar 
import ttkbootstrap as tb # ttkbootstrap for the cool looking GUI
from tkinter import PhotoImage # Tkinter for the photoimage object in the GUI
import webbrowser # Webbrowser for opening the APOD in a browser


# Fetch today's APOD
apod = mm.get_apod()

# Main GUI
def GUI():

    """
    Creates the main GUI for the NASA APOD Viewer application.

    Consists of four tabs: Intro, Find, View, and Save.
    - Intro: Welcome message and APOD image.
    - Find: Allows the user to view the daily APOD in the GUI or a as a URL and then save it.
    - View: Allows the user to view an APOD by date and save it.
    - Save: Allows the user to view and remove saved APODs.
    """
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
    # Add an APOD image into the IntroFrame
    image = PhotoImage(file="APOD image.png")
    canvas = Canvas(IntroFrame, width=300, height=200)
    canvas.pack(pady=20, padx=10)
    canvas.create_image( 0, 0, image = image,
                                 anchor = "nw")
   # Add a basic greeting and informative section about the actual system
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
    
    # Label to explain the date input (Easy to understand for the user)
    date_label = Label(ViewFrame, text="Select a date from the calendar and press the Open Image button to view, or manually input with YYYY-MM-DD format!", bg="black", fg="white")
    date_label.pack(pady=10)

    # Create a Date Entry widget for the user to select a date
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

    # Photo_ref is a variable which stores the image reference, checking if an image has been viewed or not, and in this line I dictate photo_ref to be defaulted as none
    photo_ref = None  

    root.mainloop() # Start the GUI


def View_APOD_Button():
    """ Function to view the daily APOD in the GUI as an image inside as well as the explanation. Simply press the button and it will show the APOD of the day."""
    global image_label_find, image_url, photo_ref
    if apod is None: # Check if the APOD is available
        print("Failed to fetch today's APOD. View as a URL instead?")
        return
    try:
        image_url = apod['image_url'] # Getting the image url from the APOD
        response = requests.get(image_url, timeout=10) # Making a timeout procedure for the request of the url (I made this a non-functional requirement where it must be under 10 seconds.)
        response.raise_for_status() # Raise an exception if the request was unsucessful
        image_data = response.content # From the response I get the content of the image
        image = Image.open(io.BytesIO(image_data)) # I open the image using the Pillow library, turning it into bytes
        image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS) # I use Image.LANCZOS to resize the image
        photo = ImageTk.PhotoImage(image) # I convert the image to a PhotoImage object, allowing me to insert it into the Tkinter label
        image_label_find.config(image=photo) # I then configure the Tkinter label to display the image
        image_label_find.photo = photo # To avoid the image from disappearing, I set a reference to the PhotoImage object
        photo_ref = photo # I then set the previously defined photo_ref variable from none to the reference of the PhotoImage
        # I display the title, date, explanation, image URL in the explanation text box
        explanation_text_find.delete(1.0, END)
        explanation_text_find.insert(END, f"Title: {apod['title']}\n")
        explanation_text_find.insert(END, f"Date: {apod['date']}\n")
        explanation_text_find.insert(END, f"Explanation: {apod['explanation']}\n")
        explanation_text_find.insert(END, f"Image URL: {apod['image_url']}\n")
        # Error handling
    except Exception as e: 
        print(f"Error loading image: {e} (Maybe try opening as a URL?)")

def View_APOD_URL_Button():
    """ A basic function to view the APOD as a URL and print the explanation in the console instead."""
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
    """ A function to save the Daily APOD to the favorites list/listbox by a name given by the user."""
    global photo_ref, Saved_APODs, APOD_name_find, explanation_text_find, saved_names
    find_name = APOD_name_find.get()
    saved_names = Saved_APODs.get(0, END) # Check if the name already exists
    if find_name in saved_names:
            print(f"APOD with name '{find_name}' already exists in favorites. Please choose a different name.")
            return
    if not find_name: # Check if the name given is empty
        print("Please enter a name for the Daily APOD.")
        return
    if photo_ref:  # Check if a photo has been viewed
        mm.favorites[find_name] = { # Save the APOD with the name given
            "image": photo_ref,  # Save the image reference
            "explanation": explanation_text_find.get(1.0, END)  # Save the explanation
        }
        print(f"Saved APOD with name '{find_name}' to favorites!")
        Saved_APODs.insert(END, find_name) # Insert the name into the listbox devised before
        print("No APOD image to save.")

# Function to view APOD for the specified date
def View_APOD_Input():
    """ A function to view the APOD from a specified date in the GUI as an image as well as the explanation."""
    global photo_ref, image_label_view, explanation_text_view, Date1
    date = Date1.entry.get() # Get the date from the DateEntry widget
    if date: 
        try:
            apod_data = mm.get_apod(date) # Get the APOD data for the specified date
            
            if apod_data and 'image_url' in apod_data: # Check if the APOD data is valid and has a url
                image_url = apod_data['image_url'] # Get the image url
                response = requests.get(image_url, timeout=10) # Make a request, as well as a timeout illustrated in my non-functional requirements
                response.raise_for_status() # If the request was unsucessful
                image_data = response.content # Get the content of the image
                image = Image.open(io.BytesIO(image_data)) # Then I open the image using the Pillow library
                
                image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS) # I use Image.LANCZOS to resize the image
                photo = ImageTk.PhotoImage(image) # I then convert the image into a PhotoImage object
                image_label_view.config(image=photo) # I then configure the tkinterlabel to display the image
                image_label_view.photo = photo # I set a reference to the PhotoImage object
                photo_ref = photo # I set the photo_ref variable to the reference of the perceived PhotoImage object
                # Display the explanation
                explanation_text_view.delete(1.0, END)
                explanation_text_view.insert(END, f"Title: {apod_data['title']}\n")
                explanation_text_view.insert(END, f"Date: {apod_data['date']}\n")
                explanation_text_view.insert(END, f"Explanation: {apod_data['explanation']}\n")
                explanation_text_view.insert(END, f"Image URL: {apod_data['image_url']}\n")
            else: 
                print("No image found for this date or failed to fetch APOD.")
                # Error handling 
        except Exception as e: 
            print(f"Error fetching APOD for date {date}: {e}")
            print(f"Transitioning to a URL viewing format...  (The APOD is a video with no thumbnail or an interactive one wowowowow)")
            webbrowser.open(image_url)
    else:
        print("Please enter a date in YYYY-MM-DD format.")
    
# Function to save the APOD
def Save_APOD(): 
    """ A function to save the APOD from the View Frame to the favorites list/listbox by a name given by the user."""
    global photo_ref, APOD_name_view
    try:
        name = APOD_name_view.get() # Get the name from the Entry widget
        saved_names = Saved_APODs.get(0, END) # Check if the name already exists
        if name in saved_names:
            print(f"APOD with name '{name}' already exists in favorites. Please choose a different name.")
            return
        if not name: # Check if the name is empty
            print("Please enter a name for the APOD.")
            return
        # Error handling
    except Exception as e: 
        print(f"Error saving APOD: {e}")
        return
    if photo_ref: # Check if a photo has been viewed
        mm.favorites[name] = { # Save the APOD with the name given
            "image": photo_ref, # Save the image reference
            "explanation": explanation_text_view.get(1.0, END) # Save the explanation
        }
        print(f"Saved APOD with name '{name}' to favorites!")
        Saved_APODs.insert(END, name) # Insert the name into the listbox
    else:
        print("No APOD image to save.")

# Function to remove the APOD
def Remove_Saved_APOD():
    """ A function to remove the APOD from the favorites list/listbox by curselection from the user."""
    global Saved_APODs
    try:
        selected_index = Saved_APODs.curselection() # Get the selected index from the listbox, using the curselection function
        if selected_index: # Check if the user selected an APOD
            selected_name = Saved_APODs.get(selected_index) # Get the selected name
            mm.favorites.pop(selected_name, None) # Remove the APOD from the favorites dictionary
            Saved_APODs.delete(selected_index) # Remove the selected name from the listbox
            print(f"Removed APOD '{selected_name}' from favorites!")
            explanation_text_save.delete(1.0, END) # Delete the explanation text
            image_label_save.config(image="") # Delete the image from the label
        else:
            print("Please select an APOD to remove.")
            # Error handling
    except Exception as e:
        print(f"Error removing APOD: {e}")

def View_Saved_APOD():
    """ A function to view the selected APOD from the favorites list/listbox by curselection from the user."""
    global Saved_APODs, photo_ref, image_label_save, explanation_text_save
    selected_index = Saved_APODs.curselection() #Get the selected index from the listbox, using the curselection function
    if selected_index: # Check if the user selected an APOD
        selected_name = Saved_APODs.get(selected_index) # Get the selected name
        selected_apod = mm.favorites.get(selected_name) # Get the selected APOD by name from the favorites dictionary
        if selected_apod: # Check if the selected APOD exists
            image_label_save.config(image=selected_apod["image"]) # Set the image label to that selected APOD
            explanation_text_save.delete(1.0, END) # Delete any previous explanation text
            explanation_text_save.insert(END, selected_apod["explanation"]) # Insert the explanation text of the current APOD
        else:
            # Error handling
            print(f"Error: APOD '{selected_name}' not found in favorites.")
    else:
        print("Please select an APOD to view.")
        
        
# Run the GUI (Wowza!11!1!)
GUI()