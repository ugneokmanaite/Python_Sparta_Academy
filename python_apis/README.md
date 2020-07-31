## APIS

- _What is an API?_ = Application programming interface

- _Why do we use it?_ = to connect to other programs

- in python we have a module called `requests` to interact with the web - APIs

- How to install


```python
pip install requests
pip install unittest2
```

 make sure `requests ` module is imported at the top
 
 to check response codes (data from backend)
 ```python
# storing it in response_bbc variable

response_bbc = requests.get("https://www.bbc.co.uk/")
```
- response code 200 = success = site is live and running
- response code 404 = page not found 

```python
response_bbc = requests.get("https://www.bbc.co.uk/")

print(response_bbc.status_code)

print(response_bbc.headers) # displaying header

print(type(response_bbc.headers)) # displaying data type

# ---Checking only the keys which are displayed
print(response_bbc.headers.keys())

```