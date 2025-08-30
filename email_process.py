import requests

base_url = "https://reqres.in/api"
endpoint = "/users"
my_api_header = {
    "x-api-key": "reqres-free-v1",
    "token": "sdlsfjjfvlhfnsjogjjlbnljdnkxn"
}

endpoint = "/auth"

payload = {
    'username': 'sivani',
    'password': 'password'
}

response = requests.get(url=base_url+endpoint, payload=payload)


# Our task is to fetch all the email ids from the api data in total pages

# First we will fetch total number of pages count
response = requests.get(url=base_url+endpoint, headers=my_api_header)
# print(response.status_code)
if response.status_code == 200:
    total_number_pages = response.json().get('total_pages')
    print(total_number_pages)

all_emails = []
all_users_data = [] # [[...], [...]] # [{..}, {..}]
# After getting total number we need to fetch each page data and store 
for page_no in range(1, total_number_pages+1):
    page_response = requests.get(url=base_url+endpoint+f"?page={page_no}", headers=my_api_header)
    # print(page_response.status_code)
    users_data = page_response.json().get("data")
    all_users_data.extend(users_data)

# print(all_users_data)

for user_data in all_users_data:
    all_emails.append(user_data["email"])

print(all_emails)
