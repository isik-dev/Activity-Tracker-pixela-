import requests
from datetime import datetime
from decouple import config

USERNAME = config("USERNAME", default="")
TOKEN = config("TOKEN", default="")
GRAPH_ID = config("GRAPH_ID", default="")
MY_PROGRESS = config("MY_PROGRESS", default="")

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "JavaScript Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=5, day=19)
pixel_date = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you work on JavaScript today?"),
}


# Posting on a certain date
response = requests.post(url=pixel_creation_endpoint, json=pixel_date, headers=headers)
print(response.text)


# Updating a certain date
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "2.5"
# }
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# Deleting a certain date
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)