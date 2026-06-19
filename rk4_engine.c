#include <stdio.h>
#include <math.h>

#define G 9.81  // Gravity constant
#define DT 0.02 // Time step size

// State structure for a single pendulum arm
typedef struct {
    double theta; // Angle (radians)
    double omega; // Angular velocity
} PendulumState;

// Computes derivatives for the equations of motion (Simplified single-joint non-linear model for safety/stability)
void get_derivatives(double theta, double omega, double* d_theta, double* d_omega) {
    *d_theta = omega;
    *d_omega = -(G) * sin(theta); // Restoring gravitational torque
}

// RK4 Numerical Integration step
void rk4_step(double* theta, double* omega) {
    double k1_t, k1_w;
    double k2_t, k2_w;
    double k3_t, k3_w;
    double k4_t, k4_w;

    // Step 1
    get_derivatives(*theta, *omega, &k1_t, &k1_w);

    // Step 2
    get_derivatives(*theta + 0.5 * DT * k1_t, *omega + 0.5 * DT * k1_w, &k2_t, &k2_w);

    // Step 3
    get_derivatives(*theta + 0.5 * DT * k2_t, *omega + 0.5 * DT * k2_w, &k3_t, &k3_w);

    // Step 4
    get_derivatives(*theta + DT * k3_t, *omega + DT * k3_w, &k4_t, &k4_w);

    // Update state vector using weighted averages of coefficients
    *theta += (DT / 6.0) * (k1_t + 2.0 * k2_t + 2.0 * k3_t + k4_t);
    *omega += (DT / 6.0) * (k1_w + 2.0 * k2_w + 2.0 * k3_w + k4_w);
}
