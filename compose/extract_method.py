import math 

def calculate_stats():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))

    # Calculate the mean and standard deviation of the grades
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return mean, sd

def print_stats(mean, sd):
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')
    
def get_stats():
    mean, sd = calculate_stats()
    print_stats(mean, sd)