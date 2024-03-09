
import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class GeolocationApp:
    """
    A GUI application for calculating the distance between two locations using geolocation.

    Attributes:
        master (tkinter.Tk): The root window of the application.
        source_label (tkinter.Label): The label for the current location entry.
        source_entry (tkinter.Entry): The entry widget for the current location.
        destination_label (tkinter.Label): The label for the destination entry.
        destination_entry (tkinter.Entry): The entry widget for the destination.
        calculate_button (tkinter.Button): The button to calculate the distance.
        result_label (tkinter.Label): The label to display the calculated distance.
    """

    def __init__(self, master):
        """
        Initializes the GeolocationApp.

        Args:
            master (tkinter.Tk): The root window of the application.
        """
        self.master = master
        master.title("Geolocation GUI Extension")

        # Labels and Entry widgets
        self.source_label = tk.Label(master, text="Current Location:")
        self.source_entry = tk.Entry(master, width=30)
        self.destination_label = tk.Label(master, text="Destination:")
        self.destination_entry = tk.Entry(master, width=30)

        # Button to calculate distance
        self.calculate_button = tk.Button(master, text="Calculate Distance", command=self.calculate_distance)

        # Result label to display the distance
        self.result_label = tk.Label(master, text="")

        # Grid layout
        self.source_label.grid(row=0, column=0, sticky=tk.E)
        self.source_entry.grid(row=0, column=1)
        self.destination_label.grid(row=1, column=0, sticky=tk.E)
        self.destination_entry.grid(row=1, column=1)
        self.calculate_button.grid(row=2, column=0, columnspan=2)
        self.result_label.grid(row=3, column=0, columnspan=2)

    def calculate_distance(self):
        """
        Calculates the distance between the current location and the destination.

        Retrieves the current location and destination addresses from the entry widgets,
        retrieves the geolocation information for both addresses, and calculates the distance
        using the geodesic function from the geopy.distance module. The calculated distance
        is then displayed in the result label.
        """
        source_address = self.source_entry.get()
        destination_address = self.destination_entry.get()

        try:
            source_location = get_location(source_address)
            destination_location = get_location(destination_address)
        except:
            self.result_label.config(text="Error: Unable to retrieve geolocation information. Please check your input.")
            return

        distance = geodesic(source_location, destination_location).kilometers  # Convert distance to kilometers
        self.result_label.config(text=f"Distance: {str(distance)} kilometers")  # Format distance as a string

def get_location(address):
    """
    Retrieves the geolocation information for a given address.

    Args:
        address (str): The address to retrieve geolocation information for.

    Returns:
        tuple: A tuple containing the latitude and longitude of the address.
    """
    geolocator = Nominatim(user_agent="geolocation_gui_extension")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

def main():
    """
    The main function of the application.

    Creates an instance of the GeolocationApp class and starts the main event loop.
    """
    root = tk.Tk()
    GeolocationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
