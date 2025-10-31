cities = [
    "London", "Paris", "New York", "Tokyo", "Mumbai", 
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai", 
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "London", "Paris", "New York", "Tokyo", "Mumbai", 
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "London", "Paris", "New York", "Tokyo", "Mumbai", 
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai", 
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo",
    "London", "Paris", "New York", "Tokyo", "Mumbai",
    "Berlin", "Moscow", "Beijing", "Sydney", "Toronto",
    "Rome", "Madrid", "Singapore", "Dubai", "Cairo"

]

API_KEY = "1f67cd4aa973dd153bbc2474c904ab3f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(session, cityGroup):
    if isinstance(cityGroup, str): 
        cityGroup = [cityGroup]

    for city in cityGroup:
        try:
            with session.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"}) as response:
                data = response.json()
                temp = data["main"]["temp"]
                return city, temp
        except Exception as e:
            return city, f"ERROR: {e}"
    
