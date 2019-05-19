import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
from itertools import cycle


Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Ready to be used.')


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello and Welcome to my server non gay friend')
    print('Sent message to ' + member.name)
	
	
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='80s gay music'))
    print('Ready, Freddy') 


            #talk
@client.event
async def on_message(message):
    if message.content == 'not much':
        await client.send_message(message.channel, 'okay')
    if message.content == 'hi gaybot':
        await client.send_message(message.channel, 'hi wassup?')
    if message.content == 'cool':
        await client.send_message(message.channel,'cool cool cool')
    if message.content == 'gay':
        await client.send_message(message.channel,'gay gay gay')
    if message.content == 'no u':
        await client.send_message(message.channel,'no w')
    if message.content == 'ugay':
        await client.send_message(message.channel,'no u')
    if message.content == 'i want u':
        await client.send_message(message.channel,'lets go somewhere private :smirk: ')
    if message.content == 'i want you':
        await client.send_message(message.channel, 'lets go somewhere private :smirk: ')
    if message.content == 'nothing':
        await client.send_message(message.channel,'yea thats what I thought')
    if message.content == 'botimg':
        em = discord.Embed(description='the bot image')
        em.set_image(url='https://cdn.discordapp.com/attachments/579238073318244371/579306609625268227/27581853_163641047758683_8812432065644462080_n.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'deal with it':
        em = discord.Embed(description='Just deal with it')
        em.set_image(url='https://cdn.discordapp.com/attachments/574366274084143104/575031522403418132/Banana_deal_with_it.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'serverimg':
        em = discord.Embed(description='the server image')
        em.set_image(url='https://cdn.discordapp.com/attachments/579238073318244371/579306929113792525/download.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hey gaybot':
        await client.send_message(message.channel,'What do you want?')
    if ('Nigga') in message.content:
       await client.delete_message(message)
    if ('nigga') in message.content:
       await client.delete_message(message)
    if ('Nigger') in message.content:
       await client.delete_message(message)
    if ('nigger') in message.content:
       await client.delete_message(message)
    if message.content == 'help':
        await client.send_message(message.channel, '')
    if message.content.startswith('rps'):
        randomlist = ["rock", "paper", "scissors"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('coinflip'):
        randomlist = ["Heads", "Tails"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'show me a pedophile':
        em = discord.Embed(description='ok here you go')
        em.set_image(url='https://cdn.discordapp.com/attachments/579238073318244371/579387218674843648/unknown.png')
        await client.send_message(message.channel, embed=em)

client.run('NTc5Mjc4NzU2NjE1NTUzMDM0.XN_1ww.VlVnHyYJO_LcbRRBbp5ddc77HPY')
