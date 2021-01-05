universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500],
]

num_students = 0
tuition_fees = 1

def enrollment_stats(unis):
    num_enrolled = [uni[1] for uni in unis]
    tuition_fees = [uni[2] for uni in unis]
    # to_return = [num_enrolled, tuition_fees] irrelevant, can return
    # lists without packaging up first
    return num_enrolled, tuition_fees

def mean(arg):
    total = sum(arg)
    mean = total / len(arg)
    return mean

def median(arg):
    arg.sort()
    if len(arg) % 2 == 0:
        median_value = sum(arg[(len(arg) / 2) - 1:(len(arg) /2 ) +1 ]) / 2
    else:
        median_value = arg[int(len(arg) / 2)]
    return median_value
     
list_students = enrollment_stats(universities)[num_students]
list_tuition_fees = enrollment_stats(universities)[tuition_fees]

print("\n")
print("*****" * 6)
print(f"Total students:     {sum(list_students):,}")
print(f"Total tuition:    $ {float(sum(list_tuition_fees)):,.2f}")
print("\n")
print(f"Student mean:       {mean(list_students):,.2f}")
print(f"Student median:     {median(list_students):,}")
print("\n")
print(f"Tuition mean:     $ {mean(list_tuition_fees):,.2f}")
print(f"Tuition median:   $ {float(median(list_tuition_fees)):,.2f}")
print("*****" * 6)
print("\n")

# def median(arg):
