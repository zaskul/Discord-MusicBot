import discord
from discord.ext import commands
import os
from music import Player
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")
    await bot.add_cog(Player(bot))
bot.run(TOKEN)