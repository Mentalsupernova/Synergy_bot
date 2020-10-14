import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix=config.PREFIX)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("pong")

@bot.command(pass_context=True)
async def send(ctx,arg):
    await ctx.send(arg)


bot.run(config.TOKEN)
