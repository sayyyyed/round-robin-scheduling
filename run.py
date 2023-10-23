def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    remaining_time = list(burst_time)
    current_time = 0

    while True:
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

        if all_processes_done:
            break

    print("\nRound Robin Scheduling Results:")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i, process in enumerate(processes):
        waiting_time = current_time - arrival_time[i] - burst_time[i]
        turn_around_time = current_time - arrival_time[i]
        total_waiting_time += waiting_time
        total_turnaround_time += turn_around_time
        print(f"Process {process}: Waiting Time = {waiting_time}, Turn-Around Time = {turn_around_time}")

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turn-Around Time:", average_turnaround_time)

# Example data
processes = [1, 2, 3, 4]
arrival_time = [0, 10, 20, 30]
burst_time = [100, 40, 50, 30]
time_quantum = 30

# Run the Round Robin algorithm and display step-by-step output
round_robin(processes, arrival_time, burst_time, time_quantum)
