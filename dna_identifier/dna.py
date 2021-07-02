from sys import argv, exit
import csv



def get_max_num_of_times_substring (string, sub):
    # calculate the max number of times a substring is repeated
    # string: [ATATTTATATAT]
    # ans:    [201000302010] # starting at that index how many times the substring sub repeats in string

    #sub: at


    ans = [0] * len(string) # initializing an arry zeros in teh length of string
    for i in range(len(string) - len(sub), -1 , -1 ): # for (int i = strlen(string), strlen(sub); i > -1; i--)
        if string[i: i + len(sub)] == sub:    # the base case if when sub accur in the beginning we dont want tp cross teh string boundary
                 if i + len(sub) > len(string) - 1:
                     ans[i] = 1
                 else:
                     ans[i] = 1 + ans[i + len(sub)] # 1 +  whatever was at the ans[i + len(sub)]
    return max(ans)


def print_match(reader, actual):
    for line in reader:
        person = line[0]
        values = [ int(val) for val in line[1:] ] # get the value for the line starting from index 1 and covert it to int
        if values == actual:
            print(person)
            return
    print("NO MATCH")


def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # opening the csv file
    csv_path = argv[1]
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        # for row in reader:
        #     print(row)
        all_sequences = next(reader)[1:] # take out the header and store it in all_sequences excluding the first column

    # open the sequenes file
        txt_path = argv[2]
        with open(txt_path) as txt_file:
            string = txt_file.read()
            actual = [get_max_num_of_times_substring (string, seq) for seq in all_sequences]

        print_match(reader, actual)




if __name__ == "__main__":
    main()