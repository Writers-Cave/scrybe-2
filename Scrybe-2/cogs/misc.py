import discord
import extdata
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=extdata.guilds)
    async def ping(self, ctx):
        await ctx.send_response(embed=discord.Embed(title="Pong!", description=f"Latency: `{round(self.bot.latency*1000, 2)}ms`"), ephemeral=True)


def setup(bot):
    bot.add_cog(Misc(bot))