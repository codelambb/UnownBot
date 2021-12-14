import discord
import json
from discord.ext import commands
import asyncio
import random
from discord_components import *
import typing

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
            users[str(user.id)]["pokemon"]["party"][f"{n}"]["starter"] = "True"
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

class Duel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('duel file is ready!')

    #duel command
    @commands.command(aliases=["d"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def duel(self, ctx, member: discord.Member):
        pokelist = await get_pokelist_data()
        users = await get_trainer_data()
        pokemon = await get_pokemon_data()

        if str(ctx.author.id) not in users:
            await ctx.send("You don't have a starter pokemon yet! Use `start` command to start your journey!")
            return

        if member == None:
            await ctx.send("Who do you want to duel?! Please mention someone next time!")
            return

        if str(member.id) not in users:
            await ctx.send("That member don't have a starter pokemon yet! Tell them to use `start` command to start their journey!")
            return

        col = discord.Color.orange()
        s = 0

        for i in users[str(ctx.author.id)]["pokemon"]["party"]:
            if s == 1:
                break

            name = users[str(ctx.author.id)]["pokemon"]["party"][i]["name"]
            number = i
            level = users[str(ctx.author.id)]["pokemon"]["party"][i]["level"]
            emoji = pokemon[name]["emoji"]
            x = i
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
            move1 = users[str(ctx.author.id)]["pokemon"]["party"][i]["moves"]["move1"]
            move2 = users[str(ctx.author.id)]["pokemon"]["party"][i]["moves"]["move2"]
            move3 = users[str(ctx.author.id)]["pokemon"]["party"][i]["moves"]["move3"]
            move4 = users[str(ctx.author.id)]["pokemon"]["party"][i]["moves"]["move4"]
            s += 1

        s = 0

        for i in users[str(member.id)]["pokemon"]["party"]:
            if s == 1:
                break

            name2 = users[str(member.id)]["pokemon"]["party"][i]["name"]
            number2 = i
            level2 = users[str(member.id)]["pokemon"]["party"][i]["level"]
            emoji2 = pokemon[name2]["emoji"]
            x2 = i
            basehp2 = pokemon[name2]["stats"]["hp"]
            baseattack2 = pokemon[name2]["stats"]["attack"]
            basedefense2 = pokemon[name2]["stats"]["defense"]
            basesp_atk2 = pokemon[name2]["stats"]["sp. atk"]
            basesp_def2 = pokemon[name2]["stats"]["sp. def"]
            basespeed2 = pokemon[name2]["stats"]["speed"]
            hp2 = round(basehp2 + level2 * (1/50 * basehp2))
            attack2 = round(baseattack2 + level2 * (1/50 * baseattack2))
            defense2 = round(basedefense2 + level2 * (1/50 * basedefense2))
            sp_atk2 = round(basesp_atk2 + level2 * (1/50 * basesp_atk2))
            sp_def2 = round(basesp_def2 + level2 * (1/50 * basesp_def2))
            speed2 = round(basespeed2 + level2 * (1/50 * basespeed2))
            moveai1 = users[str(member.id)]["pokemon"]["party"][i]["moves"]["move1"]
            moveai2 = users[str(member.id)]["pokemon"]["party"][i]["moves"]["move2"]
            moveai3 = users[str(member.id)]["pokemon"]["party"][i]["moves"]["move3"]
            moveai4 = users[str(member.id)]["pokemon"]["party"][i]["moves"]["move4"]
            s += 1

        moveai = [moveai1, moveai2, moveai3, moveai4]
        special = ["attack", "defense", "sp_attack", "sp_defense", "speed", "attack_decrease", "defense_decrease", "sp_attack_decrease", "sp_def_decrease", "speed_decrease"]
        specialdo1 = []
        specialdo2 = []
        match = True

        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        def check2(res):
            return member == res.user and res.channel == ctx.channel

        while match == True:
            if speed >= speed2:
                asd = discord.Embed(title=f"{ctx.author.name} please click the move number you want to use!\n\n", description=f"1st move: **{move1}**\n2nd move: **{move2}**\n3rd move: **{move3}**\n4th move: **{move4}**", color=col)
                await ctx.send(embed=asd, components = [[
                    Button(style=ButtonStyle.green, label=f"1"),
                    Button(style=ButtonStyle.red, label=f"2"),
                    Button(style=ButtonStyle.blue, label=f"3"),
                    Button(style=ButtonStyle.grey, label=f"4")
                ]])

                try:
                    res1 = await self.client.wait_for("button_click", check=check, timeout=15)
                    await res1.respond(content="You have successfully chosen your move!")
                    e = res1.component.label

                except asyncio.TimeoutError:
                    await ctx.send(f"{ctx.author.mention} didn't respond in time! Match cancelled.")
                    return

                asd = discord.Embed(title=f"{member.name} please click the move number you want to use!\n\n", description=f"1st move: **{moveai1}**\n2nd move: **{moveai2}**\n3rd move: **{moveai3}**\n4th move: **{moveai4}**", color=col)
                await ctx.send(embed=asd, components = [[
                    Button(style=ButtonStyle.green, label=f"1"),
                    Button(style=ButtonStyle.red, label=f"2"),
                    Button(style=ButtonStyle.blue, label=f"3"),
                    Button(style=ButtonStyle.grey, label=f"4")
                ]])

                try:
                    res2 = await self.client.wait_for("button_click", check=check2, timeout=15)
                    await res2.respond(content="You have successfully chosen your move!")
                    t = res2.component.label

                except asyncio.TimeoutError:
                    await ctx.send(f"{member.mention} didn't respond in time! Match cancelled.")
                    return

                if e == "1":
                    movetype = pokemon[name]["moves"][move1]["type"]
                    movedamage = pokemon[name]["moves"][move1]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move1]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                elif e == "2":
                    movetype = pokemon[name]["moves"][move2]["type"]
                    movedamage = pokemon[name]["moves"][move2]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move2]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                elif e == "3":
                    movetype = pokemon[name]["moves"][move3]["type"]
                    movedamage = pokemon[name]["moves"][move3]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move3]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                elif e == "4":
                    movetype = pokemon[name]["moves"][move4]["type"]
                    movedamage = pokemon[name]["moves"][move4]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move4]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        if movedamage2 == 0 and movedamage != 0:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                        else:
                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! They did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                else:
                    await ctx.send("That's not a valid move! Try again!")

            if speed < speed2:
                asd = discord.Embed(title=f"{member.name} please click the move number you want to use!\n\n", description=f"1st move: **{moveai1}**\n2nd move: **{moveai2}**\n3rd move: **{moveai3}**\n4th move: **{moveai4}**", color=col)
                await ctx.send(embed=asd, components = [[
                    Button(style=ButtonStyle.green, label=f"1"),
                    Button(style=ButtonStyle.red, label=f"2"),
                    Button(style=ButtonStyle.blue, label=f"3"),
                    Button(style=ButtonStyle.grey, label=f"4")
                ]])

                try:
                    res1 = await self.client.wait_for("button_click", check=check2, timeout=15)
                    await res1.respond(content="You have successfully chosen your move!")
                    t = res1.component.label

                except asyncio.TimeoutError:
                    await ctx.send(f"{member.mention} didn't respond in time! Match cancelled.")
                    return

                asd = discord.Embed(title=f"{ctx.author.name} please click the move number you want to use!\n\n", description=f"1st move: **{move1}**\n2nd move: **{move2}**\n3rd move: **{move3}**\n4th move: **{move4}**", color=col)
                await ctx.send(embed=asd, components = [[
                    Button(style=ButtonStyle.green, label=f"1"),
                    Button(style=ButtonStyle.red, label=f"2"),
                    Button(style=ButtonStyle.blue, label=f"3"),
                    Button(style=ButtonStyle.grey, label=f"4")
                ]])

                try:
                    res2 = await self.client.wait_for("button_click", check=check, timeout=15)
                    await res2.respond(content="You have successfully chosen your move!")
                    e = res2.component.label

                except asyncio.TimeoutError:
                    await ctx.send(f"{ctx.author.mention} didn't respond in time! Match cancelled.")
                    return

                if e == "1":
                    movetype = pokemon[name]["moves"][move1]["type"]
                    movedamage = pokemon[name]["moves"][move1]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move1]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return
                                
                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move1}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move1}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move1}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move1}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                elif e == "2":
                    movetype = pokemon[name]["moves"][move2]["type"]
                    movedamage = pokemon[name]["moves"][move2]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move2]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return
                                
                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move2}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move2}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move2}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move2}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                elif e == "3":
                    movetype = pokemon[name]["moves"][move3]["type"]
                    movedamage = pokemon[name]["moves"][move3]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move3]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return
                                
                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move3}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move3}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move3}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move3}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                elif e == "4":
                    movetype = pokemon[name]["moves"][move4]["type"]
                    movedamage = pokemon[name]["moves"][move4]["damage"]

                    for i in special:
                        if i in pokemon[name]["moves"][move4]:
                            specialdo1.append(i)

                    if t == "1":
                        movetype2 = pokemon[name2]["moves"][moveai1]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai1]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai1]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai1]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai1]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai1]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai1}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai1]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai1]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai1}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai1}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return
                                
                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "2":
                        movetype2 = pokemon[name2]["moves"][moveai2]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai2]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai2]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai2]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai2]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai2]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai2}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai2]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai2]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai2}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai2}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "3":
                        movetype2 = pokemon[name2]["moves"][moveai3]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai3]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai3]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai3]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai3]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai3]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai3}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai3]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai3]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai3}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai3}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    if t == "4":
                        movetype2 = pokemon[name2]["moves"][moveai4]["type"]
                        movedamage2 = pokemon[name2]["moves"][moveai4]["damage"]

                        for i in special:
                            if i in pokemon[name2]["moves"][moveai4]:
                                specialdo2.append(i)

                        if movedamage == 0 and movedamage2 != 0:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"{member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.mention} has won the battle!")
                                return

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        if movedamage2 == 0 and movedamage != 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name2]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name2]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name2]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name2]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.mention} has won the battle!")
                                return

                        if movedamage == 0 and movedamage2 == 0:
                            for i in specialdo2:
                                if i == "attack":
                                    s = pokemon[name]["moves"][moveai4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][moveai4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][moveai4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{moveai4}**. Their speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][moveai4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][moveai4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{moveai4}**. {ctx.author.name}'s pokemon's speed has been decreased!")

                            for i in specialdo1:
                                if i == "attack":
                                    s = pokemon[name]["moves"][move4]["attack"]
                                    attack2 += s
                                    await ctx.send(f"{ctx.author.name} used **{move4}**. {ctx.author.name}'s attack has been increased!")

                                if i == "defense":
                                    s = pokemon[name]["moves"][move4]["defense"]
                                    defense2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s defense has been increased!")

                                if i == "special_attack":
                                    s = pokemon[name]["moves"][move4]["sp_attack"]
                                    sp_atk2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. attack has been increased!")

                                if i == "special_defense":
                                    s = pokemon[name]["moves"][move4]["sp_defense"]
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s sp. defense has been increased!")
                                    sp_def2 += s

                                if i == "speed":
                                    s = pokemon[name]["moves"][move4]["speed"]
                                    speed2 += s
                                    await ctx.send(f"{member.name} used **{move4}**. {ctx.author.name}'s speed has been increased!")

                                if i == "attack_decrease":
                                    s = pokemon[name]["moves"][move4]["attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's attack has been decreased!")

                                if i == "defense_decrease":
                                    s = pokemon[name]["moves"][move4]["defense_decrease"]
                                    defense -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's defense has been decreased!")

                                if i == "special_attack_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_attack_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. attack has been decreased!")

                                if i == "special_defense_decrease":
                                    s = pokemon[name]["moves"][move4]["sp_defense_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's sp. defense has been decreased!")

                                if i == "speed_decrease":
                                    s = pokemon[name]["moves"][move4]["speed_decrease"]
                                    attack -= s
                                    await ctx.send(f"{member.name} used **{move4}**. Their pokemon's speed has been decreased!")

                        else:
                            if defense >= attack2:
                                if defense >= (attack2 + (movedamage2 // 2)):
                                    damage2 = random.randint(movedamage2 // 6, movedamage2 // 5)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                                else:
                                    damage2 = random.randint(movedamage2 // 5, movedamage2 // 4)
                                    hp -= damage2
                                    await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")

                            else:
                                damage2 = random.randint(attack2-defense, (attack2-defense + 10))
                                hp -= damage2
                                await ctx.send(f"The {member.name} used **{moveai4}** on {ctx.author.name}'s pokemon! {member.name} did **{damage2}** damage to {ctx.author.name}'s hp!")


                            if hp <= 0:
                                await ctx.send(f"{member.name} has won the battle!")
                                return

                            if defense2 >= attack:
                                if defense2 >= (attack + (movedamage // 5)):
                                    damage1 = random.randint(movedamage // 6, movedamage // 5)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                                else:
                                    damage1 = random.randint(movedamage // 5, movedamage // 4)
                                    hp2 -= damage1
                                    await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            else:
                                damage1 = random.randint(attack-defense2, (attack-defense2 + 10))
                                hp2 -= damage1
                                await ctx.send(f"{ctx.author.name} used **{move4}** on the {member.name}! {ctx.author.name} did **{damage1}** damage to their hp!")

                            if hp2 <= 0:
                                await ctx.send(f"{ctx.author.name} has won the battle!")
                                return

                        field = Image.open("field.png")
                        url1 = pokemon[name]["image"]
                        url2 = pokemon[name2]["image"]
                        page1 = requests.get(url1)
                        page2 = requests.get(url2)
                        f_ext1 = os.path.splitext(url1)[-1]
                        f_ext2 = os.path.splitext(url2)[-1]
                        f_name1 = 'poke1{}'.format(f_ext1)
                        f_name2 = 'poke2{}'.format(f_ext2)

                        with open(f_name1, 'wb') as f:
                            f.write(page1.content)

                        with open(f_name2, 'wb') as f:
                            f.write(page2.content)

                        pokeimage1 = Image.open("poke1.png")
                        pokeimage2 = Image.open("poke2.png")
                        pokeimage1 = pokeimage1.convert("RGBA")
                        pokeimage2 = pokeimage2.convert("RGBA")
                        field = field.convert("RGBA")
                        pokeimage1.thumbnail((267, 262))
                        pokeimage2.thumbnail((235, 223))
                        pokeimage1 = ImageOps.mirror(pokeimage1)
                        field.paste(pokeimage1, (129, 314), pokeimage1)
                        field.paste(pokeimage2, (638, 147), pokeimage2)
                        field.save("fieldready.png", format="png")
                        file = discord.File("fieldready.png", filename="fieldready.png")
                        em = discord.Embed(title=f"Ai duel of {ctx.author.name}\n\n", description=f"{emoji} {name} Hp: {hp} ({ctx.author.name}'s pokemon)\n{emoji2} {name2} Hp: {hp2} ({member.name}'s pokemon)", color=ctx.author.color)
                        em.set_image(url="attachment://fieldready.png")
                        await ctx.send(file=file, embed=em)

                    specialdo1 = []
                    specialdo2 = []

                else:
                    await ctx.send("That's not a valid move! Try again!")

    #duel error
    @duel.error
    async def duel_error(self, ctx, error):
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

def setup(client):
    client.add_cog(Duel(client))
