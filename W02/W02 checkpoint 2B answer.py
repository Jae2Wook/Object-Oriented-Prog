def setup_file1():
    with open("file1.txt", "w") as file_out:
        file_out.write("This file contains \n")
        file_out.write("three lines \n")
        file_out.write("and ten words in total. \n")

def setup_file2():
    with open("file2.txt", "w") as file_out:
        file_out.write("Love is the central motive for all we do in the \n")
        file_out.write("Church. Every program, every meeting, every action \n")
        file_out.write("we are part of as disciples of Jesus Christ should \n")
        file_out.write("spring from this attribute—for without charity, \n")
        file_out.write('''"the pure love of Christ," we are nothing.''')

def get_filename():
    filename = input("Enter file: ")
    return filename

def read_file(filename):
    line_count = 0
    word_count = 0
    with open(filename, "r") as file_in:
        for line in file_in:
            # print(line.strip().split())
            line_count += 1
            words = line.strip().split() # Can use "words" -> "line" to wrap line over. Strip(): remove beginning and end white spaces. Split(): make into an array -> ['a', 'b', 'c']
            for letter in words:
                print(letter)
                # word_count += 1 #if I use this, I don't have to use the second line below
            #print(words)
            word_count += len(words)
    return word_count, line_count

def main():
    #setup_file1()
    #setup_file2()
    for i in range(3):
        filename = get_filename()
        word_count, line_count = read_file(filename)
        print("The file contains {} lines and {} words".format(line_count, word_count))

if __name__ == "__main__":
    main()