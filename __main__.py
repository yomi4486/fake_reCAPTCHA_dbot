import discord,create_image,os
from discord import app_commands
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
APPLICATION_ID = os.environ.get("ID")

client = discord.Client(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    # この関数はBotの起動準備が終わった際に呼び出されます
    print(f'Ready: {client.user}')
    await tree.sync()#スラッシュコマンドを同期

@tree.command(name="help",description="Botの説明を表示します。")
async def test_command(interaction: discord.Interaction):
    embed = discord.Embed(title="使用方法",description="「@mention タイトル」というメッセージに最大9個の画像を添付してください。")
    embed.add_field(name='概要', inline=False ,value='')
    embed.add_field(name='コマンド', inline=False ,value='')
    embed.add_field(name='`/help`', value='Botの説明を表示します。')
    await interaction.response.send_message(embed=embed,ephemeral=True)

@client.event
async def on_message(message:discord.Message):
    if f"<@{APPLICATION_ID}>" in message.content:
        if message.attachments:
            title = message.content.replace(f"<@{APPLICATION_ID}> ","").replace(f"<@{APPLICATION_ID}>","").replace("\n","")
            if len(title) == 0:
                await message.reply("テーマが指定されていません！\n使い方を知りたい場合は、`/help`を実行してください！",silent=True,delete_after=5)
            files = message.attachments
            
            await create_image.image_process(base_text=title,files=files)
            msg = await message.reply(content="<a:load:1308731656038907924> Creating...")
            await msg.edit(content="",attachments=[discord.File('./result.png')])
            return
        else:
            await message.reply("画像が1枚も添付されていません！",silent=True,delete_after=5)

client.run(TOKEN)