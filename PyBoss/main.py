'''In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
Then convert and export the data to use the following format instead:
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
In summary, the required conversions are as follows:

The Name column should be split into separate First Name and Last Name columns.
The DOB data should be re-written into DD/MM/YYYY format.
The SSN data should be re-written such that the first five numbers are hidden from view.
The State data should be re-written as simple two-letter abbreviations.'''

import os
import csv
import us_state_abbrev
from us_state_abbrev import us_state_abbrev


# Like a boss
def flyIntoTheSun(filename):
    # File must be in the raw_data folder
    csvpath = os.path.join('raw_data', filename)

    # Declare some empty lists
    outputs = []
    eID = []
    fName = []
    lName = []
    dob = []
    ssn = []
    state = []

    # Open our csv file
    with open(csvpath, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')

        for row in csvreader:

            # Don't do things to the header row
            if (row[1] == "Name"):
                pass

            # Do things to not the header row
            else:
                # Take employee ID
                eID.append(row[0])

                # Take first and last name
                firstName, lastName = row[1].split(" ")
                fName.append(firstName)
                lName.append(lastName)
                
                # Take Date of Birth
                yyyy, mm, dd = row[2].split("-")
                dob.append(mm + "/" + dd + "/" + yyyy)
                
                # Take SSN and * out the first five digits
                ssns = row[3].split("-")
                socsec = "***-**-" + ssns[2]
                ssn.append(socsec)
                
                # Take State and make it two letter abbv
                states = row[4]
                state.append(us_state_abbrev[states])
    
    # zip everything up into a nice tuple to output
    outputs = zip(eID,fName,lName,dob,ssn,state)

    # And now we output
    outputFile = "raw_data\\" + filename[:-4] + "_cleaned.csv"
    with open(outputFile, "w", newline="", encoding="utf-8") as datafile:
        writer = csv.writer(datafile)

        # Header
        writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
        
        # Data
        writer.writerows(outputs)

    # Let the user know what's up
    print("raw_data\\" + filename + " has been cleaned and saved as " + outputFile)

flyIntoTheSun("employee_data1.csv")
flyIntoTheSun("employee_data2.csv")