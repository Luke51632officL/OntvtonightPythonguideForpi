import requests
from bs4 import BeautifulSoup
import msvcrt  # For arrow key input (Windows-specific)

def get_tv_listings(zip_code):
    url = f"https://www.ontvtonight.com/guide/{zip_code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract relevant information (station names, show titles, start times, end times)
    # You'll need to inspect the website's HTML to find the appropriate tags and classes.

    # Example: Find all station names
    station_names = soup.find_all("div", class_="station-name")

    # Example: Find all show titles
    show_titles = soup.find_all("div", class_="show-title")

    # Example: Find all start times
    start_times = soup.find_all("div", class_="start-time")

    # Example: Find all end times
    end_times = soup.find_all("div", class_="end-time")

    # Display the information
    num_stations = len(station_names)
    current_station = 0

    while True:
        print(f"Station {station_names[current_station].text} ({current_station + 1}/{num_stations}):")
        print(f"Show: {show_titles[current_station].text}")
        print(f"Start time: {start_times[current_station].text}")
        print(f"End time: {end_times[current_station].text}\n")

        # Arrow key navigation
        print("Press '←' to go to the previous station, '→' to go to the next station, or 'q' to quit.")
        key = msvcrt.getch()

        if key == b"\xe0":  # Arrow key
            key = msvcrt.getch()
            if key == b"M":  # Right arrow
                current_station = (current_station + 1) % num_stations
            elif key == b"K":  # Left arrow
                current_station = (current_station - 1) % num_stations
        elif key == b"q":
            break

if __name__ == "__main__":
    user_zip_code = input("Enter your ZIP code: ")
    get_tv_listings(user_zip_code)
