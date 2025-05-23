# Preliminary Software Engineering Assessment Task 1

***

## Requirements Definition

***

### Functional Requirements

**Data Retrieval: What does the user need to be able to view in the system?**

- A: User must be able to view images from any future chosen NASA API, as well as the information, date, and URL of that NASA image, as well as any external information that the user may want to know, and furthermore save this.

**User Interface: What is required for the user to interact with the system?**

- A: The user must have the NASA API installed, as well as any python functions in the requirements.txt file at the latest version, to access the information displayed in either GUI or Text Based format.

**Data Display: What information does the user need to obtain from the system?**

- A: Information could include NASA APOD images, Earth Imaging, Mars Rover Photos/Weather and Near Earth Object Services.

***

### Non-Functional Requirements

**Performance: How well does the system need to perform?**

- A: The system must be able to complete basic operations in under 10 seconds, including displaying certain images of APODS and must be able to give access to the user in saving certain information.

**Reliability: How reliable does the system and data need to be?**

- A: As the information derived is specifically space related, the system and data must be specifically from NASA, the most notable organisation I can think of.

**Usability and Accessibility: How easy to navigate does the system need to be? What instructions will we need for users to access the system?**

- A: The system should be relatively easy to navigate, as it will most probably be GUI based leading to a quick and easy access of the data. Following the information in the README, cloning the repository and then installing any of the python commands in the requirements file will allow for accessing the system.

***

### Functional Specifications

**User Requirements - What does the user need to be able to do? List all specifications here.**

- A: User must be able to:

1. View any NASA images from the API's chosen.

2. Be able to save and remove these images to a favourites list and the information related with it. 

3. If any graphs are involved, they should be able to view them in matplotlib graphs and furthermore save them to a list.

**Inputs & Outputs - What inputs will the system need to accept and what outputs will it need to display?**

- A: Inputs and Ouputs accepted and displayed would be:

1. Must accept input of a mouse click on a button in the GUI, it will display any information, images, or graphs regarding that mouse click in that position.

2. If it is text based, it should be able to accept integers as an input such as option 1, option 2, etc. It would then output the image in a pywebview function tab, and the related information would also be outputted with the corresponding information of saving any data.

**Core Features - At its core, what specifically does the program need to be able to do?**

- A: The program must be able to read data from any chosen NASA API and output that information to the user, with the option of saving the data and viewing it on a later date if necessary.

**User Interaction - How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?**

- A: Either command-line or GUI, it should be able to provide choices such as option 1 etc for text based, and for GUI must be able to depict any tabs for viewing certain information such as graphs in a seperate tab, saved information, daily APOD, etc.

**Error Handling - What possible errors could you face that need to be handled by the system?**

- A: Possibly the images may not render in the GUI due to network issues or the NASA API in general. To combat this, I make custom error messages in relation to those problems and suggest fixes for the problem at hand.

***

### Non-Functional Specifications

**Performance - How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?**

- A: Under 10 seconds of loading time for an image and the text will suffice for user engagement. Keeping the code clean and using functions and loops will allow for the peak efficiency of the program.

**Usability / Accessibility - How might you make your application more accessible? What could you do with the User Interface to improve usability?**

- A: Use a notebook function in the GUI. By doing so, I can maximise accessibility and usability, as functions are easily viewable. 

**Reliability - What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Duplicate data? API retrieval crash?**

- A: API retrieval may pose an issue, due to problems with the NASA API in general or network issues. As for any data issues, NASA will have the highest data integrity and duplicate data can be solved by preventing the idea of saving information twice in a list. Additionally, a name can be given to the data in order to sort the list.

***

### Use Case

Actor: User (Astronomer / Space Nerd)

Preconditions: Internet acess, NASA API's, Python Modules (Matplotlib, Tkinter, Pandas, Requests, Pillow,  etc.)

Main Flow:

1. Open System - User opens the GUI, revealing the options that can be made.

2. Search NASA Image/Information - User can find a NASA image or any information based on date or they can derive the newest or oldest API based on user preferences.

3. Save NASA Image/Information - User can save the image and the information corresponding to that in a list, giving it a custom name.

4. Visualise NASA Image/Information - User can visualise the image and the information next to that corresponding image, based on a call from the list they saved it in or by a certain date.

5. Remove Image/Information - User can remove the image and corresponding information through the date or the name they have given it in the list.

Postconditions: Image and Information is retrieved, stored, or removed successfully.

***

## Design

***

### Gantt Chart
- Link for the Gantt Chart: https://docs.google.com/spreadsheets/d/17w6MqNqxJE3_En6HbhOfRSIty1XGfrXXg17LGQqG-lg/edit?usp=sharing

- Image: ![Software Engineering Preliminary Gantt Chart](./Software%20Engineering%20Preliminary%20Gantt%20Chart.png)
***

### Structure Chart
- Link for the Structure Chart: https://lucid.app/lucidchart/4fa442b4-c20c-47bb-b0a6-0d82bf8ebd6c/edit?invitationId=inv_56e13952-b4da-4ceb-847f-882dd6c4d600

- Image: ![NASA APOD Structure Chart](./NASA_APOD_StructureChart.png)

***

### Algorithms

