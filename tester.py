elif e == "Items":
    usableCategories = ["Battle Items", "Medicine", "Berries"]

    try:
        msg = await self.client.wait_for(
            "message",
            timeout = 60,
            check = lambda message: message.author == ctx.author
                           and message.channel == ctx.channel
            )

        if msg:
            x = msg.content

            for i in users[str(ctx.author.id)]["bag"]:
                if x.lower() == i.lower():
                    checker1 = True
                    item1 = i

            if checker1 == True:
                for l in items:
                    for o in items[l]:
                        if item1.lower() == o.lower():
                            category = i   

                if users[str(ctx.author.id)]["bag"][i] == 1:
                    del users[str(ctx.author.id)]["bag"][i]

                else:
                    users[str(ctx.author.id)]["bag"][i] -= 1

    except asyncio.TimeoutError:
        return