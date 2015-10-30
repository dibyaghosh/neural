def connect(c1,l1,c2,l2):
	c1.connect(c2,l1)
	c2.connect(c1,l2)

class Constraint():
	def __init__(self,name):
		self.constraints = []
		self.name = name
	def connect(self,constraint,location):
		self.constraints[location][0] = constraint
	def propagate(self,other):
		for i in self.constraints:
			if i != other:
				i.propagate()
	def get_value(self,other):
		location = self.find_location(other) or other 
		self.constraints[location][1] = None
		for loc,val in self.constraints.items():
			if loc != location:
				if val[0]:
					self.constraints[loc][1] = self.constraints[loc][0].get_value(self)
		self.solve()
		return self.constraints[location][1]
	def find_location(self,other):
		for k,v in self.constraints.items():
			if v[0] == other:
				return k
	def get_constraint(self,name):
		return self.constraints[name][0]
	def get_number(self,name):
		return self.constraints[name][1]
	def __repr__(self):
		return self.name

class SingleConstraint(Constraint):
	def __init__(self,value,name):
		self.name = name
		self.constraints = {"A":[None,value]}
	def connect(self,constraint,location):
		self.constraints["A"][0] = constraint
	def get_value(self,other):
		return self.constraints["A"][1]

class Variable(SingleConstraint):
	def set_variable(self,value):
		self.constraints["A"][1] = value


class DoubleConstraint(Constraint):

	def __init__(self,a_to_b,b_to_a):
		self.constraints = {"A":[None,None],"B":[None,None]}
		self.a2b = a_to_b
		self.b2a = b_to_a

	def solve(self):
		a = self.constraints["A"][1]
		b = self.constraints["B"][1]
	
def helper2(a,b,a2b):
	if a is not None:
		if b is not None and b != a2b(a):
			print("Failed")
			return b
		return a2b(a)
	return b

def helper3(a,b,c,toc):
	if a is not None and b is not None:
		temp = toc(a,b)
		if c is not None and c!=temp:
			print("Failed")
		return temp
	return c

def fill(string,length):
	string = string[:length]
	return " "*(length-len(string)) + string

triple = "A_NUM--|------\\ \n" + " "*15+"|NAME|-- C_NUM\n" +"B_NUM--|------/"		   

def get_repr(object,name):
	a = repr(object.constraints[name][0]) if object.constraints[name][0] else "None"
	a += ": %s"%str(object.get_number(name))
	return fill(a,13)
class TripleConstraint(Constraint):

	def __str__(self):
		a = get_repr(self,"A")
		b = get_repr(self,"B")
		c = get_repr(self,"C")
		name = fill(self.name,6)
		return self.name + "\n" + triple.replace("A_NUM",a).replace("B_NUM",b).replace("C_NUM",c).replace("NAME",name)
	def __init__(self,ab_to_c,ac_to_b,bc_to_a,name):
		self.ab2c = ab_to_c
		self.ac2b = ac_to_b
		self.bc2a = bc_to_a
		self.name = name
		self.constraints = {"A":[None,None], "B":[None,None],"C":[None,None]}
	def solve(self):
		a = self.constraints["A"][1]
		b = self.constraints["B"][1]
		c = self.constraints["C"][1]
		self.constraints["A"][1] = helper3(b,c,a,self.bc2a)
		self.constraints["B"][1] = helper3(a,c,b,self.ac2b)
		self.constraints["C"][1] = helper3(a,b,c,self.ab2c)