- Main Routine Pseudocode:
 ``` python
BEGIN main()
    WHILE user_input is NOT "EXIT"
        INPUT user_input
        IF API REQUEST Valid THEN
            DISPLAY GUI and "IntroFrame"

            # --FindFrame Segment--
            IF user_input is "FindFrame" THEN
                DISPLAY FindFrame
                IF user_input is View_APOD_Button THEN
                    DISPLAY View_APOD_Button
                ELSEIF user_input is View_APOD_URL_Button THEN
                    DISPLAY View_APOD_URL_Button
                    IF user_input is Save_APOD_Button THEN
                        Save_APOD_Button
                    ELSE
                        CONTINUE
                    ENDIF
                ENDIF
            ENDIF

            # --ViewFrame Segment--
            ELSEIF user_input is "ViewFrame" THEN
                DISPLAY ViewFrame
                IF user_input is View_APOD_Input THEN
                    DISPLAY View_APOD_Input
                    IF user_input is Save_APOD THEN
                        Save_APOD
                    ELSE
                        CONTINUE
                    ENDIF
                ENDIF
            ENDIF

            # --SaveFrame Segment--
            ELSEIF user_input is "SaveFrame" THEN
                DISPLAY SaveFrame
                IF user_input is View_Saved_APOD THEN
                    IF APOD CLICKED THEN
                        DISPLAY View_Saved_APOD
                    ELSE
                        PRINT "Please select an APOD to view."
                        CONTINUE
                    ENDIF
                ELSEIF user_input is Remove_Saved_APOD THEN
                    IF APOD CLICKED THEN
                        DISPLAY Remove_Saved_APOD
                    ELSE
                        PRINT "Please select an APOD to remove."
                        CONTINUE
                    ENDIF
                ENDIF
            ENDIF
        ELSE
            PRINT "API Request Failed"
            EXIT
        ENDIF
    ENDWHILE
END main()
 ```
 ***

- Link for the Main Routine Flowchart (Too big to fit in this .md): https://lucid.app/lucidchart/b50196f5-49ed-465e-8f45-b1e15e7e4d8e/edit?viewport_loc=-2078%2C-1181%2C9251%2C5290%2C0_0&invitationId=inv_610aec57-f4fc-4c3b-993a-5f64bac6f6fe
***
- First Subroutine Pseudocode - Save_APOD

``` python
BEGIN Save_APOD
    TRY
        INPUT name FROM APOD_name_view
        IF name is EMPTY THEN
            PRINT "Please enter a name for the APOD"
            RETURN
        ENDIF
    EXCEPT Exception as e
        PRINT "Error saving APOD: ", e
        RETURN
    ENDTRY

    IF photo_ref EXISTS THEN
        STORE photo_ref and explanation_text_view in mm.favorites USING name AS KEY
        ADD name to Saved_APODs LISTBOX
    ELSE
        PRINT "No APOD image to save."
    ENDIF
END Save_APOD
```
***
- Link for the First Subroutine Flowchart: https://lucid.app/lucidchart/516ca3db-76b3-485d-ab0b-17b3647f4b77/edit?viewport_loc=-219%2C-190%2C3384%2C1935%2C0_0&invitationId=inv_76db8ead-9001-411f-ac58-8684e18652de
***
- Image for First Subroutine Flowchart: ![First-Subroutine-Flowchart](./First-Subroutine-Flowchart.png)
***
- Second Subroutine Pseudocode - Remove_Saved_APOD

``` python
BEGIN Remove_Saved_APOD
    TRY
        GET selected_index from Saved_APODs LISTBOX
        IF selected_index is EMPTY THEN
            PRINT "Please select an APOD to remove."
            RETURN
        ENDIF

        GET selected_name from Saved_APODs USING selected_index
        REMOVE selected_name FROM mm.favorites DICTIONARY
        DELETE selected_name FROM Saved_APODs LISTBOX
        PRINT f"Removed APOD ", selected_name, " from favorites!"

        CLEAR explanation_text_save
        CLEAR image_label_save
    EXCEPT Exception as e
        PRINT "Error removing APOD: ", e
    ENDTRY
END Remove_Saved_APOD
```
***
- Link for Second Subroutine Flowchart: https://lucid.app/lucidchart/5b3eae51-5eb8-4f83-b1bc-f728d09e4a2d/edit?viewport_loc=-849%2C1548%2C4379%2C2504%2C0_0&invitationId=inv_ce7106f4-f38a-410a-9e19-cf23e82b9b30
***
- Image for the Second Subroutine Flowchart: ![Second-Subroutine-Flowchart](./Second-Subroutine-Flowchart.png)

***

### Data Dictionary
- Link for the Data Dictionary: https://docs.google.com/document/d/1pd_3o4khOgFJZ_VoCDkAaHMMozaAgS-jTSy6FWuxrEM/edit?pli=1&tab=t.0
***

## Development

### main.py

```python
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

# Run the GUI
GUI()
```

### my_module.py

