#!C:\Python27\python.exe
'''
cs1114

Programmer: Vivek Aggarwal
Username: va713

filename: hw10 workerRec

This class allows creation of instances for each worker put into the system. This class also calculates earnings. 
It then returns a report as a string, the report including the SSN, name, earnings, and title

constraints: none

assumptions: none
'''
class workerRec():
	def __init__(self, name, SSN):
		self.__name = name
		self.__SSN = SSN
		self.__hourlyPay = 17.22
		self.__hoursWorked = 0.0
		self.__title = None
		self.__earnings = 0.0

	def set_name(self, name):
		'''changes name to passed in value'''
		self.__name = name
	def set_ssn(self, SSN):
		'''changes SSN to passed in value'''
		self.__SSN = SSN
	def set_hourly_pay(self, hourlyPay):
		'''changes rate of pay to passed in value'''
		self.__hourlyPay = hourlyPay
	def set_hours_worked(self, hoursWorked):
		'''changes hours worked to passed in value'''
		self.__hoursWorked = hoursWorked
	def set_title(self, title):
		'''changes title to passed in value'''
		self.__title = title
	def setEarnings(self, earnings):
		'''changes earnings to passed in value'''
		self.__earnings = earnings

	def getName(self):
		'''returns value of name'''
		return self.__name
	def getSSN(self):
		'''returns value of SSN '''
		return self.__SSN
	def getHourlyPay(self):
		'''returns value of rate of pay'''
		return self.__hourlyPay
	def getHoursWorked(self):
		'''returns value of hours worked'''
		return self.__hoursWorked
	def getTitle(self):
		'''returns value of title'''
		return self.__title
	def getEarnings(self):
		'''returns value of earnings'''
		return self.__earnings

	def addHours(self, hours):
		'''adds an amount of hours to the hours worked'''
		self.__hoursWorked +=hours
	def addEarnings(self, earnings):
		'''adds earnings to amount of earnings'''
		self.__earnings +=earnings
	def resetHours(self):
		'''resets hours worked back to zero'''
		self.__hoursWorked = 0
	def calculateEarnings(self):
		'''calculates earnings based on hours worked and rate of pay'''
		self.__earnings = float(self.__hourlyPay * self.__hoursWorked)

	def pay_worker(self):
		'''a function that calculates earnings and resets hours to zero. "pays" the worker'''
		self.calculateEarnings()
		self.resetHours()


	def __str__(self):

		if self.__title == None:
			return "%i\n%s $%.2f" % (self.__SSN, self.__name, self.__earnings)
		else:
			return "%i\n%s $%.2f %s" % (self.__SSN, self.__name, self.__earnings, "[" + self.__title + "]") 

