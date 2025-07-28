@echo off
set NUITKA_CACHE_DIR_CCACHE=D:\WorkSpace\python\SimpleCPDLC\build\cache\gcc
set NUITKA_CACHE_DIR_CLCACHE=D:\WorkSpace\python\SimpleCPDLC\build\cache\msvc
set NUITKA_CACHE_DIR_DOWNLOADS=D:\WorkSpace\python\SimpleCPDLC\build\cache\download
set NUITKA_CACHE_DIR_BYTECODE=D:\WorkSpace\python\SimpleCPDLC\build\cache\byte
set NUITKA_CACHE_DIR_DLL_DEPENDENCIES=D:\WorkSpace\python\SimpleCPDLC\build\cache\dll
python -m nuitka --standalone --onefile --mingw64 --windows-console-mode=disable --enable-plugin=pyside6 --include-qt-plugins=platforms,styles --remove-output --follow-imports --nofollow-import-to=PySide6.QtWebEngine --nofollow-import-to=PySide6.Qt3D --nofollow-import-to=PySide6.QtBluetooth --nofollow-import-to=PySide6.QtSql --plugin-enable=pylint-warnings --output-dir=dist --windows-icon-from-ico=./icon/favicon.ico .\main.py