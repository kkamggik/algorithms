class Tree:
    def __init__(self, dataList):
        self.data = dataList.pop()
        leftList = list(filter(lambda x:x[1]<self.data[1], dataList))
        rightList = list(filter(lambda x:x[1]>self.data[1], dataList))
        self.left = Tree(leftList) if leftList else None
        self.right = Tree(rightList) if rightList else None
def order(node, pre, post):
    pre.append(node.data[0])
    if node.left != None:
        order(node.left, pre, post)
    if node.right != None:
        order(node.right, pre, post)
    post.append(node.data[0])
def solution(nodeinfo):
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key = lambda x:x[2])
    pre = []
    post = []
    tree = Tree(nodes)
    order(tree, pre, post)
    return [pre,post]
print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))