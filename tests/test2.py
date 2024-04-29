import re





while True:
    input_str = input("Enter the input string: ")
    pattern = r'\b\d+\.\d+\b'  # Updated pattern to match floating-point numbers
    numbers = re.findall(pattern, input_str)
    numbers = [float(num) for num in numbers]

    print(numbers[0], numbers[1])
    print(numbers[0]*0.77, numbers[1]*0.44)






while True:
    input_str = input("Enter the input string: ")

    pattern = r'\b\d+\b'
    numbers = re.findall(pattern, input_str)
    numbers = [int(num) for num in numbers]


    FN = numbers[3]
    FP = numbers[2]

    POSITIVOS = numbers[0] - numbers[3] + numbers[2]
    TOTAL = numbers[1]

    TP = POSITIVOS - FP
    TN = TOTAL - POSITIVOS - FN


    print(TP, TN, FP, FN)
    print((TP + TN)* 100.0 / TOTAL, "%")


    