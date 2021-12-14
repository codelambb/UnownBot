from cogs.config import get_spawn_data, open_spawn
from cogs.fun import add_spawnpoke, changecatch, get_catch_data, get_items_data, get_pokemon_data, get_pokelist_data, open_catch, open_spawnpoke, remove_spawnpoke
import keep_alive
import discord
import json
from discord.ext import commands
import os
import random
import asyncio
from discord_components import *

#prefix function of getting prefix
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)

client.remove_command("help")

#start
@client.event
async def on_ready():
    DiscordComponents(client)
    print("The bot is ready to go!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f".help"))

#load command
@client.command()
async def load(ctx, extension):
    if ctx.author.id == 796042231538122762:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"Succesfully loaded {extension}!")
        return

    await ctx.send(f"You don't have permission to use that command!")

#unload command
@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 796042231538122762:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Succesfully unloaded {extension}!")
        return

    await ctx.send(f"You dont have permission to use that command!")

#getserver command
@client.command()
async def getserver(ctx):
    if ctx.author.id == 796042231538122762:
        activeservers = client.guilds
        for guild in activeservers:
            await ctx.send(f"{guild.name} {guild.owner_id} {guild.id}")
        return

    await ctx.send(f"You don't have permissions to use that!")

#leaveserver command
@client.command()
async def leaveserver(ctx, id: int):
    if ctx.author.id == 796042231538122762:
        guild = client.get_guild(id)
        await guild.leave()
        await ctx.send(f"Left that server successfully")
        return

    await ctx.send(f"You don't have permissions to use that!")

