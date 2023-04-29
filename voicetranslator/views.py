import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'voicetranslator/home.html')

def listen():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)

        try:
            speech = microfone.recognize_google(audio,language='pt-BR')
        except sr.UnknownValueError:
            speech = "-------"
        except sr.RequestError as e:
            speech = "Erro ao realizar a requisicao; {0}".format(e)

        return speech


def transcribe(request):

    if request.method == 'GET':
        transcription = listen()

        data = {
            'transcription': transcription
        }

        return JsonResponse(data)

def render_transcription(request):
    return render(request, 'voicetranslator/transcription.html')
