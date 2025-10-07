def too_much_screen_time(hours):
    averageseven = (sum(hours)/7)
    for i in range(0,len(hours)):
        if (hours[i] >= 10):
            return True
        elif (i <= 4):
            averagethree = (hours[i] + hours[i +1] + hours [i + 2])/3
            if (averagethree >= 8):
                return True
        if (averageseven >= 6):
            return True
    return False







