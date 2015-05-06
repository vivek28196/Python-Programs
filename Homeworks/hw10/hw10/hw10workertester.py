'''
cs1114

Programmer: Vivek Aggarwal
Username: va713

filename: hw10workertester

This is a tester main for the workerRec class

constraints: none

assumptions: none
'''
from hw10worker import workerRec
def main():
	worker = workerRec("John Doe", 78932142)
	worker.set_title("Master Snake Charmer")
	worker.set_hours_worked(15)
	worker.pay_worker()
	print(worker)
main()
