class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        if mood == "happy" or mood == "tired" or mood == "lazy":
            self.mood = mood
        else:
            self.mood = "invalid input, mood must be happy, tired or lazy"

        if healthRate >= 0 and healthRate <= 100:
            self.healthRate = healthRate
        else:
            self.healthRate = "Health rate must be between 0 and 100"

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        if self.money >= items*10:
            self.money -= items*10
        else:
            return "You don't have this amount of money, you can not buy those items"