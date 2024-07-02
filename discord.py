import discord
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print("Le bot est prêt !")
    general_channel = client.get_channel("salon_discord")
    table_message = (
            "```\n"
            "Bot prêt !\n\n"
            "------------------------\n"
            "|    Bot Information   |\n"
            "------------------------\n"
            f"| Nom du bot : {client.user.name}\n"
            f"| ID du bot  : {client.user.id}\n"
            "------------------------\n"
            "```"
        )
    if general_channel:
        await general_channel.send(table_message)
    else:
        print("Le channel spécifié n'a pas été trouvé.")


client.run("token_bot")



