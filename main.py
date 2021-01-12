# bot.py
import os
import random
import dotenv
# 1
from discord.ext import commands

dotenv.load_dotenv('.env')

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


@bot.command(name='fuck', help='fuck', pass_context=True)
async def fuck(ctx):
    await ctx.send("Fuck you, " + ctx.message.author.mention + "!")


@roll.error
async def roll_error(ctx, error):
    await ctx.send("Usage: !roll amount sides, e. g. !roll 2 4")


@bot.command(name='restart', help='Restarts dicebot for users with the "GM" role', pass_context=True)
@commands.has_role('GM')
async def restart(ctx):
    await ctx.send("Restarting and updating for "+ctx.message.author.mention)
    exit()

bot.run(os.getenv('TOKEN'))
