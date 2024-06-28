#include "slam.h"

void slam_init(SLAM *slam, int num_landmarks) {
    slam->x = 0.0;
    slam->y = 0.0;
    slam->theta = 0.0;
    slam->num_landmarks = num_landmarks;
    slam->landmarks_x = (double *)malloc(num_landmarks * sizeof(double));
    slam->landmarks_y = (double *)malloc(num_landmarks * sizeof(double));
    slam->P = (double **)malloc((3 + 2 * num_landmarks) * sizeof(double *));
    for (int i = 0; i < 3 + 2 * num_landmarks; ++i) {
        slam->P[i] = (double *)malloc((3 + 2 * num_landmarks) * sizeof(double));
    }
    for (int i = 0; i < 3 + 2 * num_landmarks; ++i) {
        for (int j = 0; j < 3 + 2 * num_landmarks; ++j) {
            slam->P[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
}

void slam_predict(SLAM *slam, double v, double w, double dt) {
    slam->x += v * dt * cos(slam->theta);
    slam->y += v * dt * sin(slam->theta);
    slam->theta += w * dt;

    // Jacobian and noise covariance not implemented for simplicity
}

void slam_update(SLAM *slam, double *z, int landmark_index, double R[2][2]) {
    double dx = z[0] - slam->landmarks_x[landmark_index];
    double dy = z[1] - slam->landmarks_y[landmark_index];

    // Kalman gain and update steps not implemented for simplicity
}

void slam_free(SLAM *slam) {
    free(slam->landmarks_x);
    free(slam->landmarks_y);
    for (int i = 0; i < 3 + 2 * slam->num_landmarks; ++i) {
        free(slam->P[i]);
    }
    free(slam->P);
}
