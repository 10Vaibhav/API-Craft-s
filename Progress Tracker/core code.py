import requests
from datetime import datetime

TOKEN = "" # Put your token here 
USERNAME = "" # Put Your username here
GRAPH_ID = "progresstracker"

##################### Creating a User ######################################

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

######################## Creating a Graph #################################
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Progress Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

########################## Add a Pixel #################################################

pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime(year=2024, month=12, day=21)
today = datetime.now()
pixel_add_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9",
}
# response = requests.post(url=pixel_add_endpoint, json=pixel_add_params, headers=headers)
# print(response.text)

######################## Update the Pixel on Graph ##########################################
Date_to_update = "20241221"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{Date_to_update}"

pixel_update_params = {
    "quantity": "2",
}

# response = requests.put(url=pixel_update_endpoint,json=pixel_update_params,headers=headers)
# print(response.text)

######################## Delete the Pixel on Graph ############################################
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{Date_to_update}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
