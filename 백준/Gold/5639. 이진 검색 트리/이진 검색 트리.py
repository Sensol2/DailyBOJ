# dawitblog.tistory.com
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

# 노드
class Node:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None

# 트리
class Tree:
    def __init__(self):
        self.root = None

    # 트리에 노드 추가
    def add(self,val):
        if(self.root == None):
            self.root = Node(val)
        
        else:
            current = self.root
            while(True):
                if(current.val > val):
                    if(current.lchild == None):
                        current.lchild = Node(val)
                        break
                    current = current.lchild

                if(current.val < val):
                    if(current.rchild == None):
                        current.rchild = Node(val)
                        break
                    current = current.rchild
    
    # 후위 순회
    def postOrder(self,node=None):
        global answer
        
        if node == None:
            node = self.root
        
        if node.lchild != None:
            self.postOrder(node.lchild)
        if node.rchild != None:
            self.postOrder(node.rchild)
        answer.append(node.val)


tree = Tree()

# 입력
while True:
    try:
        tree.add(int(input()))
    except:
        break

# 출력
answer = []
tree.postOrder()
print('\n'.join(map(str,answer)))