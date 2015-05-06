#!C:\Python27\python.exe
'''
cs1114

Programmer: Vivek Aggarwal
Username: va713

filename: hw10company.py

This class creates a dictionary of workers in a company and evaluates certain attributes. It contains functions to change worker attributes and to pay and fire workers. It then writes a 
final report for each fired worker in separate files. It also writes reports for each of the other workers in one file, listen in descending SSN order. The reports include 
SSN, name, earnings and title.

constraints: none

assumptions: none
'''
from hw10worker import workerRec

class company():
    def __init__(self, companyName):
        self.__workers = {}
        self.__companyName = companyName

    def set_company_name(self, companyName):
        '''changes company name to passed in value'''
        self.__companyName = companyName
    
    def get_company_name(self):
        '''returns value of company name'''
        return self.__companyName
        
    def set_hourly_pay_of_worker(self, SSN, hourlyPay):
        '''changes hourly pay of a worked to a passed in value'''
        if not SSN in self.__workers:
            print ("No such worker exists - request to change hourly pay REJECTED")
            return
        self.__workers[SSN].set_hourly_pay(hourlyPay)

    def hire_worker(self, worker):
        '''adds new worker to dictionary made up of existing workers'''
        if worker.getSSN() in self.__workers:
            print("Worker SSN REJECTED - Worker already in system.")
            return
        self.__workers[worker.getSSN()] = worker

    def add_hours_to_worker(self, SSN, hours):
        '''adds hours worked to a certain worker's hours worked'''
        if not SSN in self.__workers:
            print ("No such worker exists - request to add hours REJECTED")
            return
        self.__workers[SSN].addHours(hours)

    def grantTitleToWorker(self, SSN, title):
        '''gives title to a certain worker'''
        if not SSN in self.__workers:
            print ("No such worker exists - request to grant title REJECTED")
            return
        self.__workers[SSN].set_title(title)

    def pay_all_workers(self):
        '''creates a file and writes to it. the information written is a report for each worker which consists of their name, SSN, amount earned and title(if exists)'''
        companyName = self.__companyName.replace(" ", "")
        companyName = companyName.strip(".")
        acctFile = open(companyName + ".pay", "w")
        SSNs = self.__workers.keys()
        SSNs.sort()
        for x in SSNs:
        	self.__workers[x].pay_worker()
        	if self.__workers[x].getTitle() == None:
        		acctFile.write("%s\n%s $%.2f\n\n" % (x, self.__workers[x].getName(), self.__workers[x].getEarnings()))
        	else:
        		acctFile.write("%s\n%s $%.2f %s\n\n" % (x, self.__workers[x].getName(), self.__workers[x].getEarnings(), "[" + self.__workers[x].getTitle() + "]" ))
        acctFile.close()

    def fire_worker(self, SSN):
        '''removes worker from dictionary. writes their report and final earnings to a different file than above.'''
        if not SSN in self.__workers:
            print("No such worker exists - request to fire REJECTED")
            return
        worker = self.__workers[SSN]
        name = worker.getName().replace(" ","")
        worker.pay_worker()
        finalFile = open(name + ".FINAL.pay", "w")
        if worker.getTitle() == None:
        	finalFile.write("%i\n%s $%.2f\n\n" % (worker.getSSN(), str(worker.getName()), worker.getEarnings()))
        else:
        	finalFile.write("%i\n%s $%.2f %s\n\n" % (worker.getSSN(), str(worker.getName()), worker.getEarnings(), "[" + worker.getTitle() + "]"))
        finalFile.close()
        self.__workers.pop(SSN)


