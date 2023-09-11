import streamlit as st
import sounddevice as sd
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
        
        # Grabar audio
        audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
        sd.wait()  # Esperar a que termine la grabación
        
        # Guardar el audio en un archivo WAV
        archivo_wav = "audio.wav"
        sd.write(archivo_wav, audio, fs)
        
        # Transcribir el audio
        texto_transcrito = transcribir_audio(archivo_wav)
        
        st.success("Transcripción completada:")
        st.write(texto_transcrito)

if __name__ == "__main__":
    main()
