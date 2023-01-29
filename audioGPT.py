import openai
from gtts import gTTS;
from playsound import playsound;
from simple_chalk import chalk;

# Define chave de API e modelo
API_KEY = "MINHA_CHAVE_DE_API"
openai.api_key = API_KEY
model = "text-davinci-003"

#Define o texto de entrada
print(chalk.blue("*"*35))
print(chalk.yellow('Pergunte qualquer coisa à IA: '))
print(chalk.blue("*"*35))
texto = input()

#Cria o body da solicitação e envia a requisição
response = openai.Completion.create(
    prompt = texto,
    model = model,
    max_tokens = 100
)

audio = 'audio.mp3'
language = 'pt-br'

# Transforma a reposta da solicitação em áudio
sp = gTTS(
  text = response.choices[0].text,
  lang = language
)

# Salva e toca o áudio com a resposta da API
sp.save(audio)
playsound(audio)