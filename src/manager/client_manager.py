from threading import Lock, Thread
from typing import Optional

from httpx import Client
from loguru import logger


class ClientManager:
    def __init__(self):
        self._client: Optional[Client] = None
        self._lock: Lock = Lock()
        Thread(target=lambda: self.client, daemon=True).start()

    @property
    def client(self):
        with self._lock:
            if self._client is None:
                logger.debug("Creating httpx client")
                self._client = Client(verify=False)
                logger.debug("Httpx client created")
            return self._client
