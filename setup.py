import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["terra_sdk.client.lcd",'requests','sys','time','pandas'], "excludes": []}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Terra.py",
    version="0.1",
    description="My application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("Terra.py", base=base)],
)