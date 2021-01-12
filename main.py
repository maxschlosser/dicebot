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
    """
    Runs when the bot has connected to discord and can respond to commands.
    :return:
    """
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='roll', help='Roll XdY', pass_context=True)
async def roll(ctx, dice: int, sides: int):
    """
    Roll X dice with Y sides for a user.

    To do this we do the following

    1. Generate random numbers for each die.
    2. Sum the dice
    3. Send the string

    :param ctx: The discord context
    :param dice: Amount of dice
    :param sides: Amount of sides
    :return:
    """
    dice_result = [
        random.choice(range(1, int(sides) + 1))
        for _ in range(int(dice))
    ]
    total = sum(dice_result)
    result = f"Rolled {dice}d{sides} for {ctx.message.author.mention}: " + os.linesep + f"{dice_result} total: {total}"
    await ctx.send(result)


@roll.error
async def roll_error(ctx, error):
    """
    Runs if anyone tries to !roll anything else than two positive integers.
    :param ctx:
    :param error:
    :return:
    """
    await ctx.send("Usage: !roll amount sides, e. g. !roll 2 4")


@bot.command(name='fuck', help='fuck', pass_context=True)
async def fuck(ctx):
    """
    Responds with "Fuck you @author"
    :param ctx: The discord context
    :return:
    """
    await ctx.send("Fuck you, " + ctx.message.author.mention + "!")


@bot.command(name='restart', help='Restarts dicebot for users with the "GM" role', pass_context=True)
@commands.has_role('GM')
async def restart(ctx):
    """
    "Restarts" the bot by killing it and letting the host handle the rest. Works fine in the current setup
    which will restart the bot as soon as it exits. May take a few seconds if there are any changes in git.

    :param ctx: The discord context
    :return:
    """
    await ctx.send("Restarting and updating for " + ctx.message.author.mention)
    exit()


@restart.error
async def restart_error(ctx, error):
    """
    Runs when restarting the bot fails. The first condition will check if the user is missing the required role,
    if not something has gone wrong.

    :param ctx: The discord context
    :param error: The internal error object
    :return:
    """
    if isinstance(error, commands.MissingRole):
        await ctx.send("I'm sorry, " + ctx.message.author.mention +
                       ". I'm afraid that's something I cannot allow to happen.")
    else:
        await ctx.send("Uh-oh.")


bot.run(os.getenv('TOKEN'))
