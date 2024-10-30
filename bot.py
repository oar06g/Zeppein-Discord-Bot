import logging
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="zeppein.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
  print(f"Bot is ready! Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  log_channel = discord.utils.get(ctx.guild.text_channels, name="mod-log")
  if log_channel:
    await log_channel.send(f"{member.mention} has been kicked. Reason: {reason or 'No reason provided'}")
  await ctx.send(f"{member.mention} has been kicked. Reason: {reason or 'No reason provided'}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  log_channel = discord.utils.get(ctx.guild.text_channels, name="mod-log")
  if log_channel:
    await log_channel.send(f"{member.mention} has been banned. Reason: {reason or 'No reason provided'}")
  await ctx.send(f"{member.mention} has been banned. Reason: {reason or 'No reason provided'}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  try:
    member_name, member_discriminator = member.split('#')
  except ValueError:
    await ctx.send("Please provide a user in the format `name#discriminator`.")
    return

  async for ban_entry in ctx.guild.bans():
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      log_channel = discord.utils.get(ctx.guild.text_channels, name="mod-log")
      if log_channel:
        await log_channel.send(f"{user.mention} has been unbanned.")
      await ctx.send(f"{user.mention} has been unbanned.")
      return

  await ctx.send("Couldn't find user.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def list_bans(ctx):
  banned_list = []
  async for ban_entry in ctx.guild.bans():
    user = ban_entry.user
    banned_list.append(f"{user.name}#{user.discriminator}")

  if banned_list:
    await ctx.send(f"Banned users: {', '.join(banned_list)}")
  else:
    await ctx.send("No users are banned.")


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG, root_logger=True)