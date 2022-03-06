import discord
import asyncio
import logging
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print("log")
	

@client.event
async def on_member_join(member):
	channel = client.get_channel(id=947834000670588988)
	roles = client.get_channel(id=947483054962782218)
	rules = client.get_channel(id=947888817837326447)
	rty = (f"❤️ welcome  to the three heavenly Kings ⚔️ we are gratefull to you be here 🙇 please go to {roles.mention} to choose your character and see the {rules.mention}")
	embedVar = discord.Embed(title="welcome legend ⚔️",description=rty, color=0x00ff00)
	await channel.send(embed=embedVar) 

@client.event
async def on_member_remove(member):
	channet = client.get_channel(id=947834161127911444)
	rty = (f"❤we lost a legent {member.mention}")
	embedVar = discord.Embed(title="sad news",description=rty, color=0x00ff00)
	await channel.send(embed=embedVar) 



client.run("OTQ3ODY5Mzg0OTgwOTg3OTM1.YhziJw.BU8eropZvYG8t58juZNJvrht34w")
