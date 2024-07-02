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
flo = "salon_serv"
salonserv = "salon_serv"
TOKEN_BOT = "token_bot"

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
    urltest = ''
    print("Le bot est prêt !")
    general_channel = client.get_channel(salonserv)
    vintail = 100
    while True:
        try:
            items = vinted.items.search("https://www.vinted.fr/catalog?order=newest_first&price_to=30&currency=EUR",vintail,1) #https://www.vinted.fr/catalog?brand_ids[]=14&brand_ids[]=53&brand_ids[]=194976&brand_ids[]=115490&brand_ids[]=362&brand_ids[]=872289&brand_ids[]=88&brand_ids[]=430791&brand_ids[]=4559748&brand_ids[]=6962946&brand_ids[]=304&brand_ids[]=677891&brand_ids[]=2319&order=newest_first&price_to=30&currency=EUR
            for i in range(len(items)):
                item1 = items[i]
                if item1.brand_title == 'Nike' or item1.brand_title == 'Ralph Lauren' or item1.brand_title == 'Lauren Ralph Lauren' or item1.brand_title == 'RALPH Ralph Lauren' or item1.brand_title == 'Ralph Lauren Sport' or item1.brand_title == 'Carhartt' or item1.brand_title == 'Carhartt WIP' or item1.brand_title == 'adidas' or item1.brand_title == 'adidas Originals' or item1.brand_title == 'Lacoste' or item1.brand_title == 'Lacoste Sport' or item1.brand_title == 'The North Face' or item1.brand_title == 'Jordan':
                    if urltest == item1.url:
                        print("déjàfait")
                    elif item1.size_title == 'M' or item1.size_title == 'S' or item1.size_title == 'XS' or item1.size_title == 'L' or item1.size_title == 'XL' or item1.size_title == 'XXL' or item1.size_title == 'XXXL':
                        titre = item1.title
                        print(titre)
                        url = item1.url
                        urltest = url
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
                        if taille == 'XXXL':
                            member = general_channel.guild.get_member(310090172215721986)
                            await general_channel.send(member.mention)

            await asyncio.sleep(0.3)
            print("fait")

        except Exception as e:
            print(f"erreur: {e}")
            pass




client.run(TOKEN_BOT)