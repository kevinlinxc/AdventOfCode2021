# tag 7-segment display,
file1 = open('inputs\day8.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip()) for line in Lines]
counter = 0
digit0 = None
digit1 = None
digit2 = None
digit3 = None
digit4 = None
digit5 = None
digit6 = None
digit7 = None
digit8 = None

# I'm using standard 7 segment lettering, not whatever the question gave.
segmentA = None
segmentB = None
segmentC = None
segmentD = None
segmentE = None
segmentF = None
segmentG = None

sum = 0
for line in stripped:
    left_digits = line.split(' | ')[0].split(" ")

    # find 1
    for digit in left_digits:
        if len(digit) == 2:
            digit1 = digit
            break

    # find 7
    for digit in left_digits:
        if len(digit) == 3:
            digit7 = digit
            break

    # find 4
    for digit in left_digits:
        if len(digit) == 4:
            digit4 = digit
            break

    # find 8
    for digit in left_digits:
        if len(digit) == 7:
            digit8 = digit
            break

    # find 6
    for digit in left_digits:
        if len(digit) == 6:
            for letter in digit7:
                if letter not in digit:
                    # this also finds segment B
                    segmentB = letter
                    digit6 = digit

    for digit in left_digits:
        if len(digit) == 6:
            for letter in digit4:
                if letter not in digit and letter != segmentB:
                    # this also finds segment G
                    segmentG = letter
                    digit0 = digit

    for digit in left_digits:
        if len(digit) == 6 and digit is not digit0 and digit is not digit6:
            digit9 = digit

    # FIND SEGMENT A, because digit 7 has only one segment that 1 does not
    for letter in list(digit7):
        if letter not in digit1:
            segmentA = letter
            break

    # FIND SEGMENT F, because 0 will have one segment in common with 4 but not 1
    for letter in list(digit0):
        if letter in digit4 and letter not in digit1:
            segmentF = letter
            break

    # FIND SEGMENT C, because only one segment will be in common with 6 and 1
    for letter in list(digit6):
        if letter in digit1:
            segmentC = letter
            break

    # FIND SEGMENT D, using the fact that all but one of segments of number 5 have been found
    for digit in left_digits:
        if len(digit) == 5 and segmentA in digit and segmentF in digit and segmentG in digit and segmentC in digit and segmentB not in digit:
            five_list = list(digit)
            five_list2 = [digit for digit in five_list if digit not in [segmentF, segmentA, segmentG, segmentC]][0]
            segmentD = five_list2[0]

    # FIND SEGMENT E, using elimination or 8
    for letter in digit8:
        if letter not in [segmentA, segmentB, segmentC, segmentD, segmentF, segmentG]:
            segmentE = letter

    # sorted lists of segments to compare output numbers to
    sorted_0 = sorted([segmentA, segmentB, segmentC, segmentD, segmentF, segmentE])
    sorted_1 = sorted([segmentB, segmentC])
    sorted_2 = sorted([segmentA, segmentB, segmentG, segmentE, segmentD])
    sorted_3 = sorted([segmentA, segmentB, segmentG, segmentC, segmentD])
    sorted_4 = sorted([segmentF, segmentG, segmentB, segmentC])
    sorted_5 = sorted([segmentA, segmentF, segmentG, segmentC, segmentD])
    sorted_6 = sorted([segmentA, segmentF, segmentG, segmentE, segmentC, segmentD])
    sorted_7 = sorted([segmentA, segmentB, segmentC])
    sorted_8 = sorted([segmentA, segmentB, segmentC, segmentD, segmentE, segmentF, segmentG])
    sorted_9 = sorted([segmentA, segmentF, segmentB, segmentG, segmentC, segmentD])

    sorted_list = [sorted_0, sorted_1, sorted_2, sorted_3, sorted_4, sorted_5, sorted_6, sorted_7, sorted_8, sorted_9]

    right_digits = line.split(' | ')[1].split(" ")
    output = ""

    for digit in right_digits:
        digit_list = sorted(list(digit))
        actual_num = sorted_list.index(digit_list)
        output += str(actual_num)

    output_digit = int(output)
    print(line)
    print(f"Found output number of {output_digit}")
    sum += output_digit

print(sum)
