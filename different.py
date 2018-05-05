



while True:
    try:
        inp = input("")
        first_num, second_num = [int(i) for i in inp.split()]
        print(abs(first_num-second_num))
    except EOFError as e:
        exit()  
    except ValueError as e:
        exit()