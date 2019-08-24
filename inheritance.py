# Demonstrating inheritances with:
#   C inherits A
#   D inherits A and B
#   E inherits C, which inherits A
#   E inherits D, which inherits A and B

class A:
    def feature_A(self):
        print("feature_A1")
    
class B:
    def feature_B(self):
        print("feature_B1")

class C(A):
    def feature_C(self):
        print("feature_C1")

class D(A,B):
    def feature_D(self):
        print("feature_D1")

class E(C,D):
    def feature_E(self):
        print("feature_E1")

# Listing all available methods including inherited ones
a1 = A()
a1.feature_A()

# C inherits A
c1 = C()
c1.feature_A()
c1.feature_C()

# D inherits A and B
d1 = D()
d1.feature_A()
d1.feature_B()
d1.feature_D()

# E inherits C, which inherits A
# E inherits D, which inherits A and B
e1 = E()
e1.feature_A()
e1.feature_B()
e1.feature_C()
e1.feature_D()
e1.feature_E()