#!/usr/bin/env python3
#-*- coding: utf8 -*-
import time
import discord
import asyncio
import json
import logging
import logging.config
import re
import random
import datetime
import copy
import traceback
import sys
import configparser
import signal
import os
import name_list 
from collections import Counter
from discord.ext import commands

client = discord.Client()
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('rules'):
        rules = 'rules1, rules2, rules3, rulesEn'.format(message)
        if message.content.startswith('rules1'):
            rules = 'Здесь запрещены:  любого рода оскорбления и нападки; спам и реклама; шок-контент; политические материалы'.format(message)
        if message.content.startswith('rules2'):
            rules = 'Желательно: None'.format(message)
        if message.content.startswith('rules3'):
            rules = 'Если кто-то нарушает правила или как-то иначе портит времяпровождение других на сервере, желательно позвать @Админ.Позвать кого-то можно, поставив @ и начав печатать ник того, кого вы хотите позвать. Затем нужно выбрать нужного человека в появившемся сверху меню.\nНа сервере есть бот. Для отображения команд напишите (желательно в #botspam) "commands".\nВыделить текст курсивом -  "*" (звёздочка текст звёздочка); жирным - "**" \n'.format(message)
        if message.content.startswith('rulesEn'):
            rules = 'Attacks and humiliation also spam and advertising; shock content; political materials is prohibited If someone break the rules advisable to call @Админ. To call somebody - put @ and start typing the one you want to call. Then you need to select the right person from the menu above. There is a bot, on this server, To display the command post (preferably in #botspam) "commands". Highlight text in italics - "*" ; bold - "**"'.format(message)
        await client.send_message(message.channel, rules)
        return 
    if message.content.startswith('hi'):
        msg = 'hi {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        return
    if message.content.startswith('who'):
        msg = 'I am the Pl, {0.author.mention} .'.format(message)
        await client.send_message(message.channel, msg)
        return
    if message.content.startswith('youknowme'):
        msg = 'You are {0.author.mention} :)'.format(message)
        await client.send_message(message.channel, msg)
        return
    if message.content.startswith('commands'):
        await client.send_message(message.channel, 'hi, who, guess, russianroulette, aboutyou, youknowme, yourname'.format(message))
        return
    if message.content.startswith('russianroulette'):        
        answer = random.randint(1, 2)        
        if int(2) == answer:
            await client.send_message(message.channel, 'You win!')            
        else:
            await client.send_message(message.channel, 'Sorry. You are dead.')
        return
    if message.content.startswith('aboutyou'):
        sequence = ['I am Pl','I am bot','I am managed by WhiteLed','I writed on python programm language']
        about=random.choice(sequence).format(message)
        await client.send_message(message.channel, about)
        return
    if message.content.startswith('yourname'):
        aboutP=random.choice(['P l', 'p_l', 'pl', 'ПП', 'Пурпурная', 'Пурпур', 'Пеёль','Пёль','Пеель','PL', 'Pl', 'PP', 'P', 'Purple', 'Pur', 'Prl', 'Prla','Peerl','Purple']).format(message)
        await client.send_message(message.channel, aboutP)
        return
    if message.content.startswith('guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 5')
        def guess_check(m):
            return m.content.isdigit()
        guess = await client.wait_for_message(timeout=10.0, author=message.author, check=guess_check)
        answer = random.randint(1, 5)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
            return
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))
            return

@client.event  
async def on_ready():
    print('there')
    print(client.user.name)
    return
    
client.run('client')

#bywhiteled
