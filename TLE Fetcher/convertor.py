from spacetrack import SpaceTrackClient
import what3words
import json
from collections import namedtuple

# What3Words Setup
THREE_WORDS_API_KEY = "H60K6CTE";
w3w = what3words.Geocoder(THREE_WORDS_API_KEY);

# SpaceTrack setup
st = SpaceTrackClient('nielmistry1@gmail.com','oS4c0PiZncxHbo9')

ISS_TLE = st.tle_latest(object_id = '1998-067A', limit = 1, format = 'tle';

w3wQuery = 'transit.movement.biked';

w3wData = w3w.forward(addr=w3wQuery)

# Convert w3wData to python object