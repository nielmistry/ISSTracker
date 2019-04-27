from skyfield.api import Topos, load
from skyfield.units import Angle
import time
import numpy as np
import serial

ts = load.timescale()
serial = serial.Serial(port='/dev/ttyACM0')

while True:
    t = ts.now()

    stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'

    satellites = load.tle(stations_url)
    satellite = satellites['ISS (ZARYA)']

    days = t - satellite.epoch
    print('{:.3f} days away from epoch'.format(days))

    if abs(days) > 14:
        satellites = load.tle(stations_url, reload=true)
        satellite = satellites['ISS (ZARYA)']

    bluffton = Topos('43.600804N','79.698806W')
    difference = satellite - bluffton

    topocentric = difference.at(t)
    
    alt, az, distance = topocentric.altaz()

    if alt.degrees > 0:
        print("The ISS is currently above the horizon!")

    alt_deg32 = np.single(alt.degrees)
    az_deg32 = np.single(az.degrees)

    alt_deg32_bytes = alt_deg32.tobytes()
    az_deg32_bytes = az_deg32.tobytes()

    serial.write(alt_deg32_bytes)

    print(alt_deg32)
    print(az_deg32)

    time.sleep(0.5);    