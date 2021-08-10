import streamlit as st

from geopy.geocoders import Nominatim
import haversine as hs

# Openstreet map Nominatim object
geolocator = Nominatim(user_agent="geo_locator")

st.title("Calculate distance between 2 addresses")
form = st.form(key='my-form')  # create a new streamlit form
start_address = form.text_input('Enter your start address')
destination_address = form.text_input('Enter your destination address')

submit = form.form_submit_button('Get Distance')

if submit:
    start_location = geolocator.geocode(
        start_address)  # geocode the start address
    destination_location = geolocator.geocode(
        destination_address)  # geocode the destination address

    # print error if the geocode is unsuccessful
    if (start_location is None) or (destination_location is None):
        st.write(f"Invalid start address or destination address")
    else:
        # create tuple of starting point
        start_point = (start_location.latitude, start_location.longitude)
        # create tuple of destio
        destination_point = (destination_location.latitude,
                             destination_location.longitude)
        # calculate the distance between the points using the haversine formulae
        distance = hs.haversine(start_point, destination_point)
        # print the distance to the template
        st.write(
            f'The distance between {start_address} and {destination_address} is {distance:.2f} KM')
