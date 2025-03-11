import my_module as mm
import webbrowser
import tkinter as tk
from tkinter import ttk

apod = mm.get_apod()

def GUI():
    
        root = tk.Tk()
        root.title("NASA NERD GUIDE")
        root.geometry("900x600")
        root.config(bg="black")
    
        NASANOTEBOOK = ttk.Notebook(root)
        NASANOTEBOOK.pack(fill='both', expand=True)

        makeframe = ttk.Frame(NASANOTEBOOK)
        modelframe = ttk.Frame(NASANOTEBOOK)
        dataframe = ttk.Frame(NASANOTEBOOK)
        helpframe = ttk.Frame(NASANOTEBOOK)

        NASANOTEBOOK.add(makeframe, text='Find an APOD!')
        NASANOTEBOOK.add(modelframe, text='Save an APOD!')
        NASANOTEBOOK.add(dataframe, text='View an APOD!')
        NASANOTEBOOK.add(helpframe, text = 'Remove an APOD!')

        Button = tk.Button(makeframe, text="View the Daily APOD!", command=Find_APOD_Button)
        Button.pack()

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

GUI()



    






