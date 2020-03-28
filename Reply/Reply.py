from discord.ext import commands


class Reply(commands.Cog):
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
        elif  message.content.lower() == "+check":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+f":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+pay":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+find":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+buy":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+invite":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+bal":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+purchase":
            if message.channel.id != 690744388623663144:
                await message.channel.send("Please use commands in <#690744388623663144> Thank you!")
        elif message.content.lower() == "+info":
            if message.channel.id != 690744388623663144:

def setup(bot):
    bot.add_cog(Reply(bot))