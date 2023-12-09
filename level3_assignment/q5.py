class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = (self.hours + other.hours) * 60 + (self.minutes + other.minutes)
        hours, minutes = total_minutes//60, total_minutes%60
        return Time(hours, minutes)

    def displayTime(self):
        print("Hours:", self.hours, "Minutes:", self.minutes)

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print("Total minutes:", total_minutes)

time1 = Time(2, 50)
time2 = Time(1, 20)

a = time1.addTime(time2)

a.displayTime()

a.displayMinute()