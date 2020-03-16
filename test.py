from tree import Calculator, Node

A = Node(5)

A.insert_left(3)
A.insert_right(7)
B = A.left
C = A.right

B.insert_left(2)
B.insert_right(5)
D = B.left
E = B.right


C.insert_left(1)
C.insert_right(0)
F = C.left
G = C.right

G.insert_left(2)
G.insert_right(8)
H = G.left
J = G.right

J.insert_right(5)
K = J.right


calc1=Calculator()
calc1.reset()
calc1.calc(A)
calc1.output(A)

calc1.reset()
calc1.calc(C)
calc1.output(C)

calc1.reset()
calc1.calc(G)
calc1.output(G)