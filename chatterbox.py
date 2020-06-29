from chatterbot import ChatBot   #this imports chatbot
from chatterbot.trainers import ListTrainer  # method to train the chatbot

bot = ChatBot('MyChatBot')
trainer = ListTrainer(bot)
# bot.set_trainer(ListTrainer)       #set the trainer
conversation = open('intents.json','r').readlines()
trainer.train(conversation)

print('Type something to begin...')
while True:
    message = input('You:')
    if message.strip()!= 'Bye':
        reply = bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break