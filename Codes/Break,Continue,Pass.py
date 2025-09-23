for i in range(1, 11):
    if i == 3:
        print("Pass at", i)
        pass    # Just a placeholder, does nothing

    elif i == 5:
        print("Continue at", i)
        continue   # Skips printing this number

    elif i == 8:
        print("Break at", i)
        break      # Stops the loop completely

    print("Current number:", i)
