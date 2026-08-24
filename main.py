from weather import *

def main():

    country = get_country_code()
    city = get_city()
    key = get_key()

    coordinations = get_location(country, city, key=key)
    weather = get_weather(coordinations[0]["lat"],coordinations[0]["lon"], get_key())
    data = process_weather_data(coordinations,weather)
    print_weather(data)
    save_weather_to_csv(data)

main()