"""
Problem: Print Directory Tree
Topics: File System, Recursion, Python OS Module
"""

import os

IGNORE_FOLDERS = {
    ".git", "__pycache__", "node_modules", ".idea", ".vscode",
    "dist", "build", "venv", ".venv", "env",
}
IGNORE_EXTENSIONS = {".pyc", ".pyo", ".log", ".tmp"}

def print_tree(start_path, show_hidden=False, max_depth=None):
    def should_ignore(item):
        # Folder ignore
        if item.lower() in {f.lower() for f in IGNORE_FOLDERS}:
            return True

        _, ext = os.path.splitext(item)     # File extension ignore
        if ext.lower() in IGNORE_EXTENSIONS:
            return True
        return False

    def tree(dir_path, prefix="", depth=0):
        if max_depth is not None and depth > max_depth:
            return

        try:
            items = os.listdir(dir_path)
        except PermissionError:
            print(prefix + "+-- [Permission Denied]")
            return

        # Skip hidden files unless allowed
        if not show_hidden:
            items = [i for i in items if not i.startswith(".")]
        items = [i for i in items if not should_ignore(i)]    # Skip ignored items
        items.sort(key=lambda x: (not os.path.isdir(os.path.join(dir_path, x)), x.lower()))    # Sort: folders first
        total = len(items)
        for index, item in enumerate(items):
            path = os.path.join(dir_path, item)
            connector = "+-- " if index == total - 1 else "+-- "
            if os.path.isfile(path):
                size = os.path.getsize(path)
                print(prefix + connector + f"{item} ({size} bytes)")
            else:
                print(prefix + connector + item)
                extension = "    " if index == total - 1 else "�   "
                tree(path, prefix + extension, depth + 1)
    print(start_path)
    tree(start_path)

if __name__ == "__main__":
    print_tree(".", show_hidden=False, max_depth=None)
