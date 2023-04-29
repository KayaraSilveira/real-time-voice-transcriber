from django.urls import path

from . import views

app_name = 'voicetranslator'

urlpatterns = [
    path('', views.home, name='home'),
    path('transcription', views.render_transcription, name='transcription'),
    path('transcribe', views.transcribe, name='transcribe'),
]