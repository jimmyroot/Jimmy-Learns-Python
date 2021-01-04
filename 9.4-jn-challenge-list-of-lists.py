universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500],
]

name = 0
num_students = 1
tuition_fees = 3

def enrollment_stats(unis):
    num_enrolled = [uni[1] for uni in unis]
    tuition_fees = [uni[2] for uni in unis]
    to_return = [num_enrolled, tuition_fees]
    return to_return

def mean(arg):
    total = sum([arg])
    mean = total / (len(arg) + 1)
    return mean

print(mean(enrollment_stats(universities)[1]))

# def median(arg):
