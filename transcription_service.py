# transcription_service.py

import whisper

class TranscriptionService:
    """
    Utilise OpenAI Whisper v1.2 pour la transcription.
    - Chargement unique du modèle (principe de responsabilité unique).
    - Appels asynchrones possibles (à étendre).
    """
    def __init__(self, model_size: str = "base"):
        # Changements en v1.2 : meilleures performances de décodage :contentReference[oaicite:1]{index=1}
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_chunk) -> str:
        """
        Transcrit un chunk (pydub.AudioSegment).
        - retourne le texte brut.
        """
        # conversion en fichier temporaire
        audio_chunk.export("tmp.wav", format="wav")
        result = self.model.transcribe("tmp.wav")
        return result["text"]
