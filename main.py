import discord
from manage.settings import bot_connect_data
from manage.set_default_data import ManageDB


settings = bot_connect_data()
bot = discord.Bot()

class PlayerManager(ManageDB):
    def __init__(self, user_id):
        self.user_id = user_id
    
    def check_user(self, name, table):
        return self.get_one_data(f'SELECT id FROM {table} WHERE name = "{name}"')

    def user_register(self, name, lvl):
        table = 'pers'
        if not self.check_user(name, table):
            querry = f"INSERT INTO {table} (name, user, lvl) VALUES ('{name}', '{self.user_id}', '{lvl}')"
            ans = self.data_setter(querry)
            pers_id = self.get_one_data(f'SELECT id FROM {table} WHERE user = "{self.user_id}" and name = "{name}"')
            return {'ans': ans, 'id':pers_id[0]}
        else:
            return None

    def user_class_update(self, pers_class, pers_id):
        table = 'pers'
        pers_data = self.get_one_data(f'SELECT * FROM {table} WHERE id = "{pers_id}" and user = "{self.user_id}"')
        if pers_data:
            if self.get_one_data(f'SELECT class_id FROM {table} WHERE id = "{pers_id}"')[0] == None:
                class_id = self.check_user(pers_class, 'class')[0]
                querry = f'UPDATE pers SET class_id = "{class_id}" WHERE id = "{pers_id}";'
                ans = self.data_setter(querry)
                return {'ans': ans}
            else:
                return None
        else:
            return None


class MyModal(discord.ui.Modal):
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
                view=MyView(pers_id=create_ans['id'])
                )
        else:
            await interaction.response.send_message('[-] allready exist')

class MyView(discord.ui.View):
    def __init__(self, pers_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.pers_id = pers_id

    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a Flavor!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
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

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "register", description = "Register your new pers")
async def modal_slash(ctx: discord.ApplicationContext):
    modal = MyModal(title='modal', user_id=ctx.author.id)
    await ctx.send_modal(modal)

bot.run(settings['token'])


















# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

# @bot.command()
# async def register(ctx, *arg):
#     if arg:
#         pers = PlayerManager(name = arg[0])
#         ans = pers.user_register()
#         await ctx.reply(ans)
#     else:
#         await ctx.reply('[-] lost arg (press $register name)')

# @bot.command()
# async def test(ctx, *arg):

#     async def button_callback(interaction):
#         await interaction.response.edit_message(content='Button clicked!', view=None)

#     button = Button(custom_id='button1', label='WOW button!', style=discord.ButtonStyle.green)
#     button.callback = button_callback

#     await ctx.send('Hello World!', view=View(button))

# bot.run(settings['token'])
