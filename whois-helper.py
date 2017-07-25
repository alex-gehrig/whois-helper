#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import subprocess
import time

# the file which contains ip-addresses and number of occurance must be
# specified when calling the script. if not, there is a little error-
# message and the script terminates
try:
    inputfile = sys.argv[1]
except:
    print("""
    Error! You must provide a file as input like this:
    python3 whois-helper.py addresses.txt
    """)
    sys.exit()

# create and open a file to write the results in
outputfile = open("results.csv", "w")

# declare needed variables for later
countrycode = None
description = None

# writing a headline in the file for the results
outputfile.write("\"frequency\",\"IP-address\",\"countrycode\",\"description\"\n")

with open(inputfile) as source:
    for line in source:
        line = line.strip()
        # split the number of occurance and ip-address
        pieces = line.split(' ')
        # the command to execute
        command = subprocess.Popen(['whois', pieces[1]], stdout = subprocess.PIPE)
        # print-statement for the user
        print("whois-query for:", pieces[1])

        # write the number of occurance and the ip-address in the file for the results
        outputfile.write("\"" + str(pieces[0]) + "\"," + "\"" + str(pieces[1]) + "\",")

        # looping through the result of the whois-query
        for line in command.stdout:
            tmp_list = []
            line = line.strip().decode('UTF-8')

            if line.startswith("country:") or line.startswith("Country:"):
                pieces = line.strip().split(":")
                countrycode = pieces[1].strip()

            if line.startswith("descr:") or line.startswith("OrgName") or line.startswith("owner:"):
                pieces = line.strip().split(":")
                tmp_list.append(pieces[1].strip())
                # usually there is more than one line matching the current
                # pattern, but I want only the first one
                description = tmp_list[0]

        # write countrycode and description to the file for the results
        outputfile.write("\"" + str(countrycode) + "\",")
        outputfile.write("\"" + str(description) + "\"")

        # Setting the variables to "None" again, in case an incorrect ip-address is queried
        # otherwise the data of the previous ip-address would be written again
        countrycode = None
        description = None

        # adding the line break
        outputfile.write("\n")

        # wait for 5 seconds in order not to get blocked
        time.sleep(2)

# close the file for the results
outputfile.close()
