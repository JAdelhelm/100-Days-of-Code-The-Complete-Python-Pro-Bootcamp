from distutils.core import setup
import py2exe

setup(console=['pomodoro.py'],
    options = {
            "py2exe": {
                "dll_excludes": ["tcl85.dll", "tk85.dll"]
            }
        },
)
