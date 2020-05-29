import sys
import csv


def main():

    # get command line arguments
    inputdatabase = sys.argv[1]
    inputsequence = sys.argv[2]

    # open database file
    csvfile = open(inputdatabase, newline='')
    databaseobj = csv.reader(csvfile)
    # load database into array
    database = []
    for row in databaseobj:
        database.append(row)

    # open sequence file
    txtfile = open(inputsequence)
    sequence = txtfile.read()

    # initialise array to store max counts of each STR in the sequence
    STRset = [0] * (len(database[0]) - 1)

    # for each STR in the csv header row
    for i in range(1, len(database[0])):
        # get number of consecutive STRs for the sequence
        STRset[i - 1] = count(database[0][i], sequence)

    # for each name row in the database
    for i in range(1, len(database)):

        # default match is true
        match = True

        # iterate through each STR count
        for j in range(1, len(database[i])):
            # check against STRset
            if int(database[i][j]) != STRset[j - 1]:
                # set match to false if not equal
                match = False
        # if all counts match the set, print the name in database and stop program
        if match == True:
            print(database[i][0])
            return 0

    # if no matches, print No Match
    print("No match")


# function to calculate the highest number of consecutive repeats of a given STR for a given string (sequence)
def count(STR, sequence):

    # create array to store number of repeats for each position in the sequence
    repeats = [None] * len(sequence)

    # iterate through each character in the sequence
    for i in range(len(sequence)):
        # calculate how many repeats of the STR appear consecutively from this point and update repeats array
        repeats[i] = STRcheck(i, sequence, STR)

    # get highest number of repeats anywhere in the sequence
    return (max(repeats))


# function to calculate how many consecutive repeats of an STR there are at a given position in a sequence
def STRcheck(position, sequence, STR):
    # initialise counter
    count = 0
    # check if first 4 characters match the STR
    if sequence[position:position + len(STR)] == STR:
        # update counter
        count += 1
        # recall STRcheck from this position
        count += STRcheck(position + len(STR), sequence, STR)

    return count


main()