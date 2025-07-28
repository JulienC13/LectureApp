# audible_client.py

import os
import requests

class IAudioSource:
    """Interface pour accéder à une source audio."""
    def get_stream(self) -> bytes:
        raise NotImplementedError

class AudibleClient(IAudioSource):
    """
    Classe responsable de l’authentification et du streaming depuis Audible.
    - SOLID : respecte l’interface IAudioSource (principe de substitution).
    - DI : injection de la config via le constructeur.
    """
    def __init__(self, client_id: str, client_secret: str):
        self.token = self._authenticate(client_id, client_secret)

    def _authenticate(self, cid, secret) -> str:
        """Obtient un token OAuth2."""
        resp = requests.post(
            "https://api.audible.com/auth",
            data={"client_id": cid, "client_secret": secret}
        )
        resp.raise_for_status()
        return resp.json()["access_token"]

    def get_stream(self) -> bytes:
        """Retourne le binaire audio du livre complet."""
        headers = {"Authorization": f"Bearer {self.token}"}
        resp = requests.get("https://api.audible.com/v1/books/ID/stream", headers=headers, stream=True)
        resp.raise_for_status()
        return resp.raw.read()
