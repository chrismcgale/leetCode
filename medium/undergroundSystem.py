class UndergroundSystem:

    def __init__(self):
        self.arrive = {} # map id to stationName and check in time
        self.totalTime = defaultdict(int)
        self.count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrive[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        left, checkedIn = self.arrive[id]   
        routeName = (left, stationName)
        
        self.totalTime[routeName] += t - checkedIn
        self.count[routeName] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeName = (startStation, endStation)
        return self.totalTime[routeName] / self.count[routeName]