import numpy as np


class ParseData:
    """
    Simple class to parse csv file and store information in attributes easily to access and manipulate
    """
    def __init__(self, filename=None):
        self.LapNumber = np.empty(1000000)
        self.LapDistance = np.empty(1000000)
        self.Speed = np.empty(1000000)
        self.LateralAcceleration = np.empty(1000000)
        self.LongitudinalAcceleration = np.empty(1000000)
        self.FRH = np.empty(1000000)
        self.RRH = np.empty(1000000)
        self.Yaw = np.empty(1000000)
        self.Steer = np.empty(1000000)
        self.Roll = np.empty(1000000)
        self.FlapAngle = np.empty(1000000)
        self.BrakeForce = np.empty(1000000)
        self.ThrottlePedal = np.empty(1000000)
        self.CzF = np.empty(1000000)
        self.CzR = np.empty(1000000)
        self.Cx = np.empty(1000000)
        self.CornerPhase = np.empty(1000000)
        self.GPSLatCoord = np.empty(1000000)
        self.GPSLongCoord = np.empty(1000000)

        if filename is not None:
            self.load_from_file(filename)

    def load_from_file(self, filename) -> None:
        """
        read from file all values and export in relative attributes the respective column
        :param filename: path's file
        :return:
        """
        # import data from csv
        rawdata = np.genfromtxt(filename, delimiter=',')
        self.LapNumber = rawdata[1:, 0]
        self.LapDistance = rawdata[1:, 1]
        self.Speed = rawdata[1:, 2]
        self.LateralAcceleration = rawdata[1:, 3]
        self.LongitudinalAcceleration = rawdata[1:, 4]
        self.FRH = rawdata[1:, 5]
        self.RRH = rawdata[1:, 6]
        self.Yaw = rawdata[1:, 7]
        self.Steer = rawdata[1:, 8]
        self.Roll = rawdata[1:, 9]
        self.FlapAngle = rawdata[1:, 10]
        self.BrakeForce = rawdata[1:, 11]
        self.ThrottlePedal = rawdata[1:, 12]
        self.CzF = rawdata[1:, 13]
        self.CzR = rawdata[1:, 14]
        self.Cx = rawdata[1:, 15]
        self.CornerPhase = rawdata[1:, 16]
        self.GPSLatCoord = rawdata[1:, 17]
        self.GPSLongCoord = rawdata[1:, 18]