from weather import *

def main():
    
    city = get_city()
    country = get_country_code()
    key = get_key()

    location = get_location(country, city, key)
    if not location:
        print("Location not found!")
        exit()
    lat = location[0]["lat"]
    lon = location[0]["lon"]
    weather = get_weather(lat,lon, key)
    data = process_weather_data(location, weather)
    print_weather(data)
    save_weather_to_csv(data)

main()

