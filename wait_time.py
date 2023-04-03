# Tạo một task đếm ngược
import time
def count_down(times, ps_name):
     for _ in range(times):
          time.sleep(1)
          print(ps_name)

def measure_time(func, *args):
     start = time.time()
     func(*args)
     end = time.time()
     print(f"Its take {end-start}s to excecute function")

def run_n_process_sync(ps_num, ps_func, *args):
     for i in range(ps_num):
          print("Process Number: ", i+1)
          ps_func(*args)

measure_time(run_n_process_sync, 3, count_down, 4, "process is running")

# Using for loop use this count_down function 5 times
# Measure for loop in seconds

# Using thread to execute for loop as fast as possible
# Create a async function

