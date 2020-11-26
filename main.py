# bot.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll', help='Roll XdY', pass_context=True)
async def roll(ctx, dice: int, sides: int):
    dice_result = [
        random.choice(range(1, int(sides) + 1))
        for _ in range(int(dice))
    ]
    total = sum(dice_result)
    dice_str = [str(die) for die in dice_result]
    result = "I rolled " + str(dice) + " d" + str(sides) + " for " + ctx.message.author.mention + ": " + os.linesep
    result = result + ', '.join(dice_str) + " total: " + str(total)
    await ctx.send(result)

@roll.error
async def roll_error(ctx, error):
    await ctx.send("Usage: !roll amount sides, e. g. !roll 2 4")



bot.run(TOKEN)
