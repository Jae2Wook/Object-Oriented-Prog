# should main() function always stay at the end? i kinda think so

def setup_file():
  with open("file.txt","w") as file_out:
    file_out.write("Name,Age,Phone\n")      
    file_out.write("George,42,208-555-1234\n")
    file_out.write("Mary,35,208-555-2345\n")
    file_out.write("Sam,23,208-555-5313\n")
    file_out.write("Timmy,14,208-555-3523\n")
    file_out.write("Jae, 25, 343-343-2322\n")

### Read the file one record at a time and call print_record
def read_file():
    with open("file.txt", "r") as file_in:
        next(file_in)
        for line in file_in:
            data = line.strip().split(",") # strip(): remove extra characters
            print(data[1])
            print_record(data)

### Format: <name> (<age>) : <phone number>
def print_record(record):
    print("{} ({}) : {}". format(record[0], record[1], record[2]))
  
### Create the main as an entry point for your program.  
### We want python to start here!

def main():
  setup_file()
  read_file()

if __name__ == "__main__":
  main()