```python
import requests  # For getting data from the NASA API (Obviously)
from PIL import Image, ImageTk  # Pillow for image handling
import io  # For handling image data and converting it into bytes
import webbrowser  # For opening the APOD in a browser

# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"  # APOD URL
API_KEY = "c1R5mNKBtlpRqXwI29rUPfRJvcTPbE8drebdwrEI"  # Replace with your own API key

# Dictionary to store favorite APOD
favorites = {}

def get_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day (APOD)."""
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date

    try:
        response = requests.get(APOD_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
    except KeyError as e:
        print(f"Could not find today's APOD URL. ({e})")
    except requests.exceptions.ConnectionError as e:
        print(f"Network error: Could not connect to NASA API. ({e})")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out. The NASA API might be slow or your connection is unstable.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch APOD: {e}")
        return None
    except ValueError:
        print("Invalid response from NASA API (not JSON).")
        return None

def View_APOD_Button(apod, image_label_find, explanation_text_find, photo_ref):
    """View the daily APOD in the GUI."""
    if apod is None:
        print("Failed to fetch today's APOD. View as a URL instead?")
        return
    try:
        image_url = apod['image_url']
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label_find.config(image=photo)
        image_label_find.photo = photo
        photo_ref[0] = photo
        explanation_text_find.delete(1.0, "end")
        explanation_text_find.insert("end", f"Title: {apod['title']}\n")
        explanation_text_find.insert("end", f"Date: {apod['date']}\n")
        explanation_text_find.insert("end", f"Explanation: {apod['explanation']}\n")
        explanation_text_find.insert("end", f"Image URL: {apod['image_url']}\n")
    except Exception as e:
        print(f"Error loading image: {e} (Maybe try opening as a URL?)")

def View_APOD_URL_Button(apod):
    """View the APOD as a URL."""
    if apod:
        print(f"\nTitle: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"Explanation: {apod['explanation']}")
        print(f"Image URL: {apod['image_url']}")
    try:
        webbrowser.open(apod['image_url'])
    except Exception as e:
        print(f"Could not open browser: {e}")

def Save_APOD_Button(photo_ref, Saved_APODs, APOD_name_find, explanation_text_find):
    """Save the Daily APOD to the favorites list."""
    find_name = APOD_name_find.get()
    saved_names = Saved_APODs.get(0, "end")
    if find_name in saved_names:
        print(f"APOD with name '{find_name}' already exists in favorites. Please choose a different name.")
        return
    if not find_name:
        print("Please enter a name for the Daily APOD.")
        return
    if photo_ref[0]:
        favorites[find_name] = {
            "image": photo_ref[0],
            "explanation": explanation_text_find.get(1.0, "end")
        }
        print(f"Saved APOD with name '{find_name}' to favorites!")
        Saved_APODs.insert("end", find_name)
    else:
        print("No APOD image to save.")

def View_APOD_Input(Date1, image_label_view, explanation_text_view, photo_ref):
    """View the APOD for a specified date."""
    date = Date1.entry.get()
    if date:
        try:
            apod_data = get_apod(date)
            if apod_data and 'image_url' in apod_data:
                image_url = apod_data['image_url']
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                image_label_view.config(image=photo)
                image_label_view.photo = photo
                photo_ref[0] = photo
                explanation_text_view.delete(1.0, "end")
                explanation_text_view.insert("end", f"Title: {apod_data['title']}\n")
                explanation_text_view.insert("end", f"Date: {apod_data['date']}\n")
                explanation_text_view.insert("end", f"Explanation: {apod_data['explanation']}\n")
                explanation_text_view.insert("end", f"Image URL: {apod_data['image_url']}\n")
            else:
                print("No image found for this date or failed to fetch APOD.")
        except Exception as e:
            print(f"Error fetching APOD for date {date}: {e}")
    else:
        print("Please enter a date in YYYY-MM-DD format.")

def Save_APOD(photo_ref, APOD_name_view, Saved_APODs, explanation_text_view):
    """Save the APOD from the View Frame."""
    name = APOD_name_view.get()
    saved_names = Saved_APODs.get(0, "end")
    if name in saved_names:
        print(f"APOD with name '{name}' already exists in favorites. Please choose a different name.")
        return
    if not name:
        print("Please enter a name for the APOD.")
        return
    if photo_ref[0]:
        favorites[name] = {
            "image": photo_ref[0],
            "explanation": explanation_text_view.get(1.0, "end")
        }
        print(f"Saved APOD with name '{name}' to favorites!")
        Saved_APODs.insert("end", name)
    else:
        print("No APOD image to save.")

def Remove_Saved_APOD(Saved_APODs, explanation_text_save, image_label_save):
    """Remove the selected APOD from the favorites list."""
    selected_index = Saved_APODs.curselection()
    if selected_index:
        selected_name = Saved_APODs.get(selected_index)
        favorites.pop(selected_name, None)
        Saved_APODs.delete(selected_index)
        print(f"Removed APOD '{selected_name}' from favorites!")
        explanation_text_save.delete(1.0, "end")
        image_label_save.config(image="")
    else:
        print("Please select an APOD to remove.")

def View_Saved_APOD(Saved_APODs, image_label_save, explanation_text_save):
    """View the selected APOD from the favorites list."""
    selected_index = Saved_APODs.curselection()
    if selected_index:
        selected_name = Saved_APODs.get(selected_index)
        selected_apod = favorites.get(selected_name)
        if selected_apod:
            image_label_save.config(image=selected_apod["image"])
            explanation_text_save.delete(1.0, "end")
            explanation_text_save.insert("end", selected_apod["explanation"])
        else:
            print(f"Error: APOD '{selected_name}' not found in favorites.")
    else:
        print("Please select an APOD to view.")
```
## Integration/Testing and Debugging

### 1. First Commit - Basic Text Based GUI

```python
import my_module as mm
import webbrowser

def display_menu():
    """Display the main menu."""
    print("\n=== NASA APOD Explorer ===")
    print("1. View Today's APOD")
    print("2. Add Today's APOD to Favorites")
    print("3. View Favorites")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-3): ")
        try:
            choice = int(choice)
            if choice == 0:
                print("Goodbye!")
                break

            elif choice == 1:
                apod = mm.get_apod()
                if apod:
                    print(f"\nTitle: {apod['title']}")
                    print(f"Date: {apod['date']}")
                    print(f"Explanation: {apod['explanation']}")
                    print(f"Image URL: {apod['image_url']}")
                    try:
                        webbrowser.open(apod['image_url'])
                    except Exception as e:
                        print(f"Could not open browser: {e}")

            elif choice == 2:
                apod = mm.get_apod()
                if apod:
                    name = input("Enter a name for this favorite: ")
                    mm.add_favorite(name, apod)
                    print(f"Added '{name}' to favorites!")

            elif choice == 3:
                if mm.favorites:
                    print("\nFavorites:")
                    for name, data in mm.favorites.items():
                        print(f"- {name}: {data['title']}")
                        print(f"  Date: {data['date']}")
                        print(f"  URL: {data['image_url']}")
                else:
                    print("No favorites yet!")

            else:
                print("Invalid choice. Please select 0-3.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":

    main()
```
- Explanation: Created a simple text based GUI utilising the example NASA module.py in the Gitbook given.

### 2. Second Commit - Basic GUI with Tkinter (Still Errors)

``` python
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

```
- Explanation: Created a simple button pushing GUI to reveal an APOD in a webbrowser. I reused the notebook code from my previous data analysis project, as to why the notebook tab names are not NASA related. I did not find an error for this stage in development yet.

### 3. Third Commit - Basic GUI with Tkinter (Fixed)

