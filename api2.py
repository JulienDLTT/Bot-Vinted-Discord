import requests

url = "https://vinted3.p.rapidapi.com/getSearch"

querystring = {"country": "fr", "page": "1", "order": "newest_first", "maxPrice": "30"}

headers = {
	"X-RapidAPI-Key": "c777af8e5cmshc8d3372747c0dbap12cb8ajsndee993d40743",
	"X-RapidAPI-Host": "vinted3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Vérifiez si la requête a réussi (code de statut HTTP 200)
if response.status_code == 200:
    # Obtenez le contenu JSON de la réponse
    data = response.json()
    # Si la réponse contient des résultats
    if data:
        # Parcourir les éléments de la réponse (dans ce cas, il semble que la réponse soit une liste)
        for item in data:
            # Accédez à la marque ('brand') de chaque élément
            brand = item.get('brand')
            url = item.get('url')
            price = item.get('price', {}).get('amount')
            title = item.get('title')
            size = item.get('size')
            id = item.get('productId')
            #if brand == 'Nike':
            print(title)
            print(url)
            print(brand)
            print(size)
            print(price)
            print(id)
            # Imprimez la marque
            
    else:
        print("Aucun résultat trouvé.")
else:
    print("La requête a échoué avec le code de statut :", response.status_code)