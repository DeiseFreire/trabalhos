# 1 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - INTRODUÇÃO
# https://www.youtube.com/watch?v=81U0HvPJQqY&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba

-*- coding: utf-8 -*-
# importando os módulos do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import speech_recognition as sr

bot = ChatBot('Jarvis', read_only)
"""
bot.set_trainer(ListTrainer)  # definir treinamento
for _file in os.listdir('chats'):  # percorrer todos os arquivos em chats
    lines = open('chats/' + _file, 'r').readlines()  # vamos ler linhas
bot.train(lines)"""
r = sr.Recognizer()
with
    sr.Microphone() as s:
r.adjust_for_ambient_noise(s)
while True:
    audio = r.listen(s)
    speech = r.recognize_google(audio, language='pt')
    print('Você disse: ', speech)
