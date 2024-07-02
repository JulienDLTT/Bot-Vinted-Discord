import requests

url = "https://vinted3.p.rapidapi.com/getProduct"

querystring = {"country":"fr","productId":"4068444693"}

headers = {
	"X-RapidAPI-Key": "c777af8e5cmshc8d3372747c0dbap12cb8ajsndee993d40743",
	"X-RapidAPI-Host": "vinted3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())