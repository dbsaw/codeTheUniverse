import requests

url = "https://api.nasa.gov/neo/rest/v1/feed/today?api_key=DEMO_KEY"
response = requests.get(url).json()

all_neos = []
for date in response['near_earth_objects']:
    all_neos.extend(response['near_earth_objects'][date])

if not all_neos:
    print("No asteroids approaching today!")
else:
    closest_neo = None
    min_distance_km = float('inf')
    speed_kmh = 0.0
    LD_CONVERSION = 384400 

    for neo in all_neos:
        approach_data = neo['close_approach_data'][0]
        distance_km = float(approach_data['miss_distance']['kilometers'])
        if distance_km < min_distance_km:
            min_distance_km = distance_km
            closest_neo = neo
            speed_kmh = float(approach_data['relative_velocity']['kilometers_per_hour'])

    name = closest_neo['name']
    min_distance_ld = min_distance_km / LD_CONVERSION

    print(f"⚠️ Asteroid {name} is approaching! Speed: {speed_kmh:,.0f} km/h | Distance: {min_distance_ld:.2f} LD / {min_distance_km:,.0f} km")
