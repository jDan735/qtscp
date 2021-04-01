import os
from qtscp import __version__

os.system("pyinstaller app.py --onefile --noconsole --icon qtscp.ico")
os.system(f"mv dist/app.exe dist/qtscp{__version__}.exe")
