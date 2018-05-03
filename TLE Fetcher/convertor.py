from spacetrack import SpaceTrackClient
import what3words

# What3Words Setup
THREE_WORDS_API_KEY = "H60K6CTE";
w3w = what3words.Geocoder(THREE_WORDS_API_KEY);

# SpaceTrack setup
st = SpaceTrackClient('nielmistry1@gmail.com','oS4c0PiZncxHbo9');

ISS_TLE = st.tle_latest(object_id='1998-067A', limit=1, format='tle');
i = 0;
while ISS_TLE[i] != '\n':
    i = i + 1;

TLE_LINE_1 = ISS_TLE[0:i-1]
TLE_LINE_2 = ISS_TLE[i+1:]
print(TLE_LINE_1)
print(TLE_LINE_2);
w3wQuery = 'transit.movement.biked';

w3wData = w3w.forward(addr=w3wQuery)

lat = w3wData['bounds']['southwest']['lat'];
lng = w3wData['bounds']['southwest']['lng'];
