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
    to_return = [num_enrolled, tuition_fees]
    return to_return

def mean(arg):
    total = sum(arg)
    mean = total / len(arg)
    return mean

def median(arg):
    sorted_arg = arg.sort()
    if len(arg) % 2 == 0:
        median_value = sum(arg[int(len(arg)/2)-1:int(len(arg)/2)+1]) / 2
    else:
        median_value = arg[int(len(arg)/2)]
    return median_value
    
    

list_students = enrollment_stats(universities)[num_students]
list_tuition_fees = enrollment_stats(universities)[tuition_fees]

print(f"{sum(list_students):,}")
print(f"{sum(list_tuition_fees):,}")
print(f"{mean(list_students):,}")
print(median(list_students))
print(mean(list_tuition_fees))
print(median(list_tuition_fees))

# def median(arg):
