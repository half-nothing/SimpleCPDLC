import time

from loguru import logger
from python_cpdlc.cpdlc import CPDLC

from src.config import config


class CPDLCManager:
    def __init__(self):
        start_time = time.time()
        logger.trace("Initializing CPDLC")
        self._cpdlc = CPDLC()
        logger.trace(f"CPDLC initialized on {time.time() - start_time:.2f}s")

    def set_client(self):
        self._cpdlc.set_email(config.email)
        self._cpdlc.set_logon_code(config.hoppie_code)
        self._cpdlc.set_callsign(config.callsign)
        self._cpdlc.initialize_service()

    def reset_client(self):
        self._cpdlc.reset_service()
        self.set_client()

    @property
    def cpdlc(self) -> CPDLC:
        return self._cpdlc
