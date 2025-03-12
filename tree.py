#!/usr/bin/env python3

class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
    
    def add_directory(self, path, name):
        node = self._create_or_get_node(path)
        if node is not None and name not in node.children:
            node.children[name] = DirectoryNode(name)
            print(f"Directory '{name}' added under '{path}'")
        else:
            print(f"Failed to add '{name}' under '{path}': Invalid path or directory already exists")
    
    def delete_directory(self, path, name):
        node = self._get_node(path)
        if node is not None and name in node.children:
            del node.children[name]
            print(f"Directory '{name}' deleted from '{path}'")
        else:
            print(f"Failed to delete '{name}' from '{path}': Invalid path or directory does not exist")
    
    def _get_node(self, path):
        if path == "root":
            return self
        path_parts = path.split('/')
        node = self
        for part in path_parts:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node
    
    def _create_or_get_node(self, path):
        if path == "root":
            return self
        path_parts = path.split('/')
        node = self
        for part in path_parts:
            if part not in node.children:
                node.children[part] = DirectoryNode(part)
            node = node.children[part]
        return node
    
    def display(self, level=0):
        print("  " * level + self.name)
        for child in sorted(self.children):
            self.children[child].display(level + 1)

if __name__ == "__main__":
    # Initialize root directory
    directory_tree = DirectoryNode("root")

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
        directory_tree.add_directory(path, name)

    print("\nInitial Directory Structure:")
    directory_tree.display()

    # Deleting a directory
    directory_tree.delete_directory("root/Pictures/Saved Pictures/Web Images", "Opera")

    print("\nDirectory Structure After Deletion:")
    directory_tree.display()
