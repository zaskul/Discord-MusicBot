import discord
import asyncio
import youtube_dl
import pafy
from discord.ext import commands

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}
        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            ctx.voice_client.stop()
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info['entries']) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)),
                              after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.voulume = 0.2

    @commands.command()
    async def join(self, ctx):
        self.setup()
        if ctx.author.voice is None:
            return await ctx.send("Connect to a voice channel in order to use this bot")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
                await ctx.voice_client.disconnect()

        await ctx.send("I'm not connected to any channel")

    @commands.command()
    async def play(self, ctx, *, song=None):


        if song is None:
            return await ctx.send("You must enter a song to play")

        if ctx.voice_client is None:
            return await ctx.send("I must be in a voice to play")


        # when song not an url
        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            await ctx.send("Searching for song, this may take a while...")

            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Sorry i could not find the given song")

            song = result[0]

        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await ctx.send(f"Added to queue. Songs in queue: {queue_len + 1}")

            else:
                return await ctx.send("Exeded queue limit")

        await self.play_song(ctx, song)
        await ctx.send(f"Now playing: {song}")

    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("You did not include a song to search for.")

        await ctx.send("Searching for a song, this may take a while...")

        info = await self.search_song(5, song)

        embed = discord.Embed(title=f"Results for '{song}':", descriptrion="You can use the URL's to play the exact song if the one you want isn't on the list")

        amount = 0
        for entry in info['entries']:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1

        embed.set_footer(text=f"Displaying the first {amount} results")

        await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("There are no songs in the queue.")
        
        embed = discord.Embed(title="Song Queue", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        embed.set_footer(text="Capybara pull up")

        await ctx.send(embed=embed)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not playing anything right now.")

        if ctx.author.voice is None:
            return await ctx.send("You are not in any voice channel.")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("I am not playing any songs for you")

        ctx.voice_client.stop()
        await self.check_queue(ctx)

        # vote to skip

        # poll = discord.Embed(title=f"Vote to Skip song by - {ctx.author}", description="**80% of the voice channel must vote to skip**", colour=discord.Colour.blue())
        # poll.add_field(name="Skip", value=":white_check_mark:")
        # poll.add_field(name="Stay", value=":no_entry_sign:")
        # poll.set_footer(text="Voting ends in 15 seconds")

        # poll_msg = await ctx.send(embed=poll)
        # poll_id = poll_msg.id

        # await poll_msg.add_reaction(u"\u2705") # yes
        # await poll_msg.add_reaction(u"\U0001F6AB") # no

        # await asyncio.sleep(15) # 15 seconds to vote

        # poll_msg = await ctx.channel.fetch_message(poll_id)

        # votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        # reacted = []
        # for reaction in poll_msg.reactions:
        #     if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
        #         async for user in reaction.users():
        #             if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
        #                 votes[reaction.emoji] += 1

        #                 reacted.append(user.id)

        # skip = False

        # if votes[u"\u2705"] > 0:
        #     if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > 0.79:
        #         skip = True
        #         embed = discord.Embed(title="Skipped song", description="***Vote to skip passed, skipping now.***", colour = discord.Colour.blue())

        # if not skip:
        #     embed = discord.Embed(title="Skip failed", description="*Vote to skip failed")

        # embed.set_footer(text="Voting has ended.")

        # await poll_msg.clear_reactions()
        # await poll_msg.edit(embed=embed)
        
        # if skip:
        #     ctx.voice_client.stop()
        #     await self.check_queue(ctx)

        
