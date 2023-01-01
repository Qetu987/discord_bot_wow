from bot.db_manager.secret import token

def connect_data():
    return {
        'host': "localhost",
        'user': "root",
        'password': "Gfhf_1_ljrc",
        'database': "discord_bot",
    }

def bot_connect_data():
    return {
        'token': token,
        'bot': 'Pupsinator_bot',
        'id': 1051186929896534086,
        'prefix': '$'
    }
