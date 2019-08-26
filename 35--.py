class listnode:
    def __init__(self,data,pnext=None,psibling=None):
        self.data = data
        self.pnext = pnext
        self.psibling = psibling

def clone(node):  ##各个节点逐一复制
    p = node
    nhead = listnode(node.data)
    np = nhead
    while p.pnext:
        temp = listnode(p.pnext.data)
        np.pnext = temp
        if p.psibling:
            np.psibling = p.psibling
        np = np.pnext
        p = p.pnext
    return nhead

# def clone_hash(node)

if __name__ == '__main__':
    n1 = listnode('A')
    n2 = listnode('B')
    n3 = listnode('C')
    n4 = listnode('D')
    n5 = listnode('E')
    n1.pnext , n1.psibling = n2 , n3
    n2.pnext , n2.psibling = n3 , n5
    n3.pnext = n4
    n4.pnext , n4.psibling = n5 , n2
    print(clone(n1).psibling.pnext.psibling.pnext.data)