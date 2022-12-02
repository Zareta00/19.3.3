import requests
import json
import conf


base_url = 'https://petstore.swagger.io/v2'

# GET/ Logs user

username = conf.username  
password = conf.password  

res = requests.get(f'{base_url}/user/login?login={username}&password={password}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.json())
print(res.headers)


# POST/ Create user

body = json.dumps(conf.created_user)

res = requests.post(f'{base_url}/user', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=body)

print(res.status_code)
print(res.json())


# PUT /Updated user

username = conf.created_user['username']
body = json.dumps(conf.updated_user)

res = requests.put(f'{base_url}/user/{username}', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=body)

print(res.status_code)
print(res.json())


# DELETE /Delete user

username = conf.updated_user['username']

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.json())