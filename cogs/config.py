import discord
import json
from discord.channel import TextChannel
from discord.ext import commands      

#get_spawn_data function
async def get_spawn_data():
    with open("spawn.json", "r") as f:
        users = json.load(f)

    return users

#open_spawn function
async def open_spawn(server):
    users = await get_spawn_data()

    if str(server.id) in users:
        return False

    else:
        users[str(server.id)] = "None"

    with open("spawn.json", "w") as f:
        json.dump(users, f, indent=4)

    return True

#add_spawn function
async def add_spawn(server, channel):
    users = await get_spawn_data()
    users[str(server.id)] = str(channel)

    with open("spawn.json", "w") as f:
        json.dump(users, f, indent=4)

#remove_spawn function
async def remove_spawn(server):
    users = await get_spawn_data()
    users[str(server.id)] = "None"

    with open("spawn.json", "w") as f:
        json.dump(users, f, indent=4)

class Config(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('config file is ready!')

    #spawnadd command
    @commands.command(aliases=["sa"])
    @commands.has_permissions(manage_channels=True)
    async def spawnadd(self, ctx, channel: TextChannel = None):
        if channel == None:
            await ctx.send("Please provide the channel id next time!")
            return

        await open_spawn(ctx.guild)
        spawn = await get_spawn_data()

        if str(channel.id) == spawn[str(ctx.guild.id)]:
            await ctx.send("That channel is already assigned to spawn pokemons there!")
            return

        await add_spawn(ctx.guild, channel.id)
        await ctx.send(f"Successfully changed the spawning channel of pokemons to <#{channel.id}>")

    #spawnremove command
    @commands.command(aliases=["sr"])
    @commands.has_permissions(manage_channels=True)
    async def spawnremove(self, ctx):
        await open_spawn(ctx.guild)
        spawn = await get_spawn_data()

        if spawn[str(ctx.guild.id)] == "None":
            await ctx.send("There is no spawn channel there yet in this server!")
            return

        await remove_spawn(ctx.guild)
        await ctx.send(f"Successfully removed spawn channel and now pokemons will be spawned normally anywhere in the server.")

    #channel remove event
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        await remove_spawn(channel.guild)

    #prefix joinset
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "."

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    #prefix removeset
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        del prefixes[str(guild.id)]

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    #changeprefix command
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def changeprefix(self, ctx, prefix = None):

        if prefix == None:
            em = discord.Embed(title="What prefix you want to set for the bot?! Please specify the prefix next time", color=discord.Color.red())
            await ctx.send(embed=em)
            return

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title=f"Successfully set prefix to `{prefix}`\n\n\n", color=discord.Color.green())
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Config(client))