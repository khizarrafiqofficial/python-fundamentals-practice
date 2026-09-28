class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = programmer("Khizar", 120000, 56000)
print(a.company, a.name, a.salary, a.pin)
m = programmer("Maham", 130000, 56000)
print(m.company, m.name, m.salary, m.pin)