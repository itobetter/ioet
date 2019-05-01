import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re


class payroll():
    """
    this class calculate the payroll when insert a *.txt
    """
    def __init__(self, file):
        self.format_time = lambda hour: datetime.strptime(hour, '%H:%M')
        self.file = file


    def process_payroll(self):
        """
        function print the result
        :return: True if everything is ok
        """
        with open(self.file) as fp:
            while True:
                line = fp.readline()
                if not line:
                    return
                name, weekdays = line.split('=')
                amount = sum([
                    self.define_payroll(day, start, end)
                    for day, start, end in re.findall(
                        '(\w{2})([0-24]{2}:[0-59]{2})-([0-24]{2}:[0-59]{2})',
                        weekdays
                    )
                ])
                print(f"The amount to pay {name} is: {amount} USD")


    def define_money(self, hour, day):
        """
        define moneay depends of weekday
        :return: money Float 
        """
        stimete= {
            self.format_time('00:01') <= hour >= self.format_time('09:00') :25,
            self.format_time('09:01') <= hour >= self.format_time('18:00'): 15,
            self.format_time('18:01') <= hour >= self.format_time('00:00') :20,
        }.get(True) or 0
        if day not in ('SA', 'SU'):
            return stimete
        return stimete + 5


    def define_payroll(self, day, start, end):
        step = self.format_time(start)
        money = 0
        while step <= self.format_time(end):
            money += self.define_money(step, day)
            step = step + relativedelta(hours=+1)
        return money


if __name__ == "__main__":
    payroll = payroll(sys.argv[1])
    payroll .process_payroll()