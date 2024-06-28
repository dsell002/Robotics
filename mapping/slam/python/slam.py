import numpy as np

class SLAM:
    def __init__(self, num_landmarks):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.num_landmarks = num_landmarks
        self.landmarks = np.zeros((num_landmarks, 2))
        self.P = np.eye(3 + 2 * num_landmarks)

    def predict(self, v, w, dt):
        self.x += v * dt * np.cos(self.theta)
        self.y += v * dt * np.sin(self.theta)
        self.theta += w * dt

        # Jacobian and noise covariance not implemented for simplicity

    def update(self, z, landmark_index, R):
        dx = z[0] - self.landmarks[landmark_index, 0]
        dy = z[1] - self.landmarks[landmark_index, 1]

        # Kalman gain and update steps not implemented for simplicity

if __name__ == "__main__":
    num_landmarks = 5
    slam = SLAM(num_landmarks)

    v = 1.0  # velocity
    w = 0.1  # angular velocity
    dt = 0.1  # time step

    slam.predict(v, w, dt)

    z = np.array([1.0, 0.5])
    landmark_index = 0
    R = np.diag([0.1, 0.1])

    slam.update(z, landmark_index, R)

    print(f"State after update: x={slam.x:.2f}, y={slam.y:.2f}, theta={slam.theta:.2f}")
