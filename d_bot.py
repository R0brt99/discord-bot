import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'rawr ')

@client.event
async def on_ready():
    print('Bot is Online')
    client.load_extension('cogs.general')
    print('General Cog Loaded')

@client.command()
async def load(ctx, ext):
    client.load_extension(f'cogs.{ext}')
    await ctx.send(f'{ext} has been loaded.')

@client.command()
async def unload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')
    await ctx.send(f'{ext} has been unloaded.')

@client.command()
async def reload(ctx, ext):
    try:
        client.unload_extension(f'cogs.{ext}')
        client.load_extension(f'cogs.{ext}')
        await ctx.send(f'{ext} has been reloaded in {ctx.guild.name}')
    except:
        print('CogNotFoundException')

@client.command()
async def off(ctx):
    print('Shutting Down')
    exit()

client.run('NDAyOTIzMDk0NDkyMTg0NTg2.XR7KYA.ii6UYlWHAr771pDxoufRTfox480')
