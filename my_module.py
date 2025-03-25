import requests

# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "c1R5mNKBtlpRqXwI29rUPfRJvcTPbE8drebdwrEI"  # My API key
thumbs = True

# Dictionary to store favorite celestial objects
favorites = {}

def get_apod(date=None): # Function to fetch the Astronomy Picture of the Day (APOD) from NASA
    """Fetch NASA's Astronomy Picture of the Day (APOD).
    
    Args:
        date (str, optional): Date in 'YYYY-MM-DD' format to fetch APOD for a specific day.
                              If None, fetches the current day's APOD.
    
    Returns:
        dict: Dictionary containing APOD details (title, date, explanation, image_url).
        None: If the request fails.
    """
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date  # Date Parameter


    try: # Error handling
        response = requests.get(APOD_URL, params=params, timeout=10)  # Add timeout
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        return {
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
    
    except KeyError as e:
        print(f"Could not find today's APOD URL. (It is possibly video formatted and does not have a thumbnail). ({e})")
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

def add_favorite(name, details): # Function to save an APOD in the favorites collection
    """Store a celestial object in the favorites collection."""
    favorites[name] = details