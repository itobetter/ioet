import unittest
from datetime import datetime
from payroll.hr_payroll import payroll


class TestPayroll(unittest.TestCase):
    """
    this class calculate the payroll when insert a *.txt
    """

    def test_init(self):
        self.assertEqual(
            payroll("file.txt").file,
            "file.txt"
        )


    def test_process_payroll(self):
        roll = payroll("file.txt").process_payroll()
        self.assertEqual(roll, None)


    def test_define_money(self):
        """
        define moneay depends of weekday
        :return: money Float
        """
        format_time = lambda hour: datetime.strptime(hour, '%H:%M')
        money = payroll("file.txt").define_money(
            format_time('09:00'), 'MO'
        )
        self.assertEqual(money,25)


    def test_define_payroll(self):
        self.assertEqual(
            payroll("file.txt").define_payroll('MO', '10:00', '12:00'),
            75
        )

if __name__ == '__main__':
    unittest.main()
