#include "ekf.h"

int main() {
    EKF ekf = {0};
    ekf.x = 0;
    ekf.y = 0;
    ekf.theta = 0;
    ekf.P[0][0] = 1;
    ekf.P[1][1] = 1;
    ekf.P[2][2] = 1;

    double v = 1.0;  // velocity
    double w = 0.1;  // angular velocity
    double dt = 0.1; // time step

    ekf_predict(&ekf, v, w, dt);

    double z_x = 1.0;
    double z_y = 0.1;
    double z_theta = 0.05;
    double R[3][3] = {
        {0.1, 0, 0},
        {0, 0.1, 0},
        {0, 0, 0.1}
    };

    ekf_update(&ekf, z_x, z_y, z_theta, R);

    printf("State after update: x=%.2f, y=%.2f, theta=%.2f\n", ekf.x, ekf.y, ekf.theta);

    return 0;
}
