import time

print(f"fist time is {x}, second time is {y}, and the time difference is{z}")
print ("all done")

class timer:
    def __enter__(self):
        st_time=float (time.perf_counter())
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end_time=float (time.perf_counter())
        time_duration= end_time - st_time

# Using the context manager
with timer() as manager:
    print("Inside the context")

#with timer():
