import telebot
from telebot import types
import random
import emoji
import time
import threading
from telebot.types import ReplyKeyboardRemove

a = telebot.types.ReplyKeyboardRemove()
bot = telebot.TeleBot("7413275094:AAGUxkTns9ZDr66hTjWsa3SphBvTLubRE68")
image1 = "https://beebom.com/wp-content/uploads/2023/05/Gojo-vs-sukuna.jpg?w=628"
image2 = "https://beebom.com/wp-content/uploads/2023/06/GVS-224.jpg?quality=75&strip=all"
image3 = "https://i.pinimg.com/736x/d0/1b/2d/d01b2d6300b092abca93f36165395cfc.jpg"
gif1 = "https://i.pinimg.com/originals/df/05/a1/df05a177c8f9311bd7439fe26d9a7acd.gif"
gif2 = "https://c.tenor.com/b_HeThKej1EAAAAC/tenor.gif"
image4 = "https://qph.cf2.quoracdn.net/main-qimg-6a6ee6d63075704a08c023475b5d8ad0"
image5 = "https://beebom.com/wp-content/uploads/2023/09/sukuna-without-an-arm-heavily-injured-in-his-fight-against-gojo.jpg?w=750"
image6 = "https://static.wikia.nocookie.net/jujutsu-kaisen/images/3/3c/Yoshinobu_Gakuganji_%28Anime%29.png/revision/latest?cb=20201025154546"
gif3 = "https://giffiles.alphacoders.com/221/221258.gif"
gif4 = "https://i.pinimg.com/originals/59/da/0b/59da0badb6c8a4d9b58aeb37ccafc101.gif"
image8 = "https://img.spoilerhat.com/img/?url=https://cdn.onepiecechapters.com/file/CDN-M-A-N/jjk_221_gain_006.png"
gif5 = "https://media1.tenor.com/m/nQAUm8WI1rsAAAAC/gojo-run.gif"
gif6 = "https://i.pinimg.com/originals/14/fc/7d/14fc7d1120735dd8e2064a38913ea339.gif"
gif7 = "https://media1.tenor.com/m/wFIKhcjvszYAAAAC/gojo-satoru-breathing.gif"
gif8 = "https://media.tenor.com/eu4_AX5o5swAAAAM/prison-realm-jujutsu-kaisen.gif"
image9 = "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/09/playing-with-the-death-jujutsu-kaisen.jpg"
image10 = "https://a.storyblok.com/f/178900/960x540/b27a92a6d0/gojo-prism-realm.jpg/m/filters:quality(95)format(webp)"
image11 = "https://img.spoilerhat.com/img/?url=https://cdn.onepiecechapters.com/file/CDN-M-A-N/jjk_221_gain_010.png"
image12 = "https://img.spoilerhat.com/img/?url=https://cdn.onepiecechapters.com/file/CDN-M-A-N/jjk_221_gain_012.png"
loot_items = [
    {"name": "морква", "hp": 20, "cost": 5},
    {"name": "рамен", "hp": 50, "cost": 10},
    {"name": "чіпсікі з цибулею", "hp": 30, "cost": 7},
    {"name": "попкорн", "hp": 100, "cost": 15},
    {"name": "борщик", "hp": 150, "cost": 20},
    {"name": "хліб", "hp": 50, "cost": 10},
    {"name": "щавєл🙄", "hp": 30, "cost": 5},
    {"name": "шоколадка", "hp": 80, "cost": 18},
    {"name": "енергос", "hp": -20, "attack": 20, "cost": 10},
]

speed = 0
m = 0
last_interaction = {}

def remind_user(chat_id):
    global last_interaction
    if chat_id in last_interaction:
        last_interaction_time = last_interaction[chat_id]
        if (time.time() - last_interaction_time) >= 1:
            bot.send_message(chat_id, "Швидше!")
            del last_interaction[chat_id]

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
        self.sukuna = Enemy("Рьомен Сукуна", 1100, 160)
        self.hanami = Enemy("Ханамі", 600, 90)
        self.jogo = Enemy("Джоґо", 700, 100)
        self.choso = Enemy("Чосо", 800, 100)
        self.geto = Enemy("Гето Сугуру", 950, 110)
        self.current_enemy_index = 0

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

def create_reply_keyboard6():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Захист')
    btn2 = types.KeyboardButton('Удар')
    markup.add(btn1, btn2)
    return markup

def create_reply_keyboard4(random_items):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    for item in random_items:
        btn = types.KeyboardButton(f'{item["cost"]}💰 {item["name"]} + {item["hp"]} хп')
        markup.add(btn)
    return markup

def create_reply_keyboard5():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Далі --->')
    markup.add(btn1)
    return markup

def create_reply_keyboard7():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Далі -->')
    markup.add(btn1)
    return markup

def create_reply_keyboard8():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('⬆️')
    markup.add(btn1)
    return markup

