fibonacci = [0, 1, 1]
stop_value = int(input("Where should we stop the sequence? "))
#1 create while loop = while true
while True:
#2 initiate fibonacci list with 1 and 1
    # fibonacci = [0, 1, 1] -> I had to take this initiation outside the loop so it doesnt re-set every time it loops.
#3 append list[-2] + list[-1]
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
#4 print list and keep looping
    print(fibonacci)

    if fibonacci[-1] > stop_value:
        break



