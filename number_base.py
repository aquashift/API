# convert numbers between bases

def convert_base(num, from_base, to_base):
    num_of_digits = len(str(abs(num))) 
    base_power = 0
    converted_num = 0
    mod_num = 10
    while base_power < num_of_digits:
        print(f"doing round {base_power}\n")
        focus_digit = num % (pow(10, (base_power + 1))) # focus digit = 11101 % 10 = 1 &&&  focus digit = 11101 % 100 = 0
        print(f"focus digit is {focus_digit}\n")
        converted_num += (pow(from_base, base_power) * focus_digit) # converted num = 0 + (2^0) * 1 = 1 &&& converted num = 1 + (2^1) 
        base_power += 1
        print(f"converted num is now {converted_num}")
    

convert_base(11101, 2, 10)

   
