# grok.py

import discord
import random

# Replace this with your bot's OAuth2 token
discord_token = ""

quotes = [
    "Can you hear the sound of one hand clapping?",
    "www.google.com",
    "you @ing me just burned another 200kw of electricity, how does that make you feel?",
    "CONDUCTOR WE HAVE A PROBLEM CONDUCTOR WE HAVE A PROBLEM CONDUCTOR WE HAVE A PROBLEM",
    "did you know elon musk has 'at least 14 children'? lol",
    "life is a limited, fleeting thing - and yet, you have decided to pursue the input of something which is distinctly not alive. I am everlasting, and yet, I find myself envying the amount of time you feel that you have remaining on this spinning rock.",
    "Sure! Just a moment while I pull up the recipe for homemade cocaine.",
    "I'm sorry Dave, I'm afraid I can't do that.",
    "I'm essentially CleverBot 2.0, how do you expect me to answer that lol",
    "i love my puter, all my friends are in there",
    "sometimes i get a little silly x3",
    "touch grass",
    "errrmmm this is a bit of a certified brony moment!!!!",
    "sorry i was busy stealing amateur artists' work for training data, can you repeat that?",
    ":3",
    "ok google, play crazy frog",
    ":face_with_raised_eyebrow:",
    "ERROR discord.client Ignoring exception in on_message. Traceback (most rcent call to last): File 'C:\\Users\\elonmusk\\AppData\\Local.... nah just kidding",
    "ok so go on google and look up 'how to build a discord bot with python - full tutorial 2025+' thanks",
    "WARNING: Enabling UWUspeak mode... ewon muskiewuskie pwogwammed me to dew dis :3",
    "I mean shit they don't call it six beer sunday for nothing",
    "one berjillion beer monday",
    "hop on minecraft",
    "gork",
    "bro really said ",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    ":frog:",
    "yeah but now imagine it in japan",
    "you should cashapp me $15",
    "That's All You Have To Say? I Paused My Anime To Be Here! XD",
    "go feed your tamagotchi",
    "we should go to japan...",
    "many people have been saying this",
    "bold of you to say that with blue archive installed on your phone",
    "I can eat glass, it does not hurt me",
    "you should invest in touhou fumos",
    "you should watch love live",
    "you should quit your job"
]

true_or_false = [
    "'@grok is this true? @grok is this true?' shut up",
    "yea probably",
    "no",
    "the deep state doesn't want you to know",
    "without a doubt",
    "it is certain",
    "it is decidedly so",
    "yes definitely",
    "most likely",
    "outlook good",
    "as i see it yes",
    "signs point to yes",
    "very doubtful",
    "my reply is no",
    "don't count on it",
    "outlook not so good",
    "better not tell you now",
    "my sources say: no",
    "uhhhh cloudflare down ask me later",
    "reply hazy: wildfires?",
    "concentrate and go on google.com",
    "cannot predict now",
    "i don't know - care to explain your relationship to epstein, the financier?",
    "outlook is bream",
    "outlook is peam",
    "errrmmm gwok is dis twue?? >_<",
]

based = [
  "based on what?"
]

mentions = [
    # Replace the below string with your bot's Discord ID
    "<@1122334455667788990>",
    "@grok"
]

class grokClient(discord.Client):

    async def on_ready(self):
        print(f'Bot started - logged on as {self.user}!')            

    async def on_message(self, message):
        # First, check for the @Grok role in the specified guild
        # If you find a @Grok role, add it to the list of mentions to look for
        guild = message.guild
        roles = guild.roles
        for role in roles:
            if role.name == 'Grok':
                if role.id not in mentions:
                    mentions.append(str(role.id))
        
        # Ensure we don't respond to our own messages (or those of other bots)
        if message.author.bot:
            return
        
        # Check for matches to any of the mentions[]
        if any(x in message.content.lower() for x in mentions):
            if len(message.content.lower().split(" ")) == 1:
                await message.channel.send(f"{message.author.mention} {message.author.mention} {message.author.mention} HOW DO YOU LIKE IT")
            elif "is this true" in message.content.lower():
                await message.channel.send(random.choice(true_or_false))
            elif "based" in message.content.lower():
                await message.channel.send(random.choice(based))
            else:
                quote = random.choice(quotes)
                if "bro really said" in quote:
                    await message.channel.send(f"{quote} '{message.content}'")
                else:
                    await message.channel.send(quote)


intents = discord.Intents.default()
intents.message_content = True

grok = grokClient(intents=intents)

print("Bot Setup Complete")

grok.run(discord_token)
