import time
import sys


def user_input():
    interval = int(input("Please enter duration (mins) of interval: "))
    break_duration = int(input("Please enter break duration (mins) of interval: "))
    total_duration = int(input("Please enter number of sessions: "))
    return interval, break_duration, total_duration


def countdown(interval):
    for i in range(interval, -1, -1):
        for j in range(59, -1, -1):
            sys.stdout.write(f'\rDuration: {i} minutes and {j} seconds to go.')
            time.sleep(1)
            sys.stdout.flush()


if __name__ == "__main__":
    session_count = 0
    interval, break_duration, total_duration = user_input()

    while session_count < total_duration:
        countdown(interval)
        print('\nBreak time!')
        countdown(break_duration)
        session_count += 1
        print('\nSession number: ', session_count)
    print('\nEnd of session!')