``` python
from tkinter import ttk

apod = mm.get_apod()

root = tk.Tk()
root.title("NASA NERD GUIDE")
root.geometry("900x600")
root.config(bg="black")
def GUI():
    
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
            webbrowser.open(apod['image_url'])
        print(f"\nTitle: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"Explanation: {apod['explanation']}")
        print(f"Image URL: {apod['image_url']}")
        webbrowser.open(apod['image_url'])
    except Exception as e:
        print(f"Could not open browser: {e}")
        print(f"Error: {e}")

GUI()

Button = tk.Button(makeframe, text="View the Daily APOD!", command=lambda: ButtonPushed).pack()


    

root.mainloop()

```
- Explanation: I fixed this and made it more simple for me to understand (I did not understand try and except yet) and I seperated the command from the button in the line, as one of my goals in my previous commit. I for some reason kept the old line after the GUI, but even so the code snippet would still work.

### 4. Fourth Commit - Worked on the View APOD Tab (I dont know why I called it the Save APOD Tab)

``` python
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
def GUI():
        NASANOTEBOOK = ttk.Notebook(root)
        NASANOTEBOOK.pack(fill='both', expand=True)

        makeframe = ttk.Frame(NASANOTEBOOK)
        modelframe = ttk.Frame(NASANOTEBOOK)
        dataframe = ttk.Frame(NASANOTEBOOK)
        helpframe = ttk.Frame(NASANOTEBOOK)
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

        NASANOTEBOOK.add(makeframe, text='Find an APOD!')
        NASANOTEBOOK.add(modelframe, text='Save an APOD!')
        NASANOTEBOOK.add(dataframe, text='View an APOD!')
        NASANOTEBOOK.add(helpframe, text = 'Remove an APOD!')
        Label(root, text="Date Input (YYYY-MM-DD)").pack()

        Save_Button = tk.Button(SaveFrame, text="Open Image!", command = Save_APOD_Input)
        Save_Button.pack()
        Save_Input = Entry(SaveFrame, bg= "black", fg= "white")
        Save_Input.pack()

        Button = tk.Button(makeframe, text="View the Daily APOD!", command=Find_APOD_Button)
        Button.pack()

        root.mainloop()


def Find_APOD_Button():
    try:
        print(f"\nTitle: {apod['title']}")
def Find_APOD_Button():
    except Exception as e:
        print(f"Error: {e}")

def Save_APOD_Input():
    
    global Save_Input

GUI()

```
- Explanation: A very messy and failed interpretation of this, even I cannot read it. This was unfinished, and will be depicted in the fifth commit.

### 5. Fifth Commit - Worked on the View APOD Tab (Fixed)

``` python
import my_module as mm
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import io
from PIL import Image, ImageTk

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
        image = image.resize((min(image.width, 600), min(image.height, 400)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
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
            apod_data = mm.get_apod(date)  
            if apod_data and 'image_url' in apod_data:
                image_url = apod_data['image_url']
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
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

```
- Explanation: A very long and lethargic commit, I did much research on how to fetch an APOD on a specific date, inside the GUI. This worked through the fact that I used numerous new modules (io, pillow, requests) to process the APOD image. I did this through getting the input of the date from the user as a parameter (which I added in the module), along with the get_apod function, and then initialising it with the requests module to retrieve the url with an HTTP request as well as checking if it was successful or not with the function response.raise_for_status(), then from the Pillow library to open the image for the binary data and following using a conversion technique utilised in Tkinter to make the processed image into a PhotoImage, a very long process but worthwhile due to the tolerance of good image quality, and then outputting it with the line image_label_view_config(image=photo), updating the widget in the GUI to display the new image. I also stored this image in a photo_ref variable for further use in the future such as saving it, which was one of my development plans. I did the same for the daily APOD without getting the date parameter from the user, and included some error handling as well.

### 6. Sixth Commit - Explanation Labels (Errors Present)

``` python
apod = mm.get_apod()

# Main GUI function
def GUI():
   
    global View_Input, image_label_find, find_image_frame, photo_ref, image_label_view, explanation_text_frame
    
    root = tk.Tk()
    root.title("NASA NERD GUIDE")
def GUI():
    View_Button = tk.Button(FindFrame, text="View the Daily APOD!", command=View_APOD_Button, fg="black", bg="black")
    View_Button.pack(pady=30)

    # Explanation label for the chosen APOD image
    explanation_text_frame = Label(FindFrame, bg="black")
    explanation_text_frame.pack(pady=10)

    # Label to explain the date input
    date_label = Label(ViewFrame, text="Enter a date in YYYY-MM-DD format:", bg="black", fg="white")
    date_label.pack(pady=10)

        print(f"Error loading image: {e}")
        image_label_find.config(image="", text=f"Error loading image: {e}", fg="red")

# Function to view title, explanation, date url of the chosen APOD in FindFrame
def Find_APOD_Explanation():
    global explanation_text_frame

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
                # Resize image to fit within a reasonable size)
                image = image.resize((min(image.width, 2000), min(image.height, 1000)), Image.LANCZOS)
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

```
- Explanation: I started working on explanation labels, meaning that the explanation would be viewable along with the image. The function was still unfinished, so there was not that much progress from the 5th Commit.

### 7. Seventh Commit - Explanation Labels (Fixed)

