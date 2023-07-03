# Código para tranfomar o programa em executável


import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter", "shutil", "win10toast", "psutil","watchdog", "signal", ]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Ph0b14 - Anti Ransomware",
    version="0.1",
    description="Challenge da Faculdade de Informática e Administração Paulista, 2022!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)

