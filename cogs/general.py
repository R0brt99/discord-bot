import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)} ms!')
        print(ctx.channel)

"""
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = after.guild
        if str(before.status) == 'offline':
            await channel.send('{} has Returned!'.format(after.name))
            print('{} has returned'.format(after.name))
"""

def setup(client):
    client.add_cog(General(client))
