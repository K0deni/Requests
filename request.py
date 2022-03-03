import requests
# Standart view of requests
# res = request.type_of_request(url,params=params)
# Creation of user on reqres.in with request POST
# request.put, request.get, request.patch, request.post } types of requests 
# url = address of request
# payload = body of request if it needed 
# print(req1.text) } Print of text of response of this request
# print(req1.status_code) } Print of status_code of response of this request
payload = {
    "name": "morpheus",
    "job": "leader"
}  
req1 = requests.post('https://reqres.in/api/users', params=payload)
print(req1.status_code)
print(req1.text) 

# Get information about users on reqres.in with request GET
req2 = requests.get('https://reqres.in/api/users?page=2')
print(req2.status_code)
print(req2.text)

# Update information on reqres.in with request PUT
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
url = 'https://reqres.in/api/users=2'
req3 = requests.put(url,params=payload)
print(req3.status_code)
print(req3.text)

# Update information on reqres.in with request PATCH
payload = {
    "name": "morpheus",
    "job": "chief resident"
}
url = 'https://reqres.in/api/users=2'
req4 = requests.patch(url,params=payload)
print(req4.status_code)
print(req4.text)

# Delete information on reqres.in with request DELETE
url = 'https://reqres.in/api/users=2' 
req5 = requests.delete(url)
print(req5.status_code)
# On this response we can see Code: 204. Which means 'No content'

# Unsuccessfull register on reqres.in with request POST
url = 'https://reqres.in/api/register'
payload = {
    "email": "eve.holter@reqres.in"
}
req6 = requests.post(url,params=payload)
print(req6.status_code)
print(req6.text)
print(req6.headers)

