import requests

def get_current_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            weather_info = f"Weather in {city}: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            return weather_info
        else:
            return f"Failed to get weather information. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    weather_info = get_current_weather(city, api_key)
    print(weather_info)
