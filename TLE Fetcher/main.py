from skyfield.api import Topos, load
from skyfield.units import Angle
import time
import numpy as np
import serial

# MSG CODES
SOM_CODE = bytes([0x7f, 0xff, 0x00, 0x00])
EOM_CODE = bytes([0x7f, 0xff, 0xff, 0xff]) 
alt_code = bytes(0xaa)
az_code = bytes(0xab)
both_code = bytes(0xbb)
spacing = bytes(0xfe)

ts = load.timescale()
serial = serial.Serial(port='/dev/ttyACM0')

def write_serial(code, to_write):
    # WRITE SOM
    serial.write(SOM_CODE)

    # WRITE MSG CODE
    serial.write(code)

    # WRITE MESSAGE
    serial.write(to_write)

    # WRITE EOM CODE
    serial.write(EOM_CODE)

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
    
    write_serial(alt_code, alt_deg32_bytes)
    write_serial(az_code, az_deg32_bytes)

    print(alt_deg32)
    print(az_deg32)

    time.sleep(0.5);    

