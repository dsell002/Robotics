#ifndef EKF_H
#define EKF_H

#include <stdio.h>
#include <math.h>

typedef struct {
    double x;   // State: position
    double y;
    double theta;  // State: orientation
    double P[3][3];  // State covariance matrix
} EKF;

void ekf_predict(EKF *ekf, double v, double w, double dt);
void ekf_update(EKF *ekf, double z_x, double z_y, double z_theta, double R[3][3]);

#endif // EKF_H
