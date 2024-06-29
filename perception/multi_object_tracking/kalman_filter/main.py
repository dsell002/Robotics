import numpy as np
import matplotlib.pyplot as plt
from tracker import ObjectTracker

def main():
    tracker = ObjectTracker()

    measurements = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
    predictions = []

    for measurement in measurements:
        tracker.predict()
        tracker.update(measurement)
        predictions.append(tracker.get_state()[:2])

    predictions = np.array(predictions)
    plt.plot(measurements[:, 0], measurements[:, 1], 'bo', label='Measurements')
    plt.plot(predictions[:, 0], predictions[:, 1], 'r-', label='Predictions')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
