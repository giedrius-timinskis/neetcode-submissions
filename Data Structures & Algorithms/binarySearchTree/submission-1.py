class TreeNodeWithIdx:
    def __init__(self, key, val=0, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right


# https://neetcode.io/problems/binarySearchTree
class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        nodeToInsert = TreeNodeWithIdx(key, val)
        if not self.root:
            self.root = nodeToInsert
            return
        self._insert(self.root, nodeToInsert)

    def _insert(
        self, currentNode: TreeNodeWithIdx, nodeToInsert: TreeNodeWithIdx
    ) -> TreeNodeWithIdx:
        if not currentNode:
            return nodeToInsert

        if nodeToInsert.key < currentNode.key:
            currentNode.left = self._insert(currentNode.left, nodeToInsert)
        elif nodeToInsert.key > currentNode.key:
            currentNode.right = self._insert(currentNode.right, nodeToInsert)
        else:
            # If the key already exists, we update the value
            currentNode.val = nodeToInsert.val
        return currentNode

    def get(self, key: int) -> int:
        def search(node: TreeNodeWithIdx):
            if not node:
                return -1
            if node.key == key:
                return node.val
            elif key < node.key:
                return search(node.left)
            else:
                return search(node.right)

        return search(self.root)

    def getMin(self) -> int:
        res = self.getMinNode()
        if not res:
            return -1

        return res.val

    def getMinNode(
        self, startingNode: Optional[TreeNodeWithIdx] = None
    ) -> TreeNodeWithIdx | None:
        if not startingNode:
            startingNode = self.root

        node = startingNode
        if not node:
            return None

        while node and node.left:
            node = node.left

        return node

    def getMax(self) -> int:
        node = self.root
        if not node:
            return -1

        while node and node.right:
            node = node.right

        return node.val

    def getInorderKeys(self) -> List[int]:
        result: List[int] = []

        def dfs(node: TreeNodeWithIdx):
            if not node:
                return result

            dfs(node.left)
            result.append(node.key)
            dfs(node.right)
            return result

        return dfs(self.root)

    def remove(self, key: int) -> None:
        def rem(node: TreeNodeWithIdx, targetKey: int):
            if not node:
                return None

            if targetKey < node.key:
                node.left = rem(node.left, targetKey)
            elif targetKey > node.key:
                node.right = rem(node.right, targetKey)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    # Node with two children: get in-order successor
                    successor = self.getMinNode(node.right)
                    node.key = successor.key
                    node.val = successor.val
                    node.right = rem(node.right, successor.key)  # Remove the successor

            return node

        self.root = rem(self.root, key)