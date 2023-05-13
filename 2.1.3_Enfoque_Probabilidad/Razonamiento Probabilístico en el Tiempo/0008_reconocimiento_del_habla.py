

import speech_recognition as sr

# Inicializar el reconocedor de voz
r = sr.Recognizer()

# Utilizar el micrófono como fuente de audio
mic = sr.Microphone()

# Escuchar el audio desde el micrófono

with mic as source:
    
    audio = r.listen(source)


# Realizar reconocimiento de voz utilizando el servicio de reconocimiento de Google
texto_transcrito = r.recognize_google(audio, language = 'ES')

# Imprimir el resultado de la transcripción
print(f'Has dicho: {texto_transcrito}')
