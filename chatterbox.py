from chatterbot import ChatBot   #this imports chatbot
from chatterbot.trainers import ListTrainer  # method to train the chatbot

bot = ChatBot('MyChatBot')
trainer = ListTrainer(bot)
# bot.set_trainer(ListTrainer)       #set the trainer
conversation = open('chats.txt','r').readlines()
trainer.train(conversation)

print('Greetings From Grocery Shop...Type Hello to begin')
while True:
    message = input('You:')
    if message.strip()!= 'Bye':
        reply = bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break