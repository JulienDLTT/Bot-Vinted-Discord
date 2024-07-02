import Cache
import discord
intents = discord.Intents.default()
intents.members = True
intents.messages = True
import asyncio
client = discord.Client(intents=intents)
from pyVinted import Vinted
from time import sleep
vinted = Vinted()
moi = "salon_serv"
paires = "salon_serv"
TOKEN_BOT = "token_bot"
cache = Cache.Cache()

#==========================================================================================

def table_message(article,lien,photo,prix,marque,taille):
    embed = discord.Embed(
        title="Bonne chasse servez vous!",
        description="Bot créé par DELATTRE Julien (BG):",
        color=discord.Color.green()
    )

        # Ajout de champs au Embed (titre et valeur)
    embed.add_field(name="Article", value=article, inline=False)
    embed.add_field(name="Marque", value=marque, inline=False)
    embed.add_field(name="Lien", value=lien, inline=False)
    embed.add_field(name="Prix", value=f"{prix}€", inline=False)
    embed.add_field(name="Taille", value=taille, inline=False)

        # Ajout d'une image au Embed (remplacez l'URL par l'URL de votre image)
    embed.set_thumbnail(url=photo)
    return embed


@client.event
async def on_ready():
    print("Le bot est prêt !")
    general_channel = client.get_channel(paires)
    vintail = 10
    while True:
        
        try:
            try:
                items = vinted.items.search("https://www.vinted.fr/catalog?order=newest_first&price_to=250&currency=EUR",vintail,1) 
            except :
                items = 0
                print("prblmobj")
            if items != 0:
                for i in range(len(items)):
                    item1 = items[i]
                    if item1.brand_title == 'Nike' or item1.brand_title == 'adidas' or item1.brand_title == 'adidas Originals' or item1.brand_title == 'New Balance' or item1.brand_title == 'Jordan' or item1.brand_title == 'Timberland'  or item1.brand_title == 'Yeezy':
                        if (cache.verifier_valeur(item1.url)) == True:
                            print("déjàfait")
                        elif item1.size_title == '41,5' or item1.size_title == '42' or item1.size_title == '41' or item1.size_title == '42,5' or item1.size_title == '40' or item1.size_title == '40,5' or item1.size_title == '43' or item1.size_title == '43,5' or item1.size_title == '44' or item1.size_title == '44,5' or item1.size_title == '45' or item1.size_title == '45,5' or item1.size_title == '46' or item1.size_title == '46,5' or item1.size_title == '47' or item1.size_title == '47,5':
                            titre = item1.title
                            print(titre)
                            url = item1.url
                            cache.ajouter_valeur(url)
                            print(url)
                            marque = item1.brand_title
                            print(marque)
                            photo = item1.photo
                            prix = item1.price
                            print(prix)
                            taille = item1.size_title
                            print(taille)
                            embed_message = table_message(titre, url, photo, prix, marque,taille)
                            await general_channel.send(embed = embed_message)

                await asyncio.sleep(1)
                print("fait")

        except Exception as e:
            print(f"erreur: {e}")
            await asyncio.sleep(2)
            pass


client.run(TOKEN_BOT)