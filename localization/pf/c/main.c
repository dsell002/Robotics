#include "pf.h"

int main() {
    ParticleFilter pf;
    pf_init(&pf, 100);

    double v = 1.0;  // velocity
    double w = 0.1;  // angular velocity
    double dt = 0.1; // time step

    pf_predict(&pf, v, w, dt);

    double z_x = 1.0;
    double z_y = 0.1;
    double std[2] = {0.1, 0.1};

    pf_update(&pf, z_x, z_y, std);
    pf_resample(&pf);

    for (int i = 0; i < pf.num_particles; ++i) {
        printf("Particle %d: x=%.2f, y=%.2f, theta=%.2f, weight=%.2f\n", i, pf.particles[i].x, pf.particles[i].y, pf.particles[i].theta, pf.particles[i].weight);
    }

    pf_free(&pf);
    return 0;
}
