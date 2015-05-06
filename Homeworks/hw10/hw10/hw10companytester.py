'''
cs1114

Programmer: Vivek Aggarwal
Username: va713

filename: hw10companytester

This is a tester main for the company class.

constraints: none

assumptions: none
'''
from hw10company import company
from hw10worker import workerRec
def main():
    companyName = company("RockPit SnakePit and Co.")
    companyName.hire_worker(workerRec("Sally Jones", 443882354))
    companyName.set_hourly_pay_of_worker(443882354, 35.22)
    companyName.hire_worker(workerRec("Joe Smith", 283728992))
    companyName.set_hourly_pay_of_worker(283728992, 25.34)
    companyName.add_hours_to_worker(443882354, 11)
    companyName.add_hours_to_worker(283728992, 9)
    companyName.add_hours_to_worker(443882354, 3)
    companyName.pay_all_workers()
    companyName.add_hours_to_worker(443882354, 10)
    companyName.hire_worker(workerRec("Ralphael", 248339271))
    companyName.set_hourly_pay_of_worker(248339271, 26.39)
    companyName.add_hours_to_worker(283728992, 4)
    companyName.grantTitleToWorker(443882354, "Master Snake Handler")
    companyName.set_hourly_pay_of_worker(283728992, 15.15)
    companyName.add_hours_to_worker(443882354, 7)
    companyName.pay_all_workers()
    companyName.add_hours_to_worker(283728992, 9)
    companyName.add_hours_to_worker(248339271, 4)
    companyName.fire_worker(283728992)
    companyName.set_hourly_pay_of_worker(248339271, 26.41)
    companyName.add_hours_to_worker(248339271, 18)
    companyName.pay_all_workers()

if __name__ == '__main__':
	main()
