class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
    
    def add_directory(self, path, name):
        node = self._get_node(path)
        if node is not None and name not in node.children:
            node.children[name] = DirectoryNode(name)
            print(f"Directory '{name}' added under '{path}'")
        else:
            print("Invalid path or directory already exists")
    
    def delete_directory(self, path, name):
        node = self._get_node(path)
        if node is not None and name in node.children:
            del node.children[name]
            print(f"Directory '{name}' deleted from '{path}'")
        else:
            print("Invalid path or directory does not exist")
    
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
    
    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children.values():
            child.display(level + 1)

directory_tree = DirectoryNode("root")

directory_tree.add_directory("root", "Pictures")
directory_tree.add_directory("root/Pictures", "Saved Pictures")
directory_tree.add_directory("root/Pictures/Saved Pictures", "Web Images")
directory_tree.add_directory("root/Pictures/Saved Pictures/Web Images", "Chrome")
directory_tree.add_directory("root/Pictures/Saved Pictures/Web Images", "Opera")
directory_tree.add_directory("root/Pictures/Saved Pictures/Web Images", "Firefox")
directory_tree.add_directory("root/Pictures", "Screenshots")
directory_tree.add_directory("root/Pictures", "Camera Roll")
directory_tree.add_directory("root/Pictures/Camera Roll", "2025")
directory_tree.add_directory("root/Pictures/Camera Roll", "2024")
directory_tree.add_directory("root/Pictures/Camera Roll", "2023")

print("\nInitial Directory Structure:")
directory_tree.display()

directory_tree.delete_directory("root/Pictures/Saved Pictures/Web Images", "Opera")

print("\nDirectory Structure After Deletion:")
directory_tree.display()
