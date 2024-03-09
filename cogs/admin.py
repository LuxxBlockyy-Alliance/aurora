import discord
from discord.ext import commands
from discord.ext.commands import Context
import sys
import subprocess


class admin(commands.Cog, name="admin"):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def update(self, ctx) -> None:
        if ctx.author.id in ["675779525262573589", "1112646094179016846"]:
            """ Updating the bot. """

            await ctx.reply("Updating the bot...", ephemeral=True)

            try:
                subprocess.Popen(["../../update.sh"])
                sys.exit()
            except Exception as e:
                await ctx.reply(f"Error: {e}", ephemeral=True)


def setup(bot):
    bot.add_cog(admin(bot))
