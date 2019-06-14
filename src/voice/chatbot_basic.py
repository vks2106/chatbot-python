# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import pyttsx3

# intializing speach module
voice = pyttsx3.init()

# Create a new instance of a ChatBot
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    # logic_adapters=[
    #    {
    #        'import_path': 'chatterbot.logic.BestMatch'
    #    },
    #    {
    #       'import_path': 'chatterbot.logic.LowConfidenceAdapter',
    #       'threshold': 0.65,
    #       'default_response': 'I am sorry, but I do not understand.'
    #    }
    # ],
    trainer='chatterbot.trainers.ListTrainer',
    # trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    silence_performance_warning=True
)

# Train the chat bot with a few responses
# bot.train([
#    'how are you',
#    'I am good',
#    'Thats great',
#    'what are up to lately',
#    'nothing much just roaming'])

# Train the chat bot with a few responses
'''bot.train([
    'who are you',
    'I am Elisa',
    'I am Elisa',
    'no you are not',
    'yes I am, what can you do about that'])'''

# Train the chat bot with a few responses
# bot.train([
#    'how are you',
#    'I am good',
#    'Thats great',
#    'what are up to lately',
#    'nothing much just roaming'])

# bot.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations")


# Get a response for some unexpected input
print("Hai im Elisa a chatBot designed and Trained By Hari")
inpu = ""
conv = ""

while (inpu != "hehe"):
    inpu = input("Hari: ")
    if (inpu == "shutup"):
        break
    conv = bot.get_response(inpu)
    # bot.train([inpu,conv]);
    print("Elisa: ", conv)
    voice.say(conv)
    voice.runAndWait()

print("Elisa: shutting down ")