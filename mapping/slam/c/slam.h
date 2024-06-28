#ifndef SLAM_H
#define SLAM_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    double x;
    double y;
    double theta;
    double *landmarks_x;
    double *landmarks_y;
    int num_landmarks;
    double **P; // Covariance matrix
} SLAM;

void slam_init(SLAM *slam, int num_landmarks);
void slam_predict(SLAM *slam, double v, double w, double dt);
void slam_update(SLAM *slam, double *z, int landmark_index, double R[2][2]);
void slam_free(SLAM *slam);

#endif // SLAM_H
