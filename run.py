import matplotlib.pyplot as plt
# from zero_all_processes import findavgTime as original_algorithm
from different_all_processes import round_robin as modified_algorithm
from different_all_processes import calculate_turn_around_time as calculate_tat

# Process data
processes = [1, 2, 3]
arrival_time = [0, 0, 0]  # Modify arrival times as needed
burst_time = [10, 5, 8]
time_quantum = 2

# Run the Round Robin algorithm
waiting_time = modified_algorithm(processes, arrival_time, burst_time, time_quantum)
turn_around_time = calculate_tat(waiting_time, burst_time)

# Print the results
for i, process in enumerate(processes):
    print(f"Process {process}: Waiting Time = {waiting_time[i]}, Turn-Around Time = {turn_around_time[i]}")

# Visualization
plt.figure(figsize=(8, 4))
plt.bar(processes, turn_around_time, label='Turn-Around Time', color='skyblue')
plt.bar(processes, waiting_time, label='Waiting Time', color='lightcoral', alpha=0.7)
plt.xlabel('Processes')
plt.ylabel('Time')
plt.title('Round Robin Scheduling')
plt.legend()
plt.grid(True)
plt.show()
