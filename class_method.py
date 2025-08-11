class University:
    date='30-0-2025'

    @classmethod
    def college1(cls):
        print(f'Exam date college 1:{cls.date}')
    @classmethod
    def college2(cls):
        print(f'Exam date college2:{cls.date}')
    @classmethod
    def college3(cls):
        print(f'Exam date college2:{cls.date}')
    @classmethod
    def modfun(cls, newdate):
        print(f"Exam date before modification: {cls.date}")
        cls.date = newdate
        print(f"Exam date after modification: {cls.date}")

obj=University()

obj.college1()
obj.college2()
obj.college3()

obj.modfun('01-07-2025')

obj.college1()
obj.college2()
obj.college3()
 

