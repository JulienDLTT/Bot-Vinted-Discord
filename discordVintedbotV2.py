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
        title="Article trouvé",
        description="Voici quelques informations sur l'article PS : Julien",
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
        items = vinted.items.search("https://www.vinted.fr/catalog?brand_ids[]=53&order=newest_first&price_to=30&currency=EUR",10,1)
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

        sleep(0.3)
        print("nike fait")




client.run("token_bot")