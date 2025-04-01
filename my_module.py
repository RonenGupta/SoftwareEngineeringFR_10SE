import requests # For getting data from the NASA API (Obviously)

# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod" # APOD URL
API_KEY = "c1R5mNKBtlpRqXwI29rUPfRJvcTPbE8drebdwrEI"  # My API key - Replace with your own API key

# Dictionary to store favorite APOD
favorites = {}

def get_apod(date=None): # Function to fetch the Astronomy Picture of the Day (APOD) from NASA
    """Fetch NASA's Astronomy Picture of the Day (APOD).
    
    Args:
        date (str, optional): Date in 'YYYY-MM-DD' format to fetch APOD for a specific day.
                              If None, fetches the current day's APOD.
    
    Returns:
        dict: Dictionary containing APOD details (title, date, explanation, image_url).
        None: If the request fails.
    """ # Predefined docstrings for defining the function and its parameters
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date  # Date Parameter for fetching APOD for a specific day


    try: # Error handling
        response = requests.get(APOD_URL, params=params, timeout=10)  # Getting the APOD data and setting a timeout to synchronize with my non-functional requirements
        response.raise_for_status()  # If the response was unsuccessful
        data = response.json() # Getting the data in JSON format
        return { # Creating a dictionary to store the APOD details and data
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
    # Error handling
    except KeyError as e:
        print(f"Could not find today's APOD URL. (It is possibly video formatted and does not have a thumbnail, use the view APOD in a URL button instead!). ({e})")
    except requests.exceptions.ConnectionError as e:
        print(f"Network error: Could not connect to NASA API. Check your internet connection. ({e})")
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

def add_favorite(name, details): # Function to save an APOD in the favorites section
    """Store a celestial object in the favorites collection."""
    favorites[name] = details