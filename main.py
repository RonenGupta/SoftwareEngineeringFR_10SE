import my_module as mm  # Getting the module for the data and the error handling
import tkinter as tk  # Tkinter for the standardised GUI
from tkinter import *  # Tkinter for the GUI
from tkinter import ttk  # Tkinter again
from tkcalendar import DateEntry  # Tkcalendar
import ttkbootstrap as tb  # ttkbootstrap for the cool looking GUI
from tkinter import PhotoImage  # Tkinter for the photoimage object in the GUI
import requests  # Requests for getting the APOD data
import io  # IO for handling image data and converting it into bytes
from PIL import Image, ImageTk  # Pillow for further image handling
import webbrowser  # Webbrowser for opening the APOD in a browser

# Fetch today's APOD
apod = mm.get_apod()

# Main GUI
def GUI():
    """
    Creates the main GUI for the NASA APOD Viewer application.

    Consists of four tabs: Intro, Find, View, and Save.
    - Intro: Welcome message and APOD image.
    - Find: Allows the user to view the daily APOD in the GUI or as a URL and then save it.
    - View: Allows the user to view an APOD by date and save it.
    - Save: Allows the user to view and remove saved APODs.
    """
    global Date1, image_label_find, find_image_frame, photo_ref, image_label_view, explanation_text_find, explanation_text_view, APOD_name_find, explanation_text_save, Saved_APODs, image_label_save, save_image_frame, APOD_name_view, find_label, date_label, NASANOTEBOOK, intro_image

    # Configure the style of the Notebook
    root = tb.Window(themename="cyborg")
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
    NASANOTEBOOK.add(IntroFrame, text='🌌 Introduction 🌌')
    NASANOTEBOOK.add(FindFrame, text='⭐ Find an APOD! ⭐')
    NASANOTEBOOK.add(ViewFrame, text='💫 View and Save an APOD! 💫')
    NASANOTEBOOK.add(SaveFrame, text='🪐 View and Remove Saved APODS! 🪐')

    # -- IntroFrame Code --
    # Add an APOD image into the IntroFrame
    intro_image = PhotoImage(file="APOD image.png")  # Load the APOD image
    canvas = Canvas(IntroFrame, width=300, height=200)
    canvas.pack(pady=20, padx=10)
    canvas.create_image(0, 0, image=intro_image, anchor="nw")  # Use the global reference

    # Add a basic greeting and informative section about the actual system
    intro_label_find = Label(IntroFrame,text="Welcome to the NASA Astronomy Picture of the Day system!\nYou'll be able to:\n1. Find the Daily APOD!\n2. View an APOD of your choice!\n3. Save that APOD for later viewing!\nHave fun in your astronomical fantasies!\nMade by Ronen Gupta",font=("Arial", 10))
    intro_label_find.pack(pady=10)

    # -- FindFrame Code --
    # Add frame to the FindFrame tab for the APOD image
    find_image_frame = Frame(FindFrame, bg="black")
    find_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_find = Label(find_image_frame, bg="black")
    image_label_find.pack(pady=10)

    # FindFrame Button to view the daily APOD
    View_Button = tk.Button(FindFrame,text="View the Daily APOD!",command=lambda: mm.View_APOD_Button(apod, image_label_find, explanation_text_find, photo_ref),fg="white",bg="black")
    View_Button.pack(pady=30)

    # FindFrame Button to view the daily APOD as a URL
    View_URL_Button = tk.Button(FindFrame,text="View the Daily APOD as a URL!",command=lambda: mm.View_APOD_URL_Button(apod),fg="white",bg="black")
    View_URL_Button.pack(pady=30)

    # Explanation, title, URL text for the chosen APOD image
    explanation_text_find = Text(FindFrame, height=15, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_find.pack(pady=10)

    # Label to explain the APOD name input
    find_label = Label(FindFrame,text="Enter a name for the Daily APOD you have viewed to save it:",bg="black",fg="white")
    find_label.pack(pady=10)

    # Entry widget for Daily APOD name
    APOD_name_find = Entry(FindFrame, bg="black", fg="white", insertbackground="white", font=("Arial", 12))
    APOD_name_find.pack(pady=10)

    # Button to save the Daily APOD
    Save_Button = tk.Button(FindFrame,text="Save the Daily APOD!",command=lambda: mm.Save_APOD_Button(photo_ref, Saved_APODs, APOD_name_find, explanation_text_find),fg="white",bg="black")
    Save_Button.pack(pady=10)

    # -- ViewFrame Code --
    # Label to explain the date input
    date_label = Label(ViewFrame,text="Select a date from the calendar and press the Open Image button to view, or manually input with YYYY-MM-DD format!", bg="black",fg="white")
    date_label.pack(pady=10)

    # Create a Date Entry widget for the user to select a date
    Date1 = tb.DateEntry(ViewFrame, dateformat='%Y-%m-%d', bootstyle="dark")
    Date1.pack(pady=10)

    # Button to open the View Frame image
    View_Button = tk.Button(ViewFrame,text="Open Image!",command=lambda: mm.View_APOD_Input(Date1, image_label_view, explanation_text_view, photo_ref),fg="white",bg="black")
    View_Button.pack(pady=10)

    # Add frame to the ViewFrame tab for the APOD image
    view_image_frame = Frame(ViewFrame, bg="black")
    view_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_view = Label(view_image_frame, bg="black")
    image_label_view.pack(pady=10)

    # Add an explanation, title, URL text for the chosen APOD image
    explanation_text_view = Text(ViewFrame, height=15, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_view.pack(pady=10)

    # Label to explain the APOD name input
    view_label = Label(ViewFrame,text="Enter a name for the APOD you have viewed to save it:",bg="black",fg="white")
    view_label.pack(pady=10)

    # Entry widget for APOD name
    APOD_name_view = Entry(ViewFrame, bg="black", fg="white", insertbackground="white", font=("Arial", 12))
    APOD_name_view.pack(pady=10)

    # Button to save the APOD
    Save_Button = tk.Button(ViewFrame,text="Save the APOD!",command=lambda: mm.Save_APOD(photo_ref, APOD_name_view, Saved_APODs, explanation_text_view),fg="white",bg="black")
    Save_Button.pack(pady=10)

    # -- SaveFrame Code --
    # Add frame to the SaveFrame tab for the APOD image
    save_image_frame = Frame(SaveFrame, bg="black")
    save_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_save = Label(save_image_frame, bg="black")
    image_label_save.pack(pady=10)

    # Add an explanation, title, URL text for the chosen APOD image
    explanation_text_save = Text(SaveFrame, height=15, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_save.pack(pady=10)

    # Add a listbox to display the saved APODs
    Saved_APODs = Listbox(SaveFrame, height=15, width=80, bg="black", fg="white", font=("Arial", 10), bd=2, relief="solid")
    Saved_APODs.pack(pady=10)

    # Add a button to view the selected APOD from the saved list
    View_Button = tk.Button(SaveFrame,text="View Selected APOD!",command=lambda: mm.View_Saved_APOD(Saved_APODs, image_label_save, explanation_text_save),fg="white",bg="black")
    View_Button.pack(pady=10)

    # Add a button to remove the selected APOD from the saved list
    Remove_Button = tk.Button(SaveFrame,text="Remove Selected APOD!",command=lambda: mm.Remove_Saved_APOD(Saved_APODs, explanation_text_save, image_label_save),fg="white",bg="black")
    Remove_Button.pack(pady=10)

    # Photo_ref is a variable which stores the image reference
    photo_ref = [None]

    root.mainloop()  # Start the GUI

# Run the GUI (Wowza!1!1)
GUI()