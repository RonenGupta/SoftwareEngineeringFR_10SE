import my_module as mm
import webbrowser
import tkinter as tk
from tkinter import ttk

apod = mm.get_apod()

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

def ButtonPushed():
     
    print(f"\nTitle: {apod['title']}")
    print(f"Date: {apod['date']}")
    print(f"Explanation: {apod['explanation']}")
    print(f"Image URL: {apod['image_url']}")
    try:
            webbrowser.open(apod['image_url'])
    except Exception as e:
        print(f"Could not open browser: {e}")

Button = tk.Button(makeframe, text="View the Daily APOD!", command=lambda: ButtonPushed).pack()


    

root.mainloop()




