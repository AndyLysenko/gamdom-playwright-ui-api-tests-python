import sys
import os
from pathlib import Path

root_path = Path(os.path.dirname(__file__)).parent

for directory_name, subdirectory_list, file_list in os.walk(root_path):
    sys.path.insert(0, directory_name)