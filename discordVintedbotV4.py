import discord
client = discord.Client(intents=discord.Intents.default())
from pyVinted import Vinted
from time import sleep
vinted = Vinted()
moi = "salon_discord"
flo = "salon_discord"

#==========================================================================================

def table_message(article,lien,photo,prix,marque):
    embed = discord.Embed(
        title="Article trouvé !",
        description="Bot créé par DELATTRE Julien (BG):",
        color=discord.Color.green()
    )

        # Ajout de champs au Embed (titre et valeur)
    embed.add_field(name="Article", value=article, inline=False)
    embed.add_field(name="Marque", value=marque, inline=False)
    embed.add_field(name="Lien", value=lien, inline=False)
    embed.add_field(name="Prix", value=f"{prix}€", inline=False)

        # Ajout d'une image au Embed (remplacez l'URL par l'URL de votre image)
    embed.set_thumbnail(url=photo)
    return embed


@client.event
async def on_ready():
    print("Le bot est prêt !")
    general_channel = client.get_channel(flo)
    while True:
        try:
            items = vinted.items.search("https://www.vinted.fr/catalog?brand_ids[]=53&order=newest_first&price_to=30&currency=EUR&size_ids[]=207&size_ids[]=208&size_ids[]=784&size_ids[]=785&size_ids[]=786&size_ids[]=787&size_ids[]=788&size_ids[]=789&size_ids[]=206&size_ids[]=209&size_ids[]=210&size_ids[]=782&size_ids[]=783&size_ids[]=790&size_ids[]=791&size_ids[]=792&size_ids[]=793&size_ids[]=794&size_ids[]=795&size_ids[]=1190",10,1)
            for i in range(9):
                item1 = items[i]
                if item1.brand_title == 'Nike':
                    titre = item1.title
                    print(titre)
                    url = item1.url
                    print(url)
                    marque = item1.brand_title
                    print(marque)
                    photo = item1.photo
                    prix = item1.price
                    print(prix)
                    embed_message = table_message(titre, url, photo, prix, marque)
                    await general_channel.send(embed = embed_message)
                    print(item1.size_title)

            sleep(0.3)
            print("nike fait")

            items = vinted.items.search("https://www.vinted.fr/catalog?currency=EUR&price_to=30&order=newest_first&brand_ids[]=88&brand_ids[]=430791&brand_ids[]=4559748&brand_ids[]=6962946",10,1)
            for i in range(9):
                item1 = items[i]
                if item1.brand_title == 'Ralph Lauren' or item1.brand_title == 'Lauren Ralph Lauren' or item1.brand_title == 'RALPH Ralph Lauren' or item1.brand_title == 'Ralph Lauren Sport' :
                    titre = item1.title
                    print(titre)
                    url = item1.url
                    print(url)
                    marque = item1.brand_title
                    print(marque)
                    photo = item1.photo
                    prix = item1.price
                    print(prix)
                    embed_message = table_message(titre, url, photo, prix, marque)
                    await general_channel.send(embed = embed_message)

            sleep(0.3)
            print("Ralph Lauren fait")

            items = vinted.items.search("https://www.vinted.fr/catalog?price_to=30&currency=EUR&order=newest_first&brand_ids[]=362&brand_ids[]=872289",10,1)
            for i in range(9):
                item1 = items[i]
                if item1.brand_title == 'Carhartt' or item1.brand_title == 'Carhartt WIP':
                    titre = item1.title
                    print(titre)
                    url = item1.url
                    print(url)
                    marque = item1.brand_title
                    print(marque)
                    photo = item1.photo
                    prix = item1.price
                    print(prix)
                    embed_message = table_message(titre, url, photo, prix, marque)
                    await general_channel.send(embed = embed_message)

            sleep(0.3)
            print("Carharrt fait")

            items = vinted.items.search("https://www.vinted.fr/catalog?price_to=30&currency=EUR&order=newest_first&brand_ids[]=14&brand_ids[]=194976&brand_ids[]=115490",10,1)
            for i in range(9):
                item1 = items[i]
                if item1.brand_title == 'adidas' or item1.brand_title == 'adidas Originals' or item1.brand_title == 'Yeezy':
                    titre = item1.title
                    print(titre)
                    url = item1.url
                    print(url)
                    marque = item1.brand_title
                    print(marque)
                    photo = item1.photo
                    prix = item1.price
                    print(prix)
                    embed_message = table_message(titre, url, photo, prix, marque)
                    await general_channel.send(embed = embed_message)
                    print(item1.size_title)

            sleep(0.3)
            print("Adidas fait")
        except:
            pass




client.run("token_bot")