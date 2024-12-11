import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#load enviroment variables
load_dotenv()
client = discord.Client()
token = os.getenv('TOKEN')

#initalizing the bot
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#setting up bot responses
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f"Hello {username} Your EC2 Data: {ec2_metadata.region}")
            return

        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "EC2 Data":
            await message.channel.send("Your instance data is" + ec2_metadata.region)

#running the bot 
client.run(token) 


from discord.ext import commands 

#choosing a prefix for when bot will listen to commands
client = commands.Bot(command_prefix="!")
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')




















