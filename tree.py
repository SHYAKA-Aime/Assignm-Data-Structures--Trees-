#!/usr/bin/env python3

def add_directory(directory_tree, path, name):
    node = create_or_get_node(directory_tree, path)
    if node is not None and name not in node:
        node[name] = {}
        print(f"Directory '{name}' added under '{path}'")
    else:
        print(f"Failed to add '{name}' under '{path}': Invalid path or directory already exists")

def delete_directory(directory_tree, path):
    parent_path, _, dir_name = path.rpartition('/')
    parent_node = get_node(directory_tree, parent_path) if parent_path else directory_tree
    
    if parent_node is not None and dir_name in parent_node:
        del parent_node[dir_name]
        print(f"Directory '{dir_name}' deleted from '{parent_path or 'root'}'")
    else:
        print(f"Failed to delete '{dir_name}' from '{parent_path or 'root'}': Invalid path or directory does not exist")

def get_node(directory_tree, path):
    if path == "root" or path == "":
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
    if path == "root" or path == "":
        return directory_tree
    path_parts = path.split('/')
    node = directory_tree
    for part in path_parts:
        if part not in node:
            node[part] = {}
        node = node[part]
    return node

def display(directory_tree, indent=0):
    for name in sorted(directory_tree):
        print("  " * indent + name)
        display(directory_tree[name], indent + 1)

directory_tree = {}

directories_to_add = [
    ("", "Pictures"),
    ("Pictures", "Saved Pictures"),
    ("Pictures/Saved Pictures", "Web Images"),
    ("Pictures/Saved Pictures/Web Images", "Chrome"),
    ("Pictures/Saved Pictures/Web Images", "Opera"),
    ("Pictures/Saved Pictures/Web Images", "Firefox"),
    ("Pictures", "Screenshots"),
    ("Pictures", "Camera Roll"),
    ("Pictures/Camera Roll", "2025"),
    ("Pictures/Camera Roll", "2024"),
    ("Pictures/Camera Roll", "2023")
]

for path, name in directories_to_add:
    add_directory(directory_tree, path, name)

print("\nInitial Directory Structure:")
display(directory_tree)

delete_directory(directory_tree, "Pictures/Saved Pictures/Web Images/Opera")

print("\nDirectory Structure After Deletion:")
display(directory_tree)
