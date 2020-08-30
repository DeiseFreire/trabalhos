# parte do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# speech recognition
import speech_recognition as sr
# speech synthesis
import pyttsx3
bot = ChatBot('Logo')  # inicia o bot
speak = pyttsx3.init('sapi5')
def Speak(text):
    speak.say(text)
chats = ['hi', 'hello', 'how are you?', 'I am fine.', 'thanks']  # conversas
bot.set_trainer(ListTrainer)  # define o método de treinamento
bot.train(chats)  # define a lista de conversas
r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)  # se adaptar ao ruído
print('Say something: ')
while True:
    try:
        audio = r.listen(s)  # escutar
speech = r.recognize_google(audio)  # fala
response = bot.get_response(speech)
# request=input('Enter a text: ')
print('You: ', speech)
print('Bot: ', response)
Speak(response)
except:
print('Sorry. ')
