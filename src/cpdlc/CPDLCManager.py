from asyncio import run
from threading import Thread
from typing import Callable, Optional

from python_cpdlc import CPDLC

from src.config import config


class CPDLCManager:
    def __init__(self):
        self._cpdlc: Optional[CPDLC] = None
        self._create_callback: list[Callable[[], None]] = []

    def add_create_callback(self, callback: Callable[[], None]):
        self._create_callback.append(callback)

    def create_client(self):
        self._cpdlc = CPDLC(config.email, config.hoppie_code)
        self._cpdlc.set_callsign(config.callsign)
        for callback in self._create_callback:
            callback()
        Thread(target=self._cpdlc.start_poller, daemon=True).start()

    async def recreate_client(self):
        await self._cpdlc.poller.stop()
        self.create_client()

    @property
    def cpdlc(self) -> CPDLC:
        if self._cpdlc is None:
            raise ValueError("CPDLC has not been created yet")
        return self._cpdlc
