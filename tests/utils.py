import sys, os

class TestUtils:
    @staticmethod
    def add_parent_path():
        current_script_path = os.path.abspath(__file__)  # Path of the current script
        parent_dir = os.path.dirname(os.path.dirname(current_script_path))  # Parent directory
        if parent_dir not in sys.path:
            sys.path.append(parent_dir) 