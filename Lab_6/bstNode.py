class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def print_tree(self, level=0, is_right=False):
        if is_right:
            print(' ' * 4, (level - 1) * 5 * ' ', end='', sep='')
        print('-' * level, self.val, end='', sep='')
        if len(str(self.val).split('.')[1]) == 1:
            print(' ', end='', sep='')
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1, is_right=self.left is not None)
        if (not self.left) and (not self.right):
            print()
