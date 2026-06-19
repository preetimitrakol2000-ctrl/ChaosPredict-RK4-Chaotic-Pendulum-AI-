# ChaosPredict-RK4 🌀

An investigation into deterministic chaos and numerical integration. This project builds a high-fidelity pendulum mechanics simulation using standard **Runge-Kutta 4th Order (RK4)** solvers in **C**, maintains states in a memory-efficient **Circular Queue (Ring Buffer)**, and passes them to a **Python** time-series predictive model.

## 🧠 Key DSA & Architectural Concepts Implemented
* **Runge-Kutta (RK4) Integration:** Solves complex, non-linear Ordinary Differential Equations (ODEs) using high-accuracy numerical calculus approximations.
* **Circular Buffer Ring Queues:** Avoids memory leaks and pointer shifts by creating a fixed-capacity FIFO structure that handles modulo index wraps ($i = (i + 1) \pmod N$).
* **Time-Series Predictive Forecasting:** Converts spatial histories inside localized temporal windows into linear feature regressions.

## 🛠️ Project Structure
* `rk4_engine.c`: Handles kinematic differential velocity updates.
* `bounded_queue.c`: Memory-efficient rolling queue tracking past physics steps.
* `lstm_predictor.py`: Time-series forecasting intelligence engine.
* `animate.py`: Controls data bindings and monitors prediction divergence.

## 🚀 Execution Instructions

Compile dependencies and launch the simulation pipeline using:
```bash
python animate.py