def create_reply_keyboard9():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Далі ->')
    markup.add(btn1)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    game.player = Player("Ґоджо")
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}! Це текстовий RPG по магічній битві! Щоб почати, нажміть 'Грати'.", reply_markup=create_reply_keyboard())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global speed
    if message.text == "Грати":
        bot.send_message(message.chat.id, f"Арка:")
        bot.send_message(message.chat.id, f"**ІНЦИДЕНТ В ШИБУЇ**")
        bot.send_photo(message.chat.id, image6)
        bot.send_message(message.chat.id, "-----------------------------------\nТи - найсильніший маг сьогодення Годжо Сатору, повинен знищити короля проклять Рьомен Сукуну! Але на шляху до цього тобі можуть завадити інші вищі прокляття, тож постарайся виграти цю тисячолітню війну!", reply_markup=create_reply_keyboard5())
    elif message.text == "Далі --->":
        bot.send_message(message.chat.id, f"Місце знаходження: метро", reply_markup=a)
        bot.send_message(message.chat.id, f"Ти маєш: {game.player.hp} здоров'я, {game.player.dmg} сили, {game.player.coins} гривень, {game.player.superhit} супер ударів. Твоє ім'я Ґоджо.")
        bot.send_message(message.chat.id, f"Ти зустрічаєш Ханамі, Джоґо і Чосо\nВсі вони - на стороні гето Сугуру")
        bot.send_message(message.chat.id, f"Джоґо - це страшне прокляття, що народилося від страху людей щодо вулканів. Цей страх є дуже великим, тому джого є одне з найсильніших проклять. Має вулканічну здібність, володіє розширенням володінь")
        bot.send_message(message.chat.id, f"Чосо - має здібності крові, один з картини смерті, був вдалим експерименом давнього прокляття з ім'ям Кендзяку щодо схрещення людей з прокляттями")
        bot.send_message(message.chat.id, f"Ханамі нападає!", reply_markup=create_reply_keyboard7())
        
    elif message.text == "Далі -->":
        while game.hanami.hp >= 0:
            time.sleep(0.8)
            game.player.hp -= game.hanami.dmg
            bot.send_message(message.chat.id, f"Ханамі атакує Ґоджо! удар - {game.hanami.dmg}\n хп Ґоджо - {game.player.hp}", reply_markup=types.ReplyKeyboardRemove())
            game.hanami.hp -= game.player.dmg
            time.sleep(0.8)
            bot.send_message(message.chat.id, f"Ґоджо б'є у відповідь! удар - {game.player.dmg}\n хп Ханамі - {game.hanami.hp}")
            game.jogo.hp -= game.player.dmg
            time.sleep(0.8)
            bot.send_message(message.chat.id, f"Джоґо атакує Ґоджо! удар - {game.jogo.dmg}\n хп Ґоджо - {game.player.hp}")
            game.player.hp -= game.jogo.dmg
            time.sleep(0.8)
            bot.send_message(message.chat.id, f"Ґоджо б'є у відповідь! удар - {game.player.dmg}\n хп Джоґо - {game.jogo.hp}")
        if game.hanami.hp <= 0:
            bot.send_document(message.chat.id, gif3)
            game.hanami.hp -= 200
            bot.send_message(message.chat.id, "Ханамі вдовбало у стінку")
            bot.send_message(message.chat.id, "--Ханамі переможено!-- ти отримуєш +20 монет")
            game.player.coins += 20
            random_items = random.sample(loot_items, 4)
            bot.send_message(message.chat.id, "Вибери предмет:", reply_markup=create_reply_keyboard4(random_items))
            bot.send_message(message.chat.id, f"Ти маєш {game.player.coins}💰")
    elif message.text.startswith(tuple(f'{item["cost"]}💰 {item["name"]}' for item in loot_items)):
        selected_item = None
        for item in loot_items:
            if message.text.startswith(f'{item["cost"]}💰 {item["name"]}'):
                selected_item = item
                break
        
        if selected_item and game.player.coins >= selected_item["cost"]:
            if selected_item["name"] == "енергос":
                game.player.hp += selected_item["hp"]
                if game.player.hp <= 0:
                    game.player.hp = 0
                    bot.send_message(message.chat.id, f"Ти випив {selected_item['name']} і втратив все здоров'я. Ти помер!", reply_markup=create_reply_keyboard6())
                else:
                    game.player.dmg += selected_item["attack"]
                    game.player.coins -= selected_item["cost"]
                    bot.send_message(message.chat.id, f"Ти випив {selected_item['name']} і отримав +{selected_item['attack']} до урону, але втратив {selected_item['hp']} хп. Твоє здоров'я тепер {game.player.hp}", reply_markup=create_reply_keyboard6())
            else:
                game.player.hp += selected_item["hp"]
                game.player.coins -= selected_item["cost"]
                bot.send_message(message.chat.id, f"Ти з'їв {selected_item['name']}-у і отримав {selected_item['hp']} хп. Твоє здоров'я тепер {game.player.hp}", reply_markup=create_reply_keyboard6())
        else:
            bot.send_message(message.chat.id, "Недостатньо грошей або ти витратив всі пурпурові.", reply_markup=create_reply_keyboard6())

        bot.send_document(message.chat.id, gif4)
        bot.send_message(message.chat.id, f"Чосо атакує ззаду!", reply_markup=create_reply_keyboard6())
    if message.text == "Захист":
        bot.send_message(message.chat.id, f"Це було правильним рішенням, Ти захистився і отримав 0 урону!")
        bot.send_message(message.chat.id, f"-Джоґо тікає!-")
        bot.send_message(message.chat.id, "Махіто перетворив занадто велику кількість людей на проклядих духів, тому вам варто зупинити цей процес, що ви виберете?0\n 1. Знищити прокляття / 2. Використати розширення володінь", reply_markup=types.ReplyKeyboardRemove())
    if message.text == "Удар":
        game.player.hp -= 100
        bot.send_message(message.chat.id, f"Спроба атакувати виявилася невдалою, -100 хп")
        bot.send_message(message.chat.id, "Махіто перетворив занадто велику кількість людей на проклядих духів, тому вам варто зупинити цей процес, що ви виберете?0\n 1. Знищити прокляття / 2. Використати розширення володінь", reply_markup=types.ReplyKeyboardRemove())
    if message.text == '2':
        bot.send_message(message.chat.id, f"Свідомість людей не здатна витримати ваше розширення володінь, але якщо використати його на 0,2 секунди, то людський мозок не встигне отримати негативний ефект вашого рв. У вас є 0,2 сек на знищення усіх проклять. Швидше!", reply_markup=create_reply_keyboard8())
        
    elif message.text == "⬆️":
        chat_id = message.chat.id
        last_interaction[chat_id] = time.time()
        speed += 8.5
        bot.send_message(message.chat.id, f"Швидкість {speed}")
        threading.Timer(1.1, remind_user, [chat_id]).start()

        if speed >= 100:
            bot.send_document(message.chat.id, gif7)
            bot.send_message(message.chat.id, f"Всі прокляття перебиті.. Все у крові, але люди збережені.")
            bot.send_message(message.chat.id, f"Хтось був ззаду!")
            bot.send_message(message.chat.id, f"Це.. Гето Сугуру! Чи.. Як це може бути? Він повинен бути мертвим.")
            bot.send_message(message.chat.id, f"Це не правда, це не може бути він")
            bot.send_message(message.chat.id, f"*Гето*: тільки не злякайся", parse_mode="Markdown")
            bot.send_photo(message.chat.id, image9)
            bot.send_message(message.chat.id, f"Перед тобою - Тюремне царство. Через хвилину воно може тебе запечатати")
            bot.send_message(message.chat.id, f"Доведеться битись", reply_markup=create_reply_keyboard9())
    if message.text == 'Далі ->':
        bot.send_message(message.chat.id, f"Ти маєш: {game.player.hp} здоров'я, {game.player.dmg} сили, {game.player.coins} гривень, {game.player.superhit} супер ударів.", reply_markup=ReplyKeyboardRemove())
        while game.player.hp >= 50:
            time.sleep(0.8)
            bot.send_message(message.chat.id, f"Гето атакує Ґоджо! удар - {game.hanami.dmg}\n хп Ґоджо - {game.player.hp}")
            game.player.hp -= game.geto.dmg
            time.sleep(0.8)
            bot.send_message(message.chat.id, f"Ґоджо б'є у відповідь! удар - {game.player.dmg}\n хп Гето - {game.hanami.hp}")
            game.geto.hp -= game.player.dmg
        bot.send_message(message.chat.id, f"В тебе занадто мало хп щоб битись, тебе запечатали! Тобі доведеться почекати ")
        bot.send_document(message.chat.id, gif8)
        for i in range(1, 61):
            time.sleep(1)
            if i % 10 == 0:
                bot.send_message(message.chat.id, f"{i}..")
                if i == 30:
                    bot.send_photo(message.chat.id, image10)
                bot.send_photo(message.chat.id, image8)
                bot.send_message(message.chat.id, f"Ти потрібен. Тебе розпечатав янгол, але у ту ж секунду ти телепортнувсь прямо до сукуни")
                bot.send_message(message.chat.id, f"То почнеться ж бій")
                bot.send_photo(message.chat.id, image11)
                bot.send_message(message.chat.id, f"ФІОЛЕТОВИЙ")
                bot.send_photo(message.chat.id, image12)

    if message.text == '1':
        bot.send_message(message.chat.id, f"Ви не встигаєте знищити прокляття, всі люди вмерли, ви програли\n Хочте ще раз?", reply_markup=create_reply_keyboard())


bot.infinity_polling()
