# audio_chunker.py

import io
from pydub import AudioSegment
from queue import Queue
from audible_client import IAudioSource

class AudioChunker:
    """
    Découpe l’audio en morceaux de X secondes.
    - back-pressure : on stocke les chunks dans une Queue.
    - retry possible si chunk corrompu.
    """
    def __init__(self, source: IAudioSource, chunk_sec: int = 60):
        self.source = source
        self.chunk_sec = chunk_sec

    def get_chunks(self) -> Queue:
        data = self.source.get_stream()
        audio = AudioSegment.from_file(io.BytesIO(data), format="mp3")
        q = Queue()
        for i in range(0, len(audio), self.chunk_sec * 1000):
            chunk = audio[i:i + self.chunk_sec * 1000]
            q.put(chunk)
        return q
