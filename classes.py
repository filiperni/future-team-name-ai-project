class Przystanek:
    def __init__(self, stopId, stopLon, stopLat):
        self.stopId = stopId
        self.stopLon = stopLon
        self.stopLat = stopLat
        self.dist_to_start = 0
        self.dist_to_dest = 0


class Linia:
    def __init__(self, routeID, routeShortName, routeType):
        self.routeID = routeID
        self.routeShortName = routeShortName
        self.routeType = routeType
        self.przystanki_na_linii = []

    def add_przstanek(self, przystanek):
        self.przystanki_na_linii.append(przystanek)


class StopInTrip:
    def __init__(self, routeId, stopID):
        self.routeID = routeId
        self.stopID = stopID


class GpsPosition:
    def __init__(self, routeShortName, lon, lat):
        self.routeShortName = routeShortName
        self.lat = lat
        self.lon = lon

