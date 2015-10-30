INPUT = 2
OUTPUT  = 3
INPUT2 = 4
not_func = lambda x: not(x)
not_constraint = lambda: Constraint2(not_func,not_func)
class Constraint2:
    prefix = "A --> B"
    def __init__(self,a2b,b2a):
        self.a_to_b = a2b
        self.b_to_a = b2a
        self.a = None
        self.b = None

    def set(self,var,number):
        olda,oldb = self.a,self.b
        if var == INPUT:
            self.a = number
        elif var == OUTPUT:
            self.b = number

    def get(self,var):
        if var == INPUT:
            return self.a
        if var == OUTPUT:
            return self.b
    def find(self,var):
        if var == INPUT:
            self.a = None
            self.solve()
            return(self.a)
        if var == OUTPUT:
            self.b = None
            self.solve()
            return(self.b)
    def get_val(self,var):
        if var == self.a:
            value = self.find(INPUT)
            self.a = var
            return value
        if var == self.b:
            value = self.find(OUTPUT)
            self.b = var
            return value
        return None

    def solve(self):
        a = self.a.get_val(self) if type(self.a) == Constraint2 else self.a
        b = self.b.get_val(self) if type(self.b) == Constraint2 else self.b
        if self.a is not None:
            tempb = self.a_to_b(a)
            if b is not None and tempb!= b:
                print("Could not resolve values for B \nOld Value: %s \nNew Value: %s"%(str(b),str(tempb)))
                return False
            else:
                self.b = tempb
        elif self.b is not None:
            tempa = self.b_to_a(b)
            self.a = tempa
        return True

    def __repr__(self):
        a = self.a.get_val(self) if type(self.a) == Constraint2 else self.a
        b = self.b.get_val(self) if type(self.b) == Constraint2 else self.b
        a, b = str(a) , str(b)
        return "%s \nA: %s \nB: %s" % (self.prefix,a,b)

if True:
    g,h,i = not_constraint(),not_constraint(),not_constraint()
    g.set(OUTPUT,h)
    h.set(INPUT,g)

    h.set(OUTPUT,i)
    i.set(INPUT,h)
    i.set(OUTPUT,True)
    g.solve()
