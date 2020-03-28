import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def dm(self, ctx, member: discord.Member, *, arg):
        """Dm member in the guild.
        Usage:
        {prefix}dm @member Nice guy
        """
        if member is None:
            return await ctx.send("Please specify a user")

        dmchannel = await member.create_dm()
        await dmchannel.send(f'arg')

def setup(bot):
	bot.add_cog(Dm(bot))