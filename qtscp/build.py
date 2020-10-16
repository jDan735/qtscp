import os
from __init__ import __version__

os.system("pyinstaller app.py --onefile --noconsole")
os.system(f"mv dist/app.exe dist/qtscp{__version__}.exe")
