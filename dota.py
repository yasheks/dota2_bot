import telebot
import random


bot = telebot.TeleBot("token")
heroess = ["Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe", "Bane", "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster", "Bristleback", "Broodmother", "Centaur Warrunner", "Chaos Knight", "Chen", "Clinkz", "Clockwerk", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dazzle", "Death Prophet", "Disruptor", "Doom", "Dragon Knight", "Drow Ranger", "Earth Spirit", "Earthshaker", "Elder Titan", "Ember Spirit", "Enchantress", "Enigma", "Faceless Void", "Grimstroke", "Gyrocopter", "Huskar", "Invoker", "Io", "Jakiro", "Juggernaut", "Keeper of the Light", "Kunkka", "Legion Commander", "Leshrac", "Lich", "Lifestealer", "Lina", "Lion", "Lone Druid", "Luna", "Lycan", "Magnus", "Mars", "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Naga Siren", "Nature's Prophet", "Necrophos", "Night Stalker", "Nyx Assassin", "Ogre Magi", "Omniknight", "Oracle", "Outworld Destroyer", "Pangolier", "Phantom Assassin", "Phantom Lancer", "Phoenix", "Puck", "Pudge", "Pugna", "Queen of Pain", "Razor", "Riki", "Rubick", "Sand King", "Shadow Demon", "Shadow Fiend", "Shadow Shaman", "Silencer", "Skywrath Mage", "Slardar", "Slark", "Sniper", "Spectre", "Spirit Breaker", "Storm Spirit", "Sven", "Techies", "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw", "Tinker", "Tiny", "Treant Protector", "Troll Warlord", "Tusk", "Underlord", "Undying", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Visage", "Void Spirit", "Warlock", "Weaver", "Windranger", "Winter Wyvern", "Witch Doctor", "Wraith King", "Zeus"]
hero = random.choice(heroess)

@bot.message_handler(commands=["start"])
def help(message):
    bot.send_message(message.chat.id, "Привет пользователь, это ТГ бот, который создал Яша, используй команду /help, чтобы узнать что умеет этот бот=)")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "используй команду /pick для того, чтобы выбрать кого пикнуть в доту\nвыберите команду /heroes чтобы посмотреть всех персонажей в dota2\nиспользуй команду /start для перезапуска бота")

@bot.message_handler(commands=["heroes"])
def heroes(message):
    bot.send_photo(message.chat.id, "https://dota2.ru/img/heroes/" + hero.lower().replace(" ", '_') + "/icon.jpg")
    bot.send_message(message.chat.id, "Abaddon, Alchemist, Ancient Apparition, Anti-Mage, Arc Warden, Axe, Bane, Batrider, Beastmaster, Bloodseeker, Bounty Hunter, Brewmaster, Bristleback, Broodmother, Centaur Warrunner, Chaos Knight, Chen, Clinkz, Clockwerk, Crystal Maiden, Dark Seer, Dark Willow, Dazzle, Death Prophet, Disruptor, Doom, Dragon Knight, Drow Ranger, Earth Spirit, Earthshaker, Elder Titan, Ember Spirit, Enchantress, Enigma, Faceless Void, Grimstroke, Gyrocopter, Huskar, Invoker, Io, Jakiro, Juggernaut, Keeper of the Light, Kunkka, Legion Commander, Leshrac, Lich, Lifestealer, Lina, Lion, Lone Druid, Luna, Lycan, Magnus, Mars, Medusa, Meepo, Mirana, Monkey King, Morphling, Naga Siren, Nature's Prophet, Necrophos, Night Stalker, Nyx Assassin, Ogre Magi, Omniknight, Oracle, Outworld Destroyer, Pangolier, Phantom Assassin, Phantom Lancer, Phoenix, Puck, Pudge, Pugna, Queen of Pain, Razor, Riki, Rubick, Sand King, Shadow Demon, Shadow Fiend, Shadow Shaman, Silencer, Skywrath Mage, Slardar, Slark, Sniper, Spectre, Spirit Breaker, Storm Spirit, Sven, Techies, Templar Assassin, Terrorblade, Tidehunter, Timbersaw, Tinker, Tiny, Treant Protector, Troll Warlord, Tusk, Underlord, Undying, Ursa, Vengeful Spirit, Venomancer, Viper, Visage, Void Spirit, Warlock, Weaver, Windranger, Winter Wyvern, Witch Doctor, Wraith King, Zeus.")

@bot.message_handler(commands=["pick"])
def pick(message):
    global hero

    bot.send_message(message.chat.id, "я думаю, что лучше тебе пикнуть: " + hero)

    hero = random.choice(heroess)

@bot.message_handler()
def anymessage(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "здарова")
    elif message.text.lower() == "новый год будет?":
        bot.send_message(message.chat.id, "нет")
        bot.send_photo(message.chat.id, "https://www.meme-arsenal.com/memes/a2dd37b1b9fac89b7beea376803d5eba.jpg")

bot.infinity_polling()
