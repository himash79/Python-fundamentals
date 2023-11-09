import requests as req
import urllib3
import json

r = req.get('https://jsonplaceholder.typicode.com/users')
# print(r.text)

http = urllib3.PoolManager()
resp = http.request('GET', 'https://jsonplaceholder.typicode.com/users')
# print(resp.data)
# print(resp.status)
# print(resp.info())

respPost_01 = http.request('POST', 'https://jsonplaceholder.typicode.com/users',
                           fields = {'id': 3})
# print(respPost_01.data)
# print(json.loads(respPost_01.data.decode('utf-8')))
# print(respPost_01.status)

respAuth = req.get('https://api.github.com/user', auth=('user', 'pass'))
print(respAuth)