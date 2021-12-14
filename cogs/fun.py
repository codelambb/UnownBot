import discord
import json
from discord.ext import commands
import asyncio
import random
from discord.ext.commands.cooldowns import BucketType
from discord_components import *

#get_items_data function
async def get_items_data():
    with open("items.json", "r") as f:
        items = json.load(f)

    return items

#get_spawnpoke_data function
async def get_spawnpoke_data():
    with open("randomcatch.json", "r") as f:
        spawnpoke = json.load(f)

    return spawnpoke

#open_spawnpoke function
async def open_spawnpoke(server):
    users = await get_spawnpoke_data()

    if str(server.id) in users:
        return False

    else:
        users[str(server.id)] = "None"

    with open("randomcatch.json", "w") as f:
        json.dump(users, f, indent=4)

    return True

#add_spawnpoke function
async def add_spawnpoke(server, poke):
    users = await get_spawnpoke_data()
    users[str(server.id)] = str(poke)

    with open("randomcatch.json", "w") as f:
        json.dump(users, f, indent=4)

#remove_spawnpoke function
async def remove_spawnpoke(server, poke):
    users = await get_spawnpoke_data()

    if poke == users[str(server.id)]:
        users[str(server.id)] = "None"

    with open("randomcatch.json", "w") as f:
        json.dump(users, f, indent=4)

#get_catch_data function
async def get_catch_data():
    with open("catchwait.json", "r") as f:
        catch = json.load(f)

    return catch

#open_catch function
async def open_catch(server):
    catch = await get_catch_data()

    if str(server.id) in catch:
        return False

    else:
        catch[str(server.id)] = "True"

    with open("catchwait.json", "w") as f:
        json.dump(catch, f, indent=4)

    return True

#changecatch function
async def changecatch(server, mode):
    catch = await get_catch_data()
    catch[str(server.id)] = mode

    with open("catchwait.json", "w") as f:
        json.dump(catch, f, indent=4)

#get_pokelist_data function
async def get_pokelist_data():
    with open("pokelist.json", "r") as f:
        pokelist = json.load(f)

    return pokelist

#get_pokemon_data function
async def get_pokemon_data():
    with open("pokemons.json", "r") as f:
        pokemons = json.load(f)

    return pokemons

#get_trainer_data function
async def get_trainer_data():
    with open("trainers.json", "r") as f:
        users = json.load(f)

    return users

#open_trainer function
async def open_trainer(user):
    users = await get_trainer_data()

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = {}
        users[str(user.id)]["bag"] = {}
        users[str(user.id)]["pokemon"] = {}
        users[str(user.id)]["pokemon"]["party"] = {}
        users[str(user.id)]["pokemon"]["box"] = {}
        users[str(user.id)]["money"] = 0
        users[str(user.id)]["reputation"] = 0

    with open("trainers.json", "w") as f:
        json.dump(users, f, indent=4)

    return True

#get_pokenumber_data function
async def get_pokenumber_data():
    with open("pokenumber.json", "r") as f:
        users = json.load(f)

    return users

#open_pokenumber function
async def open_pokenumber(user):
    users = await get_pokenumber_data()

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = 1

    with open("pokenumber.json", "w") as f:
        json.dump(users, f, indent=4)

    return True

#add_pokenumber function
async def add_pokenumber(user):
    number = await get_pokenumber_data()
    number[str(user.id)] += 1

    with open("pokenumber.json", "w") as f:
        json.dump(number, f, indent=4)