``` python
apod = mm.get_apod()

# Main GUI function
def GUI():
    
    global View_Input, image_label_find, find_image_frame, photo_ref, image_label_view, explanation_text_find, explanation_text_view
    global NASANOTEBOOK
    
    root = tk.Tk()
    root.title("NASA NERD GUIDE")
def GUI():
    View_Button = tk.Button(FindFrame, text="View the Daily APOD!", command=View_APOD_Button, fg="black", bg="black")
    View_Button.pack(pady=30)

    # Explanation, title, url text for the chosen APOD image
    explanation_text_find = Text(FindFrame, height=10, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_find.pack(pady=10)

    # Label to explain the date input
    date_label = Label(ViewFrame, text="Enter a date in YYYY-MM-DD format:", bg="black", fg="white")
def GUI():
    view_image_frame = Frame(ViewFrame, bg="black")
    view_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_view = Label(view_image_frame, bg="black")
    image_label_view.pack(pady=10)

    # Add an explanation, title, url text for the chosen APOD image
    explanation_text_view = Text(ViewFrame, height=10, width=80, bg="black", fg="white", wrap="word", font=("Arial", 10))
    explanation_text_view.pack(pady=10)

    # Initialize photo_ref to None
    photo_ref = None

def View_APOD_Button():
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        # Resize image to fit within a reasonable size)
        image = image.resize((min(image.width, 600), min(image.height, 400)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        # Update the image_label with the new image
        image_label_find.config(image=photo)
        image_label_find.photo = photo
        photo_ref = photo

        # Update the explanation_text with the APOD details
        explanation_text_find.delete(1.0, END)
        explanation_text_find.insert(END, f"Title: {apod['title']}\n")
        explanation_text_find.insert(END, f"Date: {apod['date']}\n")
        explanation_text_find.insert(END, f"Explanation: {apod['explanation']}\n")
        explanation_text_find.insert(END, f"Image URL: {apod['image_url']}\n")
    except Exception as e:
        print(f"Error loading image: {e}")
        image_label_find.config(image="", text=f"Error loading image: {e}", fg="red")

# Function to view APOD for the specified date
def View_APOD_Input():
    global View_Input, photo_ref, image_label_view, explanation_text_view
    date = View_Input.get()
    if date:
        try:
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                # Resize image to fit within a reasonable size)
                image = image.resize((min(image.width, 600), min(image.height, 400)), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                image_label_view.config(image=photo)
                image_label_view.photo = photo
                photo_ref = photo
                # Update the explanation_text with the APOD details
                explanation_text_view.delete(1.0, END)
                explanation_text_view.insert(END, f"Title: {apod_data['title']}\n")
                explanation_text_view.insert(END, f"Date: {apod_data['date']}\n")
                explanation_text_view.insert(END, f"Explanation: {apod_data['explanation']}\n")
                explanation_text_view.insert(END, f"Image URL: {apod_data['image_url']}\n")
            else:
                print("No image found for this date or failed to fetch APOD.")
        except Exception as e:
            print(f"Error fetching APOD for date {date}: {e}")
    else:
        print("Please enter a date in YYYY-MM-DD format.")

# Run the GUI
GUI()

```

- Explanation: I fixed the explanation labels, and made them for both the FindFrame and the ViewFrame, this worked due to the original get_apod() function, where I derived the date, title, url, and explanation and integrated it into a text widget. I also configured some notebook styling.

### 8. Eighth Commit - Save Function and Remove Function (Finished)

``` python
import my_module as mm
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import io
from PIL import Image, ImageTk

# Fetch today's APOD
apod = mm.get_apod()

# Main GUI
def GUI():
    global View_Input, image_label_find, find_image_frame, photo_ref, image_label_view, explanation_text_find, explanation_text_view, APOD_name_find, explanation_text_save, Saved_APODs, image_label_save, save_image_frame, photo_ref, APOD_name_view, find_label, date_label
    global NASANOTEBOOK
    
    root = tk.Tk()
    root.title("NASA NERD GUIDE")
    root.geometry("900x600")
    root.config(bg="black")

    style = ttk.Style()
    
    # Notebook style
    style.theme_use("default")  #
    style.configure("TNotebook", background="black", borderwidth=0)  
    style.configure("TNotebook.Tab", background="black", foreground="white", padding=[10, 5], borderwidth=0) 
    style.map("TNotebook.Tab", background=[("selected", "#1a1a1a"), ("active", "#333333")], foreground=[("selected", "white"), ("active", "white")])  # Tab states
    style.configure("TFrame", background="black") 
    
    # Create a Notebook 
    NASANOTEBOOK = ttk.Notebook(root)
    NASANOTEBOOK.pack(fill='both', expand=True)

    # Create frames for each tab
    FindFrame = ttk.Frame(NASANOTEBOOK)
    ViewFrame = ttk.Frame(NASANOTEBOOK)
    SaveFrame = ttk.Frame(NASANOTEBOOK)

    # Add tabs to the Notebook
    NASANOTEBOOK.add(FindFrame, text='Find an APOD!')
    NASANOTEBOOK.add(ViewFrame, text='View and Save an APOD!')
    NASANOTEBOOK.add(SaveFrame, text='View and Remove Saved APODS!')

    # -- FindFrame Code --
    # Add frame to the FindFrame tab for the APOD image
    find_image_frame = Frame(FindFrame, bg="black")
    find_image_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Add an image label inside the frame for the APOD image
    image_label_find = Label(find_image_frame, bg="black")
    image_label_find.pack(pady=10)

    # ViewFrame Button to view the daily APOD
    View_Button = tk.Button(FindFrame, text="View the Daily APOD!", command=View_APOD_Button, fg="black", bg="black")
    View_Button.pack(pady=30)

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
    Save_Button = tk.Button(FindFrame, text="Save the Daily APOD!", command=Save_APOD_Button, fg="black", bg="black")
    Save_Button.pack(pady=10)

    # -- ViewFrame Code --
    # Label to explain the date input
    date_label = Label(ViewFrame, text="Enter a date in YYYY-MM-DD format:", bg="black", fg="white")
    date_label.pack(pady=10)
    
    # Entry widget for date input
    View_Input = Entry(ViewFrame, bg="black", fg="white", insertbackground="white", font=("Arial", 12))
    View_Input.pack(pady=10)  # Add padding for spacing

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
    Save_Button = tk.Button(ViewFrame, text="Save the APOD!", command=Save_APOD, fg="black", bg="black")
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
    View_Button = tk.Button(SaveFrame, text="View Selected APOD!", command=View_Saved_APOD, fg="black", bg="black")
    View_Button.pack(pady=10) 

    # Add a button to remove the selected APOD from the saved list
    Remove_Button = tk.Button(SaveFrame, text="Remove Selected APOD!", command=Remove_Saved_APOD, fg="black", bg="black")
    Remove_Button.pack(pady=10)

    # Initialize photo_ref to None
    photo_ref = None  

    root.mainloop() # Start the GUI

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
    global View_Input, photo_ref, image_label_view, explanation_text_view
    date = View_Input.get()  
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
    else:
        print("Please enter a date in YYYY-MM-DD format.")
    
# Function to save the APOD
def Save_APOD(): 
    global photo_ref, APOD_name_view
    try:
        name = APOD_name_view.get()
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
```

