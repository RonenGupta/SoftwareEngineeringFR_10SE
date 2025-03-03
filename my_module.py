import requests

# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"  # Replace with your own API key from https://api.nasa.gov/

# Dictionary to store favorite celestial objects
favorites = {}

def get_apod():
    """Fetch NASA's Astronomy Picture of the Day (APOD)."""
    params = {"api_key": API_KEY}
    try:
        response = requests.get(APOD_URL, params=params, timeout=10)  # Add timeout
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        return {
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
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

def add_favorite(name, details):
    """Store a celestial object in the favorites collection."""
    favorites[name] = details