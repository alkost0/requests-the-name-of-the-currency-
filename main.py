import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=100"

payload = {}
headers= {
  "apikey": "SRytJ4WcGXamDBx4vlkTbBHe3utUBcd6"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

#text_test