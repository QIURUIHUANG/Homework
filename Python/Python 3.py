def case_count(input):
    lower_count = 0
    upper_count = 0
    for each_letter in input:
        if each_letter.islower():
            lower_count += 1
        elif each_letter.isupper():
            upper_count += 1
    print("('Uppercase: {}', 'Lowercase: {}')".format(upper_count, lower_count))
case_count("Hello World")