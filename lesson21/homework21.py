# წინა დავალების პირველი ამოცანა

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


p1 = Person("Otar", 35)


def student_serializer(student):
    if isinstance(student, Person):
        return f"Name: {student.name}, Age: {student.age}"
    return "Not a Person instance"


with open("lesson20/persons.txt", "w") as file:
    file.write(student_serializer(p1))


def student_deserializer(data_string):
    if "Name:" in data_string and "Age:" in data_string:
        parts = data_string.split(",")
        name = parts[0].split(":")[1].strip()
        age = int(parts[1].split(":")[1].strip())
        return Person(name, age)
    return "not a valid data format"


with open("lesson20/persons.txt", "r") as file:
    file_content = file.read().strip()
    student = student_deserializer(file_content)

print(student)


# დღევანდელი დავალება


# import requests

# city_input = input("Enter city name: ").strip()


# geo_url = "https://geocoding-api.open-meteo.com/v1/search"
# geo_params = {"name": city_input, "count": 1}

# geo_response = requests.get(geo_url, params=geo_params)
# geo_data = geo_response.json()


# if "results" in geo_data and len(geo_data["results"]) > 0:
#     city_info = geo_data["results"][0]
#     lat = city_info["latitude"]
#     lon = city_info["longitude"]
#     city_name = city_info["name"]

#     weather_url = "https://api.open-meteo.com/v1/forecast"
#     weather_params = {
#         "latitude": lat,
#         "longitude": lon,
#         "current": "temperature_2m,wind_speed_10m",
#         "timezone": "auto",
#     }

#     weather_response = requests.get(weather_url, params=weather_params)
#     weather_data = weather_response.json()

#     current = weather_data["current"]
#     units = weather_data.get("current_units", {})

#     print(f"City: {city_name}")
#     print(
#         f"Temperature: {current['temperature_2m']} {units.get('temperature_2m', '°C')}")
#     print(
#         f"Wind Speed: {current['wind_speed_10m']} {units.get('wind_speed_10m', 'km/h')}")
#     print(f"Time: {current['time']}")
# else:
#     print("City not found")
