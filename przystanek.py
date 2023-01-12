class Przystanek:
    def __init__(self, stopId, stopLon, stopLat):
        self.id = stopId
        self.x = stopLon
        self.y = stopLat
        self.dist_to_start = 0
        self.dist_to_dest = 0