from email.mime import image
import tkinter as tk
from tkinter.tix import IMAGETEXT
from typing import Self
from openai import Image
import speech_recognition as sr
import pyttsx3
import webbrowser

from PIL import Image, ImageTk

recognizer = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
voice_id = 0
engine.setProperty('voice', voices[voice_id].id)

def ouvir():
    with sr.Microphone() as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return ""
        except sr.RequestError:
            print("Não foi possível reconhecer a fala. Verifique sua conexão com a internet.")
            return ""

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def responder(pergunta):
    if "qual é o seu nome" in pergunta:
        falar("Meu nome é Sexta Feira.")
    elif "como você está" in pergunta:
        falar("Estou funcionando perfeitamente, obrigado por perguntar!")
    elif "jarvis" in pergunta:
        falar("Sim, como posso ajudar?")
    elif "tocar música" in pergunta:
        falar("Claro! Estou abrindo o YouTube.")
        webbrowser.open("https://www.youtube.com/results?search_query=acdc")
    else:
        falar("Desculpe, não entendi a pergunta.")

def iniciar_assistente():
    while True:
        comando = ouvir().lower()
        if "tina" in comando:
            responder(comando)
        elif "parar" in comando:
            falar("Até a próxima!")
            break
        
        
        
        
        
if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Sexta Feira")
    janela.geometry("400x300")

    img = Image.open('gif.gif')
    minhatela = ImageTk.PhotoImage(img)

    fundo = tk.Label(janela, image=minhatela)
    fundo.place(relwidth=1, relheight=1)

    rotulo = tk.Label(janela, text="Sexta Feira", font=("Arial", 16))
    rotulo.pack(pady=20)

    botao_iniciar = tk.Button(janela, text="Iniciar Assistente", command=iniciar_assistente)
    botao_iniciar.pack()

    

    janela.mainloop()

