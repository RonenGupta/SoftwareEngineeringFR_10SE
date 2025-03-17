import my_module as mm
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk


apod = mm.get_apod()

def GUI():
        
        global Save_Input

    
        root = tk.Tk()
        root.title("NASA NERD GUIDE")
        root.geometry("900x600")
        root.config(bg="black")
    
        NASANOTEBOOK = ttk.Notebook(root)
        NASANOTEBOOK.pack(fill='both', expand=True)

        FindFrame = ttk.Frame(NASANOTEBOOK)
        SaveFrame = ttk.Frame(NASANOTEBOOK)
        ViewFrame = ttk.Frame(NASANOTEBOOK)
        RemoveFrame = ttk.Frame(NASANOTEBOOK)

        NASANOTEBOOK.add(FindFrame, text='Find an APOD!')
        NASANOTEBOOK.add(SaveFrame, text='Save an APOD!')
        NASANOTEBOOK.add(ViewFrame, text='View an APOD!')
        NASANOTEBOOK.add(RemoveFrame, text = 'Remove an APOD!')

        View_Button = tk.Button(FindFrame, text="View the Daily APOD!", command=Find_APOD_Button)
        View_Button.pack()


        Label(root, text="Enter a Date Of the APOD to Save It!").pack()

        Label(root, text="Date Input (YYYY-MM-DD)").pack()

        Save_Button = tk.Button(SaveFrame, text="Open Image!", command = Save_APOD_Input)
        Save_Button.pack()
        Save_Input = Entry(SaveFrame, bg= "black", fg= "white")
        Save_Input.pack()


        root.mainloop()


def Find_APOD_Button():
    try:
        print(f"\nTitle: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"Explanation: {apod['explanation']}")
        print(f"Image URL: {apod['image_url']}")
        webbrowser.open(apod['image_url'])
    except Exception as e:
        print(f"Error: {e}")

def Save_APOD_Input():
    
    global Save_Input

    






GUI()

          



    



    






