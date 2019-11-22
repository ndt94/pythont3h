import requests, json
url = 'http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8'

request = requests.get(url)
obj = json.loads(request.text)

for item in obj['list']:
    print(item['dt_txt'], ':', item['main']['temp'], ' độ C')
