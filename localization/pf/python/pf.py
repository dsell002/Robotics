import numpy as np

class ParticleFilter:
    def __init__(self, num_particles):
        self.num_particles = num_particles
        self.particles = np.zeros((num_particles, 3))  # [x, y, theta]
        self.weights = np.ones(num_particles) / num_particles

    def init(self, x_range, y_range, theta_range):
        self.particles[:, 0] = np.random.uniform(x_range[0], x_range[1], self.num_particles)
        self.particles[:, 1] = np.random.uniform(y_range[0], y_range[1], self.num_particles)
        self.particles[:, 2] = np.random.uniform(theta_range[0], theta_range[1], self.num_particles)

    def predict(self, v, w, dt):
        theta = self.particles[:, 2]
        self.particles[:, 0] += v * dt * np.cos(theta)
        self.particles[:, 1] += v * dt * np.sin(theta)
        self.particles[:, 2] += w * dt

    def update(self, z, std):
        z_x, z_y = z
        distances = np.linalg.norm(self.particles[:, :2] - np.array([z_x, z_y]), axis=1)
        self.weights = np.exp(-(distances ** 2) / (2 * std[0] ** 2))
        self.weights += 1.e-300  # avoid division by zero
        self.weights /= self.weights.sum()

    def resample(self):
        indices = np.arange(self.num_particles)
        cumulative_sum = np.cumsum(self.weights)
        cumulative_sum[-1] = 1.0  # avoid round-off error
        random_values = np.random.rand(self.num_particles)
        new_indices = np.searchsorted(cumulative_sum, random_values)
        self.particles[:] = self.particles[new_indices]
        self.weights.fill(1.0 / self.num_particles)

if __name__ == "__main__":
    pf = ParticleFilter(num_particles=100)
    pf.init(x_range=(0, 1), y_range=(0, 1), theta_range=(0, 2 * np.pi))

    v = 1.0  # velocity
    w = 0.1  # angular velocity
    dt = 0.1  # time step

    pf.predict(v, w, dt)

    z = np.array([1.0, 0.1])
    std = [0.1, 0.1]

    pf.update(z, std)
    pf.resample()

    for i, particle in enumerate(pf.particles):
        print(f"Particle {i}: x={particle[0]:.2f}, y={particle[1]:.2f}, theta={particle[2]:.2f}, weight={pf.weights[i]:.2f}")
