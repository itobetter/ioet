import sys
from payroll import hr_payroll as payroll

if __name__ == "__main__":
    payroll = payroll.payroll(sys.argv[1])
    payroll.process_payroll()