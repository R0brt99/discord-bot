import discord
from discord.ext import commands
from time import sleep

class Games(commands.Cog):

    is_chall = True
    chall_memb = ''
    chall_rps = ''

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, rps_opt):

        if self.is_chall == True:
            await ctx.message.delete()
            if rps_opt == 'r':
                self.chall_memb = ctx.author
                self.chall_rps = rps_opt
                await ctx.send(f'{self.chall_memb.name} is the Challenger!')
                self.is_chall = False
            elif rps_opt == 'p':
                self.chall_memb = ctx.author
                self.chall_rps = rps_opt
                await ctx.send(f'{self.chall_memb.name} is the Challenger!')
                self.is_chall = False
            elif rps_opt == 's':
                self.chall_memb = ctx.author
                self.chall_rps = rps_opt
                await ctx.send(f'{self.chall_memb.name} is the Challenger!')
                self.is_chall = False
            else:
                await ctx.send('That is not an option.')

        elif self.is_chall == False:
            await ctx.message.delete()
            if ctx.author == self.chall_memb:
                await ctx.send(f'{ctx.author.name} is a Big Idiot!')
                sleep(2)
                await ctx.send("You can't challenge yourself!")
                return
            if rps_opt == 'r':
                await ctx.send(f'{ctx.author.name} accepts the Challenge!')
                sleep(2)
                if self.chall_rps == 'r':
                    await ctx.send(f'{self.chall_memb.name} chose Rock and {ctx.author.name} chose Rock!')
                    sleep(1)
                    await ctx.send('It is a Draw!')
                elif self.chall_rps == 'p':
                    await ctx.send(f'{self.chall_memb.name} chose Paper and {ctx.author.name} chose Rock!')
                    sleep(1)
                    await ctx.send(f'{self.chall_memb.name} is the Winner!')
                elif self.chall_rps == 's':
                    await ctx.send(f'{self.chall_memb.name} chose Scissors and {ctx.author.name} chose Rock!')
                    sleep(1)
                    await ctx.send(f'{ctx.author.name} is the Winner!')
                self.is_chall = True
            elif rps_opt == 'p':
                await ctx.send(f'{ctx.author.name} accepts the Challenge!')
                sleep(2)
                if self.chall_rps == 'r':
                    await ctx.send(f'{self.chall_memb.name} chose Rock and {ctx.author.name} chose Paper!')
                    sleep(1)
                    await ctx.send(f'{ctx.author.name} is the Winner!')
                elif self.chall_rps == 'p':
                    await ctx.send(f'{self.chall_memb.name} chose Paper and {ctx.author.name} chose Paper!')
                    sleep(1)
                    await ctx.send('It is a Draw!')
                elif self.chall_rps == 's':
                    await ctx.send(f'{self.chall_memb.name} chose Scissors and {ctx.author.name} chose Paper!')
                    sleep(1)
                    await ctx.send(f'{self.chall_memb.name} is the Winner!')
                self.is_chall = True
            elif rps_opt == 's':
                await ctx.send(f'{ctx.author.name} accepts the Challenge!')
                sleep(2)
                if self.chall_rps == 'r':
                    await ctx.send(f'{self.chall_memb.name} chose Rock and {ctx.author.name} chose Scissors!')
                    sleep(1)
                    await ctx.send(f'{self.chall_memb.name} is the Winner!')
                elif self.chall_rps == 'p':
                    await ctx.send(f'{self.chall_memb.name} chose Paper and {ctx.author.name} chose Scissors!')
                    sleep(1)
                    await ctx.send(f'{ctx.author.name} is the Winner!')
                elif self.chall_rps == 's':
                    await ctx.send(f'{self.chall_memb.name} chose Scissors and {ctx.author.name} chose Scissors!')
                    sleep(1)
                    await ctx.send('It is a Draw')
                self.is_chall = True
            else:
                await ctx.send("That's Illegal! Pick Rock (r), Paper (p), or Scissors (s)!")

def setup(client):
    client.add_cog(Games(client))
