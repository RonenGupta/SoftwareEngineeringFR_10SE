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