import discord
from discord.ext import commands
import datetime
import asyncio
import random
client = commands.Bot(command_prefix = 'm!')

@client.event
async def on_ready():
    print('bot ist ready')



@client.command()
async def gstart(ctx, mins : int, * , prize: str):
    if not ctx.author.guild_permissions.administrator:
        msg1 = await ctx.send("Du darfst diesen command nicht Benutzen!")
        await ctx.message.delete()
        await asyncio.sleep(5)
        await msg1.delete()
        return

    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} mintues from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")



client.run('TOCKEN')