#add_pokemon function
async def add_pokemon(user, pokemon, level, starter):
    users = await get_trainer_data()
    number = await get_pokenumber_data()
    n = number[str(user.id)]
    s = 0

    for i in users[str(user.id)]["pokemon"]["party"]:
        s += 1

    if s > 5:
        if starter == True:
            users[str(user.id)]["pokemon"]["box"][f"{n}"] = {}
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["name"] = pokemon
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["level"] = level
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["exp"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["starter"] = "True"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["protein"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["iron"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["calcium"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["zinc"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["carbos"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"] = {}
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move1"] = "Tackle"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move2"] = "Tackle"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move3"] = "Tackle"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move4"] = "Tackle"
            await add_pokenumber(user)

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            return False

        else:
            users[str(user.id)]["pokemon"]["box"][f"{n}"] = {}
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["name"] = pokemon
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["level"] = level
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["exp"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["starter"] = "False"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["protein"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["iron"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["calcium"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["zinc"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["carbos"] = 0
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"] = {}
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move1"] = "Tackle"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move2"] = "Tackle"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move3"] = "Tackle"
            users[str(user.id)]["pokemon"]["box"][f"{n}"]["moves"]["move4"] = "Tackle"
            await add_pokenumber(user)

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            return False

    else:
        if starter == True:
            users[str(user.id)]["pokemon"]["party"][f"{n}"] = {}
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["name"] = pokemon
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["level"] = level
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["exp"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["starter"] = "True"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["protein"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["iron"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["calcium"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["zinc"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["carbos"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"] = {}
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move1"] = "Tackle"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move2"] = "Tackle"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move3"] = "Tackle"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move4"] = "Tackle"
            await add_pokenumber(user)

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            return True

        else:
            users[str(user.id)]["pokemon"]["party"][f"{n}"] = {}
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["name"] = pokemon
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["level"] = level
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["exp"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["starter"] = "False"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["protein"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["iron"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["calcium"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["zinc"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["carbos"] = 0
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"] = {}
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move1"] = "Tackle"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move2"] = "Tackle"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move3"] = "Tackle"
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["moves"]["move4"] = "Tackle"
            await add_pokenumber(user)

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            return True

#add_exp function
async def add_exp(user, number, exp):
    users = await get_trainer_data()

    if number in users[str(user.id)]["pokemon"]["party"]:
        users[str(user.id)]["pokemon"]["party"][f"{number}"]["exp"] += exp

    elif number in users[str(user.id)]["pokemon"]["box"]:
        users[str(user.id)]["pokemon"]["box"][f"{number}"]["exp"] += exp

    with open("trainers.json", "w") as f:
        json.dump(users, f, indent=4)

#add_lvl function
async def add_lvl(user, number):
    users = await get_trainer_data()

    if number in users[str(user.id)]["pokemon"]["party"]:
        exp = users[str(user.id)]["pokemon"]["party"][f"{number}"]["exp"]
        lvl = users[str(user.id)]["pokemon"]["party"][f"{number}"]["level"]
        lvl_end = lvl ** 4

        if exp >= lvl_end:
            users[str(user.id)]["pokemon"]["party"][f"{number}"]["level"] += 1


            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            return True

        else:
            return False

    elif number in users[str(user.id)]["pokemon"]["box"]:
        exp = users[str(user.id)]["pokemon"]["box"][f"{number}"]["exp"]
        lvl = users[str(user.id)]["pokemon"]["box"][f"{number}"]["level"]
        lvl_end = lvl ** 4

        if exp >= lvl_end:
            users[str(user.id)]["pokemon"]["box"][f"{number}"]["level"] += 1

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            return True

        else:
            return False

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('fun file is ready!')

    #catch command
    @commands.command(aliases=["c"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def catch(self, ctx, poke=None):
        await open_spawnpoke(ctx.guild)
        randomcatch = await get_spawnpoke_data()
        users = await get_trainer_data()
        total_poke = 0

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if poke == None:
            await ctx.send("Please provide the pokemon's name next time!")
            return

        p = randomcatch[str(ctx.guild.id)]

        if p == "None":
            await ctx.send("No pokemon has been spawned yet!")
            return

        for i in users[str(ctx.author.id)]["pokemon"]["party"]:
            total_poke += 1

        for i in users[str(ctx.author.id)]["pokemon"]["box"]:
            total_poke += 1

        if total_poke > 150:
            await ctx.send("The max total limit of pokemons is 150! You have reached the limit of 150 already! Please use the `release` command in order to release few of your pokemons and make space for your new pokemons!")
            return

        elif poke.lower() == p.lower():
            level = random.randint(1, 12)
            x = await add_pokemon(ctx.author, p, level, False)

            if x == True:
                await ctx.send(f"{ctx.author.mention} has successfully captured a **lvl {level} {p}**! It has been successfully added their party!")
                await remove_spawnpoke(ctx.guild, p)
                return

            else:
                await ctx.send(f"{ctx.author.mention} has successfully captured a **lvl {level} {p}**! It has been successfully added their box!")
                await remove_spawnpoke(ctx.guild, p)
                return

        else:
            await ctx.send("Incorrect pokemon name according to the spawn! Try again!")
            return

    #start command
    @commands.command(aliases=["st"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def start(self, ctx):
        trainer = await open_trainer(ctx.author)
        await open_pokenumber(ctx.author)
        number = await get_pokenumber_data()
        users = await get_trainer_data()

        if trainer == False:
            await ctx.send("You already have a starter pokemon!")
            return

        em = discord.Embed(title="Welcome pokemon trainer to your wonderful pokemon journey! In order to start with your journey you need a starter pokemon, also choose wisely cause you can't change your starter pokemon later! We have 3 options right now -:\n", color=discord.Color.orange())
        em.add_field(name="<:charmander:867638757175459852> Charmander", value="Type `charmander` to choose charmander as your starter!")
        em.add_field(name="<:bulbasaur:867639023522676736> Bulbasaur", value="Type `bulbasaur` to choose bulbasaur as your starter!")
        em.add_field(name="<:squirtle:867637866830102558> Squirtle", value="Type `squirtle` to choose squirtle as your starter!")
        em.set_footer(text = f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        em.set_thumbnail(url="https://media.tenor.com/images/971791eab2deb9bcd40c5f1c0f8d5287/tenor.gif")
        await ctx.send(embed=em)

        try:
            msg = await self.client.wait_for(
                "message",
                timeout = 60,
                check = lambda message: message.author == ctx.author
                               and message.channel == ctx.channel
                )

            if msg:
                x = msg.content

                if x.lower() == "charmander":
                    a = await add_pokemon(ctx.author, "Charmander", 1, True)

                    if a == True:
                        await ctx.send("Successfully added Charmander to your party!")
                        return

                    else:
                        await ctx.send("Successfully added Charmander to your box!")
                        return

                if x.lower() == "bulbasaur":
                    a = await add_pokemon(ctx.author, "Bulbasaur", 1, True)

                    if a == True:
                        await ctx.send("Successfully added Bulbasaur to your party!")
                        return

                    else:
                        await ctx.send("Successfully added Bulbasaur to your box!")
                        return

                if x.lower() == "squirtle":
                    a = await add_pokemon(ctx.author, "Squirtle", 1, True)

                    if a == True:
                        await ctx.send("Successfully added Squirtle to your party!")
                        return

                    else:
                        await ctx.send("Successfully added Squirtle to your box!")
                        return

                else:
                    await ctx.send("That's not a valid starter pokemon!")

                    del users[str(ctx.author.id)]
                    del number[str(ctx.author.id)]
                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    with open("pokenumber.json", "w") as f:
                        json.dump(number, f, indent=4)

                    return

        except asyncio.TimeoutError:
            await ctx.send(f'You were late to response')
            del users[str(ctx.author.id)]
            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

    #party command
    @commands.command(aliases=["pa", "team"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def party(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(member.id) not in users:
            await ctx.send("You or that user you mentioned dosen't have a starter pokemon yet!")
            return

        await open_trainer(member)
        em = discord.Embed(title=f"{member.name}'s Party -:\n", color=discord.Color.orange())
        s = 1

        for i in users[str(member.id)]["pokemon"]["party"]:
            if "starter" in users[str(member.id)]["pokemon"]["party"][str(i)]:
                level = users[str(member.id)]["pokemon"]["party"][str(i)]["level"]
                name = users[str(member.id)]["pokemon"]["party"][str(i)]["name"]
                emoji = pokemon[name]["emoji"]

            else:
                level = users[str(member.id)]["pokemon"]["party"][str(i)]
                name = users[str(member.id)]["pokemon"]["party"][str(i)]["name"]
                emoji = pokemon[name]["emoji"]

            em.add_field(name=f"{s}) {emoji} {name}", value=f"Level: {level}\nNumber: {i}")
            s += 1

        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    #pokemon command
    @commands.command(aliases=["p"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pokemon(self, ctx, page: int = None, member: discord.Member = None):
        if page == None:
            page = 1

        if page < 1:
            await ctx.send("Page artribute can't be smaller than 0!")
            return

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if member == None:
            member = ctx.author

        if str(member.id) not in users:
            await ctx.send("You or the mentioned user doesn't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        s = 1
        l = 1
        t = 1
        m = 25
        em = discord.Embed(title=f"Pokemons of {member.name}", color=discord.Color.orange())
        for i in users[str(member.id)]["pokemon"]["party"]:
            if l > m:
                t += 1
                m += 25

            name = users[str(member.id)]["pokemon"]["party"][str(i)]["name"]
            level = users[str(member.id)]["pokemon"]["party"][str(i)]["level"]
            emoji = pokemon[name]["emoji"]
            l += 1

        for i in users[str(member.id)]["pokemon"]["box"]:
            if l > m:
                t += 1
                m += 25

            name = users[str(member.id)]["pokemon"]["box"][str(i)]["name"]
            level = users[str(member.id)]["pokemon"]["box"][str(i)]["level"]
            emoji = pokemon[name]["emoji"]
            l += 1

        if page > t:
            await ctx.send(f"That page is invalid! Your max page currently is **{t}**")
            return

        p = page - 1
        x = 25 * p

        for i in users[str(member.id)]["pokemon"]["party"]:
            if x < s:
                name = users[str(member.id)]["pokemon"]["party"][str(i)]["name"]
                level = users[str(member.id)]["pokemon"]["party"][str(i)]["level"]
                emoji = pokemon[name]["emoji"]
                em.add_field(name=f"**{s})** {emoji} {name}", value=f"Lvl: {level}\nNumber: {i}")
            s += 1

        for i in users[str(member.id)]["pokemon"]["box"]:
            if x < s:
                name = users[str(member.id)]["pokemon"]["box"][str(i)]["name"]
                level = users[str(member.id)]["pokemon"]["box"][str(i)]["level"]
                emoji = pokemon[name]["emoji"]
                em.add_field(name=f"**{s})** {emoji} {name}", value=f"Lvl: {level}\nNumber: {i}")
            s += 1

        em.set_footer(text=f"Page {page}/{t}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    #info command
    @commands.command(aliases=["i"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def info(self, ctx, number = None):
        if number == None:
            await ctx.send("Please provide the pokemon number next time!")
            return

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if number in users[str(ctx.author.id)]["pokemon"]["party"]:
            name = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
            level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
            image = pokemon[name]["image"]
            basehp = pokemon[name]["stats"]["hp"]
            baseattack = pokemon[name]["stats"]["attack"]
            basedefense = pokemon[name]["stats"]["defense"]
            basesp_atk = pokemon[name]["stats"]["sp. atk"]
            basesp_def = pokemon[name]["stats"]["sp. def"]
            basespeed = pokemon[name]["stats"]["speed"]
            hp = round(basehp + level * (1/50 * basehp))
            attack = round(baseattack + level * (1/50 * baseattack))
            defense = round(basedefense + level * (1/50 * basedefense))
            sp_atk = round(basesp_atk + level * (1/50 * basesp_atk))
            sp_def = round(basesp_def + level * (1/50 * basesp_def))
            speed = round(basespeed + level * (1/50 * basespeed))
            ty = pokemon[name]["type"]
            rarity = pokemon[name]["rarity"]
            emoji = pokemon[name]["emoji"]

            if rarity == "common":
                c = discord.Color.dark_grey()

            elif rarity == "uncommon":
                c = discord.Color.green()

            elif rarity == "rare":
                c = discord.Color.blue()

            elif rarity == "epic":
                c = discord.Color.purple()

            elif rarity == "legendary":
                c = discord.Color.red()

            em = discord.Embed(title=f"**{emoji} {name}**\n\n", description= f"**Level:** {level}\n**Number:** {number}\n**Type:** {ty}\n**Rarity:** {rarity}\n**Master:** {ctx.author.name}\n\n**Stats-:**\n**Hp:** {hp}\n**Attack:** {attack}\n**Defense:** {defense}\n**Sp. atk:** {sp_atk}\n**Sp. def:** {sp_def}\n**Speed:** {speed}", color=c)
            em.set_image(url=image)
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)

        elif number in users[str(ctx.author.id)]["pokemon"]["box"]:
            name = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
            level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
            image = pokemon[name]["image"]
            hp = pokemon[name]["stats"]["hp"]
            attack = pokemon[name]["stats"]["attack"]
            defense = pokemon[name]["stats"]["defense"]
            sp_atk = pokemon[name]["stats"]["sp. atk"]
            sp_def = pokemon[name]["stats"]["sp. def"]
            speed = pokemon[name]["stats"]["speed"]
            ty = pokemon[name]["type"]
            rarity = pokemon[name]["rarity"]
            emoji = pokemon[name]["emoji"]

            if rarity == "common":
                c = discord.Color.dark_grey()

            elif rarity == "uncommon":
                c = discord.Color.green()

            elif rarity == "rare":
                c = discord.Color.blue()

            elif rarity == "epic":
                c = discord.Color.purple()

            elif rarity == "legendary":
                c = discord.Color.red()

            em = discord.Embed(title=f"**{emoji} {name}**\n\n", description= f"**Level:** {level}\n**Number:** {number}\n**Type:** {ty}\n**Rarity:** {rarity}\n**Master:** {ctx.author.name}\n\n**Stats-:**\n**Hp:** {hp}\n**Attack:** {attack}\n**Defense:** {defense}\n**Sp. atk:** {sp_atk}\n**Sp. def:** {sp_def}\n**Speed:** {speed}", color=c)
            em.set_image(url=image)
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)

        else:
            await ctx.send("That is not a valid pokemon number that you have!")
            return

    #moves command
    @commands.command(aliases=["m"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def moves(self, ctx, number = None):
        if number == None:
            await ctx.send("Please provide the pokemon number next time!")
            return

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if number in users[str(ctx.author.id)]["pokemon"]["party"]:
            name = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
            level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
            move1 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move1"]
            move2 =users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move4"]
            image = pokemon[name]["image"]
            emoji = pokemon[name]["emoji"]
            em = discord.Embed(title=f"**{emoji} {name}**", color=discord.Color.red())
            em.add_field(name="**Level:**", value=f"{level}")
            em.add_field(name="**Number:**", value=f"{number}\n\n", inline=False)
            em.add_field(name="**Move 1:**", value=f"{move1}")
            em.add_field(name="**Move 2:**", value=f"{move2}")
            em.add_field(name="**Move 3:**", value=f"{move3}")
            em.add_field(name="**Move 4:**", value=f"{move4}")
            em.set_thumbnail(url=image)
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)

        elif number in users[str(ctx.author.id)]["pokemon"]["box"]:
            name = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
            level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
            move1 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move1"]
            move2 =users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move4"]
            image = pokemon[name]["image"]
            emoji = pokemon[name]["emoji"]
            em = discord.Embed(title=f"**{emoji} {name}**", color=discord.Color.red())
            em.add_field(name="**Level:**", value=f"{level}")
            em.add_field(name="**Number:**", value=f"{number}\n\n", inline=False)
            em.add_field(name="**Move 1:**", value=f"{move1}")
            em.add_field(name="**Move 2:**", value=f"{move2}")
            em.add_field(name="**Move 3:**", value=f"{move3}")
            em.add_field(name="**Move 4:**", value=f"{move4}")
            em.set_thumbnail(url=image)
            em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)

        else:
            await ctx.send("That is not a valid pokemon number that you have!")
            return

    #moveslist command
    @commands.command(aliases=["ml"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def moveslist(self, ctx, number = None):
        if number == None:
            await ctx.send("Please provide the pokemon number next time!")
            return

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if number in users[str(ctx.author.id)]["pokemon"]["party"]:
            name = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
            emoji = pokemon[name]["emoji"]
            em = discord.Embed(title=f"{emoji} {name}", color=ctx.author.color)

            for i in pokemon[name]["moves"]:
                ty = pokemon[name]["moves"][i]["type"]
                damage = pokemon[name]["moves"][i]["damage"]
                level = pokemon[name]["moves"][i]["level"]
                em.add_field(name=f"{i}", value=f"**Type:** {ty}\n**Damage:** {damage}\n**Level Required:** {level}\n",)

            await ctx.send(embed=em)

        elif number in users[str(ctx.author.id)]["pokemon"]["box"]:
            name = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
            emoji = pokemon[name]["emoji"]
            em = discord.Embed(title=f"{emoji} {name}", color=ctx.author.color)

            for i in pokemon[name]["moves"]:
                ty = pokemon[name]["moves"][i]["type"]
                damage = pokemon[name]["moves"][i]["damage"]
                level = pokemon[name]["moves"][i]["level"]
                em.add_field(name=f"{i}", value=f"**Type:** {ty}\n**Damage:** {damage}\n**Level Required:** {level}\n", inline=False)

            await ctx.send(embed=em)

        else:
            await ctx.send("That is not a valid pokemon number that you have!")
            return

    #learn command
    @commands.command(aliases=["l"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def learn(self, ctx, number = None, *, move = None):
        if number == None:
            await ctx.send("Please provide the first pokemon number next time!")
            return

        if move == None:
            await ctx.send("Please provide the move name next time!")
            return

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if number in users[str(ctx.author.id)]["pokemon"]["party"]:
            name = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
            emoji = pokemon[name]["emoji"]
            level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
            move1 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move1"]
            move2 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move4"]

            for i in pokemon[name]["moves"]:
                if i.lower() == move.lower():
                    requiredlevel = pokemon[name]["moves"][i]["level"]

                    if level >= requiredlevel:
                        await ctx.send("Please type the move you want to replce this with!")

                        try:
                            msg = await self.client.wait_for(
                                "message",
                                timeout = 60,
                                check = lambda message: message.author == ctx.author
                                            and message.channel == ctx.channel
                                )

                            if msg:
                                x = msg.content

                                if x.lower() == "1":
                                    users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move1"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 1st move to **{i}**")
                                    return


                                if x.lower() == "2":
                                    users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move2"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 2nd move to **{i}**")
                                    return


                                if x.lower() == "3":
                                    users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move3"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 3rd move to **{i}**")
                                    return


                                if x.lower() == "4":
                                    users[str(ctx.author.id)]["pokemon"]["party"][number]["moves"]["move4"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 4th move to **{i}**")
                                    return

                                else:
                                    await ctx.send(f"That's not a valid pokemon move number! Please choose from 1 to 4 next time!")
                                    return

                        except asyncio.TimeoutError:
                            await ctx,send("You didn't respond in time!")
                            return

                    else:
                        await ctx.send("Your pokemon can't learn that move cause your pokemon needs to be higher level for it!")
                        return

            await ctx.send("That's not a valid move which your pokemon can learn!")
            return

        if number in users[str(ctx.author.id)]["pokemon"]["box"]:
            name = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
            emoji = pokemon[name]["emoji"]
            level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
            move1 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move1"]
            move2 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move4"]

            for i in pokemon[name]["moves"]:
                if i.lower() == move.lower():
                    requiredlevel = pokemon[name]["moves"][i]["level"]

                    if level >= requiredlevel:
                        await ctx.send("Please type the move you want to replce this with!")

                        try:
                            msg = await self.client.wait_for(
                                "message",
                                timeout = 60,
                                check = lambda message: message.author == ctx.author
                                            and message.channel == ctx.channel
                                )

                            if msg:
                                x = msg.content

                                if x.lower() == "1":
                                    users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move1"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 1st move to **{i}**")
                                    return


                                if x.lower() == "2":
                                    users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move2"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 2nd move to **{i}**")
                                    return


                                if x.lower() == "3":
                                    users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move3"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 3rd move to **{i}**")
                                    return


                                if x.lower() == "4":
                                    users[str(ctx.author.id)]["pokemon"]["box"][number]["moves"]["move4"] = i
                                    with open("trainers.json", "w") as f:
                                        json.dump(users, f, indent=4)

                                    await ctx.send(f"Successfully changed your pokemon's 4th move to **{i}**")
                                    return

                                else:
                                    await ctx.send(f"That's not a valid pokemon move number! Please choose from 1 to 4 next time!")
                                    return

                        except asyncio.TimeoutError:
                            await ctx,send("You didn't respond in time!")
                            return

                    else:
                        await ctx.send("Your pokemon can't learn that move cause your pokemon needs to be higher level for it!")
                        return

            await ctx.send("That's not a valid move which your pokemon can learn!")
            return

        else:
            await ctx.send("That's not a valid pokemon number which you have!")

    #swap command
    @commands.command(aliases=["sw"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def swap(self, ctx, n1 = None, n2 = None):
        if n1 == None:
            await ctx.send("Please provide the first pokemon number next time!")
            return

        if n2 == None:
            await ctx.send("Please provide the second pokemon number next time!")
            return

        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if n1 in users[str(ctx.author.id)]["pokemon"]["party"]:
            name = users[str(ctx.author.id)]["pokemon"]["party"][n1]["name"]
            emoji = pokemon[name]["emoji"]
            level = users[str(ctx.author.id)]["pokemon"]["party"][n1]["level"]
            exp = users[str(ctx.author.id)]["pokemon"]["party"][n1]["exp"]
            starter = users[str(ctx.author.id)]["pokemon"]["party"][n1]["starter"]
            move1 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move1"]
            move2 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move4"]

            if n2 in users[str(ctx.author.id)]["pokemon"]["party"]:
                name2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["name"]
                emoji2 = pokemon[name2]["emoji"]
                level2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["level"]
                exp2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["exp"]
                starter2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["starter"]
                move12 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move1"]
                move22 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move2"]
                move32 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move3"]
                move42 = users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move4"]

                users[str(ctx.author.id)]["pokemon"]["party"][n1]["name"] = name2
                pokemon[name]["emoji"] = emoji2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["level"] = level2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["exp"] = exp2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["starter"] = starter2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move1"] = move12
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move2"] = move22
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move3"] = move32
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move4"] = move42

                users[str(ctx.author.id)]["pokemon"]["party"][n2]["name"] = name
                pokemon[name2]["emoji"] = emoji
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["level"] = level
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["exp"] = exp
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["starter"] = starter
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move1"] = move1
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move2"] = move2
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move3"] = move3
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move4"] = move4

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"Successfully swapped {emoji} **{name}** with {emoji2} **{name2}**")
                return

            elif n2 in users[str(ctx.author.id)]["pokemon"]["box"]:
                name2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["name"]
                emoji2 = pokemon[name2]["emoji"]
                level2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["level"]
                exp2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["exp"]
                starter2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["starter"]
                move12 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move1"]
                move22 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move2"]
                move32 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move3"]
                move42 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move4"]

                users[str(ctx.author.id)]["pokemon"]["party"][n1]["name"] = name2
                pokemon[name]["emoji"] = emoji2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["level"] = level2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["exp"] = exp2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["starter"] = starter2
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move1"] = move12
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move2"] = move22
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move3"] = move32
                users[str(ctx.author.id)]["pokemon"]["party"][n1]["moves"]["move4"] = move42

                users[str(ctx.author.id)]["pokemon"]["box"][n2]["name"] = name
                pokemon[name2]["emoji"] = emoji
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["level"] = level
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["exp"] = exp
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["starter"] = starter
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move1"] = move1
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move2"] = move2
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move3"] = move3
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move4"] = move4

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"Successfully swapped {emoji} **{name}** with {emoji2} **{name2}**")
                return

            else:
                await ctx.send("The 2nd pokemon number is not a valid pokemon number that you have!")
                return

        elif n1 in users[str(ctx.author.id)]["pokemon"]["box"]:
            name = users[str(ctx.author.id)]["pokemon"]["box"][n1]["name"]
            emoji = pokemon[name]["emoji"]
            level = users[str(ctx.author.id)]["pokemon"]["box"][n1]["level"]
            exp = users[str(ctx.author.id)]["pokemon"]["box"][n1]["exp"]
            starter = users[str(ctx.author.id)]["pokemon"]["box"][n1]["starter"]
            move1 = users[str(ctx.author.id)]["pokemon"]["box"]["moves"][n1]["move1"]
            move2 = users[str(ctx.author.id)]["pokemon"]["box"]["moves"][n1]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["box"]["moves"][n1]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["box"]["moves"][n1]["move4"]

            if n2 in users[str(ctx.author.id)]["pokemon"]["party"]:
                name2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["name"]
                emoji2 = pokemon[name2]["emoji"]
                level2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["level"]
                exp2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["exp"]
                starter2 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["starter"]
                move12 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move1"]
                move22 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move2"]
                move32 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move3"]
                move42 = users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move4"]

                users[str(ctx.author.id)]["pokemon"]["box"][n1]["name"] = name2
                pokemon[name]["emoji"] = emoji2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["level"] = level2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["exp"] = exp2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["starter"] = starter2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move1"] = move12
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move2"] = move22
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move3"] = move32
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move4"] = move42

                users[str(ctx.author.id)]["pokemon"]["party"][n2]["name"] = name
                pokemon[name2]["emoji"] = emoji
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["level"] = level
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["exp"] = exp
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["starter"] = starter
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move1"] = move1
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move2"] = move2
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move3"] = move3
                users[str(ctx.author.id)]["pokemon"]["party"][n2]["moves"]["move4"] = move4

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"Successfully swapped {emoji} **{name}** with {emoji2} **{name2}**")
                return

            elif n2 in users[str(ctx.author.id)]["pokemon"]["box"]:
                name2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["name"]
                emoji2 = pokemon[name2]["emoji"]
                level2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["level"]
                exp2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["exp"]
                starter2 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["starter"]
                move12 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move1"]
                move22 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move2"]
                move32 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move3"]
                move42 = users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move4"]

                users[str(ctx.author.id)]["pokemon"]["box"][n1]["name"] = name2
                pokemon[name]["emoji"] = emoji2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["level"] = level2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["exp"] = exp2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["starter"] = starter2
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move1"] = move12
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move2"] = move22
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move3"] = move32
                users[str(ctx.author.id)]["pokemon"]["box"][n1]["moves"]["move4"] = move42

                users[str(ctx.author.id)]["pokemon"]["box"][n2]["name"] = name
                pokemon[name2]["emoji"] = emoji
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["level"] = level
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["exp"] = exp
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["starter"] = starter
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move1"] = move1
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move2"] = move2
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move3"] = move3
                users[str(ctx.author.id)]["pokemon"]["box"][n2]["moves"]["move4"] = move4

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"Successfully swapped {emoji} **{name}** with {emoji2} **{name2}**")
                return

        else:
            await ctx.send("The 1st pokemon number is not a valid pokemon number that you have!")
            return

    #pokedex command
    @commands.command(aliases=["pd"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pokedex(self, ctx, name = None):
        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            pokedex.reset_cooldown(ctx)
            return

        if name == None:
            await ctx.send("The pokemon's name is required in order to get info on it!")
            pokedex.reset_cooldown(ctx)
            return

        if str(name) not in pokemon:
            await ctx.send("That's not a valid pokemon in this bot!")
            pokedex.reset_cooldown(ctx)
            return

        emoji = pokemon[str(name)]["emoji"]
        ty = pokemon[str(name)]["type"]
        rarity = pokemon[str(name)]["rarity"]
        evolve_to = pokemon[str(name)]["evolve_to"]
        evolve = pokemon[str(name)]["evolve"]
        image = pokemon[name]["image"]
        hp = pokemon[name]["stats"]["hp"]
        attack = pokemon[name]["stats"]["attack"]
        defense = pokemon[name]["stats"]["defense"]
        sp_atk = pokemon[name]["stats"]["sp. atk"]
        sp_def = pokemon[name]["stats"]["sp. def"]
        speed = pokemon[name]["stats"]["speed"]

        if rarity == "common":
            c = discord.Color.dark_grey()

        elif rarity == "uncommon":
            c = discord.Color.green()

        elif rarity == "rare":
            c = discord.Color.blue()

        elif rarity == "epic":
            c = discord.Color.purple()

        elif rarity == "legendary":
            c = discord.Color.red()

        em = discord.Embed(title=f"**{emoji} {name}**\n\n", description= f"**Type:** {ty}\n**Rarity:** {rarity}\n**Evolve into:** {evolve_to}\n**Evolve level:** {evolve}\n\n**Stats-:**\n**Hp:** {hp}\n**Attack:** {attack}\n**Defense:** {defense}\n**Sp. atk:** {sp_atk}\n**Sp. def:** {sp_def}\n**Speed:** {speed}", color=c)
        em.set_image(url=image)
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    #profile command
    @commands.command(aliases=["pf"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def profile(self, ctx, member: discord.Member = None):
        users = await get_trainer_data()

        if member == None:
            member = ctx.author

        if str(member.id) not in users or str(ctx.author.id) not in users:
            await ctx.send("You or the user mentioned doesn't have a starter pokemon yet! Use `start` command to start your journey!")
            profile.reset_cooldown(ctx)
            return

        em = discord.Embed(title=f"{member.name}'s profile", color=ctx.author.color)
        pokecash = users[str(member.id)]["money"]
        rep = users[str(member.id)]["reputation"]
        boxpoke = 0
        partypoke = 0

        for i in users[str(member.id)]["pokemon"]["party"]:
            partypoke += 1

        for i in users[str(member.id)]["pokemon"]["box"]:
            boxpoke += 1

        rank = None

        if member.id == 796042231538122762:
            rank = "Bot Developer"

        elif member.id == 699767957374500941 or member.id == 869204667601666061:
            rank = "Web Developer"

        else:
            rank = "Bot User"

        em.add_field(name="Reputation Points", value=rep)
        em.add_field(name="PokeCash", value=pokecash)
        em.add_field(name="Number of pokemons in party", value=partypoke)
        em.add_field(name="Number of pokemons in box", value=boxpoke)
        em.add_field(name="Total number of pokemons", value=partypoke + boxpoke)
        em.add_field(name="Rank", value=rank)
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    #respect command
    @commands.command(aliases=["r"])
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def respect(self, ctx, member: discord.Member = None):
        users = await get_trainer_data()

        if str(member.id) not in users or str(ctx.author.id) not in users:
            await ctx.send("You or the mentioned user dosen't have a starter pokemon yet! Use `start` command to start your journey!")
            profile.reset_cooldown(ctx)
            return

        if member == None:
            await ctx.send("Please provide the member you want to respect next time!")
            return

        if member == ctx.author:
            await ctx.send("You can't give reputation points to yourself!")
            return

        users[str(member.id)]["reputation"] += 1

        with open("trainers.json", "w") as f:
            json.dump(users, f, indent=4)

        await ctx.send(f"Successfully given 1 reputation point to {member.name}!")
        await member.send(f"You have recieved 1 reputation point from {ctx.author.name} in {ctx.guild.name}!")

    #release command
    @commands.command(aliases=["re"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def release(self, ctx, poke = None):
        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            release.reset_cooldown(ctx)
            return

        if str(poke) == None:
            await ctx.send("Please provide the pokemon number you want to release next time!")
            return

        if str(poke) in users[str(ctx.author.id)]["pokemon"]["party"]:
            if users[str(ctx.author.id)]["pokemon"]["party"][str(poke)]["starter"] == "True":
                await ctx.send("The pokemon number you have mentioned is your starter pokemon! You cannot remove your starter pokemon once choosen!")
                return

            name = users[str(ctx.author.id)]["pokemon"]["party"][str(poke)]["name"]
            level = users[str(ctx.author.id)]["pokemon"]["party"][str(poke)]["level"]
            emoji = pokemon[name]["emoji"]
            del users[str(ctx.author.id)]["pokemon"]["party"][str(poke)]
            
            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)
            
            await ctx.send(f"Successfully released your pokemon named level {emoji} **{level} {name}**")


        elif str(poke) in users[str(ctx.author.id)]["pokemon"]["box"]:
            if users[str(ctx.author.id)]["pokemon"]["box"][str(poke)]["starter"] == "True":
                await ctx.send("The pokemon number you have mentioned is your starter pokemon! You cannot remove your starter pokemon once choosen!")
                return

            name = users[str(ctx.author.id)]["pokemon"]["box"][str(poke)]["name"]
            level = users[str(ctx.author.id)]["pokemon"]["box"][str(poke)]["level"]
            emoji = pokemon[name]["emoji"]
            del users[str(ctx.author.id)]["pokemon"]["box"][str(poke)]
            
            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)
            
            await ctx.send(f"Successfully released your pokemon named level {emoji} **{level} {name}**")

        else:
            await ctx.send(f"Coudn't find any pokemon of yours with the mentioned pokemon number!")

    #market command
    @commands.command(aliases=["ma"])
    @commands.cooldown(1, 5, BucketType.user)
    async def market(self, ctx):
        users = await get_trainer_data()
        items = await get_items_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            market.reset_cooldown(ctx)
            return


        em = discord.Embed(title="All marketplace categories", color=ctx.author.color)
        em.set_image(url="https://media.discordapp.net/attachments/872710700701712384/900957829089886228/imageedit_5_5780878976.png")
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        m = await ctx.send(embed=em,
        components=[Select(placeholder="Choose the market you want to access!",
                           options=[
                               SelectOption(label="Pokeballs", value=1),
                               SelectOption(label="Medicine", value=2),
                               SelectOption(label="Berries", value=3),
                               SelectOption(label="Battle Items", value=4),
                               SelectOption(label="Money Items", value=5)
                           ]
        )])  

        checker = True

        while checker:
            try:
                res = await self.client.wait_for("select_option", timeout = 30, check=lambda inter:
                    inter.message.id == m.id and
                    inter.user == ctx.author
                )

                if res:
                    if res.values[0] == "0":
                        em = discord.Embed(title="All marketplace categories", color=ctx.author.color) 
                        em.set_image(url="https://media.discordapp.net/attachments/872710700701712384/900957829089886228/imageedit_5_5780878976.png")
                        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await m.delete()
                        m = await ctx.send(embed=em,
                        components=[Select(placeholder="Choose the market you want to access!",
                                        options=[
                                            SelectOption(label="Pokeballs", value=1),
                                            SelectOption(label="Medicine", value=2),
                                            SelectOption(label="Berries", value=3),
                                            SelectOption(label="Battle Items", value=4),
                                            SelectOption(label="Money Items", value=5)
                                        ]
                        )])   

                    if res.values[0] == "1":
                        em = discord.Embed(title="Pokeballs Market", color=ctx.author.color)
                        
                        for i in items["Pokeballs"]:
                            price = items["Pokeballs"][i]["price"]
                            use = items["Pokeballs"][i]["use"]
                            emoji = items["Pokeballs"][i]["emoji"]
                            em.add_field(name=f"{emoji} {i}", value=f"`Price`: {price}\n `Use`: {use}", inline=False)

                        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await m.delete()
                        m = await ctx.send(embed=em,
                        components=[Select(placeholder="Choose the market you want to access!",
                                        options=[
                                            SelectOption(label="Home", value=0),
                                            SelectOption(label="Medicine", value=2),
                                            SelectOption(label="Berries", value=3),
                                            SelectOption(label="Battle Items", value=4),
                                            SelectOption(label="Money Items", value=5)
                                        ]
                        )])   

                    if res.values[0] == "2":
                        em = discord.Embed(title="Medicines Market", color=ctx.author.color)
                        
                        for i in items["Medicines"]:
                            price = items["Medicines"][i]["price"]
                            use = items["Medicines"][i]["use"]
                            emoji = items["Medicines"][i]["emoji"]
                            em.add_field(name=f"{emoji} {i}", value=f"`Price`: {price}\n `Use`: {use}", inline=False)

                        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await m.delete()
                        m = await ctx.send(embed=em,
                        components=[Select(placeholder="Choose the market you want to access!",
                                        options=[
                                            SelectOption(label="Home", value=0),
                                            SelectOption(label="Pokeballs", value=1),
                                            SelectOption(label="Berries", value=3),
                                            SelectOption(label="Battle Items", value=4),
                                            SelectOption(label="Money Items", value=5)
                                        ]
                        )]) 

                    if res.values[0] == "3":
                        em = discord.Embed(title="Berries Market", color=ctx.author.color)
                        
                        for i in items["Berries"]:
                            price = items["Berries"][i]["price"]
                            use = items["Berries"][i]["use"]
                            emoji = items["Berries"][i]["emoji"]
                            em.add_field(name=f"{emoji} {i}", value=f"`Price`: {price}\n `Use`: {use}", inline=False)

                        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await m.delete()
                        m = await ctx.send(embed=em,
                        components=[Select(placeholder="Choose the market you want to access!",
                                        options=[
                                            SelectOption(label="Home", value=0),
                                            SelectOption(label="Pokeballs", value=1),
                                            SelectOption(label="Medicine", value=2),
                                            SelectOption(label="Battle Items", value=4),
                                            SelectOption(label="Money Items", value=5)
                                        ]
                        )]) 

                    if res.values[0] == "4":
                        em = discord.Embed(title="Battle Items Market", color=ctx.author.color)
                        
                        for i in items["Battle Items"]:
                            price = items["Battle Items"][i]["price"]
                            use = items["Battle Items"][i]["use"]
                            emoji = items["Battle Items"][i]["emoji"]
                            em.add_field(name=f"{emoji} {i}", value=f"`Price`: {price}\n `Use`: {use}", inline=False)

                        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await m.delete()
                        m = await ctx.send(embed=em,
                        components=[Select(placeholder="Choose the market you want to access!",
                                        options=[
                                            SelectOption(label="Home", value=0),
                                            SelectOption(label="Pokeballs", value=1),
                                            SelectOption(label="Medicine", value=2),
                                            SelectOption(label="Berries", value=3),
                                            SelectOption(label="Money Items", value=5)
                                        ]
                        )]) 

                    if res.values[0] == "5":
                        em = discord.Embed(title="Money Items Market", color=ctx.author.color)
                        
                        for i in items["Money Items"]:
                            price = items["Money Items"][i]["price"]
                            use = items["Money Items"][i]["use"]
                            emoji = items["Money Items"][i]["emoji"]
                            em.add_field(name=f"{emoji} {i}", value=f"`Price`: {price}\n `Use`: {use}", inline=False)

                        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await m.delete()
                        m = await ctx.send(embed=em,
                        components=[Select(placeholder="Choose the market you want to access!",
                                        options=[
                                            SelectOption(label="Home", value=0),
                                            SelectOption(label="Pokeballs", value=1),
                                            SelectOption(label="Medicine", value=2),
                                            SelectOption(label="Berries", value=3),
                                            SelectOption(label="Battle Items", value=4)
                                        ]
                        )]) 

            except asyncio.TimeoutError:
                await m.delete()
                return

    #buy command
    @commands.command(aliases=["b"])
    @commands.cooldown(1, 5, BucketType.user)
    async def buy(self, ctx, amt = None, *, item = None):
        users = await get_trainer_data()
        items = await get_items_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            market.reset_cooldown(ctx)
            return

        if item == None:
            await ctx.send("Please specify the item you want to buy next time!")

        if amt == None:
            amt = 1

        checker = False
        category = None

        for i in items:
            for x in items[i]:
                if x.lower() == item.lower():
                    category = i
                    item = x
                    checker = True

        if checker == True:
            price = items[category][item]["price"]
            balance = users[str(ctx.author.id)]["money"]

            if balance < price * int(amt):
                await ctx.send("You don't have enough money to buy this item!")
                return

            users[str(ctx.author.id)]["money"] -= price * int(amt)

            if item in users[str(ctx.author.id)]["bag"]:
                users[str(ctx.author.id)]["bag"][item] += int(amt)

            else:
                users[str(ctx.author.id)]["bag"][item] = int(amt)

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            emoji = items[category][item]["emoji"]

            await ctx.send(f"Successfully bought **{amt} {emoji} {item}**!")
            return

        await ctx.send("Thats not a valid item in the market!")

    #sell command
    @commands.command(aliases=["s"])
    @commands.cooldown(1, 5, BucketType.user)
    async def sell(self, ctx, amt = None, *, item = None):
        users = await get_trainer_data()
        items = await get_items_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            sell.reset_cooldown(ctx)
            return

        if item == None:
            await ctx.send("Please specify the item you want to sell next time!")

        if amt == None:
            amt = 1

        checker = False
        category = None

        for i in users[str(ctx.author.id)]["bag"]:
            if i.lower() == item.lower():
                checker = True

        if checker == True:
            for x in items:
                for g in items[x]:
                    if g.lower() == item.lower():
                        category = x
                        item = g

            emoji = items[category][item]["emoji"]

            if users[str(ctx.author.id)]["bag"][item] < int(amt):
                await ctx.send(f"You don't have **{amt} {emoji} {item}**")
                return

            sellprice = items[category][item]["sell"] * int(amt)

            if users[str(ctx.author.id)]["bag"][item] == 1:
                del users[str(ctx.author.id)]["bag"][item]

            else:
                users[str(ctx.author.id)]["bag"][item] -= 1

            users[str(ctx.author.id)]["money"] += sellprice

            with open("trainers.json", "w") as f:
                json.dump(users, f, indent=4)

            await ctx.send(f"Successfully sold **{amt} {emoji} {item}** for **{sellprice}** PokeCash!")
            return

        await ctx.send("You don't have that item in your bag!")

    #inventory command
    @commands.command(aliases=["inv", "bag"])
    @commands.cooldown(1, 5, BucketType.user)
    async def inventory(self, ctx, member: discord.Member = None):
        users = await get_trainer_data()
        items = await get_items_data()

        if member == None:
            member = ctx.author

        if str(ctx.author.id) not in users or str(member.id) not in users:
            await ctx.send("You or the mentioned user dosen't have a starter pokemon yet! Use `start` command to start your journey!")
            inventory.reset_cooldown(ctx)
            return

        total_items = 0

        for i in users[str(ctx.author.id)]["bag"]:
            total_items += 1

        if total_items < 5:
            total_pages = 1
        
        else:
            total_pages = total_items // 5

            if total_items % 5 != 0:
                total_pages += 1

        if total_pages == 1:
            em = discord.Embed(title=f"Inventory of {member.name}", color=ctx.author.color)
            em.set_footer(text=f"Page: 1/{total_pages}", icon_url=ctx.author.avatar_url)

            for i in users[str(ctx.author.id)]["bag"]:
                amt = users[str(ctx.author.id)]["bag"][i]
                
                for g in items:
                    for f in items[g]:
                        if f.lower() == i.lower():
                            emoji = items[g][f]["emoji"]
                            em.add_field(name=f"{emoji} {i}", value=f"Amount: **{amt}**", inline=False)

            await ctx.send(embed=em, components = [[
                Button(style=ButtonStyle.green, label="Next", disabled=True, emoji="⏩"),
                Button(style=ButtonStyle.red, label="Back", disabled=True, emoji="⏪"),
            ]])
        
        else:
            x = True
            p = 1
            em = discord.Embed(title=f"Inventory of {member.name}", color=ctx.author.color)
            em.set_footer(text=f"Page: {p}/{total_pages}", icon_url=ctx.author.avatar_url)
            l = (p-1) * 5 + 1
            e = p * 5
            c = 1

            for i in users[str(ctx.author.id)]["bag"]:
                if c >= l and c <= e:
                    amt = users[str(ctx.author.id)]["bag"][i]

                    for g in items:
                        for f in items[g]:
                            if f.lower() == i.lower():
                                emoji = items[g][f]["emoji"]
                                em.add_field(name=f"{emoji} {i}", value=f"Amount: **{amt}**", inline=False)

                c += 1

            m = await ctx.send(embed=em, components = [[
                Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
            ]])

            while x:
                def check(res):
                    return ctx.author == res.user and res.channel == ctx.channel

                try:
                    res = await self.client.wait_for("button_click", check=check, timeout=15)
                    e = res.component.label

                    if e == "Next":
                        p += 1

                        if p == total_pages:
                            em = discord.Embed(title=f"Inventory of {member.name}", color=ctx.author.color)
                            l = (p-1) * 5 + 1
                            e = p * 5
                            c = 1

                            for i in users[str(ctx.author.id)]["bag"]:
                                if c >= l and c <= e:
                                    amt = users[str(ctx.author.id)]["bag"][i]
                                    for g in items:
                                        for f in items[g]:
                                            if f.lower() == i.lower():
                                                emoji = items[g][f]["emoji"]
                                                em.add_field(name=f"{emoji} {i}", value=f"Amount: **{amt}**", inline=False)

                                c += 1

                            em.set_footer(text=f"Page: {p}/{total_pages}", icon_url=ctx.author.avatar_url)
                            await m.delete()
                            m = await ctx.send(embed=em, components = [[
                                Button(style=ButtonStyle.green, label="Next", disabled=True, emoji="⏩"),
                                Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                            ]])

                        else:
                            em = discord.Embed(title=f"Inventory of {member.name}", color=ctx.author.color)
                            l = (p-1) * 5 + 1
                            e = p * 5
                            c = 1

                            for i in users[str(ctx.author.id)]["bag"]:
                                if c >= l and c <= e:
                                    amt = users[str(ctx.author.id)]["bag"][i]
                                    for g in items:
                                        for f in items[g]:
                                            if f.lower() == i.lower():
                                                emoji = items[g][f]["emoji"]
                                                em.add_field(name=f"{emoji} {i}", value=f"Amount: **{amt}**", inline=False)

                                c += 1

                            em.set_footer(text=f"Page: {p}/{total_pages}", icon_url=ctx.author.avatar_url)
                            await m.delete()
                            m = await ctx.send(embed=em, components = [[
                                Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                                Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                            ]])

                    if e == "Back":
                        p -= 1

                        if p == 1:
                            em = discord.Embed(title=f"Inventory of {member.name}", color=ctx.author.color)
                            l = (p-1) * 5 + 1
                            e = p * 5
                            c = 1

                            for i in users[str(ctx.author.id)]["bag"]:
                                if c >= l and c <= e:
                                    amt = users[str(ctx.author.id)]["bag"][i]
                                    for g in items:
                                        for f in items[g]:
                                            if f.lower() == i.lower():
                                                emoji = items[g][f]["emoji"]
                                                em.add_field(name=f"{emoji} {i}", value=f"Amount: **{amt}**", inline=False)

                                c += 1

                            em.set_footer(text=f"Page: {p}/{total_pages}", icon_url=ctx.author.avatar_url)
                            await m.delete()
                            m = await ctx.send(embed=em, components = [[
                                Button(style=ButtonStyle.green, label="Next", emoji="⏩"),
                                Button(style=ButtonStyle.red, label="Back", disabled=True, emoji="⏪"),
                            ]])

                        else:
                            em = discord.Embed(title=f"Inventory of {member.name}", color=ctx.author.color)
                            l = (p-1) * 5 + 1
                            e = p * 5
                            c = 1

                            for i in users[str(ctx.author.id)]["bag"]:
                                if c >= l and c <= e:
                                    amt = users[str(ctx.author.id)]["bag"][i]
                                    for g in items:
                                        for f in items[g]:
                                            if f.lower() == i.lower():
                                                emoji = items[g][f]["emoji"]
                                                em.add_field(name=f"{emoji} {i}", value=f"Amount: **{amt}**", inline=False)

                                c += 1

                            em.set_footer(text=f"Page: {p}/{total_pages}", icon_url=ctx.author.avatar_url)
                            await m.delete()
                            m = await ctx.send(content="", embed=em, components = [[
                                Button(style=ButtonStyle.green, label="Next", disabled=True, emoji="⏩"),
                                Button(style=ButtonStyle.red, label="Back", emoji="⏪"),
                            ]])

                except asyncio.TimeoutError:
                    return

    #item command
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def item(self, ctx, *, name = None):
        items = await get_items_data()
        users = await get_trainer_data()

        if name == None:
            await ctx.send("Please provide the name of the item you want info on next time!")

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            item.reset_cooldown(ctx)
            return

        checker = False
        category = None

        for i in items:
            for x in items[i]:
                if name.lower() == x.lower():
                    checker = True
                    category = i
                    name = x
                    price = items[i][x]["price"]
                    sell = items[i][x]["sell"]
                    emoji = items[i][x]["emoji"]
                    image = items[i][x]["image"]
                    use = items[i][x]["use"]

        if checker == True:
            em = discord.Embed(title=f"Info on {emoji} {name}", description=f"\n**Price:** {price}\n**Selling Price:** {sell}\n**Use:** {use}\n**Category:** {category}", color=ctx.author.color)
            em.set_image(url=image)
            await ctx.send(embed=em)
            return

        else:
            await ctx.send("That's not a valid item!")
            return
            
    #vitamin command
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def vitamin(self, ctx, name = None, number = None):
        items = await get_items_data()
        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if name == None:
            await ctx.send("Please provide the name of the vitamin you want to use next time!")
            return

        if number == None:
            await ctx.send("Please provide the pokemon number of the pokemon you want to use the vitamin on!")
            return

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            item.reset_cooldown(ctx)
            return


        if number in users[str(ctx.author.id)]["pokemon"]["party"]:
            checker = False
            category = None

            for i in users[str(ctx.author.id)]["bag"]:
                if name.lower() == i.lower():
                    for g in items:
                        for l in items[g]:
                            if name.lower() == l.lower():
                                category = g

                    checker = True
                    name = i

            if checker == True:
                usableitems = ["Protein", "Iron", "Calcium", "Zinc", "Carbos"]
               
                if name not in usableitems:
                    await ctx.send("That's not a valid vitamin name!")
                    return

                if name == "Protein":
                    pokename = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["party"][number]["protein"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage proteins which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["party"][number]["protein"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Attack Stat")
                    return

                if name == "Iron":
                    pokename = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["party"][number]["iron"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage iron which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["party"][number]["iron"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Defense Stat")
                    return

                if name == "Calcium":
                    pokename = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["party"][number]["calcium"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage calcium which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["party"][number]["calcium"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Special Attack Stat")
                    return

                if name == "Zinc":
                    pokename = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["party"][number]["zinc"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage zinc which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["party"][number]["zinc"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Special Defense Stat")
                    return

                if name == "Carbos":
                    pokename = users[str(ctx.author.id)]["pokemon"]["party"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["party"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["party"][number]["carbos"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage carbos which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["party"][number]["carbos"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Speed Stat")
                    return

            else:
                await ctx.send("You don't have that item in your bag!")
                return

        elif number in users[str(ctx.author.id)]["pokemon"]["box"]:
            checker = False
            category = None

            for i in users[str(ctx.author.id)]["bag"]:
                if name.lower() == i.lower():
                    for g in items:
                        for l in items[g]:
                            if name.lower() == l.lower():
                                category = g

                    checker = True
                    name = i

            if checker == True:
                usableitems = ["Protein", "Iron", "Calcium", "Zinc", "Carbos"]
               
                if name not in usableitems:
                    await ctx.send("That's not a valid vitamin name!")
                    return

                if name == "Protein":
                    pokename = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["box"][number]["protein"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage proteins which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["box"][number]["protein"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Attack Stat")
                    return

                if name == "Iron":
                    pokename = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["box"][number]["iron"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage iron which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["box"][number]["iron"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Defense Stat")
                    return

                if name == "Calcium":
                    pokename = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["box"][number]["calcium"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage calcium which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["box"][number]["calcium"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Special Attack Stat")
                    return

                if name == "Zinc":
                    pokename = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["box"][number]["zinc"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage zinc which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["box"][number]["zinc"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Special Defense Stat")
                    return

                if name == "Carbos":
                    pokename = users[str(ctx.author.id)]["pokemon"]["box"][number]["name"]
                    level = users[str(ctx.author.id)]["pokemon"]["box"][number]["level"]
                    emoji1 = pokemon[pokename]["emoji"]
                    emoji2 = items["Medicines"][name]["emoji"]


                    if users[str(ctx.author.id)]["pokemon"]["box"][number]["carbos"] == 10:
                        await ctx.send("Your pokemon has already reached the max limit of usage carbos which is **10**!")
                        return

                    if users[str(ctx.author.id)]["bag"][name] > 1:
                        users[str(ctx.author.id)]["bag"][name] -= 1

                    else:
                        del users[str(ctx.author.id)]["bag"][name]

                    users[str(ctx.author.id)]["pokemon"]["box"][number]["carbos"] += 1

                    with open("trainers.json", "w") as f:
                        json.dump(users, f, indent=4)

                    await ctx.send(f"You successfully used a/an **{emoji2} {name}** vitamin on your **{emoji1} {pokename}**!\n\n+2 Speed Stat")
                    return

            else:
                await ctx.send("You don't have that item in your bag!")
                return

        else:
            await ctx.send("That is not a valid pokemon number that you have!")
            return

    #fish command
    @commands.command()
    @commands.cooldown(1, 15, BucketType.user)
    async def fish(self, ctx, *, name = None):
        items = await get_items_data()
        users = await get_trainer_data()

        if name == None:
            await ctx.send("Please provide the name of the rod you want to use next time!")

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            item.reset_cooldown(ctx)
            return

        checker = False

        rods = ["Old Rod", "Good Rod", "Super Rod"]

        for i in rods:
            if name.lower() == i.lower():
                name = i

                if name in users[str(ctx.author.id)]["bag"]:
                    checker = True

        if checker == True:
            if name == "Old Rod":
                chance = random.randint(1, 10)

                if chance == 6 or chance == 7:
                    await ctx.send("You caught nothing.. Better luck next time!")
                    return

                num = random.randint(1, 100)
                fish = None

                if num >= 1 and num <= 50:
                    fish = "Common Fish"

                if num == 51 or num == 52:
                    fish = "Legendary Fish"

                if num >= 53 and num <= 90:
                    fish = "Uncommon Fish"

                else:
                    fish = "Rare Fish"

                emoji = items["Fishes"][fish]["emoji"]

                if fish in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][fish] += 1

                else:
                    users[str(ctx.author.id)]["bag"][fish] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just caught a/an {emoji} **{fish}**! It has been moved to your bag!")
                return

            if name == "Good Rod":
                chance = random.randint(1, 10)

                if chance == 6:
                    await ctx.send("You caught nothing.. Better luck next time!")
                    return

                num = random.randint(1, 100)
                fish = None

                if num >= 1 and num <= 30:
                    fish = "Common Fish"

                if num == 31 or num == 32 or num == 33:
                    fish = "Legendary Fish"

                if num >= 34 and num <= 54:
                    fish = "Rare Fish"

                else:
                    fish = "Uncommon Fish"

                emoji = items["Fishes"][fish]["emoji"]

                if fish in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][fish] += 1

                else:
                    users[str(ctx.author.id)]["bag"][fish] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just caught a/an {emoji} **{fish}**! It has been moved to your bag!")
                return                    

            if name == "Super Rod":
                num = random.randint(1, 100)
                fish = None

                if num >= 1 and num <= 20:
                    fish = "Common Fish"

                if num >= 21 and num <= 25:
                    fish = "Legendary Fish"

                if num >= 26 and num <= 50:
                    fish = "Rare Fish"

                else:
                    fish = "Uncommon Fish"

                emoji = items["Fishes"][fish]["emoji"]

                if fish in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][fish] += 1

                else:
                    users[str(ctx.author.id)]["bag"][fish] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just caught a/an {emoji} **{fish}**! It has been moved to your bag!")
                return   

        else:
            await ctx.send("You don't have that item in your bag or that item is not a fishing rod!")
            return

    #mine command
    @commands.command()
    @commands.cooldown(1, 15, BucketType.user)
    async def mine(self, ctx, *, name = None):
        items = await get_items_data()
        users = await get_trainer_data()

        if name == None:
            await ctx.send("Please provide the name of the pickaxe you want to use next time!")

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            item.reset_cooldown(ctx)
            return

        checker = False

        picks = ["Wooden Pickaxe", "Stone Pickaxe", "Iron Pickaxe", "Diamond Pickaxe"]

        for i in picks:
            if name.lower() == i.lower():
                name = i

                if name in users[str(ctx.author.id)]["bag"]:
                    checker = True

        if checker == True:
            if name == "Wooden Pickaxe":
                chance = random.randint(1, 10)

                if chance == 6 or chance == 7 or chance == 8 or chance == 5:
                    await ctx.send("You caught nothing.. Better luck next time!")
                    return

                num = random.randint(1, 100)
                ore = None

                if num >= 1 and num <= 50:
                    ore = "Coal Ore"

                if num == 51 or num == 52:
                    ore = "Diamond Ore"

                if num >= 53 and num <= 90:
                    ore = "Copper Ore"

                if num >= 91 and num <= 93:
                    ore = "Emerald Ore"

                else:
                    ore = "Iron Ore"

                emoji = items["Ores"][ore]["emoji"]

                if ore in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][ore] += 1

                else:
                    users[str(ctx.author.id)]["bag"][ore] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just found a/an {emoji} **{ore}**! It has been moved to your bag!")
                return

            if name == "Stone Pickaxe":
                chance = random.randint(1, 10)

                if chance == 6 or chance == 7 or chance == 8:
                    await ctx.send("You found nothing.. Better luck next time!")
                    return

                num = random.randint(1, 100)
                ore = None

                if num >= 1 and num <= 40:
                    ore = "Coal Ore"

                if num >= 41 and num <= 43:
                    ore = "Diamond Ore"

                if num >= 44 and num <= 80:
                    ore = "Copper Ore"

                if num >= 81 and num <= 89:
                    ore = "Emerald Ore"

                else:
                    ore = "Iron Ore"

                emoji = items["Ores"][ore]["emoji"]

                if ore in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][ore] += 1

                else:
                    users[str(ctx.author.id)]["bag"][ore] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just found a/an {emoji} **{ore}**! It has been moved to your bag!")
                return

            if name == "Iron Pickaxe":
                chance = random.randint(1, 100)

                if chance == 6 or chance == 7:
                    await ctx.send("You found nothing.. Better luck next time!")
                    return

                num = random.randint(1, 100)
                ore = None

                if num >= 1 and num <= 30:
                    ore = "Coal Ore"

                if num >= 31 or num <= 34:
                    ore = "Diamond Ore"

                if num >= 35 and num <= 70:
                    ore = "Copper Ore"

                if num >= 71 and num <= 85:
                    ore = "Emerald Ore"

                else:
                    ore = "Iron Ore"

                emoji = items["Ores"][ore]["emoji"]

                if ore in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][ore] += 1

                else:
                    users[str(ctx.author.id)]["bag"][ore] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just found a/an {emoji} **{ore}**! It has been moved to your bag!")
                return

            if name == "Diamond Pickaxe":
                chance = random.randint(1, 10)

                if chance == 6:
                    await ctx.send("You found nothing.. Better luck next time!")
                    return

                num = random.randint(1, 100)
                ore = None

                if num >= 1 and num <= 20:
                    ore = "Coal Ore"

                if num >= 21 or num <= 25:
                    ore = "Diamond Ore"

                if num >= 26 and num <= 50:
                    ore = "Copper Ore"

                if num >= 51 and num <= 71:
                    ore = "Emerald Ore"

                else:
                    ore = "Iron Ore"

                emoji = items["Ores"][ore]["emoji"]

                if ore in users[str(ctx.author.id)]["bag"]:
                    users[str(ctx.author.id)]["bag"][ore] += 1

                else:
                    users[str(ctx.author.id)]["bag"][ore] = 1

                with open("trainers.json", "w") as f:
                    json.dump(users, f, indent=4)

                await ctx.send(f"You just found a/an {emoji} **{ore}**! It has been moved to your bag!")
                return

        else:
            await ctx.send("You don't have that item in your bag or that item is not a pickaxe!")
            return

    #daily command
    @commands.command()
    @commands.cooldown(1, 86400, BucketType.user)
    async def daily(self, ctx):
        users = await get_trainer_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            daily.reset_cooldown(ctx)
            return 

        users[str(ctx.author.id)]["money"] += 2000       

        with open("trainers.json", "w") as f:
            json.dump(users, f, indent=4)

        await ctx.send("Successfully given **2000 PokeCash** to your account")

    #test command
    @commands.command()
    async def test(self, ctx):
        users = await get_trainer_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            daily.reset_cooldown(ctx)
            return 

        m = await ctx.send("I am testing the drop downs!",
        components=[Select(placeholder="Choose what you want to see!",
                           options=[
                               SelectOption(label="Option 1", value=1),
                               SelectOption(label="Option 2", value=2),
                               SelectOption(label="Option 3", value=3),
                               SelectOption(label="❌ Cancel", value="Cancel")
                           ]
        )])

        res = await self.client.wait_for("select_option", check=lambda inter:
             inter.message.id == m.id and
             inter.user == ctx.author
        )
        await ctx.send(f"{res.values[0]} Choosen!")

    #all errors

    #party error
    @party.error
    async def party_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #pokemon error
    @pokemon.error
    async def pokemon_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #info error
    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #moveslist error
    @moveslist.error
    async def moveslist_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #catch error
    @catch.error
    async def catch_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #start error
    @start.error
    async def start_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #learn error
    @learn.error
    async def learn_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #swap error
    @swap.error
    async def swap_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #moves error
    @moves.error
    async def moves_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #pokedex error
    @pokedex.error
    async def pokedex_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)
        pokedex.reset_cooldown(ctx)

    #profile error
    @profile.error
    async def profile_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 60:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #respect error
    @respect.error
    async def respect_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #release error
    @release.error
    async def release_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #market error
    @market.error
    async def market_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #buy error
    @buy.error
    async def buy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #inventory error
    @inventory.error
    async def inventory_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #fish error
    @fish.error
    async def fish_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #daily error
    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 86400:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} days** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #mine error
    @mine.error
    async def mine_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 86400:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} days** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

    #vitamin error
    @vitamin.error
    async def vitamin_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Coudn't a find a user with that name or id in this server")
            return

        if isinstance(error, commands.CommandOnCooldown):
            if int(error.retry_after) >= 86400:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} days** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            if int(error.retry_after) >= 3600:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 3600} hours** in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

            elif int(error.retry_after) >= 60:
                    em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait **{int(error.retry_after) // 60} minutes** in order to use it again!", color=discord.Color.red())
                    await ctx.send(embed=em)
                    return

            else:
                em = discord.Embed(title="Woah! Calm down there bud..", description=f"Please wait {int(error.retry_after)} seconds in order to use it again!", color=discord.Color.red())
                await ctx.send(embed=em)
                return

        await ctx.send(error)

def setup(client):
    client.add_cog(Fun(client))
