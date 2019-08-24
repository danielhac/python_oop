# Demonstrating constructors with inheritances:
#   Subclass will call superclass' constructor if subclass has no constructor.
#   Otherwise, subclass will use its own constructor.

# Method Resolution Order (MRO): if 2+ superclass' constructor or same named methods exist
# when calling super() from subclass, it will choose the leftmost one.

# Superclass WITHOUT constructor
class A:
    def feature_A(self):
        print("feature_A1")


# Superclass WITH constructor
class B:
    def __init__(self):
        print("constructor B")

    def feature_B(self):
        print("feature_B1")


# Superclass WITH constructor
class BB:
    def __init__(self):
        print("constructor BB")

    def feature_BB(self):
        print("feature_BB1")


# Subclass of A WITH constructor
class C(A):
    def __init__(self):
        print("constructor C")
    def feature_C(self):
        print("feature_C1")


# Subclass of B WITHOUT constructor
class D(B):
    def feature_D(self):
        print("feature_D1")


# Subclass of B WITH constructor
class E(B):
    def __init__(self):
        print("constructor E")
    def feature_E(self):
        print("feature_E1")


# Subclass of B WITH constructor
# NOTE: calling superclass' constructor first
class F(B):
    def __init__(self):
        super().__init__()
        print("constructor F")
    def feature_E(self):
        print("feature_F1")


# Subclass of A and B WITH constructor
# Method Resolution Order (MRO), will call BB's constructor since it is leftmost
class G(BB,B):
    def __init__(self):
        super().__init__()
        print("constructor G")


# Create and run one at a time to see what is happening  
# c1 = C()            # no  constructor in A, yes constructor in C
# d1 = D()            # yes constructor in B, no  constructor in D
# e1 = E()            # yes constructor in B, yes constructor in D
# f1 = F()            # yes constructor in B, yes constructor in D
g1 = G()            # yes constructor in BB, yes constructor in B