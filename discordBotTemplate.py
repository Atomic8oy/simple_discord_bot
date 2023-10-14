import interactions
from interactions import slash_command, SlashContext

# Your bot's Activity // remove "activity=" if you dont want any
bot = interactions.Client(activity="ACTIVITY")

# Creating your first slash command
# name is your command's name [/command-name] 
@slash_command(name="my_command", description="my_Command's Description") 
async def my_command_function(ctx: SlashContext): # - make sure to change [your command's name]_function here -
    await ctx.send(f"Hello world") # Your command's output is going here
    print("Someone used /my_Command") # This part is for log its not necessary



@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.start("YOUR-BOT-TOKEN") # Make sure to change this part to your bot's token
