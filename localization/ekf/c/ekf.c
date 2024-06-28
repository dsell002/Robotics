#include "ekf.h"

void ekf_predict(EKF *ekf, double v, double w, double dt) {
    // State prediction
    ekf->x += v * dt * cos(ekf->theta);
    ekf->y += v * dt * sin(ekf->theta);
    ekf->theta += w * dt;

    // Jacobian of the motion model
    double Fx[3][3] = {
        {1, 0, -v * dt * sin(ekf->theta)},
        {0, 1, v * dt * cos(ekf->theta)},
        {0, 0, 1}
    };

    // Process noise covariance
    double Q[3][3] = {
        {0.1, 0, 0},
        {0, 0.1, 0},
        {0, 0, 0.1}
    };

    // State covariance prediction
    double P[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int k = 0; k < 3; ++k) {
                P[i][j] += Fx[i][k] * ekf->P[k][j];
            }
        }
    }

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            ekf->P[i][j] = P[i][j] + Q[i][j];
        }
    }
}

void ekf_update(EKF *ekf, double z_x, double z_y, double z_theta, double R[3][3]) {
    // Measurement prediction
    double z_pred[3] = {ekf->x, ekf->y, ekf->theta};

    // Innovation
    double y[3] = {z_x - z_pred[0], z_y - z_pred[1], z_theta - z_pred[2]};

    // Measurement matrix
    double H[3][3] = {
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 1}
    };

    // Innovation covariance
    double S[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int k = 0; k < 3; ++k) {
                S[i][j] += H[i][k] * ekf->P[k][j];
            }
        }
    }

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            S[i][j] += R[i][j];
        }
    }

    // Kalman gain
    double K[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int k = 0; k < 3; ++k) {
                K[i][j] += ekf->P[i][k] * H[k][j];
            }
        }
    }

    // State update
    for (int i = 0; i < 3; ++i) {
        ekf->x += K[i][0] * y[0];
        ekf->y += K[i][1] * y[1];
        ekf->theta += K[i][2] * y[2];
    }

    // State covariance update
    double I[3][3] = {
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 1}
    };

    double KH[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int k = 0; k < 3; ++k) {
                KH[i][j] += K[i][k] * H[k][j];
            }
        }
    }

    double IKH[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            IKH[i][j] = I[i][j] - KH[i][j];
        }
    }

    double P[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int k = 0; k < 3; ++k) {
                P[i][j] += IKH[i][k] * ekf->P[k][j];
            }
        }
    }

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            ekf->P[i][j] = P[i][j];
        }
    }
}
