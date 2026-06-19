import ctypes
import os
import sys
import time
from lstm_predictor import ChaosTimeSeriesPredictor

def compile_chaos_backend():
    print("[*] Compiling backend Runge-Kutta & Queue engines...")
    ext = "dll" if sys.platform.startswith("win") else "so"
    os.system(f"gcc -shared -o rk4_engine.{ext} -fPIC rk4_engine.c")
    os.system(f"gcc -shared -o bounded_queue.{ext} -fPIC bounded_queue.c")
    return f"./rk4_engine.{ext}", f"./bounded_queue.{ext}"

def main():
    rk_path, queue_path = compile_chaos_backend()
    rk_lib = ctypes.CDLL(rk_path)
    q_lib = ctypes.CDLL(queue_path)

    # Setup core types
    class CircularQueue(ctypes.Structure):
        _fields_ = [
            ("data", ctypes.c_double * 5),
            ("head", ctypes.c_int),
            ("tail", ctypes.c_int),
            ("size", ctypes.c_int)
        ]

    # Initialize state values (Starting angle: 45 degrees in radians)
    theta = ctypes.c_double(0.785)
    omega = ctypes.c_double(0.0)

    queue = CircularQueue()
    q_lib.init_queue(ctypes.byref(queue))
    
    predictor = ChaosTimeSeriesPredictor()
    
    print("\n[*] Booting Physics Simulation Engine Loop...")
    print("====================================================================")
    
    for step in range(1, 7):
        # 1. Advance physics clock step via C Runge-Kutta integration
        rk_lib.rk4_step(ctypes.byref(theta), ctypes.byref(omega))
        
        # 2. Append the current angle coordinate to the C ring buffer queue
        q_lib.enqueue(ctypes.byref(queue), theta)
        
        # 3. Flatten the queue elements to extract sequential historical records
        flat_buffer = (ctypes.c_double * 5)()
        q_lib.structural_flatten(ctypes.byref(queue), flat_buffer)
        history_list = list(flat_buffer)[:queue.size]
        
        # 4. Generate Machine Learning prediction inference for the next step
        ml_prediction = predictor.forecast_next_state(history_list)
        
        print(f"Step {step} | Real Coordinate: {theta.value:.5f} rad | ML Predicted Next: {ml_prediction:.5f} rad")
        time.sleep(0.1)
        
    print("====================================================================\n")

if __name__ == "__main__":
    main()
