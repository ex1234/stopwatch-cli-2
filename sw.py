import time
print("Press Ctrl+C to stop; laps every Enter.")
t0=time.time()
try:
    while True:
        input(); print(f"lap: {time.time()-t0:.2f}s")
except KeyboardInterrupt:
    print(f"total: {time.time()-t0:.2f}s")
