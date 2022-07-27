#  RODAR NO PYTHON 3.6 PARA FACILITAR O IMPORT DO PYAUDIO

import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
import pyttsx3
import os

# Converse com ela em inglês
# Para fazer uma pesquisa no youtube diga search youtube for + o que pesquisar, no google diga search for + o que pesquisar

class AssitenteVirtual:
    def __init__(self, assistente_nome='Júpiter', usuario='Leonardo'):
        self.usuario = usuario
        self.assistente = assistente_nome  # Defini os nomes tanto da assitente quanto do usuário, por padrão a assistente se chama júpiter e o usuário Leonardo

        # Definindo configurações
        self.engine = pyttsx3.init()  # Inicia a engine que converte texto para voz
        self.reconhecer_voz = sr.Recognizer()

        self.dados_da_voz = ''

    def engine_falar(self, texto):  # Esse método é para a fala da assistente

        self.engine.say(texto)
        self.engine.runAndWait()

    def gravar_audio(self, fale=''):

        with sr.Microphone() as source:
            if fale:
                print('\033[32mrecording...\033[m')
                self.engine_flr(fale)

            audio = self.reconhecer_voz.listen(source, 5, 5)  # variavel que armazena os dados do audio
            print('looking at the data base')
            try:
                self.dados_da_voz = self.reconhecer_voz.recognize_google(audio)  # converte audio para texto

            except sr.UnknownValueError:  # Erro de reconhecimento
                print('\033[31m\n')
                self.engine_flr('Sorry Boss, I did not get what you said. Can you please repeat?')
                print('\033[m')

            except sr.RequestError:  # Erro de conexão
                self.engine_flr('Sorry Boss, my server is down')

            print(">>", self.dados_da_voz.lower())  # Entrando com o texto em minúsculo, para facilitar o reconhecimento
            self.dados_da_voz = self.dados_da_voz.lower()

            return self.dados_da_voz.lower()

    def engine_flr(self,
                   audio_str):  # Tratamento de áudio usando o gTTS, que é uma ferramenta de interface com a ferramenta da Google de transformar texto em audio
        numeros_indice = []

        tts = gTTS(text=audio_str, lang='en')

        while True:  # Verificando se o número gerado já não ocupa outro índice
            naleatorio = random.randint(1, 2000)  # Gerando números aleátorios para dar índices aos audios

            if naleatorio not in numeros_indice:  # Quebra o loop se o número não tiver sido gerado
                break

        arquivo_de_audio = 'audio' + str(naleatorio) + '.mp3'

        tts.save(arquivo_de_audio)

        playsound.playsound(arquivo_de_audio)
        print(self.assistente + ':', audio_str)
        os.remove(arquivo_de_audio)

        return

    def verificando_existencia(self, termos):  # Função para identificar se o termo existe

        for termo in termos:
            if termo in self.dados_da_voz:
                return True

    def responder(self, dados_da_voz):
        if self.verificando_existencia(['hey', 'hi', 'hello', 'oi', 'holla']):
            cumprimentos = [f'Hi {self.usuario}, what are we doing today?',
                            'Hi Boss, how can I help you?',
                            'Hi Boss, what do you need?']

            cumprimento = random.choice(cumprimentos)
            self.engine_flr(cumprimento)

        if self.verificando_existencia(['search for']) and 'youtube' not in dados_da_voz:  # Pesquisando no google
            termo_da_busca = dados_da_voz.split("for")[-1]
            url = "http://google.com/search?q=" + termo_da_busca
            webbrowser.get().open(url)
            self.engine_flr("here is what I found for " + termo_da_busca + 'on google')

        if self.verificando_existencia(['search youtube for', 'look on youtube for']):  # Pesquisando no youtube
            termo_da_busca = dados_da_voz.split("for")[-1]
            url = "http://www.youtube.com/results?search_query=" + termo_da_busca
            webbrowser.get().open(url)
            self.engine_flr("Here is what i found for" + termo_da_busca + 'on youtube')

        if self.verificando_existencia(['what is your age', "what's your age", 'whats your age', 'how old are you']):
            self.engine_flr('I have 3 days, im younger than artificial intelligence bachalor in federal university of goiania')



assistente = AssitenteVirtual(usuario='Artur')
print(f'Olá, sou a {assistente.assistente}, e posso te auxiliar a pesquisar coisas no google ou yotube')

while True:

    dados_voz = assistente.gravar_audio('im listening you...')
    assistente.responder(dados_voz)

    if assistente.verificando_existencia(['bye', 'goodbye', 'seeyou', 'see you later', 'see you']):
        assistente.engine_flr("Have a nice day! Good bye!")
        break


# Código da assistente em português

# Eu fiz um código com uma assinstente que falava e reconhecia portugûes, todavia o sistema fica bem precário desse modo,
# pois ela tem dificuldade no reconhecimento e muitas vezes não entende o que é dito

