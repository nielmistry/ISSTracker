from spacetrack import SpaceTrackClient
import what3words
import ephem
import datetime
import loadvars
import os


# What3Words Setup
THREE_WORDS_API_KEY = os.environ["W3W_API_KEY"]
w3w = what3words.Geocoder(THREE_WORDS_API_KEY)

# SpaceTrack setup
st = SpaceTrackClient('nielmistry1@gmail.com',os.environ["SPACETRACK_PW"])

ISS_TLE = st.tle_latest(object_id='1998-067A', limit=1, format='tle')

i = 0
while ISS_TLE[i] != '\n':
    i += 1

TLE_LINE_1 = ISS_TLE[0:i]
TLE_LINE_2 = ISS_TLE[i+1:-1]

print(TLE_LINE_1)
print(TLE_LINE_2)

w3wQuery = 'transit.movement.biked'

w3wData = w3w.forward(addr=w3wQuery)

lat = w3wData['bounds']['southwest']['lat']
lng = w3wData['bounds']['southwest']['lng']

observer = ephem.Observer()
observer.lat, observer.long = lat, lng
observer.date = datetime.datetime.now()
observer.elevation = 170

iss = ephem.readtle("ISS (ZARYA)", TLE_LINE_1, TLE_LINE_2)
iss.compute(observer)


# IDEA - A script running forever will update the TLE data when a timer >= some number
# The rest of the script will just be sending alt/az data to the arduino over I2C or serial