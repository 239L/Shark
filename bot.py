# -*- coding: utf-8 -*-

import os
import re
import discord

from discord.ext import commands
from discord import utils
import random
from datetime import datetime

token = os.environ['TOKEN']

client = commands.Bot(command_prefix=".")



@client.event
async def on_message(msg):
    now = datetime.now()
    mins = now.minute
    secs=now.second
    hours=now.hour
    if (mins == 34 and (secs == 34 or secs==1 or secs==59)) or ((secs==10 or secs==45 or secs==1) and (mins==15 and hours==16)) or (hours==23 and mins==15 and (secs==20 and secs==44) ) and not msg.author.bot:
        await msg.channel.send("<a:bananan:890261338780233758> не мешайте мне дрочить!")
    
    if msg.content.startswith(".shoot") or msg.content.startswith(".grab") or msg.content.startswith(".eat") or msg.content.startswith(".bb") or msg.content.startswith(".бб") or msg.content.startswith(".съем") or msg.content.startswith(".take"):
        await msg.delete()
    list = []
    if ".h" == msg.content or ".help"==msg.content:

        embed=discord.Embed(
            title="Emoji list",
            description="Here's the list of emojis available"
        )

        a=0
        i=0
        b=0
        for e in client.guilds:

            for em in e.emojis:
                a += 1
                i+=1
                if a==25:
                    await msg.channel.send(embed=embed)
                    b += 1
                    embed=discord.Embed(
                        title=f"Page {b}"
                    )
                    embed.clear_fields()
                    a=0

                embed.add_field(
                    name=em.name,
                    value=em,
                )

        await msg.channel.send(embed=embed)

    message=msg.content.lower()
    if (secs<=10&&(message.content.startswith("не хочу") or message.content.endswith("а я не хочу") or message.content.startswith("я не хочу"))):
        await msg.channel.send("ну ты щас, конечно, кринжанулся <:shark1:924014769743220756>")
    text = re.compile("da+$|да+$|дa+$|dа+$")
    da=re.compile("da+[%&',;=)(}\[/\]/{?$\":./\-/+\\//]+$|дa+[%&',;=)(}\[/\]/{?$\":./\-/+\\//]+$")
    da2=re.compile("d+\s+a+$|д+\s+a+$")
    if (text.search(message) or da.search(message) or da2.search(message)) and not msg.author.bot:

        await msg.channel.send("пизда <:moai:875355368623046667>")
    text2=re.compile("н+е+т+$")
    if text2.search(msg.content) and not msg.author.bot:
        await msg.channel.send("пидора ответ <:moairev:875357014350512168>")
    if msg.content.startswith(":") and msg.content.endswith(":"):
        emoji=msg.content[1:-1]
        for e in client.guilds:
            em=utils.get(e.emojis, name=emoji)
            if em:
                await msg.channel.send(str(em))
                #await msg.channel.send(em.name)
                await msg.delete()
                break
    await client.process_commands(msg)


@client.command(name='ok', aliases=['ок', 'к', 'k', 'kk'])
async def ok(ctx):
    await ctx.send("<:aok:924016637382893578><:lmao2:924016508936531999>")

class switch(object):
    def __init__(self, value):
        self.value = value  # значение, которое будем искать
        self.fall = False   # для пустых case блоков

    def __iter__(self):     # для использования в цикле for
        """ Возвращает один раз метод match и завершается """
        yield self.match
        raise StopIteration

    def match(self, *args):
        """ Указывает, нужно ли заходить в тестовый вариант """
        if self.fall or not args:
            # пустой список аргументов означает последний блок case
            # fall означает, что ранее сработало условие и нужно заходить
            #   в каждый case до первого break
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False


@client.command(name='grab', aliases=['take', 'съем', 'eat'])
async def grab(ctx):
    for case in switch(random.randint(1, 4)):
        if case(1):
            await ctx.send("<:handrev:897143171899850822><:catxok:924017382589100062><:hand1:897142817846087701>")
            break
        if case(2):
            await ctx.send("<:handrev:897143171899850822><a:frok:924017176216739900><:hand1:897142817846087701>")
            break
        if case(3):
            await ctx.send("<:handrev:897143171899850822><a:hehehe:887343779030384650><:hand1:897142817846087701>")
            break
        if case(4):
            await ctx.send("<:handrev:897143171899850822><a:bounce:924016841431609376><:hand1:897142817846087701>")
            break

@client.command(name='shoot', aliases=['бб', 'bb'])
async def shoot(ctx, emoji:str):
    for e in client.guilds:
        try:
            em = utils.get(e.emojis, name=emoji)
            if em:
                await ctx.send("<:ishoot:924069869882863656>"+str(em))
        except Exception as e:
            await ctx.send("The emote doesn't exist in the pool")

@client.command(name='nya', aliases=['3', 'з'])
async def nya(ctx):
    await ctx.send("<a:3x3:882236999564677210>")

client.run(token)
