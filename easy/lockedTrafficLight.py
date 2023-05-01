class TrafficLight:
    def __init__(self):
        self.cross_lock = Lock()
        self.dir = 1                    # 1 for n/s 2 for e/w
        

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        
        with self.cross_lock:
            if roadId != self.dir:
                self.dir = roadId
                turnGreen()

            crossCar()