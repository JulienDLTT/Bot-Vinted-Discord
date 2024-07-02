import discord
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)
from pyVinted import Vinted
from time import sleep
vinted = Vinted()
moi = "salon_discord"
flo = "salon_discord"
baptou = "salon_discord"

#==========================================================================================

def table_message(article,lien,photo,prix,marque,taille):
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
    embed.add_field(name="Taille", value=taille, inline=False)

        # Ajout d'une image au Embed (remplacez l'URL par l'URL de votre image)
    embed.set_thumbnail(url=photo)
    return embed


@client.event
async def on_ready():
    urltest = ''
    print("Le bot est prêt !")
    general_channel = client.get_channel(baptou)
    vintail = 50
    while True:
        try:
            items = vinted.items.search("https://www.vinted.fr/catalog?order=newest_first&currency=EUR&price_to=100&brand_ids[]=44",vintail,1)#https://www.vinted.fr/catalog?order=newest_first&currency=EUR&price_to=100&brand_ids[]=44
            for i in range(vintail):
                item1 = items[i]
                if item1.brand_title == 'Timberland':
                    if urltest == item1.url:
                        pass
                    elif item1.size_title == '44' or item1.size_title == '44.5' or item1.size_title == '45' or item1.size_title == '45.5':
                        member = general_channel.guild.get_member(310090172215721986)
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
                        await general_channel.send(member.mention)

            sleep(1)
            print("fait")

        except:
            pass




client.run("Token_bot")