from weather import *

def main():

    country = get_country_code()
    if is_usa(country):
        state = get_us_code()
    else:
        state = None
    city = get_city()
    key = get_key()

    coordinations = get_location(country, state, city, key, )
    weather = get_weather(coordinations[0]["lat"],coordinations[0]["lon"], get_key())
    data = process_weather_data(coordinations,weather)
    save_weather_to_csv(data)
    print_weather(data)


main()