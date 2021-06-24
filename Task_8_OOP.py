
class Individual:
    def __init__(self, age, driver_license):

        if age >= 18 and driver_license == True:
            print("You can vote and drive!")
        elif age >= 18 and driver_license == False:
            print("You can vote!")
        elif age == 17 and driver_license == True:
            print("You can drive and legally you cant drink but your friends will have your back!")
        elif age == 16:
            print("You can't legally drink but your uncles might have your back!")
        else:
            print("Go back to school")


person1 = Individual(19, True)



