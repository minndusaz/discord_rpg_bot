import discord
from discord.ext import commands
from utilities.gamebot import GameBot
from .classmenu import ClassMenu
from rpgbot.models import Player
from asgiref.sync import sync_to_async

class UsernameEntry(commands.Cog):
    def __init__(self, bot: GameBot):
        self.bot = bot

    @commands.command()
    async def startrpg(self, ctx):
        def check_author(m):
            return m.author == ctx.author

        player = await sync_to_async(Player.objects.filter(player_id=ctx.author.id).exists)()
        channel_name = 'rpg-channelis'
        existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        channel_number = 1
        while existing_channel:
            channel_number += 1
            new_channel_name = f'{channel_name}-{channel_number}'
            existing_channel = discord.utils.get(ctx.guild.channels, name=new_channel_name)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }
        
        channel = await ctx.guild.create_text_channel(new_channel_name, overwrites=overwrites)
        ctx.channel = channel  # Update ctx with the new channel

        print(channel.id)
        def check(message):
            return message.channel == ctx.channel and not message.author.bot
        if player:
            # Player entry exists, proceed to the class menu
            class_menu_command = self.bot.get_command("classmenu")
            await ctx.invoke(class_menu_command)
            return

        await ctx.send("Please enter your username.")
        try:
            username_msg = await self.bot.wait_for("message", check=check_author, timeout=60.0)
            username = username_msg.content
            await sync_to_async(Player.objects.create)(player_id=ctx.author.id, discord_name=ctx.author.name, username=username)

            # Proceed to the class menu
            class_menu_command = self.bot.get_command("classmenu")
            await ctx.invoke(class_menu_command)

        except:
            await ctx.send("Username entry timed out.", delete_after=10)
            return

def setup(bot):
    bot.add_cog(UsernameEntry(bot))
