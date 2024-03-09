# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# def get_coordinates(place_name):
#     geolocator = Nominatim(user_agent="my_app")
#     location = geolocator.geocode(place_name)
#     return location.latitude, location.longitude

# def calculate_distance(origin, destination):
#     return geodesic(origin, destination).meters

# def main():
#     # Input source and destination place names from the user
#     source_name = input("Enter the name of the source place: ")
#     destination_name = input("Enter the name of the destination place: ")

#     # Get coordinates of the source and destination
#     source_location = get_coordinates("Bangalore")
#     destination_location = get_coordinates(destination_name)

#     # Calculate distance
#     distance = calculate_distance(source_location, destination_location)
#     kmd=distance/1000

#     # Display the result
#     print(f"The distance from {source_name} to {destination_name} is approximately {kmd} kilometers.")

# if __name__ == "__main__":
#     main()



# import geocoder
# from geopy.distance import geodesic

# def get_user_location():
#     # Automatically detect user's location using the geocoder library
#     user_location = geocoder.ip('me')
#     return user_location.latlng

# def get_coordinates(place_name):
#     # Geocode the place name to get its coordinates
#     location = geocoder.osm(place_name)
#     return location.latlng

# def calculate_distance(origin, destination):
#     # Calculate distance in kilometers
#     return geodesic(origin, destination).kilometers

# def main():
#     # Get the user's location
#     user_location = get_user_location()

#     # Input destination place name from the user
#     destination_name = input("Enter the name of the destination place: ")

#     # Get coordinates of the destination
#     destination_location = get_coordinates(destination_name)

#     # Calculate distance
#     distance = calculate_distance(user_location, destination_location)

#     # Display the result in a single line
#     print(f"The distance from your location to {destination_name} is approximately {distance:.2f} kilometers.")

# if __name__ == "__main__":
#     main()


import geocoder
from geopy.distance import geodesic

def get_user_location():
    # Automatically detect user's location using the geocoder library
    user_location = geocoder.ip('me')
    return user_location.latlng, user_location.city

def get_coordinates(place_name):
    # Geocode the place name to get its coordinates
    location = geocoder.osm(place_name)
    return location.latlng

def calculate_distance(origin, destination):
    # Calculate distance in kilometers
    return geodesic(origin, destination).kilometers

def main():
    # Get the user's location and city name
    user_location, user_city = get_user_location()

    # Input destination place name from the user
    destination_name = input("Enter the name of the destination place: ")

    # Get coordinates of the destination
    destination_location = get_coordinates(destination_name)

    # Calculate distance
    distance = calculate_distance(user_location, destination_location)

    # Display the result in a single line
    print(f"The distance from {user_city} to {destination_name} is approximately {distance:.2f} kilometers.")

if __name__ == "__main__":
    main()

