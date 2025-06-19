from abc import ABC, abstractmethod
from json import dump, load
from os.path import join
from pathlib import Path

from loguru import logger

from ..meta import config_path, config_version
from ..types import VersionType
from ..utils import Version
from ..utils.file_utils import check_directory


class BaseConfig(ABC):
    @property
    @abstractmethod
    def config(self) -> dict:
        raise NotImplementedError

    @property
    @abstractmethod
    def config_file_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def parse_config(self, data: dict) -> None:
        raise NotImplementedError

    def load_config(self) -> None:
        check_directory(config_path, create_if_not_exist=True)
        file_path = join(config_path, self.config_file_name)
        if Path(file_path).is_file():
            self.parse_config(load(open(file_path, "r", encoding="utf-8")))
        else:
            self.save_config()

    def save_config(self) -> None:
        check_directory(config_path, create_if_not_exist=True)
        file_path = join(config_path, self.config_file_name)
        dump(self.config, open(file_path, "w", encoding="utf-8"), indent=4)


class Config(BaseConfig):
    config_version: str = "1.0.0"
    remember_me: bool = False
    callsign: str = ""
    email: str = ""
    hoppie_code: str = ""
    log_level: str = "TRACE"

    def __init__(self):
        pass

    def parse_config(self, data: dict) -> None:
        self.__dict__ = data

    @property
    def config_file_name(self) -> str:
        return "config.json"

    def load_config(self) -> None:
        super().load_config()
        version = Version(self.config_version)
        res = config_version.check_version(version)
        if res == VersionType.MAJOR_UNMATCH or res == VersionType.MINOR_UNMATCH:
            logger.critical(
                f"Config version error! Require {config_version} but got {version}")
            exit(-1)
        if res == VersionType.PATCH_UNMATCH:
            logger.warning(
                f"Config version not match! Require {config_version} but got {version}")

    @property
    def config(self) -> dict:
        data = {
            "config_version": self.config_version,
            "remember_me": self.remember_me,
            "callsign": self.callsign,
            "email": self.email,
            "hoppie_code": self.hoppie_code,
            "log_level": self.log_level
        }
        if not data["remember_me"]:
            data["callsign"] = ""
            data["email"] = ""
            data["hoppie_code"] = ""
        return data


config = Config()
