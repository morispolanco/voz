import streamlit as st
import pyaudio
import wave
import speech_recognition as sr

def transcribir_audio(audio):
    r = sr.Recognizer()
    
    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        
    try:
        texto = r.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo transcribir el audio"
    except sr.RequestError as e:
        return f"Error al solicitar la transcripción: {e}"

def main():
    st.title("Transcriptor de mensajes de voz")
    st.write("¡Bienvenido al Transcriptor de mensajes de voz!")
    st.write("Esta aplicación te permite grabar mensajes de voz y transcribirlos en texto.")
    
    grabar = st.button("Grabar")
    
    if grabar:
        # Configurar la grabación de audio
        fs = 44100  # Frecuencia de muestreo
        duracion = 5  # Duración de la grabación en segundos
        
        # Inicializar PyAudio
        p = pyaudio.PyAudio()
        
        # Abrir el stream de audio
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True, frames_per_buffer=1024)
        
        # Leer los datos del stream de audio
        frames = []
        for i in range(0, int(fs / 1024 * duracion)):
            data = stream.read(1024)
            frames.append(data)
        
        # Detener la grabación
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # Guardar el audio en un archivo WAV
        archivo_wav = "audio.wav"
        wf = wave.open(archivo_wav, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        # Transcribir el audio
        texto_transcrito = transcribir_audio(archivo_wav)
        
        st.success("Transcripción completada:")
        st.write(texto_transcrito)

if __name__ == "__main__":
    main()
