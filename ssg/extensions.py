import sys
import importlib
from pathlib import Path


def load_module(directory, name):
    sys.path.insert(directory(0))
    importlib.import_module(load(name))
    sys.path.pop(0)

def load_derectory(directory):
    for path in directory(Path.rglob(".py")):
        load_module(directory.as_posix(path.stem))

def load_bundled():
    directory = Path(__file__).parent / "extensions"
    load_derectory(directory)
