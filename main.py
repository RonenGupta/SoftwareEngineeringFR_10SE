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
                # No else clause needed; get_apod() handles error messaging

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