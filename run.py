def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    remaining_time = list(burst_time)
    current_time = 0

    all_processes_done = False

    while (all_processes_done == False):
        all_processes_done = True 

        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                all_processes_done = False

                if remaining_time[i] <= time_quantum:
                    print(f"Time {current_time}: Process {processes[i]} is running for {remaining_time[i]} time units.")
                    current_time += remaining_time[i]
                    remaining_time[i] = 0
                else:
                    print(f"Time {current_time}: Process {processes[i]} is running for {time_quantum} time units.")
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum


processes = [1, 2, 3, 4]
arrival_time = [0, 10, 20, 30]
burst_time = [100, 40, 50, 30]
time_quantum = 30

round_robin(processes, arrival_time, burst_time, time_quantum)