- Explanation: I finished creating the save and remove functions of the APOD GUI, and integrated it into only 3 Tabs. The major differences are the buttons and text widgets integrated, not only that but also 2 new functions I utilised in the Tkinter module called curselection and listbox. These 2 functions allowed me to store and select my saved apods at ease. Multiple new functions were also made to create this save and remove feature, and I added saving the daily apod, saving the APOD with the date given by the user, viewing these in the menu tab with the explanation, and removing these, using indexing features in the listbox function. This took tutorials from NASA API and Tkinter GUI videos/links, specifically from Codemy (Link: https://www.youtube.com/watch?v=wEv3BworNK8&t=1s&ab_channel=Codemy.com) and a video from Alta3 Research (Link: https://www.youtube.com/watch?v=UetUm0q0sBE&ab_channel=Alta3Research). Some of these channels also assisted in functions I used beforehand, but this commit concluded most of my project.

### 9. Ninth Commit - Calendar Function and Opening Videobased/Interactive APODs as a URL (Finished)

``` python
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
    
    root = tk.Tk()
    root.title("NASA NERD GUIDE")
    root.geometry("900x600")
    root.config(bg="black")

    style = ttk.Style()
    
    # Notebook style
    style.theme_use("default")  #
    style.configure("TNotebook", background="black", borderwidth=0)  
    style.configure("TNotebook.Tab", background="black", foreground="white", padding=[10, 5], borderwidth=0) 
    style.map("TNotebook.Tab", background=[("selected", "#1a1a1a"), ("active", "#333333")], foreground=[("selected", "white"), ("active", "white")])  # Tab states
    style.configure("TFrame", background="black") 
    
    # Create a Notebook 
    NASANOTEBOOK = ttk.Notebook(root)
    NASANOTEBOOK.pack(fill='both', expand=True)

    # Create frames for each tab
    IntroFrame = ttk.Frame(NASANOTEBOOK)
    FindFrame = ttk.Frame(NASANOTEBOOK)
    ViewFrame = ttk.Frame(NASANOTEBOOK)
    SaveFrame = ttk.Frame(NASANOTEBOOK)

    # Add tabs to the Notebook
    NASANOTEBOOK.add(IntroFrame, text = 'Introduction')
    NASANOTEBOOK.add(FindFrame, text='Find an APOD!')
    NASANOTEBOOK.add(ViewFrame, text='View and Save an APOD!')
    NASANOTEBOOK.add(SaveFrame, text='View and Remove Saved APODS!')

    # -- IntroFrame Code --

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
        image_label_find.config(image="", text="Failed to fetch APOD", fg="red")
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
```
- Explanation: As of now, I've made the calendar function with the tkcalendar module and imported the DateEntry function to create calendars for entering the desired date, a very enticed part of my project and also good for maximised user interface. For dates such as 2025/03/02, (this was an interactive APOD) if you choose this date in the ViewAPOD frame, it will automatically take you to the URL for that APOD, and I've also added a button in the DailyAPOD frame if the person wishes to go to the website and view the APOD instead of on the GUI. However an issue with this is that the user cannot actively save these types of APOD's, and if the user tries to save the date 2025/03/02, when you try to view it in the SavedAPOD's frame, the APOD will instead by outputted as the daily APOD and there will be no explanation (There was no explanation for this date I think). The goal would be saving these interactive APOD's but not outputting them as an image in the GUI when clicked on in the selected index but rather taking you to the website (I scrapped this idea.)

***

### 10. Tenth Commit - Almost forgot to integrate functions into my_module.py and keep main.py clean (Finished) 9/4/25

``` python
- main.py
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
```
``` python
- my_module.py
import requests  # For getting data from the NASA API (Obviously)
from PIL import Image, ImageTk  # Pillow for image handling
import io  # For handling image data and converting it into bytes
import webbrowser  # For opening the APOD in a browser

# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"  # APOD URL
API_KEY = "c1R5mNKBtlpRqXwI29rUPfRJvcTPbE8drebdwrEI"  # Replace with your own API key

# Dictionary to store favorite APOD
favorites = {}

def get_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day (APOD)."""
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date

    try:
        response = requests.get(APOD_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
    except KeyError as e:
        print(f"Could not find today's APOD URL. ({e})")
    except requests.exceptions.ConnectionError as e:
        print(f"Network error: Could not connect to NASA API. ({e})")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out. The NASA API might be slow or your connection is unstable.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch APOD: {e}")
        return None
    except ValueError:
        print("Invalid response from NASA API (not JSON).")
        return None

def View_APOD_Button(apod, image_label_find, explanation_text_find, photo_ref):
    """View the daily APOD in the GUI."""
    if apod is None:
        print("Failed to fetch today's APOD. View as a URL instead?")
        return
    try:
        image_url = apod['image_url']
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label_find.config(image=photo)
        image_label_find.photo = photo
        photo_ref[0] = photo
        explanation_text_find.delete(1.0, "end")
        explanation_text_find.insert("end", f"Title: {apod['title']}\n")
        explanation_text_find.insert("end", f"Date: {apod['date']}\n")
        explanation_text_find.insert("end", f"Explanation: {apod['explanation']}\n")
        explanation_text_find.insert("end", f"Image URL: {apod['image_url']}\n")
    except Exception as e:
        print(f"Error loading image: {e} (Maybe try opening as a URL?)")

def View_APOD_URL_Button(apod):
    """View the APOD as a URL."""
    if apod:
        print(f"\nTitle: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"Explanation: {apod['explanation']}")
        print(f"Image URL: {apod['image_url']}")
    try:
        webbrowser.open(apod['image_url'])
    except Exception as e:
        print(f"Could not open browser: {e}")

def Save_APOD_Button(photo_ref, Saved_APODs, APOD_name_find, explanation_text_find):
    """Save the Daily APOD to the favorites list."""
    find_name = APOD_name_find.get()
    saved_names = Saved_APODs.get(0, "end")
    if find_name in saved_names:
        print(f"APOD with name '{find_name}' already exists in favorites. Please choose a different name.")
        return
    if not find_name:
        print("Please enter a name for the Daily APOD.")
        return
    if photo_ref[0]:
        favorites[find_name] = {
            "image": photo_ref[0],
            "explanation": explanation_text_find.get(1.0, "end")
        }
        print(f"Saved APOD with name '{find_name}' to favorites!")
        Saved_APODs.insert("end", find_name)
    else:
        print("No APOD image to save.")

def View_APOD_Input(Date1, image_label_view, explanation_text_view, photo_ref):
    """View the APOD for a specified date."""
    date = Date1.entry.get()
    if date:
        try:
            apod_data = get_apod(date)
            if apod_data and 'image_url' in apod_data:
                image_url = apod_data['image_url']
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                image_label_view.config(image=photo)
                image_label_view.photo = photo
                photo_ref[0] = photo
                explanation_text_view.delete(1.0, "end")
                explanation_text_view.insert("end", f"Title: {apod_data['title']}\n")
                explanation_text_view.insert("end", f"Date: {apod_data['date']}\n")
                explanation_text_view.insert("end", f"Explanation: {apod_data['explanation']}\n")
                explanation_text_view.insert("end", f"Image URL: {apod_data['image_url']}\n")
            else:
                print("No image found for this date or failed to fetch APOD.")
        except Exception as e:
            print(f"Error fetching APOD for date {date}: {e}")
    else:
        print("Please enter a date in YYYY-MM-DD format.")

def Save_APOD(photo_ref, APOD_name_view, Saved_APODs, explanation_text_view):
    """Save the APOD from the View Frame."""
    name = APOD_name_view.get()
    saved_names = Saved_APODs.get(0, "end")
    if name in saved_names:
        print(f"APOD with name '{name}' already exists in favorites. Please choose a different name.")
        return
    if not name:
        print("Please enter a name for the APOD.")
        return
    if photo_ref[0]:
        favorites[name] = {
            "image": photo_ref[0],
            "explanation": explanation_text_view.get(1.0, "end")
        }
        print(f"Saved APOD with name '{name}' to favorites!")
        Saved_APODs.insert("end", name)
    else:
        print("No APOD image to save.")

def Remove_Saved_APOD(Saved_APODs, explanation_text_save, image_label_save):
    """Remove the selected APOD from the favorites list."""
    selected_index = Saved_APODs.curselection()
    if selected_index:
        selected_name = Saved_APODs.get(selected_index)
        favorites.pop(selected_name, None)
        Saved_APODs.delete(selected_index)
        print(f"Removed APOD '{selected_name}' from favorites!")
        explanation_text_save.delete(1.0, "end")
        image_label_save.config(image="")
    else:
        print("Please select an APOD to remove.")

def View_Saved_APOD(Saved_APODs, image_label_save, explanation_text_save):
    """View the selected APOD from the favorites list."""
    selected_index = Saved_APODs.curselection()
    if selected_index:
        selected_name = Saved_APODs.get(selected_index)
        selected_apod = favorites.get(selected_name)
        if selected_apod:
            image_label_save.config(image=selected_apod["image"])
            explanation_text_save.delete(1.0, "end")
            explanation_text_save.insert("end", selected_apod["explanation"])
        else:
            print(f"Error: APOD '{selected_name}' not found in favorites.")
    else:
        print("Please select an APOD to view.")
```
***
- Explanation: I went through a large process of moving the functions from the main.py to my_module.py. I had to in turn remove the previous favorites function for this because it was not required and could already be put in a list inside the module, as well as creating new arguments for initialising the functions in the main.py and in the my_module.py. After around 3 hours on 8 April 2025 I got it to work (finally) and it was a last minute forgetfulness which I was glad to clear up. I also made photo_ref a list instead of a variable, so that would allow me to pass the image reference easier being a mutable object and could check photo_ref[0] if the image had been loaded and I had to make changes in different areas for this, for example when I was saving the photo_ref to the favorites dictionary I had to change it from a variable to a mutable list ("image": photo_ref[0]), this was also an ongoing issue then because the arguments I was posting to photo_ref when I moved the functions to the my_module.py were not taking it as an argument and leaving it undefined. Instead of reassigning photo_ref in the function I modified the contents with a list, being a mutable component and easier to handle and thus worked. This was one of the major changes in the code, and after doing so I applied it to the main.py. After this, the module was containing all the functions and the main.py all the objects ready to be loaded with the functions using lambda: mm.(functionnameandarguments) so I could access all arguments and mitigate any errors. Even after this close call, I would have to redo my data dictionary for some variables such as photo_ref being changed to a list object, which will not be too long however I will have to. Additionally I changed the END statements to "end" because it was not defined and the tkinter text widget system used "end" as it was the correct syntax. I also added error handling for functions missing error handling such as View_APOD_Button, Save_APOD_Button and View_APOD_Input. I also forgot to configure a minor error where the photo_ref was not configured for moving across frames e.g. I view an APOD in the findframe, then move to the viewframe and view an APOD and then move back to the findframe to save the APOD. However, it will save the APOD intialised in the viewframe instead. I may do this in the future but with time not being on my side I probably won't configure this issue.I instead added an instruction for this in the README. I also made a minor change in one of my functions, where in the View_APOD_URl_Button function, I put this line: webbrowser.open(apod['image_url']) instead of the actual link, just for better maintainability if the link changes. Other minor changes such as adding an additional timeout in the get_apod, adding keys in my save variables e.g explanation_text_save.insert("end", selected_apod["explanation"]) where I did not include the "explanation" key and also for the "image" key Overall, this was the final part of my project.

***
## Installation
***
### README.md

``` python
# NASA APOD Viewing System

## Intro - Welcome to the NASA APOD Viewing App! 

## Features - In here, you can view your favorite APOD's and save them for later viewing! There are 4 different tabs for this:

1. Intro Tab
2. Daily APOD Tab
3. View an APOD by date
4. Save an APOD

We hope you have fun in your astronomical fantasies!

## Requirements

For the following program, you will require these modules:
- 'requests' for getting APOD data
- 'pillow' for image handling
- 'ttkbootstrap' for cool GUI graphics
- 'tkcalendar' for a cool DateEntry feature in the GUI

## Install Dependencies
Clone the repository and navigate to the project directory:

Then run the command:

``` bash
pip install -r requirements.txt
```
***

### requirements.txt
```python
pillow==10.0.0
requests==2.31.0
ttkbootstrap
tkcalendar
```

***

## Maintenance
***
### Maintenance Questions
***

1. Explain how you would handle issues caused by changes to the NASA API over time.

- Answer: If the NASA API changes its structure, or data format, I would regularly monitor the API documentation for major updates, edit the get_apod() function in order to accomodate any changes in the API's response structure or parameters, if users are on previous versions of the API, I would implement version control in order to ensure compatibility with diffferent API versions, as well as add new error handling cases in order to manage unexpected API changes.

2. Explain how you would ensure the program remains compatible with new versions of Python and libraries like requests and matplotlib.

- Answer: Ensuring compatibility with versions of python and other libraries would require testing of certain versions in accordance with the program and API, updating dependencies in the requirements.txt for any large changes, as well as following release documentation for python and other libraries. This would allow me to mitigate any risk of error in my program, as well as any potential compatibitlity issues very early.

3. Describe the steps you would take to fix a bug found in the program after deployment.

- Answer: Using a certain process (Reproducing, Debugging, Fixing, Testing, Deploying, and Documenting), I first attempt to replicate the issue to understand the cause, use debugging tools such as VScode debugger or pdb to identify the actual causation, fix the relevant part of the code to resolve the issue, to test, try and document test cases to ensure the bug is fully mitigated, deploy the fixed code and the entire application, and finally document the fixtures made in the changelog or documentation.

4. Outline how you would maintain clear documentation and ensure the program remains easy to update in the future.

- Answer: In the future, clear documentation can be made sufficiently through a simply CHANGELOG or through the same README, which tracks the features, updates and fixes of past versions, as well as tools such as comments and docstrings which can help understand the code and furthermore allow for easy update architecture. In my program, I could utilise comments and docstrings more efficiently in order to explain complex logic and functionality properly as well as create a seperate CHANGELOG instead of inside this markdown file to ensure clear documentation.
***
### Final Evaluation
***


1. Evaluate the current functionality of the program in terms of how well it addresses the functional and non-functional requirements.

- Answer: The program successfully allows users to view NASA APOD images, including the daily APODs and APODs retrieved from a certain date fulfilling the requirement to display data from the NASA API as well as other external information. Users can also save APODs with custom names and view or remove them from a favorites list, meeting the requirement for data saving and management. For non-functional requirements, the program runs quite efficiently among my set timelimit of 10 seconds, (In the code and in the documentation), also meeting the need for user-friendliness with ttkbootstrap and DateEntry objects for modern styling and enhanced usability and accessibility. This program also derives reliable information from NASA, and is quick and easy to understand for new and old users alike.

2. Discuss areas for improvement or new features that could be added.

- Answer: Through improving, I could allow for video-based and interactive APODs to be saved and viewed as URLs directly from the favorites list, enhance error messages, and use less global variables and integrate classes instead for better maintainability. New features could include adding a search feature instead of a DateEntry search in order for users to find APODs by keywords or titles and adding support for other NASA APIs such as Mars Rover photos or Earth Imagery. I also could've incorporated local image/explanation saving.

3. Evaluate how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.

- Answer: The project was developed with many key milestones, from the development phase to the theory phase, where I implemented frequent commits and detailed explanations of changes in the markdown file as well as github, and illustrated many challenges in there as well. Time was utilised carefully for the development phase, where I allocated slots for new features and fixes such as ttkbootstrap for styling and tkcalendar for date selection. Handling new functions and steps such as displaying an APOD in the GUI required many systematic tutorials (Listed below). However time management was faulty in my theory, as my Gantt chart illustrated the design phase to be completed before the development phase but my lingering thirst for coding overtook this idea. Overall I can improve on my theory management not only in this assessment but in classwork as well, as I strive to complete classwork and the project theory work. Many challenges throughout the code included new functions and modules, as well as the utilisation of global variables in my code which I can address better, however the time required for these challenges ultimately improved the program's functionality and usability. I could've incorporated functions such as saving the images locally for later date usage, but this was an interpretation of what it may look like in a real application. Overall, the project was managed effectively, while I did greatly well in the development subchapter of the lifecycle, I can improve in theory management as well as time management as a young developer.

## Additional Notes (Tutorials I used, etc.)
1. Link: https://realpython.com/image-processing-with-the-python-pillow-library/ - I went through Pillow basics, manipulating images into bytes with ioBytesIO, as well as resizing and using filters such as LANCZOS, BILINEAR, NEAREST, and then pairing this with the original requests module for maximum capabilities.

2. Link: https://ttkbootstrap.readthedocs.io/en/latest/ - I went through ttkbootstrap, a separate module where I integrated widget styles as well to make it look cleaner as new widgets such as DateEntry in my code.

3. Link: https://coderslegacy.com/python/tkcalendar-date-picker-calendar/ - I also went through the basic tkcalendar module, however I mitigated this idea due to the cleanliness of ttkbootstrap as a whole.

4. Link: https://www.pythontutorial.net/tkinter/tkinter-listbox/ - A simple tutorial for tkinter listboxes.

5. Link: https://www.geeksforgeeks.org/image-viewer-app-in-python-using-tkinter/ - This incredibly useful tutorial served as a basis for my code, introducing me to PhotoImage data types as well as utilising pillow and tkinter together.

 - Other tutorials, such as from youtube were also linked in my previous development frameworks.

 6. Link: https://realpython.com/python-dicts/ - This was utilised for my module, specifically for the favourites dictionary as it possessed more leeway into dictionaries as a whole, I also addressed the date parameter in the module which was not related to this however.