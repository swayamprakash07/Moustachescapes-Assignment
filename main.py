from flask import Flask, request, jsonify
import requests
import math
from dotenv import load_dotenv
import os

load_dotenv() 

# Import your data file (replace with actual list or module if needed)
from data import moustacheLocations

app = Flask(_name_)


# Helper: Haversine formula to calculate distance in kilometers
def get_distance_in_km(lat1, lon1, lat2, lon2):

    def to_rad(angle):
        return math.radians(angle)

    R = 6371  # Radius of the Earth in km
    d_lat = to_rad(lat2 - lat1)
    d_lon = to_rad(lon2 - lon1)

    a = math.sin(d_lat / 2)**2 + math.cos(to_rad(lat1)) * math.cos(
        to_rad(lat2)) * math.sin(d_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


@app.route("/geocode", methods=["POST"])
def geocode():
    data = request.get_json()
    address = data.get("address")

    if not address:
        return jsonify({"error": "Address is required"}), 400

    encoded_address = requests.utils.quote(address)
    mapbox_access_token = os.getenv("MAPBOX_API_KEY")
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{encoded_address}-india.json?access_token={mapbox_access_token}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        features = response.json().get("features", [])

        if not features:
            return jsonify({"error": "No results found"}), 404

        lng, lat = features[0]["center"]

        # Filter locations within 50 km
        nearby_locations = [
            loc for loc in moustacheLocations if get_distance_in_km(
                lat, lng, loc["latitude"], loc["longitude"]) <= 50
        ]

        return jsonify({
            "inputLocation": {
                "lat": lat,
                "lng": lng
            },
            "nearbyLocations": nearby_locations
        })

    except requests.RequestException as e:
        print("Error fetching from Mapbox API:", str(e))
        return jsonify({"error": "Failed to fetch geocoding data"}), 500


if _name_ == "_main_":
    app.run(port=3000)