class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}

    def add_directory(self, path, name):
        """Adds a new directory at the specified path, creating missing parents."""
        node = self._ensure_path(path)
        node.subdirectories[name] = Directory(name)

    def delete_directory(self, path):
        """Deletes the specified directory and its subdirectories."""
        parent_path, dir_name = path.rsplit('/', 1) if '/' in path else ('', path)
        parent_node = self._traverse(parent_path) if parent_path else self
        
        if parent_node and dir_name in parent_node.subdirectories:
            del parent_node.subdirectories[dir_name]
        else:
            print(f"Directory '{path}' not found.")

    def _traverse(self, path):
        """Traverses the tree to find the node at the given path."""
        node = self
        for part in path.split('/'):
            if part in node.subdirectories:
                node = node.subdirectories[part]
            else:
                return None
        return node
    
    def _ensure_path(self, path):
        """Ensures all directories in the given path exist."""
        node = self
        for part in path.split('/'):
            if part not in node.subdirectories:
                node.subdirectories[part] = Directory(part)
            node = node.subdirectories[part]
        return node

    def display(self, level=0):
        """Displays the directory structure."""
        print("    " * level + self.name)
        for sub in self.subdirectories.values():
            sub.display(level + 1)

tree = Directory("Pictures")
tree.add_directory("Pictures", "Saved Pictures")
tree.add_directory("Pictures/Saved Pictures", "Web Images")
tree.add_directory("Pictures/Saved Pictures/Web Images", "Chrome")
tree.add_directory("Pictures/Saved Pictures/Web Images", "Opera")
tree.add_directory("Pictures/Saved Pictures/Web Images", "Firefox")
tree.add_directory("Pictures", "Screenshots")
tree.add_directory("Pictures", "Camera Roll")
tree.add_directory("Pictures/Camera Roll", "2025")
tree.add_directory("Pictures/Camera Roll", "2024")
tree.add_directory("Pictures/Camera Roll", "2023")

print("Directory Structure:")
tree.display()

print("\nDeleting 'Pictures/Saved Pictures/Web Images'")
tree.delete_directory("Pictures/Saved Pictures/Web Images")
tree.display()
