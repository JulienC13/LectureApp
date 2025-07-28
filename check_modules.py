# check_modules.py
import requests
import pydub
import whisper

print("OK – requests v", requests.__version__)
print("OK – pydub   v", pydub.__version__)
print("OK – whisper module:", whisper.__name__)
