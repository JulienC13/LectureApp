# txt_writer.py

class TxtWriter:
    """
    Agrège les textes et écrit dans un .txt en streaming.
    - évite de garder tout en mémoire.
    """
    def __init__(self, output_path: str):
        self.out = open(output_path, "w", encoding="utf-8")

    def write(self, text: str):
        """Ajoute le texte au fichier."""
        self.out.write(text + "\n")

    def close(self):
        self.out.close()
