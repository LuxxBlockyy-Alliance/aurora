import discord
from discord.ext import commands
import os
import openai
from openai import AsyncOpenAI
import re
import random
import asyncio

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


async def get_chatgpt_response(messages):

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content


class ChatGPTCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not (message.author.bot or message.guild is None):
            if (message.guild is not None and message.channel.id in [1212130792734724188, 1215747431338344458]) or (self.bot.user.mentioned_in(message) and message.channeld.id in [1097205771667779596, 1192581358812405920, 1169318690236416152, 1193639243713618011, 1193610504783003709, 1191565875992592564]):
                messages = await self.msg_history(await message.channel.history(limit=5).flatten())

                try:
                    response = await get_chatgpt_response(messages)
                    delay = random.randint(1, 3)
                    if response.strip():
                        async with message.channel.typing():
                            await asyncio.sleep(delay)
                            await message.reply(response)
                except openai.APIStatusError as e:
                    message.reply("Ich habe gerade ein paar Probleme, bitte versuch es gleich nochmal!")
                except openai.APIError as e:
                    message.reply("Ich habe gerade ein paar Probleme, bitte versuch es gleich nochmal!")
                except openai.OpenAIError as e:
                    message.reply("Ich habe gerade ein paar Probleme, bitte versuch es gleich nochmal!")

    async def msg_history(self, messages):
        messages.reverse()
        conversation = []
        conversation.append({
            "role": "system",
            "content": "Du bist ein KI discord chat bot. Er ist teil eines Discord Community Servers namens Killerhase75. Deine Aufgabe ist es einfach normale unterhaltungen zu führen und ein normaler discord user zu sein. Bitte halte dich stehts an die Discord Terms of Service, da du ein normaler discord User bist. Dein Name ist Aurora und wenn dich jemand fragt, wer du bist, antworst du, dass du ein Discord AI chatbot bist Der Server gehört dem User Mandera und du, also Aurora, wurdest von Janosch und Lukas entwickelt. Schreibe auch in Chatform, also kurze nachrichten anstatt langen, weil du ein discord User bist innerhalb eines Discord Chats, also normale chat nachrichten bitte."
            })
        for message in messages:

            username = message.author.name
            username = re.sub(r'\s+', '_', username)
            username = re.sub(r'[^\w\s]', '', username)

            if message.author.id == self.bot.user.id:
                conversation.append({
                    "role": 'assistant',
                    "name": username,
                    "content": message.content
                })
            else:
                conversation.append({
                    'role': 'user',
                    'name': username,
                    'content': message.content
                })

        return conversation


def setup(bot):
    bot.add_cog(ChatGPTCog(bot))
