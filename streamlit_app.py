import streamlit as st
import speech_recognition as sr

def transcribir_audio(archivo):
    r = sr.Recognizer()
    
    with sr.AudioFile(archivo) as source:
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
    st.write("Esta aplicación te permite transcribir mensajes de voz en texto.")
    
    archivo = st.file_uploader("Selecciona un archivo de audio", type=["wav", "mp3"])
    
    if archivo is not None:
        texto_transcrito = transcribir_audio(archivo)
        
        st.success("Transcripción completada:")
        st.write(texto_transcrito)

if __name__ == "__main__":
    main()
