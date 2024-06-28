#include "slam.h"

int main() {
    int num_landmarks = 5;
    SLAM slam;
    slam_init(&slam, num_landmarks);

    double v = 1.0;  // velocity
    double w = 0.1;  // angular velocity
    double dt = 0.1; // time step

    slam_predict(&slam, v, w, dt);

    double z[2] = {1.0, 0.5};
    int landmark_index = 0;
    double R[2][2] = {
        {0.1, 0},
        {0, 0.1}
    };

    slam_update(&slam, z, landmark_index, R);

    printf("State after update: x=%.2f, y=%.2f, theta=%.2f\n", slam.x, slam.y, slam.theta);

    slam_free(&slam);
    return 0;
}
