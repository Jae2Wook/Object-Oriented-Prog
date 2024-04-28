def setup_file():
    with open("file1.txt", "w") as file_out:
        file_out.write("This file contains")
        file_out.write("three lines")
        file_out.write("and ten words in total.")

def setup_file2():
    with open("file2", "w") as file_out:
        file_out.write("Love is the central motive for all we do in the")
        file_out.write("Church. Every program, every meeting, every action")
        file_out.write("we are part of as disciples of Jesus Christ should")
        file_out.write("spring from this attribute—for without charity,")
        file_out.write('''"the pure love of Christ," we are nothing.''')

def read_files ():
    files = input("Enter file: ")
    with open(files, "r") as file_in:
        for line in file_in:
            lin = files.line("")
        for letter in file_in:
            chr = files.read("")
    print("The file contains {} linds and {} words".format(lin + 1, chr + 1))

def main():
    setup_file2()
    read_files()
    read_files()
    read_files()

if __name__ == "main__":
    main()

