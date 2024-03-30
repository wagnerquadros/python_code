import pyaudio
import numpy as np

# Configurações do PyAudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Abrir o stream de áudio
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Gravando...")

# Loop para capturar áudio continuamente
try:
    while True:
        # Ler dados do stream de áudio
        data = stream.read(CHUNK)
        # Converter os dados para array numpy
        audio_data = np.frombuffer(data, dtype=np.int16)
        # Aqui você pode fazer o processamento dos dados de áudio, como reconhecimento de fala ou análise de espectrograma
        # Por exemplo, você pode usar bibliotecas como SpeechRecognition para reconhecimento de fala
        # Ou bibliotecas como matplotlib e librosa para visualização e análise de áudio
except KeyboardInterrupt:
    print("Parando a gravação...")

# Fechar o stream de áudio
stream.stop_stream()
stream.close()

# Terminar o PyAudio
p.terminate()
