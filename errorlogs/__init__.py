"""ErrorLogs, a cog for logging command errors to a discord channel."""
from redbot.core.bot import Red
import discord

from .errorlogs import ErrorLogs

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot: Red):
    if discord.__version__ > "1.7.3":
        await bot.add_cog(ErrorLogs())
    else:
        bot.add_cog(ErrorLogs())
