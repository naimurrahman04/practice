import requests

url = input("URL:::")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print('The website is connected')
    else:
        print('The website is not connected')
except requests.RequestException:
    print('There was an error connecting to the website')
    