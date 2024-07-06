import telebot
from telebot import types
from random import randint, random
import emoji

bot = telebot.TeleBot("7413275094:AAGUxkTns9ZDr66hTjWsa3SphBvTLubRE68")
image1 = "https://beebom.com/wp-content/uploads/2023/05/Gojo-vs-sukuna.jpg?w=628"
image2 = "https://beebom.com/wp-content/uploads/2023/06/GVS-224.jpg?quality=75&strip=all"
image3 = "https://i.pinimg.com/736x/d0/1b/2d/d01b2d6300b092abca93f36165395cfc.jpg"
gif1 = "https://i.pinimg.com/originals/df/05/a1/df05a177c8f9311bd7439fe26d9a7acd.gif"
gif2 = "https://media1.tenor.com/m/b_HeThKej1EAAAAC/sukuna-domain-expansion.gif"
image4 = "https://qph.cf2.quoracdn.net/main-qimg-6a6ee6d63075704a08c023475b5d8ad0"
image5 = "https://beebom.com/wp-content/uploads/2023/09/sukuna-without-an-arm-heavily-injured-in-his-fight-against-gojo.jpg?w=750"

class Character:
    def __init__(self, name, hp, dmg, coins):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.coins = coins

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 1000, 150, 20)
        self.superhit = 3

class Enemy(Character):
    def __init__(self, name, hp, dmg):
        super().__init__(name, hp, dmg, 0)

class Game:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.state = "start"
        self.stage = 1

    def start_game(self, player_name):
        self.player = Player(player_name)
        self.enemy = Enemy("Рьомен Сукуна", 1100, 160)
        self.state = "battle"
        self.stage = 1

    def next_stage(self):
        self.stage += 1
        if self.stage == 2:
            self.player.dmg += 30
            self.enemy.dmg += 30
        elif self.stage == 3:
            self.player.dmg += 40
            self.enemy.dmg += 40

game = Game()

def create_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Грати')
    markup.add(btn1)
    return markup

def create_reply_keyboard2():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('інвентар')
    btn2 = types.KeyboardButton('бій')
    markup.add(btn1, btn2)
    return markup

def create_reply_keyboard3():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton('захист')
    btn2 = types.KeyboardButton('удар')
    btn3 = types.KeyboardButton('🫸🔴🔵🫷🤌🫴⏤͟͟🟣(3 на гру)')
    markup.add(btn1, btn2, btn3)
    return markup

