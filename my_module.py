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
    """Fetch NASA's Astronomy Picture of the Day (APOD). This function handles the API request and error handling."""
    params = {"api_key": API_KEY} # Set the API key in the dictionary
    if date:
        params["date"] = date # Set the date

    try:
        response = requests.get(APOD_URL, params=params, timeout=10) # Get the APOD data
        response.raise_for_status() # Check for errors
        data = response.json() # From the JSON response get the data
        return {
            # Explanation text extraction
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
    # Error handling
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
    if apod is None: # Check if the APOD is available, if none:
        print("Failed to fetch today's APOD. View as a URL instead?")
        return
    try:
        image_url = apod['image_url'] # Get the image URL
        response = requests.get(image_url, timeout=10) # Get the image data
        response.raise_for_status() # Check for errors
        image_data = response.content # Get the image data
        image = Image.open(io.BytesIO(image_data)) # Open the image
        image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS) # Resize the image
        photo = ImageTk.PhotoImage(image) # Convert to PhotoImage
        image_label_find.config(image=photo) # Set the image in the label
        image_label_find.photo = photo # Keep a reference to avoid garbage collection
        photo_ref[0] = photo # Store the photo reference in a list
        explanation_text_find.delete(1.0, "end") # Delete previous text

        # Insert explanation
        explanation_text_find.insert("end", f"Title: {apod['title']}\n") 
        explanation_text_find.insert("end", f"Date: {apod['date']}\n")
        explanation_text_find.insert("end", f"Explanation: {apod['explanation']}\n")
        explanation_text_find.insert("end", f"Image URL: {apod['image_url']}\n")
        # Error handling
    except Exception as e:
        print(f"Error loading image: {e} (Maybe try opening as a URL?)")

def View_APOD_URL_Button(apod):
    """View the APOD as a URL."""
    # Check if the APOD is available
    if apod:
        print(f"\nTitle: {apod['title']}")
        print(f"Date: {apod['date']}")
        print(f"Explanation: {apod['explanation']}")
        print(f"Image URL: {apod['image_url']}")
    try:
        # Open the image URL in the default web browser
        webbrowser.open(apod['image_url'])
    # Error handling
    except Exception as e:
        print(f"Could not open browser: {e}")

def Save_APOD_Button(photo_ref, Saved_APODs, APOD_name_find, explanation_text_find):
    """Save the Daily APOD to the favorites list."""
    find_name = APOD_name_find.get() # Get the name from the entry field
    saved_names = Saved_APODs.get(0, "end") # Get the list of saved names
    if find_name in saved_names: # Check if the name already exists
        print(f"APOD with name '{find_name}' already exists in favorites. Please choose a different name.")
        return
    if not find_name: # Check if the name is empty from the entry field
        print("Please enter a name for the Daily APOD.")
        return
    if photo_ref[0]: # If a photo has been viewed
        favorites[find_name] = { # Save the APOD
            "image": photo_ref[0], # Save the image reference
            "explanation": explanation_text_find.get(1.0, "end") # Save the explanation text
        }
        print(f"Saved APOD with name '{find_name}' to favorites!")
        Saved_APODs.insert("end", find_name) # Insert the name into the list
    else:
        print("No APOD image to save.")

def View_APOD_Input(Date1, image_label_view, explanation_text_view, photo_ref):
    """View the APOD for a specified date."""
    date = Date1.entry.get() # Get the date from the DateEntry widget
    if date: # Check if the date is not empty (Validate the date format)
        try:
            apod_data = get_apod(date) # Get the APOD for the specific date using the get_apod function
            if apod_data and 'image_url' in apod_data: # Check if the APOD data is valid
                image_url = apod_data['image_url'] # Get the image URL
                response = requests.get(image_url, timeout=10) # Get the image data from the URL
                response.raise_for_status() # Check for errors
                image_data = response.content # Store the image data
                image = Image.open(io.BytesIO(image_data)) # Open the image in bytes
                image = image.resize((min(image.width, 500), min(image.height, 300)), Image.LANCZOS) # Resize the image
                photo = ImageTk.PhotoImage(image) # Convert to a PhotoImage object
                image_label_view.config(image=photo) # Set the image in the label
                image_label_view.photo = photo # Store in a variable to keep a reference
                photo_ref[0] = photo # Then store the variable in a list for mutability

                # Explanation text insertion
                explanation_text_view.delete(1.0, "end")
                explanation_text_view.insert("end", f"Title: {apod_data['title']}\n")
                explanation_text_view.insert("end", f"Date: {apod_data['date']}\n")
                explanation_text_view.insert("end", f"Explanation: {apod_data['explanation']}\n")
                explanation_text_view.insert("end", f"Image URL: {apod_data['image_url']}\n")
            else:
                print("No image found for this date or failed to fetch APOD.")
                # Error handling
        except Exception as e:
            print(f"Error fetching APOD for date {date}: {e}")
    else:
        print("Please enter a date in YYYY-MM-DD format.")

def Save_APOD(photo_ref, APOD_name_view, Saved_APODs, explanation_text_view):
    """Save the APOD from the View Frame."""
    name = APOD_name_view.get() # Get the name from the ViewFrame name entry field
    saved_names = Saved_APODs.get(0, "end") # Get the list of saved names
    if name in saved_names: # Check if the name is already in the saved names
        print(f"APOD with name '{name}' already exists in favorites. Please choose a different name.")
        return
    if not name: # Check if the name is empty
        print("Please enter a name for the APOD.")
        return
    if photo_ref[0]: # If a photo has been viewed
        favorites[name] = {  # Save the APOD
            "image": photo_ref[0], # Save the image reference
            "explanation": explanation_text_view.get(1.0, "end") # Save the explanation text
        }
        print(f"Saved APOD with name '{name}' to favorites!")
        Saved_APODs.insert("end", name) # Insert the name into the list
    else:
        print("No APOD image to save.")

def Remove_Saved_APOD(Saved_APODs, explanation_text_save, image_label_save):
    """Remove the selected APOD from the favorites list."""
    selected_index = Saved_APODs.curselection() # Get the selected index from cursor selection
    if selected_index: # Check if an index has been selected in the listbox from cursor selection
        selected_name = Saved_APODs.get(selected_index) # Get the selected name from the listbox
        favorites.pop(selected_name, None) # Use the pop function to remove the selected name from the favorites dictionary
        Saved_APODs.delete(selected_index) # Delete the visual listbox representation of the selected name
        print(f"Removed APOD '{selected_name}' from favorites!")
        explanation_text_save.delete(1.0, "end") # Delete the previous explanation text
        image_label_save.config(image="") # Clear the image label
    else:
        print("Please select an APOD to remove.")

def View_Saved_APOD(Saved_APODs, image_label_save, explanation_text_save):
    """View the selected APOD from the favorites list."""
    selected_index = Saved_APODs.curselection() # Use the cursor selection to get the selected index
    if selected_index: # Check if an index has been selected in the listbox from cursor selection
        selected_name = Saved_APODs.get(selected_index) # Get the selected name from the listbox
        selected_apod = favorites.get(selected_name) # Get the selected APOD from the favorites dictionary
        if selected_apod: # Check if the selected APOD exists in the favorites dictionary by name
            image_label_save.config(image=selected_apod["image"]) # Set the image in the label
            explanation_text_save.delete(1.0, "end") # Delete previous text
            explanation_text_save.insert("end", selected_apod["explanation"]) # Insert the explanation text
        else:
            # Error handling
            print(f"Error: APOD '{selected_name}' not found in favorites.") 
    else:
        print("Please select an APOD to view.")