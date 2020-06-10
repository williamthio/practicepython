def get_target_status():
    status = ""
    while status not in ["low", "high", "exact"]:
        status = input("Target status [high|low|exact]: ")
    return status

if __name__ == "__main__":
    print("Think a number between 0 and 100")

    low = 0
    high = 100
    guess_count = 0
    while low <= high:
        guess_count += 1
        mid = low + (high - low) // 2
        print("Number: {}".format(mid))
        status = get_target_status()
        if status == "low":
            low = mid + 1
        elif status == "high":
            high = mid - 1
        else:
            break

    if low > high:
        print("Number not in between 0 and 100.")
    else:
        print("Guess count: {}".format(guess_count))

    print("Game over.")
