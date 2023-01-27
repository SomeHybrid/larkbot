"""Ping cog"""

from discord import Embed, Interaction, app_commands
from discord.ext import commands

from bot.bot import Bot
from bot.constants import Colours


class Ping(commands.Cog):
    """Get info about the bot's ping and uptime."""

    def __init__(self, bot: Bot):
        self.bot = bot

    def _build_ping_embed(self) -> Embed:
        embed = Embed(
            title=":ping_pong: Pong!",
            colour=Colours.bright_green,
            description=f"Gateway Latency: {round(self.bot.latency * 1000)}ms",
        )

        return embed

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        """Ping the bot to see its latency and state."""
        embed = self._build_ping_embed() 
        await ctx.send(embed=embed)

    @app_commands.command(name="ping", description="Get gateway latency")
    async def ping_app_command(self, interaction: Interaction) -> None:
        embed = self._build_ping_embed()
        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot) -> None:
    """Load the Ping cog."""
    await bot.add_cog(Ping(bot))
