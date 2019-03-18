import numpy as np
from db import DBManager
class WaterLevel:
    def __init__(self):
        self.max = None
        self.row = None
        self.col = None
        self.unit = None
        self.totalUnit = None
        self.cube = None

    def loadNumpyFile(self, filename):
        self.cube = np.load(filename)
        return self.cube
    def getWaterUnit(self, cube):
        self.row, self.col = cube.shape
        self.max = np.max(cube)
        zone = np.ones((self.max + 1, self.row, self.col))
        for i in range(0, self.max):
            zone[i] = np.where(cube - i <= 0, 1, 0)
        zone[0] *= 2
        for level in range(0, self.max + 1):
            oCount = 0
            zero = np.argwhere(zone[level] == 1)
            for y,x in zero:
                if x == 0 or y == 0 or y == self.row - 1 or x == self.col - 1:
                    zone[level, y, x] = 2
            count = np.count_nonzero(zone[level] == 2)
            spill = np.argwhere(zone[level] == 2)
            while oCount != count:
                oCount = count
                for yy,xx in spill:
                    if xx-1 >= 0 and zone[level,yy,xx-1] == 1:
                        zone[level,yy,xx-1] = 2
                    if xx+1 < self.col and zone[level,yy,xx+1] == 1:
                        zone[level,yy,xx+1] = 2
                    if yy+1 < self.row and zone[level,yy+1,xx] == 1:
                        zone[level,yy+1,xx] = 2
                    if yy-1 >= 0 and zone[level,yy-1,xx] == 1:
                        zone[level,yy-1,xx] = 2
                    if level+1 <= self.max and zone[level+1,yy,xx] == 1:
                        zone[level+1,yy,xx] = 2
                spill = np.argwhere(zone[level] == 2)
                count = np.count_nonzero(zone[level] == 2)
            zone[level] = np.where(zone[level] == 1, 1, 0)
        self.unit = np.sum(zone)
        return self.unit
    def getWaterTotalUnit(self):
        self.totalUnit = self.row * self.col * self.max
        return self.totalUnit

    def saveValue(self, data):
        db = DBManager()
        db.connect()
        data['waterunit'] = str(self.unit)
        data['totalunit'] = str(self.totalUnit)
        return db.save( data )
    def getAll(self):
        db = DBManager()
        db.connect()
        units = db.find_all()
        return units

