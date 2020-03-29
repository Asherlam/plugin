import discord
from discord.ext import commands
import json
import random
import datetime
import asyncio

with open('Asherlam/plugin/nsfw/pic.json', 'r', encoding='utf8') as data:
    pdata = json.load(data)

class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #web
    @commands.command()
    async def web(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['web-pic'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['web-pic'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

    #hentai
    @commands.command()
    async def hentai(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['hentai-pic'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['hentai-pic'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

    #boobs
    @commands.command()
    async def boobs(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['boobs-pic'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['boobs-pic'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

    #booty
    @commands.command(aliases=['ass'])
    async def booty(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['booty-pic'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['booty-pic'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

    #pussy
    @commands.command()
    async def pussy(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['pussy-pic'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['pussy-pic'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

    #fuck
    @commands.command()
    async def fuck(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['fuck-pic'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['fuck-pic'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

    #gif
    @commands.command()
    async def gif(self, ctx):
        member = ctx.message.author
        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name="🔞")
        if '🔞' in [y.name.lower() for y in member.roles]:
            random_pic = random.choice(pdata['gif'])
            embed=discord.Embed(color=0xff80c0)
            embed.set_image(url=random_pic)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="⚠️ Add Reaction To Get Permission To Use Nsfw Commands", color=0xf40006)
            embed.set_footer(text="You must be least eighteen years old to view the adult content")
            reactionid = await ctx.send(embed=embed)
            await reactionid.add_reaction('🔞')

            def check(reaction, user):
                return user == member and str(reaction.emoji) == '🔞'

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await reactionid.delete()
            else:
                random_pic = random.choice(pdata['gif'])
                embed=discord.Embed(color=0xff80c0)
                embed.set_image(url=random_pic)
                embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.datetime.now()
                await reactionid.delete()
                await ctx.send(embed=embed)
                await member.add_roles(role)

def setup(bot):
    bot.add_cog(Nsfw(bot))
