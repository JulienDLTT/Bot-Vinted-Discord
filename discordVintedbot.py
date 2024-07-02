import discord
client = discord.Client(intents=discord.Intents.default())
from pyVinted import Vinted
from time import sleep
vinted = Vinted()

#==========================================================================================

def table_message(article,lien,photo,prix,marque):
    embed = discord.Embed(
        title="Article trouvé",
        description="Voici quelques informations sur l'article PS : Julien ",
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
    general_channel = client.get_channel("salon_discord")
    items = vinted.items.search("https://www.vinted.fr/vetement?order=newest_first&price_to=60&currency=EUR",10,1)
    item1 = items[0]
    #title
    titre = item1.title
    print(titre)
    #photo url
    photo = item1.photo
    #brand
    marque = item1.brand_title
    #price
    prix = item1.price
    print(prix)
    #url
    url = item1.url
    print(url)
    #currency
    item1.currency
    embed_message = table_message(titre, url, photo, prix, marque)
    await general_channel.send(embed = embed_message)



client.run("token_bot")