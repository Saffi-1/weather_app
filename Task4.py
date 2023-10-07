import requests
API_KEY = "444adcd4ba774d10e4d5cb154868483b"

def fetch_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather_data(data):
    if 'name' in data:
        print("Weather Data:")
        print(f"Location: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Weather Condition: {data['weather'][0]['description']}")
    else:
        print("Location not found.")

def fetch_weather_forecast(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather_forecast(data):
    if data["cod"] != "404":
        print("Weather Forecast:")
        for forecast in data["list"]:
            date = forecast["dt_txt"].split()[0]
            time = forecast["dt_txt"].split()[1]
            temperature = forecast["main"]["temp"]
            print(f"Date: {date}, Time: {time}, Temperature: {temperature}°C")
    else:
        print("Location not found.")

def save_location(location):
    with open("locations.txt", "a") as file:
        file.write(location + "\n")
    print(f"{location} saved successfully.")

def load_locations():
    try:
        with open("locations.txt", "r") as file:
            locations = file.readlines()
        print("Saved Locations:")
        for location in locations:
            print(location.strip())
    except FileNotFoundError:
        print("No saved locations found.")

def weather_app():
    print("Welcome to the Weather App!")
    while True:
        print("\nMenu:")
        print("1. Fetch Weather Data")
        print("2. Fetch Weather Forecast")
        print("3. Save Location")
        print("4. Load Saved Locations")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            location = input("Enter a location: ")
            weather_data = fetch_weather_data(location)
            display_weather_data(weather_data)
        elif choice == "2":
            location = input("Enter a location: ")
            weather_forecast = fetch_weather_forecast(location)
            display_weather_forecast(weather_forecast)
        elif choice == "3":
            location = input("Enter a location to save: ")
            save_location(location)
        elif choice == "4":
            load_locations()
        elif choice == "5":
            print("Thank you for using the Weather App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

weather_app()