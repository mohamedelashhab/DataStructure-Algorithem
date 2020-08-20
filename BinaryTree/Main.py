from BinaryTree import BinaryTree

if __name__ == '__main__':
    BT = BinaryTree()
    BT.insert(5)
    BT.insert(6)
    BT.insert(4)
    BT.insert(7)
    BT.insert(8)
    BT.insert(9)
    print(BT.find(9))
    # BT.traversePostOreder()
    print(BT.height())