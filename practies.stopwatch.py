# stopwatch

def stopwatch():

    print("\n stopwatch")

    start_time = None
    elapsed_time = 0

    while True:

        print("\n1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            if start_time is None:
                start_time = time.time()
                print("Stopwatch started.")

            else:
                print("stopwatch is already running.")

        elif choice == 2:

            if start_time is not None:
                elapsed_time += time.time() - start_time
                start_time = None
                print("Stopwatch stopped.")
                print("Time :" , round(elapsed_time , 2) , "seconds")

            else:
                print("Stopwatch is not running.")

        elif choice == 3:

            start_time = None
            elapsed_time = 0

            print("Stopwatch Reset.")

        elif choice == 4:

            print("Stopwatch Closed.")

            break
        else:

            print("Invalid choice. Please try again.")

stopwatch()

