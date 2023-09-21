import time


def atomic_clock():
    # Get the current time in seconds
    current_time = time.time()

    # Calculate the number of seconds since the epoch (January 1, 1970)
    seconds_since_epoch = int(current_time)

    # Calculate the number of nanoseconds within the current second
    nanoseconds = int((current_time - seconds_since_epoch) * 1e9)

    # Print the current time in seconds and nanoseconds
    print(f"Seconds since epoch: {seconds_since_epoch}")
    print(f"Nanoseconds: {nanoseconds}")


# Call the atomic_clock function
atomic_clock()
