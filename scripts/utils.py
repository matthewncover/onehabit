import os, sys

def add_parent_path():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(parent_dir, '..'))