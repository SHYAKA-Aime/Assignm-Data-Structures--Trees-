#!/usr/bin/env python3

def add_directory(directory_tree, path, name):
    node = create_or_get_node(directory_tree, path)
    if node is not None and name not in node:
        node[name] = {}
        print(f"Directory '{name}' added under '{path}'")
    else:
        print(f"Failed to add '{name}' under '{path}': Invalid path or directory already exists")

def delete_directory(directory_tree, path, name):
    node = get_node(directory_tree, path)
    if node is not None and name in node:
        del node[name]
        print(f"Directory '{name}' deleted from '{path}'")
    else:
        print(f"Failed to delete '{name}' from '{path}': Invalid path or directory does not exist")

def get_node(directory_tree, path):
    if path == "root":
        return directory_tree
    path_parts = path.split('/')
    node = directory_tree
    for part in path_parts:
        if part in node:
            node = node[part]
        else:
            return None
    return node

def create_or_get_node(directory_tree, path):
    if path == "root":
        return directory_tree
    path_parts = path.split('/')
    node = directory_tree
    for part in path_parts:
        if part not in node:
            node[part] = {}
        node = node[part]
    return node

def display(directory_tree, level=0):
    for name in sorted(directory_tree):
        print("  " * level + name)
        display(directory_tree[name], level + 1)

if __name__ == "__main__":
    # Initialize root directory
    directory_tree = {"root": {}}

    # Adding directories
    directories_to_add = [
        ("root", "Pictures"),
        ("root/Pictures", "Saved Pictures"),
        ("root/Pictures/Saved Pictures", "Web Images"),
        ("root/Pictures/Saved Pictures/Web Images", "Chrome"),
        ("root/Pictures/Saved Pictures/Web Images", "Opera"),
        ("root/Pictures/Saved Pictures/Web Images", "Firefox"),
        ("root/Pictures", "Screenshots"),
        ("root/Pictures", "Camera Roll"),
        ("root/Pictures/Camera Roll", "2025"),
        ("root/Pictures/Camera Roll", "2024"),
        ("root/Pictures/Camera Roll", "2023")
    ]

    for path, name in directories_to_add:
        add_directory(directory_tree["root"], path[5:], name)

    print("\nInitial Directory Structure:")
    display(directory_tree["root"])

    # Deleting a directory
    delete_directory(directory_tree["root"], "Pictures/Saved Pictures/Web Images", "Opera")

    print("\nDirectory Structure After Deletion:")
    display(directory_tree["root"])
