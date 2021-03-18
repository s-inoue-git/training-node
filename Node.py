class Node:
    def __init__(self, name, parent=None, children=None):
        
        self.name = name

        if parent is None:
            self.__parent = parent
        else:
            self.parent = parent

        if children is None:
            self.__children = []
        else:
            self.children = children
        


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent      
        if self.name not in [child.name for child in parent.children]:  
            parent.children += [self]

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children
        for child in children:
            child.parent = self
    
    def show_sub_node(self):
        
        def _show_sub_node(node, depth=0):
            
            for child in node.children:
                print(' '*depth, '|--', f'{child}')
                _show_sub_node(child, depth+1)
        
        print(self)
        _show_sub_node(self)
        
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


a = Node('a', None)
b = Node('b', a)
c = Node('c', a)
d = Node('d', c)
e = Node('e', c)
f = Node('f', b)
g = Node('g', b)
h = Node('h', f)
a.show_sub_node()


d = Node('d', None)
e = Node('e', None)
b = Node('b', None)
c = Node('c', None, [d, e])
a = Node('a', None, [b,c])
print(a.children)
a.show_sub_node()

