class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_cap = big
        self.big_count = 0
        self.med_cap = medium
        self.med_count = 0
        self.small_cap = small
        self.small_count = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big_count + 1 <= self.big_cap:
            self.big_count += 1
            return True
        
        elif carType == 2 and self.med_count + 1 <= self.med_cap:
            self.med_count += 1
            return True
        
        elif carType == 3 and self.small_count + 1 <= self.small_cap:
            self.small_count += 1
            return True
        
        else:
            return False