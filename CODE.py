import nextcord
import inquirer

token = "MTA0NzE5ODIxODM2ODMyMzY4NA.G0lB6I.m252j7HQwoaamQksRrm53gcizabSd4gnDB3CbQ"
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
    questions = [inquirer.List('cnl', message="What channel would you like to send the message to?", choices=choices, carousel=True), inquirer.Text('Title', message="What would you like the Title to be?"), inquirer.Text('Description', message="What would you like the description to be?"), inquirer.Text('url', message="What is the image url?"),]
    
    answers = inquirer.prompt(questions)
    cnlid = int(answers['cnl'][10:-1])
    cnl = guild.get_channel(cnlid)

    #Embed and send message
    embed = nextcord.Embed(title=answers['Title'], description=answers['Description'], color=0xAAFF00)
    if answers['url'] != "" and answers['url'].startswith('ht'): 
        embed.set_image(url = answers['url'])
    await cnl.send(embed=embed)

    print("Message Sent")

client.run(token)