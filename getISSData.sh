#!/bin/sh

# CURL='/usr/bin/curl'
curl -c cookies.txt -b cookies.txt https://www.space-track.org/ajaxauth/login -d "identity=nielmistry1@gmail.com&password=oS4c0PiZncxHbo9"

# curlCmd2()
# {
# 	curl --limit-rate 100K --cookie cookies.txt https://www.space-track.org/basicspacedata/query/class/tle_latest/OBJECT_ID/1998-067A/orderby/ORDINAL%20asc/limit/1/metadata/false > iss.json
# }

# curlCmd
# curlCmd2