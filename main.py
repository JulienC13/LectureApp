# main.py

from audible_client import AudibleClient
from audio_chunker import AudioChunker
from transcription_service import TranscriptionService
from txt_writer import TxtWriter

def main():
    # 1) Config Audible
    client_id = "<TON_CLIENT_ID>"
    client_secret = "<TON_CLIENT_SECRET>"
    audible = AudibleClient(client_id, client_secret)

    # 2) Découpage
    chunker = AudioChunker(audible, chunk_sec=60)
    chunks = chunker.get_chunks()

    # 3) Transcription
    transcriber = TranscriptionService(model_size="base")
    
    # 4) Writer
    writer = TxtWriter("livre_transcrit.txt")

    print("Début de la transcription…")
    index = 0
    while not chunks.empty():
        chunk = chunks.get()
        index += 1
        print(f"  → Transcription du chunk #{index}")
        try:
            text = transcriber.transcribe(chunk)
            writer.write(text)
        except Exception as e:
            print(f"    ! Erreur sur chunk #{index}:", e)
            # ici tu peux ajouter un retry ou log dans un fichier
    writer.close()
    print("Terminé – fichier créé : livre_transcrit.txt")

if __name__ == "__main__":
    main()
