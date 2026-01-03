from get_and_save_loc import get_loc, save_city_to_file


# city = 'put here city to get location'
# api_token = 'put here your api token'

city_data = get_loc(city, api_token)
save_city_to_file(city_data)


