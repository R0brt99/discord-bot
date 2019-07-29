import random
import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms!')
        print(ctx.channel)

    @commands.command()
    async def ts(self, ctx):
        number = random.randint(1, 3)
        if number == 1:
            await ctx.send('R0brt & DiamondTrident vs. Dolphino & Garrett Gaming')
        elif number == 2:
            await ctx.send('DiamondTrident & Dolphino vs. R0brt & Garrett Gaming')
        elif number == 3:
            await ctx.send('Garrett Gaming & DiamondTrident vs. Dolphino & R0brt')

def setup(client):
    client.add_cog(General(client))
