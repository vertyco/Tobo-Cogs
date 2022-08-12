"""ErrorLogs, a cog for logging command errors to a discord channel."""
from redbot.core.bot import Red

from .errorlogs import ErrorLogs

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot: Red):
    await bot.add_cog(ErrorLogs())