#reload command
@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 796042231538122762:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"Succesfully reloaded {extension}")
        return

    await ctx.send(f"You dont have permission to use that command!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#on_message event
@client.listen('on_message')
async def prefixresponse(message):
    try:
        if client.user in message.mentions:
            with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

            prefix = prefixes[str(message.guild.id)]
            await message.channel.send(f"My prefix here is `{prefix}`")

    except:
        pass

#on_message event
@client.event
async def on_message(msg):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(msg.guild.id) not in prefixes:
        prefixes[str(msg.guild.id)] = "."

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    await open_catch(msg.guild)
    await open_spawnpoke(msg.guild)
    catch = await get_catch_data()

    if catch[str(msg.guild.id)] == "True" and msg.author.id != 867604316932014120:
        await open_spawn(msg.guild)
        await changecatch(msg.guild, "False")
        spawn = await get_spawn_data()
        id_ = spawn[str(msg.guild.id)]
        if id_ == "None":
            pokelist = await get_pokelist_data()
            r = random.randint(1, 200)

            if 200 <= r and r >= 195:
                ka = "legendary"
                col = discord.Color.red()

            elif 194 <= r and r >= 184:
                ka = "epic"                                 
                col = discord.Color.purple()

            elif 183 <= r and r >= 143:
                ka = "rare"
                col = discord.Color.blue()

            elif 142 <= r and r >= 92:
                ka = "uncommon"
                col = discord.Color.green()
                                                            
            else:
                ka = "common"
                col = discord.Color.dark_grey()

            pok = pokelist["test"][ka]
            pokemon = random.choice(pok)
            p = await get_pokemon_data()
            image = p[pokemon]["image"]
            em = discord.Embed(title="A wild pokemon has appeared! Type its name to catch it!", color=col)
            em.set_image(url=image)
            em.set_footer(text=f"Use catch (pokemon) command to catch it!")
            await msg.channel.send(embed=em)
            await add_spawnpoke(msg.guild, pokemon)
            await asyncio.sleep(30)
            await changecatch(msg.guild, "True")
            await remove_spawnpoke(msg.guild, pokemon)

        else:
            c = await client.fetch_channel(id_)
            pokelist = await get_pokelist_data()
            r = random.randint(1, 200)

            if 200 <= r and r >= 195:
                ka = "legendary"
                col = discord.Color.red()

            elif 194 <= r and r >= 184:
                ka = "epic"                                 
                col = discord.Color.purple()

            elif 183 <= r and r >= 143:
                ka = "rare"
                col = discord.Color.blue()

            elif 142 <= r and r >= 92:
                ka = "uncommon"
                col = discord.Color.green()
                                                            
            else:
                ka = "common"
                col = discord.Color.dark_grey()

            pok = pokelist["test"][ka]
            pokemon = random.choice(pok)
            p = await get_pokemon_data()
            image = p[pokemon]["image"]
            em = discord.Embed(title="A wild pokemon has appeared! Type its name to catch it!", color=col)
            em.set_image(url=image)
            em.set_footer(text=f"Use catch (pokemon) command to catch it!")
            await c.send(embed=em)
            await add_spawnpoke(msg.guild, pokemon)
            await changecatch(msg.guild, "False")
            await asyncio.sleep(30)
            await changecatch(msg.guild, "True")
            await remove_spawnpoke(msg.guild, pokemon)

    await client.process_commands(msg)

#help command
@client.command()
async def help(ctx):
    x = True
    p = 1
    em = discord.Embed(title="Help Menu\n\n1) Main Commands\n2) Battling Commands\n3) Config Commands", color=discord.Color.orange())
    em.set_footer(text=f"{ctx.author.name}'s Help Menu", icon_url=ctx.author.avatar_url)
    m = await ctx.send(embed=em, components = [[
        Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
        Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
    ]])

    while x:
        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        try:
            res = await client.wait_for("button_click", check=check, timeout=15)
            e = res.component.label

            if e == "Next":
                p += 1
                
                if p == 2:
                    em = discord.Embed(title="Main Commands\n\n", description="`party <user>`: Tells your pokemon party or the mentioned users party", color=discord.Color.orange())
                    await m.delete()
                    await res.respond(content="Showing the Next page!")
                    m = await ctx.send(embed=em, components = [[
                        Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                        Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
                        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
                    ]])

                if p == 3:
                    em = discord.Embed(title="Battling Commands\n\n", description="`aiuel`: Do a pokemon battle against an AI!", color=discord.Color.orange())
                    await m.delete()
                    await res.respond(content="Showing the Next page!")
                    m = await ctx.send(embed=em, components = [[
                        Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                        Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
                        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
                    ]])

                if p == 4:
                    em = discord.Embed(title="Config Commands\n\n", description="`spawnadd (channel)`: Tells your pokemon party", color=discord.Color.orange())
                    await m.delete()
                    await res.respond(content="Showing the Next page!")
                    m = await ctx.send(embed=em, components = [[
                        Button(style=ButtonStyle.green, label="Next", emoji="⏩", disabled=True),
                        Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
                        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
                    ]])

            if e == "Back":
                p -= 1
                
                if p == 2:
                    em = discord.Embed(title="Main Commands\n\n", description="`party <user>`: Tells your pokemon party or the mentioned users party", color=discord.Color.orange())
                    await m.delete()
                    await res.respond(content="Showing the Previous page!")
                    m = await ctx.send(embed=em, components = [[
                        Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                        Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
                        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
                    ]])

                if p == 3:
                    em = discord.Embed(title="Main Commands\n\n", description="`party <user>`: Tells your pokemon party or the mentioned users party", color=discord.Color.orange())
                    await m.delete()
                    await res.respond(content="Showing the Previous page!")
                    m = await ctx.send(embed=em, components = [[
                        Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                        Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
                        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
                    ]])

                if p == 1:
                    em = discord.Embed(title="Main Commands\n\n", description="`party <user>`: Tells your pokemon "
                                                                              "party or the mentioned users party",
                                       color=discord.Color.orange())
                    await m.delete()
                    await res.respond(content="Showing the Previous page!")
                    m = await ctx.send(embed=em, components = [[
                        Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                        Button(style=ButtonStyle.red, label="Back", emoji="⏪", disabled=True),
                        Button(style=ButtonStyle.URL, label="Invite", url="https://gladosbot.ml/"),
                        Button(style=ButtonStyle.URL, label="Vote", url="https://top.gg/bot/791891067309785108")
                    ]])

        except asyncio.TimeoutError:
            await m.delete()
            return

#pokemon_remove command
@client.command()
async def pokemon_remove(ctx, poke = None):
    allowed_people = ["706028362895720520", "796042231538122762", "756053421420707928", "744820658935955536", "740883324083503155"]

    if str(ctx.author.id) not in allowed_people:
        await ctx.send("Your not allowed to use this command! It's a bot staff only command!")
        return

    if poke == None:
        await ctx.send("Please provide the pokemon's name next time!")
        return

    pokemon = await get_pokemon_data()

    if str(poke) not in pokemon:
        await ctx.send("That's not a valid pokemon that the bot has right now! Make sure to check the spelling and the character case")
        return

    rarity = pokemon[str(poke)]["rarity"]
    pokelist = await get_pokelist_data()
    del pokelist["test"][str(rarity)][str(poke)]
    print(pokelist)
    del pokemon[str(poke)]

    with open("pokemons.json", "w") as f:
        json.dump(pokemon, f, indent=4)

    with open("pokelist.json", "w") as f:
        json.dump(pokelist, f, indent=4)

    await ctx.send("Successfully done!")

#pokemon_add command
@client.command()
async def pokemon_add(ctx):
    allowed_people = ["706028362895720520", "796042231538122762", "756053421420707928", "744820658935955536", "740883324083503155"]

    if str(ctx.author.id) not in allowed_people:
        await ctx.send("Your not allowed to use this command! It's a bot staff only command!")
        return

    pokemon = await get_pokemon_data()
    await ctx.send("Please type the pokemon's name to add! (Make sure the 1st letter of the name is in caps for eg: Charizard not charizard)")

    try:
        message = await client.wait_for(
            "message",
            timeout = 60,
            check = lambda message: message.author == ctx.author
                            and message.channel == ctx.channel
            )

        if message:
            p = message.content
            pokemon[str(p)] = {}

            await ctx.send("Please type the pokemon's hp to add!")

            try:
                message = await client.wait_for(
                    "message",
                    timeout = 60,
                    check = lambda message: message.author == ctx.author
                                    and message.channel == ctx.channel
                    )

                if message:
                    h = message.content
                    pokemon[str(p)]["stats"] = {}
                    pokemon[str(p)]["stats"]["hp"] = int(h)

                    await ctx.send("Please type the pokemon's attack to add!")

                    try:
                        message = await client.wait_for(
                            "message",
                            timeout = 60,
                            check = lambda message: message.author == ctx.author
                                            and message.channel == ctx.channel
                            )

                        if message:
                            a = message.content
                            pokemon[str(p)]["stats"]["attack"] = int(a)
                            await ctx.send("Please type the pokemon's defense to add!")

                            try:
                                message = await client.wait_for(
                                    "message",
                                    timeout = 60,
                                    check = lambda message: message.author == ctx.author
                                                    and message.channel == ctx.channel
                                    )

                                if message:
                                    d = message.content
                                    pokemon[str(p)]["stats"]["defense"] = int(d)
                                    await ctx.send("Please type the pokemon's sp. atk to add!")

                                    try:
                                        message = await client.wait_for(
                                            "message",
                                            timeout = 60,
                                            check = lambda message: message.author == ctx.author
                                                            and message.channel == ctx.channel
                                            )

                                        if message:
                                            spa = message.content
                                            pokemon[str(p)]["stats"]["sp. atk"] = int(spa)
                                            await ctx.send("Please type the pokemon's sp. def to add!")

                                            try:
                                                message = await client.wait_for(
                                                    "message",
                                                    timeout = 60,
                                                    check = lambda message: message.author == ctx.author
                                                                    and message.channel == ctx.channel
                                                    )

                                                if message:
                                                    spd = message.content
                                                    pokemon[str(p)]["stats"]["sp. def"] = int(spd)
                                                    await ctx.send("Please type the pokemon's speed to add!")

                                                    try:
                                                        message = await client.wait_for(
                                                            "message",
                                                            timeout = 60,
                                                            check = lambda message: message.author == ctx.author
                                                                            and message.channel == ctx.channel
                                                            )

                                                        if message:
                                                            s = message.content
                                                            pokemon[str(p)]["stats"]["speed"] = int(s)
                                                            await ctx.send("Please type the big image url!")

                                                            try:
                                                                message = await client.wait_for(
                                                                    "message",
                                                                    timeout = 60,
                                                                    check = lambda message: message.author == ctx.author
                                                                                    and message.channel == ctx.channel
                                                                    )

                                                                if message:
                                                                    im = message.content
                                                                    pokemon[str(p)]["image"] = im
                                                                    await ctx.send("Please type the emoji utf form!")

                                                                    try:
                                                                        message = await client.wait_for(
                                                                            "message",
                                                                            timeout = 60,
                                                                            check = lambda message: message.author == ctx.author
                                                                                            and message.channel == ctx.channel
                                                                            )

                                                                        if message:
                                                                            em = message.content
                                                                            pokemon[str(p)]["emoji"] = em
                                                                            await ctx.send("Please type the rarity of pokemon!")

                                                                            try:
                                                                                message = await client.wait_for(
                                                                                    "message",
                                                                                    timeout = 60,
                                                                                    check = lambda message: message.author == ctx.author
                                                                                                    and message.channel == ctx.channel
                                                                                    )

                                                                                if message:
                                                                                    rar = message.content
                                                                                    pokemon[str(p)]["rarity"] = rar.lower()
                                                                                    await ctx.send("Please type the evolve level of pokemon! If it dosen't have evolve level type `None`")

                                                                                    try:
                                                                                        message = await client.wait_for(
                                                                                            "message",
                                                                                            timeout = 60,
                                                                                            check = lambda message: message.author == ctx.author
                                                                                                            and message.channel == ctx.channel
                                                                                            )

                                                                                        if message:
                                                                                            ae = message.content

                                                                                            if ae == "None":
                                                                                                evo = message.content
                                                                                                pokemon[str(p)]["evolve"] = evo

                                                                                            else:
                                                                                                evo = message.content
                                                                                                pokemon[str(p)]["evolve"] = int(evo)

                                                                                            await ctx.send("Please write the type of the pokemon!")

                                                                                            try:
                                                                                                message = await client.wait_for(
                                                                                                    "message",
                                                                                                    timeout = 60,
                                                                                                    check = lambda message: message.author == ctx.author
                                                                                                                    and message.channel == ctx.channel
                                                                                                    )

                                                                                                if message:
                                                                                                    ty = message.content
                                                                                                    pokemon[str(p)]["type"] = ty   
                                                                                                    await ctx.send("Please write the name of the pokemon it evolves into! If none then type `None`")

                                                                                                    try:
                                                                                                        message = await client.wait_for(
                                                                                                            "message",
                                                                                                            timeout = 60,
                                                                                                            check = lambda message: message.author == ctx.author
                                                                                                                            and message.channel == ctx.channel
                                                                                                            )

                                                                                                        if message:
                                                                                                            evo_name = message.content

                                                                                                            if evo_name == "None":
                                                                                                                evo_name = message.content
                                                                                                                pokemon[str(p)]["evolve_to"] = evo_name

                                                                                                            else:
                                                                                                                evo_name = message.content
                                                                                                                pokemon[str(p)]["evolve_to"] = evo_name
                                                                                
                                                                                                            pokemon[str(p)]["moves"] = {}
                                                                                                            pokemon[str(p)]["moves"]["Tackle"] = {}
                                                                                                            pokemon[str(p)]["moves"]["Tackle"]["type"] = "normal"
                                                                                                            pokemon[str(p)]["moves"]["Tackle"]["damage"] = 40
                                                                                                            pokemon[str(p)]["moves"]["Tackle"]["accuracy"] = 100
                                                                                                            pokemon[str(p)]["moves"]["Tackle"]["level"] = 1
                                                                                                            pokelist = await get_pokelist_data()
                                                                                                            pokelist["test"][str(rar)].append(str(p))

                                                                                                            with open("pokelist.json", "w") as f:
                                                                                                                json.dump(pokelist, f)

                                                                                                            with open("pokemons.json", "w") as f:
                                                                                                                json.dump(pokemon, f)

                                                                                                            await ctx.send("Successfully added that pokemon!")
                                                                                                            return

                                                                                                    except asyncio.TimeoutError:
                                                                                                        await ctx.send("You didn't write the pokemon's type to add in time!")
                                                                                                        return

                                                                                            except asyncio.TimeoutError:
                                                                                                await ctx.send("You didn't write the pokemon's type to add in time!")
                                                                                                return

                                                                                    except asyncio.TimeoutError:
                                                                                        await ctx.send("You didn't write the pokemon's evolve level to add in time!")
                                                                                        return

                                                                            except asyncio.TimeoutError:
                                                                                await ctx.send("You didn't write the pokemon's rarity to add in time!")
                                                                                return

                                                                    except asyncio.TimeoutError:
                                                                        await ctx.send("You didn't write the pokemon's emoji utf form to add in time!")
                                                                        return

                                                            except asyncio.TimeoutError:
                                                                await ctx.send("You didn't write the pokemon's image to add in time!")
                                                                return

                                                    except asyncio.TimeoutError:
                                                        await ctx.send("You didn't write the pokemon's speed to add in time!")
                                                        return

                                            except asyncio.TimeoutError:
                                                await ctx.send("You didn't write the pokemon's sp. def to add in time!")
                                                return

                                    except asyncio.TimeoutError:
                                        await ctx.send("You didn't write the pokemon's defense to add in time!")
                                        return

                            except asyncio.TimeoutError:
                                await ctx.send("You didn't write the pokemon's defense to add in time!")
                                return

                    except asyncio.TimeoutError:
                        await ctx.send("You didn't write the pokemon's attack to add in time!")
                        return
                
            except asyncio.TimeoutError:
                await ctx.send("You didn't write the pokemon's hp to add in time!")
                return

    except asyncio.TimeoutError:
        await ctx.send("You didn't write the pokemon's name to add in time!")
        return

#item_add command
@client.command()
async def item_add(ctx):
    items = await get_items_data()
    await ctx.send("Please type the name of item to be added!")

    try:
        message = await client.wait_for(
            "message",
            timeout = 60,
            check = lambda message: message.author == ctx.author
                            and message.channel == ctx.channel
            )

        if message:
            name = message.content
            await ctx.send("Please type the category of the item!")

            try:
                message = await client.wait_for(
                    "message",
                    timeout = 60,
                    check = lambda message: message.author == ctx.author
                                    and message.channel == ctx.channel
                    )

                if message:
                    cateogory = message.content
                    await ctx.send("Please type the price of the item!")

                    try:
                        message = await client.wait_for(
                            "message",
                            timeout = 60,
                            check = lambda message: message.author == ctx.author
                                            and message.channel == ctx.channel
                            )

                        if message:
                            price = int(message.content)
                            await ctx.send("Please type the selling price of the item!")

                            try:
                                message = await client.wait_for(
                                    "message",
                                    timeout = 60,
                                    check = lambda message: message.author == ctx.author
                                                    and message.channel == ctx.channel
                                    )

                                if message:
                                    sellprice = int(message.content)
                                    await ctx.send("Please type the emoji for the item in the special form!")

                                    try:
                                        message = await client.wait_for(
                                            "message",
                                            timeout = 60,
                                            check = lambda message: message.author == ctx.author
                                                            and message.channel == ctx.channel
                                            )

                                        if message:
                                            emoji = message.content
                                            await ctx.send("Please type the image url for the item!")

                                            try:
                                                message = await client.wait_for(
                                                    "message",
                                                    timeout = 60,
                                                    check = lambda message: message.author == ctx.author
                                                                    and message.channel == ctx.channel
                                                    )

                                                if message:
                                                    image = message.content
                                                    await ctx.send("Please type the use of the item in short!")

                                                    try:
                                                        message = await client.wait_for(
                                                            "message",
                                                            timeout = 60,
                                                            check = lambda message: message.author == ctx.author
                                                                            and message.channel == ctx.channel
                                                            )

                                                        if message:
                                                            use = message.content
                                                            items[cateogory][str(name)] = {}
                                                            items[cateogory][str(name)]["price"] = price
                                                            items[cateogory][str(name)]["use"] = use
                                                            items[cateogory][str(name)]["emoji"] = emoji
                                                            items[cateogory][str(name)]["image"] = image
                                                            items[cateogory][str(name)]["sell"] = sellprice

                                                            with open("items.json", "w") as f:
                                                                json.dump(items, f, indent=4)

                                                            await ctx.send(f"Successfully added **{name}** to the market place!")
                                                            return

                                                    except asyncio.TimeoutError:
                                                        await ctx.send("You didn't write use of the item to be added in time!")

                                            except asyncio.TimeoutError:
                                                await ctx.send("You didn't write the image url of the item to be added in time!")

                                    except asyncio.TimeoutError:
                                        await ctx.send("You didn't write the emoji of the item to be added in time!")

                            except asyncio.TimeoutError:
                                await ctx.send("You didn't write the selling price of the item to be added in time!")

                    except asyncio.TimeoutError:
                        await ctx.send("You didn't write the price of the item to be added in time!")

            except asyncio.TimeoutError:
                await ctx.send("You didn't write the category of the item to be added in time!")

    except asyncio.TimeoutError:
        await ctx.send("You didn't write the name of the item to be added in time!")

#ping command
@client.command()
async def ping(ctx):
    em = discord.Embed(title=f"Pong! `{round(client.latency * 1000)}ms`", color=discord.Color.orange())
    em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)

#all errors

#on_command_error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That's not a valid command!")
        return

    raise error

#ping error
@ping.error
async def ping_error(ctx, error):
    raise error

keep_alive.keep_alive()
#run event
token = os.environ.get("Token")
client.run(token)