import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.OWNER)
    async def dm(self, ctx, user: discord.Member, *,arg):
        """Dm user in the guild.
        Usage:
        {prefix}dm @user Nice guy
        """
        if not user:
            return await ctx.send("Please specify a user")

            embed=discord.Embed(description=f"You Are Sure To Send Direct Message To **{user.name}**?", color=0xff0000)
            embed.add_field(name="User Info", value=f"Name: `{user}`\n ID: `{user.id}`\n Message: `{arg}`", inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('✅')

            def check(reaction, user):
              return user == ctx.author and str(reaction.emoji) == '✅'

            try:
                reaction, ctx.author = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                await ctx.message.delete()
                await reactionid.delete()
            else:
                await ctx.message.delete()
                await reactionid.delete()
                
                dmchannel = await member.create_dm()
                await dmchannel.send(f"{arg}")

def setup(bot):
	bot.add_cog(Dm(bot))