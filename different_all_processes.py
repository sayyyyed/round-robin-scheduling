def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    waiting_time = [0] * n
    remaining_time = list(burst_time)
    current_time = 0

    while True:
        all_processes_done = True

        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                all_processes_done = False

                if remaining_time[i] <= time_quantum:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - burst_time[i] - arrival_time[i]
                    remaining_time[i] = 0
                else:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum

        if all_processes_done:
            break

    return waiting_time

def calculate_turn_around_time(waiting_time, burst_time):
    return [waiting + burst for waiting, burst in zip(waiting_time, burst_time)]
