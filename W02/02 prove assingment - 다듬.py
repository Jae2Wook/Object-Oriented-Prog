def prompt_filename():
    filename = input("Please enter the file: ")
    information = input('''Choose a rate you want to see "comm_rate", "ind_rate", "res_rate": ''')
    return filename, information

def read_file(file_is, info_is):
    count = 0
    summ = 0
    average = 0
    maxx_list = 0
    minn_list = 0 # better to use '[]'
    with open(file_is, "r") as file_in:
        first_line = file_in.readline().strip().split(",")  #reading the first line
        num = first_line.index(info_is) 
        #next(file_in)          # reading the first line makes the first line removed? YES
        #second_line = file_in.readline().strip().split(",")  #reading the second line. MUST NOT
        #maxx = float(second_line[num])                 --> reading the second line skips the data
        maxx = 0
        minn = 1  
        for line in file_in:#Here file_in is alrady read the first line, so it reads from the second line
            alist = line.split(",")
            summ += float(alist[num])
            count += 1
            if maxx < float(alist[num]): #'if' will not run when the values are equal which keeps 
                maxx = float(alist[num]) #the earlier company information
                maxx_list = alist
            if minn > float(alist[num]): 
                minn = float(alist[num])
                minn_list = alist
    average = summ / count
    return average, maxx_list, minn_list

def info_name(info_is):
    if info_is == "comm_rate":
        return "commercial rate"
    if info_is == "ind_rate":
        return "industrial rate"
    if info_is == "res_rate":
        return "residential rate"

def main():
    file_is, info_is = prompt_filename()
    category = info_name(info_is)
    average, max_list, min_list = read_file(file_is, info_is)
    print()
    print("The average {} is: {} \n". format(category, average))
    print("The highest rate is:\n{} ({}, {}) - ${} \n".format(max_list[2], max_list[0], max_list[3], max_list[6]))
    print("The lowest rate is: \n{} ({}, {}) - ${}".format(min_list[2], min_list[0], min_list[3], min_list[6]))
    print()
    input('Press "Enter" to exit') #for the python.exe

if __name__ == "__main__":
    main()


"""

# CS241 Week 12D Solved

import functools

def help(x):
    print(x, x[6])
    input()
    return x[6]

with open("rates.csv","r") as file:
    # Skip the first row
    next(file)

    # Create list of records
    data = [line.strip().split(",") for line in file]

    # Calculate min and max rates
    min_rate = min(data, key=lambda x : help(x))
    max_rate = max(data, key=lambda x : float(x[6]))

    # Calculate average
    avg_rate = functools.reduce(lambda prev, x : prev + float(x[6]), data, 0) / len(data)

    # Here is another way with list comprehensions
    avg_rate = sum([float(x[6]) for x in data]) / len(data)

    print("Average Rate: {}".format(avg_rate))
    print()
    print("Lowest Rate:")
    print("{} ({}, {}) - ${}".format(min_rate[2], min_rate[0], min_rate[3], min_rate[6]))
    print()
    print("Highest Rate:")
    print("{} ({}, {}) - ${}".format(max_rate[2], max_rate[0], max_rate[3], max_rate[6]))
"""