from os.path import expandvars, join
from .utils.version import Version

config_version: Version = Version([1, 0, 0])
config_path: str = "config"
app_version: Version = Version([1, 0, 0])
app_name: str = "SimpleCPDLC"
appdata_path: str = join(expandvars("%APPDATA%"), app_name)
