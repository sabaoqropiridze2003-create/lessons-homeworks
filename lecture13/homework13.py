import requests


def get_user_info(user_id):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()

    for d in data:
        if d.get("id") == user_id:
            return {
                "name": d.get("name"),
                "email": d.get("email"),
                "city": d.get("address", {}).get("city"),
                "company": d.get("company", {}).get("name")
            }
    return None


print("User 1:", get_user_info(1))
print("User 2:", get_user_info(9))
print("user 200:", get_user_info(200))
