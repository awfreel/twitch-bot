from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token="oauth:7lhvngwp9oyc4ejdx1i4nnb49mvimn",  # Replace with your bot's OAuth token
            prefix="!",
            initial_channels=["Thesassypancake"],  # Replace with your wife's Twitch channel name
        )

    async def event_ready(self):
        print(f"Logged in as {self.nick}")
        print(f"Connected to {self.connected_channels}")

    async def event_message(self, message):
        if message.echo:
            return  # Ignore bot's own messages
        print(f"Message from {message.author.name}: {message.content}")
        await self.handle_commands(message)

    @commands.command(name="hello")
    async def hello_command(self, ctx):
        await ctx.send(f"Hello, {ctx.author.name}!")

if __name__ == "__main__":
    bot = Bot()
    bot.run()

