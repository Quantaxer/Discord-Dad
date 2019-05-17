# import statements
import datetime
import asyncio
from discord.ext import commands
import discord
import os
import random

# The token which is used to connect to discord
TOKEN = 'NTc4NzUwNzUxODU0Mjk3MTA2.XN4J5w._qTNQaUIUKMIT2lnMntSaaG6CmA'
client = commands.Bot(command_prefix='~', case_insensitive=True)
# remove default help command to replace with custom help command
client.remove_command('help')

# Shows we are connected and running
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # The "I'm" commands for the dad jokes
    if 'I\'m' in message.content:
        phrase = message.content.split('I\'m')
        msg = 'Hi' + phrase[1] + ', I\'m Dad!'.format(message)
        await message.channel.send(msg)

    if 'Im' in message.content:
        phrase = message.content.split('Im')
        msg = 'Hi' + phrase[1] + ', I\'m Dad!'.format(message)
        await message.channel.send(msg)

    if 'im' in message.content:
        phrase = message.content.split('im')
        msg = 'Hi' + phrase[1] + ', I\'m Dad!'.format(message)
        await message.channel.send(msg)

    # BRUH THIS IS STUPID for some reason you need this line here for commands to work
    await client.process_commands(message)


# Command just to test if it is connected
@client.command()
async def ping(ctx):
    await ctx.send(client.latency)

# Command for the bot to yeet out of the server because why not, it's funny
@client.command(pass_context=True)
async def leave(ctx):
    await ctx.send("I'm just going to get some smokes from the store, I'll be back in a few minutes I swear!")
    # Find the server ID that you will leave
    to_leave = client.get_guild(ctx.message.guild.id)
    await to_leave.leave()

# Bedtime command, because everyone should go to sleep at 7 pm like civilized people
@client.command()
async def bedtime(ctx):
    current = datetime.datetime.now().time()
    if ((current.hour >= 19) or (current.hour < 6)) and (current.minute > 0):
        await ctx.send("You should really go to sleep, You are past your bedtime of 7:00 pm")
    elif ((current.hour >= 0) and (current.hour < 6)) and (current.minute > 0):
        await ctx.send("Boi it's past midnight you have school tomorrow, Mrs. Jablinski will slap you silly!")
    else:
        await ctx.send("It is not 7:00 pm yet, keep on doing what you're doing!")

# puns command, reads puns fro ma file and selects one at random
@client.command()
async def pun(ctx):
    list_of_puns = []
    # Get path of pun file
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath('data\\puns.txt', cur_path)
    # open file and append each line to the list
    with open(new_path, 'r') as f:
        for line in f:
            list_of_puns.append(line)

    # select a random pun and print it
    i = random.randint(0, 39)
    await ctx.send(list_of_puns[i])

# colossal command, injects a bunch of garbage into the channel it was called in
@client.command()
async def colossal(ctx):
    trash = ["the bruh momentum is the events leading up to a bruh moment",
             "hf hf hf hf hf hf hf hf\nhf hf hf hf hf hf hf hf",
             "anyways, {} is getting their ass exposed".format(ctx.author.mention),
             "dedotated W A M",
             "Help my pee is orange I'm turning into a pineapple",
             "Meet marcel toing. proud owner of ratatatatoing\nchef toing toing.\nta toing\nonly the freshest toing.",
             "seeya idot",
             "THAT'S IT, I\'M GONNA DDOS YOU",
             "mmmmm c r e a m y",
             "snans",
             "SNANS",
             "MINECRAP",
             "wan go diney wurl\nflawda?\northano\nme wanna go flawda\ndindlee whirld!",
             "This is an absolute colossal mess",
             "Don't mind me I'm just a bit of a mess"]

    # loop and choose a random t r a s h to print
    for i in range(30):
        await ctx.send(trash[random.randint(0, 14)])
        await asyncio.sleep(1.5)

# custom help command
@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.blue())
    # Create the embed
    embed.set_author(name="List of commands")
    embed.add_field(name="~bedtime", value="Tells you to go to sleep", inline=False)
    embed.add_field(name="~colossal", value="Creates a colossal mess in chat. Not for the faint of heart", inline=False)
    embed.add_field(name="~leave",
                    value="leaves the server to go get smokes at the convenience store, never to return again",
                    inline=False)
    embed.add_field(name="~ping", value="returns time it takes to reach server", inline=False)
    embed.add_field(name="~pun", value="Tells a random dad joke that nobody likes", inline=False)

    # send the embed
    await ctx.send(author.mention, embed=embed)

# Run the client with the token
client.run(TOKEN)
