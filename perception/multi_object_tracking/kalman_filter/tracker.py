import numpy as np
from filterpy.kalman import KalmanFilter

class ObjectTracker:
    def __init__(self):
        self.kf = KalmanFilter(dim_x=4, dim_z=2)
        self.kf.F = np.array([[1, 0, 1, 0],
                              [0, 1, 0, 1],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])
        self.kf.H = np.array([[1, 0, 0, 0],
                              [0, 1, 0, 0]])
        self.kf.R *= 10
        self.kf.P *= 1000
        self.kf.Q *= 0.1

    def predict(self):
        self.kf.predict()

    def update(self, z):
        self.kf.update(z)

    def get_state(self):
        return self.kf.x