def create_reply_keyboard4():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('5💰 морква + 20 хп')
    btn2 = types.KeyboardButton('10💰 рамен + 50 хп')
    btn3 = types.KeyboardButton('7💰 чіпсікі з цибулею + 30 хп')
    btn4 = types.KeyboardButton('15💰 попкорн + 100 хп')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}! Це текстовий RPG по магічній битві! Щоб почати, нажміть 'Грати'.", reply_markup=create_reply_keyboard())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Грати":
        game.start_game("Ґоджо Сатору")
        bot.send_message(message.chat.id, "Ґоджо Сатору - найсильніший маг, успадкувавший Безмежність і Шість очей.", reply_markup=create_reply_keyboard2())
        bot.send_message(message.chat.id, "Рьомен Сукуна - небезпечний проклятий маг, який жив 1000 років тому.")
        bot.send_message(message.chat.id, f"Ти маєш: {game.player.hp} здоров'я, {game.player.dmg} сили, {game.player.coins} гривень, {game.player.superhit} супер ударів. Твоє ім'я Ґоджо.")
        bot.send_photo(message.chat.id, image2)
    elif message.text == "бій" and game.state == "battle":
        bot.send_message(message.chat.id, "Етап бою", reply_markup=create_reply_keyboard3())
    elif message.text == "інвентар" and game.state == "battle":
        bot.send_message(message.chat.id, "Оберіть їжу:", reply_markup=create_reply_keyboard4())
    elif game.state == "battle":
        if message.text == "удар":
            player_attack = randint(game.player.dmg - 40, game.player.dmg)
            enemy_attack = randint(game.enemy.dmg - 10, game.enemy.dmg)
            game.enemy.hp -= player_attack
            game.player.hp -= enemy_attack
            bot.send_photo(message.chat.id, image1)
            bot.send_message(message.chat.id, f"Ґоджо атакує Сукуну - {player_attack} хп Сукуні")
            bot.send_photo(message.chat.id, image3)
            bot.send_message(message.chat.id, f"Сукуна атакує Ґоджо - {enemy_attack} хп Ґоджо")
            check_battle_state(message)
        elif message.text == "🫸🔴🔵🫷🤌🫴⏤͟͟🟣(3 на гру)" and game.player.superhit > 0:
            player_attack = 310
            enemy_attack = randint(game.enemy.dmg - 10, game.enemy.dmg)
            game.enemy.hp -= player_attack
            game.player.hp -= enemy_attack
            game.player.superhit -= 1
            bot.send_message(message.chat.id, f"КРАСНІ СІНІ - ПУРПОРОВИЙ - {player_attack} хп Сукуні!")
            bot.send_document(message.chat.id, gif1)
            bot.send_message(message.chat.id, f"Сукуна атакує Ґоджо - {enemy_attack} хп Ґоджо")
            bot.send_document(message.chat.id, gif2)
            check_battle_state(message)
        elif message.text == "захист":
            bot.send_message(message.chat.id, emoji.emojize(":game_die:"))
            dice_result = randint(1, 6)
            enemy_attack = randint(game.enemy.dmg - 10, game.enemy.dmg)
            if dice_result <= 3:
                bot.send_message(message.chat.id, "Перший удар у твою сторону був незначним.")
                player_attack = randint(game.player.dmg - 40, game.player.dmg)
                game.enemy.hp -= player_attack
                bot.send_message(message.chat.id, f"Ґоджо атакує Сукуну - {player_attack} хп Сукуні")
            else:
                game.player.hp -= enemy_attack
                bot.send_message(message.chat.id, f"Удар був занадто сильним - {enemy_attack} хп Ґоджо")
            check_battle_state(message)
        elif message.text.startswith('5💰') and game.player.coins >= 5:
            game.player.hp += 20
            game.player.coins -= 5
            bot.send_message(message.chat.id, f"Ти з'їв моркву і отримав 20 хп. Твоє здоров'я тепер {game.player.hp}", reply_markup=create_reply_keyboard3())
        elif message.text.startswith('10💰') and game.player.coins >= 10:
            game.player.hp += 50
            game.player.coins -= 10
            bot.send_message(message.chat.id, f"Ти з'їв рамен і отримав 50 хп. Твоє здоров'я тепер {game.player.hp}", reply_markup=create_reply_keyboard3())
        elif message.text.startswith('7💰') and game.player.coins >= 7:
            game.player.hp += 30
            game.player.coins -= 7
            bot.send_message(message.chat.id, f"Ти з'їв чіпсікі з цибулею і отримав 30 хп. Твоє здоров'я тепер {game.player.hp}", reply_markup=create_reply_keyboard3())
        elif message.text.startswith('15💰') and game.player.coins >= 15:
            game.player.hp += 100
            game.player.coins -= 15
            bot.send_message(message.chat.id, f"Ти з'їв попкорн і отримав 100 хп. Твоє здоров'я тепер {game.player.hp}", reply_markup=create_reply_keyboard3())
        else:
            bot.send_message(message.chat.id, "Недостатньо грошей або ти витратив всі пурпурові.", reply_markup=create_reply_keyboard3())

def check_battle_state(message):
    if game.enemy.hp <= 0:
        bot.send_message(message.chat.id, "Ґоджо переміг Сукуну! Хочеш ще?", reply_markup=create_reply_keyboard())
        bot.send_photo(message.chat.id, image5)
    elif game.player.hp <= 0:
        bot.send_message(message.chat.id, "Ти програв! Хочеш ще раз?", reply_markup=create_reply_keyboard())
        bot.send_photo(message.chat.id, image4)
    elif game.enemy.hp <= 800 and game.stage == 1:
        bot.send_message(message.chat.id, "Етап 1 завершено!")
        game.next_stage()
        bot.send_message(message.chat.id, f"Ти маєш: {game.player.hp} здоров'я, {game.player.dmg} сили, {game.player.coins} гривень, {game.player.superhit} супер ударів. Твоє ім'я Ґоджо.", reply_markup=create_reply_keyboard2())
    elif game.enemy.hp <= 200 and game.stage == 2:
        bot.send_message(message.chat.id, "Етап 2 завершено!")
        game.next_stage()
        bot.send_message(message.chat.id, f"Ти маєш: {game.player.hp} здоров'я, {game.player.dmg} сили, {game.player.coins} гривень, {game.player.superhit} супер ударів. Твоє ім'я Ґоджо.", reply_markup=create_reply_keyboard2())
    else:
        bot.send_message(message.chat.id, f"Здоров'я Ґоджо: {game.player.hp}")
        bot.send_message(message.chat.id, f"Здоров'я Сукуни: {game.enemy.hp}")

bot.infinity_polling()
