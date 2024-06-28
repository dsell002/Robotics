#ifndef PF_H
#define PF_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    double x;
    double y;
    double theta;
    double weight;
} Particle;

typedef struct {
    Particle *particles;
    int num_particles;
} ParticleFilter;

void pf_init(ParticleFilter *pf, int num_particles);
void pf_predict(ParticleFilter *pf, double v, double w, double dt);
void pf_update(ParticleFilter *pf, double z_x, double z_y, double std[]);
void pf_resample(ParticleFilter *pf);
void pf_free(ParticleFilter *pf);

#endif // PF_H
