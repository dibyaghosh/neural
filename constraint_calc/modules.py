from constraint import *

add_ab2c = lambda a,b:a+b
add_ac2b = lambda a,c: c-a
add_bc2a = lambda b,c: c-b
addconstraint = lambda name: TripleConstraint(add_ab2c,add_ac2b,add_bc2a,name)

mul_ab2c = lambda a,b:a*b
mul_ac2b = lambda a,c: c/a
mul_bc2a = lambda b,c: c/b
mulconstraint = lambda name: TripleConstraint(mul_ab2c,mul_ac2b,mul_bc2a,name)
constant = 10
a2b = lambda x: x*constant
b2a = lambda x: x/constant


g1 = SingleConstraint(10,"X")
g2 = Variable(20,"Y")
g = addconstraint("Adder 1")
h = mulconstraint("Multiplier 1")
h1 = SingleConstraint(10,"Z")
connect(g,"B",h,"C")
connect(h,"A",h1,"A")
connect(g,"A",g1,"A")
connect(g,"C",g2,"A")