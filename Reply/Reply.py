from discord.ext import commands

class Rely(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if  message.content.lower() == "hello":
            await message.channel.send("Hey")
        elif message.content.lower() == "yo":
            await message.channel.send("yo")
        elif message.content.lower() == "gm":
            await message.channel.send("Good Morning")
        elif message.content.lower() == "gn":
            await message.channel.send("Good Night")
        elif message.content.lower() == "good morning":
            await message.channel.send("Good Morning !")
        elif message.content.lower() == "good night":
            await message.channel.send("Good Night !")
        elif message.content.lower() == "hey":
            await message.channel.send("Hello !")
        elif message.content.lower() == "sup":
            await message.channel.send("Sup")
        elif message.content.lower() == "hi":
            await message.channel.send("Hi")
        elif  message.content.lower() == "check":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+f":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+pay":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+find":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+buy":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+invite":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+bal":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+purchase":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")
        elif message.content.lower() == "+info":
            await message.channel.send("Please use commands in <#{690744388623663144}> Thank you!")


def setup(bot):
    bot.add_cog(Rely(bot))