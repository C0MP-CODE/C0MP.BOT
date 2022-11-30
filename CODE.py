import nextcord
import inquirer

token = "YOUR BOT TOKEN"
client = nextcord.Client()

@client.event
async def on_ready():
    guild = client.guilds[0]
    choices = []

    #Append all channels into array "choices"
    for channel in guild.channels: 
        if str(channel.type) == "text":
            choices.append(f"#{channel.name} ({channel.id})")

    #Show choices and questions, get user input for questions
    questions = [inquirer.List('cnl', message="What channel would you like to send the message to?", choices=choices, carousel=True), inquirer.Text('Title', message="What would you like the Title to be?"), inquirer.Text('Description', message="What would you like the description to be?"), inquirer.Text('url', message="What is the image url?"), inquirer.Text('price', message="What is the product price?"),]

    #Get the selected channel id and save the channel into "cnl"
    answers = inquirer.prompt(questions)
    channel = answers['cnl'].replace(")", "").split("(")[1]
    cnlid = int(channel)
    cnl = guild.get_channel(cnlid)
    
    #Embed and send message
    embed = nextcord.Embed(title=answers['Title'], description=answers['Description'], color=0xAAFF00)
    if answers['url'] != "" and answers['url'].startswith('ht'): 
        embed.set_image(url = answers['url'])
    if answers['price'] != "":
        message = client.get_channel(1046435381148668013).mention
        embed.add_field(name="PRICE:", value=answers['price'], inline=False)
        embed.add_field(name="Open a ticket at:", value=message, inline=False)
    await cnl.send(embed=embed)

    #If message sent print on console "Message Sent"
    print("Message Sent")

client.run(token)
