import sys
sys.path.insert(1, '/Users/ruslan/workspace/dis_bot')

import discord
from db_manager.settings import bot_connect_data
from db_manager.operations_db import PlayerManager


settings = bot_connect_data()
bot = discord.Bot()

class PlayerRegiester(discord.ui.Modal):
    def __init__(self, user_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.user_id = user_id
        self.add_item(discord.ui.InputText(label="Input name of pers"))
        self.add_item(discord.ui.InputText(label="Input pers lvl"))

    async def callback(self, interaction: discord.Interaction):
        pers = PlayerManager(user_id=self.user_id)
        create_ans = pers.user_register(
            name=self.children[0].value, 
            lvl=self.children[1].value
            )
        print(create_ans)
        if create_ans['ans']:
            embed = discord.Embed(title=create_ans['ans'], color=discord.Colour.blue())
            embed.add_field(name="Name", value=self.children[0].value)
            embed.add_field(name="lvl", value=self.children[1].value)
            await interaction.response.send_message(
                embeds=[embed], 
                view= ThraceDropdown(pers_id=create_ans['id']))
        else:
            await interaction.response.send_message('[-] allready exist')

class ClassDropdown(discord.ui.View):
    def __init__(self, pers_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.pers_id = pers_id

    @discord.ui.select(
        placeholder = "Choose a class!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label='паладин',
            ),
            discord.SelectOption(
                label='охотник',
            ),
            discord.SelectOption(
                label='разбойник',
            ),
            discord.SelectOption(
                label='воин',
            ),
            discord.SelectOption(
                label='жрец',
            ),
            discord.SelectOption(
                label='шаман',
            ),
            discord.SelectOption(
                label='маг',
            ),
            discord.SelectOption(
                label='чернокнижник',
            ),
            discord.SelectOption(
                label='друид',
            ),
            discord.SelectOption(
                label='рыцарь смерти',
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        pers = PlayerManager(user_id=interaction.user.id)
        ans = pers.user_class_update(pers_class=select.values[0], pers_id=self.pers_id)
        print(ans)
        if ans:
            await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")
        else:
            await interaction.response.send_message('[-] class allready exist')

class ThraceDropdown(discord.ui.View):
    def __init__(self, pers_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.pers_id = pers_id

    @discord.ui.select(
        placeholder = "Choose a thrace!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label='альянс',
            ),
            discord.SelectOption(
                label='орда',
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        pers = PlayerManager(user_id=interaction.user.id)
        ans = pers.user_thrace_update(pers_thrace=select.values[0], pers_id=self.pers_id)
        print(ans)
        
        if ans:
            await interaction.response.send_message(
                f"За { 'орду' if select.values[0] == 'орда' else select.values[0]}!\
                \n\n Please choose the class of your pers",
                view = ClassDropdown(pers_id=self.pers_id)
            )
        else:
            await interaction.response.send_message('[-] thrace allready exist')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "register", description = "Register your new pers")
async def modal_slash(ctx: discord.ApplicationContext):
    modal = PlayerRegiester(title='modal', user_id=ctx.author.id)
    await ctx.send_modal(modal)

bot.run(settings['token'])
