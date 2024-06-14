import googlemaps
import requests

def get_first_place_photo(location_name, api_key):
    gmaps = googlemaps.Client(key=api_key)
    
    # Отримання місця за іменем
    places = gmaps.places(query=location_name)
    
    if places['results']:
        place_id = places['results'][0]['place_id']
        
        # Отримання фотографій місця
        photos = gmaps.place(place_id)['result']['photos']
        
        if photos:
            # Отримання першої фотографії
            photo_reference = photos[0]['photo_reference']
            
            # Формування URL для завантаження фото
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
            
            # Завантаження фото і збереження на диск
            response = requests.get(photo_url)
            if response.status_code == 200:
                with open(f"{location_name}_photo.jpg", 'wb') as f:
                    f.write(response.content)
                print(f"Photo saved as {location_name}_photo.jpg")
            else:
                print("Failed to download photo")
        else:
            print("No photos found for this place")
    else:
        print("Place not found")

# Приклад використання:
location_name = 'Eiffel Tower'
api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
get_first_place_photo(location_name, api_key)
