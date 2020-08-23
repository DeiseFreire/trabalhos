# parte do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# speech recognition
import speech_recognition as sr
# speech synthesis
import pyttsx3
bot=ChatBot('Logo') # inicia o bot
chats=['hi','hello','how are you?','I"me fine.','thanks'] # conversas
bot.set_trainer(ListTrainer) # define o método de treinamento
bot.train(chats) # define a lista de conversas 
while True:
request=input('Enter a text: ')
print(bot.get_response(request))    
