import discord
import Cache
intents = discord.Intents.default()
intents.members = True
intents.messages = True
import asyncio
client = discord.Client(intents=intents)
from pyVinted import Vinted
from time import sleep
vinted = Vinted()
moi = "salon_discord"
adidas = "salon_discord"
carhartt = "salon_discord"
jordanike = "salon_discord"
lacoste = "salon_discord"
ralph = "salon_discord"
TNF = "salon_discord"
salonserv = "salon_discord"
bagSac = "salon_discord"
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
    adidas_channel = client.get_channel(adidas)
    carhartt_channel = client.get_channel(carhartt)
    jordanike_channel = client.get_channel(jordanike)
    lacoste_channel = client.get_channel(lacoste)
    ralph_channel = client.get_channel(ralph)
    TNF_channel = client.get_channel(TNF)
    Baggy_sacoche = client.get_channel(bagSac)
    salonserv_channel = client.get_channel(salonserv)
    vintail = 100
    while True:
        try:
            try:
                items = vinted.items.search("https://www.vinted.fr/catalog?order=newest_first&price_to=30&currency=EUR",vintail,1) 
            except :
                items = 0
                print("prblmobj")
            if items != 0:
                for i in range(len(items)):
                    item1 = items[i]
                    if item1.brand_title == 'Nike' or item1.brand_title == 'Ralph Lauren' or item1.brand_title == 'Lauren Ralph Lauren' or item1.brand_title == 'RALPH Ralph Lauren' or item1.brand_title == 'Ralph Lauren Sport' or item1.brand_title == 'Carhartt' or item1.brand_title == 'Carhartt WIP' or item1.brand_title == 'adidas' or item1.brand_title == 'adidas Originals' or item1.brand_title == 'Lacoste' or item1.brand_title == 'Lacoste Sport' or item1.brand_title == 'The North Face' or item1.brand_title == 'Jordan' or 'sacoche' in item1.title or 'Sacoche' in item1.title or 'baggy' in item1.title or 'Baggy' in item1.title or item1.brand_title == 'BoohooMAN' or item1.brand_title == 'Bohooman' :
                        if (cache.verifier_valeur(item1.url)) == True:
                            print("déjàfait")
                        elif item1.size_title == 'M' or item1.size_title == 'S' or item1.size_title == 'XS' or item1.size_title == 'L' or item1.size_title == 'XL' or item1.size_title == 'XXL' or item1.size_title == 'XXXL':
                            titre = item1.title
                            url = item1.url
                            cache.ajouter_valeur(url)
                            marque = item1.brand_title
                            photo = item1.photo
                            prix = item1.price
                            taille = item1.size_title
                            print(titre)
                            print(url)
                            print(marque)
                            print(prix)
                            print(taille)
                            embed_message = table_message(titre, url, photo, prix, marque,taille)
                            await salonserv_channel.send(embed = embed_message)
                            if marque == 'Nike' or marque == 'Jordan':
                                await jordanike_channel.send(embed = embed_message)
                            elif marque == 'Ralph Lauren' or marque == 'Lauren Ralph Lauren' or marque == 'RALPH Ralph Lauren' or marque == 'Ralph Lauren Sport':
                                await ralph_channel.send(embed = embed_message)
                            elif marque == 'Carhartt' or marque == 'Carhartt WIP':
                                await carhartt_channel.send(embed = embed_message)
                            elif marque == 'adidas' or marque == 'adidas Originals':
                                await adidas_channel.send(embed = embed_message)
                            elif marque == 'Lacoste Sport' or marque == 'Lacoste':
                                await lacoste_channel.send(embed = embed_message)
                            elif marque == 'The North Face':
                                await TNF_channel.send(embed = embed_message)
                        elif 'sacoche' in item1.title or 'Sacoche' in item1.title or 'baggy' in item1.title or 'Baggy' in item1.title or item1.brand_title == 'BoohooMAN' or item1.brand_title == 'Bohooman' :
                            titre = item1.title
                            url = item1.url
                            cache.ajouter_valeur(url)
                            marque = item1.brand_title
                            photo = item1.photo
                            prix = item1.price
                            taille = item1.size_title
                            print(titre)
                            print(url)
                            print(marque)
                            print(prix)
                            print(taille)
                            embed_message = table_message(titre, url, photo, prix, marque,taille)
                            await salonserv_channel.send(embed = embed_message)
                            await Baggy_sacoche.send(embed = embed_message)

            await asyncio.sleep(0.3)
            print("fait")

        except Exception as e:
            print(f"erreur: {e}")
            pass




client.run(TOKEN_BOT)