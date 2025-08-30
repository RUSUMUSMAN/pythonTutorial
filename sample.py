import requests

my_url = "https://reqres.in/api/users"
base_url = "https://reqres.in/api"
endpoint = "/users?page=100"
my_api_header = {
    "x-api-key": "reqres-free-v1"
}

response = requests.get(url=base_url+endpoint, headers=my_api_header)

# what if we get hundred pages 
print(response.status_code)
print(response.text)
# response_data = response.json()
# print(response_data)

# Below 2 lines will do same thing
# total_pages = response_data.get("total_pages")
# total_pages = response_data["total_pages"]
# print(total_pages)

# for fetching a specififc data we can use
# for page_no in range(1,total_pages+1):
#     query = f"?page={page_no}"
#     page_url = base_url + endpoint + query
#     page_response = requests.get(url=page_url, headers=my_api_header)
#     print(f"Page No: {page_no} Status:{page_response.status_code}")
#     print(f"Response of page: {page_response.text}")
#     print(f"{'='*70}")
