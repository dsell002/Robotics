#include "pf.h"

void pf_init(ParticleFilter *pf, int num_particles) {
    pf->num_particles = num_particles;
    pf->particles = (Particle *)malloc(num_particles * sizeof(Particle));
    for (int i = 0; i < num_particles; ++i) {
        pf->particles[i].x = rand() / (double)RAND_MAX;
        pf->particles[i].y = rand() / (double)RAND_MAX;
        pf->particles[i].theta = rand() / (double)RAND_MAX * 2 * M_PI;
        pf->particles[i].weight = 1.0 / num_particles;
    }
}

void pf_predict(ParticleFilter *pf, double v, double w, double dt) {
    for (int i = 0; i < pf->num_particles; ++i) {
        double theta = pf->particles[i].theta;
        pf->particles[i].x += v * dt * cos(theta);
        pf->particles[i].y += v * dt * sin(theta);
        pf->particles[i].theta += w * dt;
    }
}

void pf_update(ParticleFilter *pf, double z_x, double z_y, double std[]) {
    double sum_weights = 0.0;
    for (int i = 0; i < pf->num_particles; ++i) {
        double dx = z_x - pf->particles[i].x;
        double dy = z_y - pf->particles[i].y;
        double distance = sqrt(dx * dx + dy * dy);
        double weight = exp(-(distance * distance) / (2 * std[0] * std[0]));
        pf->particles[i].weight = weight;
        sum_weights += weight;
    }
    for (int i = 0; i < pf->num_particles; ++i) {
        pf->particles[i].weight /= sum_weights;
    }
}

void pf_resample(ParticleFilter *pf) {
    Particle *new_particles = (Particle *)malloc(pf->num_particles * sizeof(Particle));
    double beta = 0.0;
    int index = rand() % pf->num_particles;
    double max_weight = 0.0;
    for (int i = 0; i < pf->num_particles; ++i) {
        if (pf->particles[i].weight > max_weight) {
            max_weight = pf->particles[i].weight;
        }
    }
    for (int i = 0; i < pf->num_particles; ++i) {
        beta += ((rand() / (double)RAND_MAX) * 2.0 * max_weight);
        while (beta > pf->particles[index].weight) {
            beta -= pf->particles[index].weight;
            index = (index + 1) % pf->num_particles;
        }
        new_particles[i] = pf->particles[index];
    }
    free(pf->particles);
    pf->particles = new_particles;
}

void pf_free(ParticleFilter *pf) {
    free(pf->particles);
}
