import numpy as np

class EKF:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.P = np.eye(3)  # State covariance matrix

    def predict(self, v, w, dt):
        # State prediction
        self.x += v * dt * np.cos(self.theta)
        self.y += v * dt * np.sin(self.theta)
        self.theta += w * dt

        # Jacobian of the motion model
        Fx = np.array([
            [1, 0, -v * dt * np.sin(self.theta)],
            [0, 1, v * dt * np.cos(self.theta)],
            [0, 0, 1]
        ])

        # Process noise covariance
        Q = np.diag([0.1, 0.1, 0.1])

        # State covariance prediction
        self.P = Fx @ self.P @ Fx.T + Q

    def update(self, z, R):
        # Measurement prediction
        z_pred = np.array([self.x, self.y, self.theta])

        # Innovation
        y = z - z_pred

        # Measurement matrix
        H = np.eye(3)

        # Innovation covariance
        S = H @ self.P @ H.T + R

        # Kalman gain
        K = self.P @ H.T @ np.linalg.inv(S)

        # State update
        state_update = K @ y
        self.x += state_update[0]
        self.y += state_update[1]
        self.theta += state_update[2]

        # State covariance update
        I = np.eye(3)
        self.P = (I - K @ H) @ self.P

if __name__ == "__main__":
    ekf = EKF()

    v = 1.0  # velocity
    w = 0.1  # angular velocity
    dt = 0.1  # time step

    ekf.predict(v, w, dt)

    z = np.array([1.0, 0.1, 0.05])
    R = np.diag([0.1, 0.1, 0.1])

    ekf.update(z, R)

    print(f"State after update: x={ekf.x:.2f}, y={ekf.y:.2f}, theta={ekf.theta:.2f}")
