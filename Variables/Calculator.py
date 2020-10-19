def Addition(value1, value2):
	sum = float(value1) + float(value2)
	return sum	

def Subtraction(value1, value2):
	sub = float(value1) - float(value2)
	return sub	

def Multiplication(value1, value2):
	mul = float(value1) * float(value2)
	return mul	

def Division(value1, value2):
	try:
		div = float(value1) / float(value2)
		return div		
	except:
		print("Arithmetic Excption")
		return "Divide by zero"
	
def MathsRule(value):	
	valueList = value.split("/")
	value5 = valueList[1]
	valueList = valueList[0].split("*")
	value4 = valueList[1]
	valueList = valueList[0].split("-")
	value3 = valueList[1]
	valueList = valueList[0].split("+")
	value2 = valueList[1]
	value1 = valueList[0]
	result = Division(value4, value5)
	if result=="Divide by zero":
		return "Divide by zero exception"
	else:
		result = Multiplication(value3, result)
		result = Subtraction(value2, result)
		result = Addition(value1, result)
	return result	