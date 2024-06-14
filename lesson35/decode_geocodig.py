from opencage.geocoder import OpenCageGeocode

def reverse_geocode(coordinates, api_key):
    geocoder = OpenCageGeocode(api_key)
    lat, lng = map(float, coordinates.split(','))
    result = geocoder.reverse_geocode(lat, lng)
    
    if result and len(result):
        return result[0]['formatted']
    else:
        return "Address not found"

# Приклад використання:
coordinates = '50.479944,30.489993'
api_key = 'YOUR_OPENCAGE_API_KEY'
address = reverse_geocode(coordinates, api_key)
print(f"Address for coordinates {coordinates}: {address}")
