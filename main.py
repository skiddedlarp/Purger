import discord, os

from discord.ext import commands

os.system(f'title [PURGER]')
os.system(f'mode 80,20')

token = input(f'Token: ')
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')

print(f'                       $ = channel, $$ = server\n\n')

print(f'                                   Purger\n')

class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="$$"):
            channels=message.channel.guild.channels
        elif(message.content=="$"):  
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(channel)
            try:
                async for mss in channel.history(limit=None):
                    if(mss.author==self.user):
                        print(mss.content)
                        try:
                            await mss.delete()
                        except:
                            print(f"Can't delete!\n")
            except:
                print("Can't read history!\n")
            

client=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
client.run(token, bot=False)
