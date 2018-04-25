#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import subprocess
import time

"""Takes a textfile with ip-adresses and their frequency as input, performs
whois-request using the Linux-Bash and produces a csv-output showing the
ip-address and the correspondign frequency, the countrycode and the owner
of the ip-address"""

# the file which contains the ip-addresses and number of occurance must be
# specified when calling the script. if not, there is a little error-
# message and the script terminates
try:
    inputfile = sys.argv[1]
except:
    print("""
    Error! You must provide a file as input like this:
    python3 whois-helper.py addresses.txt
    The script will be terminated now.
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
        cc_tmp_list = []
        desc_tmp_list = []
        # split the frequency and ip-address
        pieces = line.split(' ')
        # the command to execute
        command = subprocess.Popen(['whois', pieces[1]], stdout = subprocess.PIPE)
        # print-statement for the user
        print("whois-query for:", pieces[1])

        # write the number of occurance and the ip-address in the file for the results
        outputfile.write("\"{}\",\"{}\",".format(pieces[0], pieces[1]))

        # looping through the result of the whois-query
        for line in command.stdout:
            line = line.strip().decode('UTF-8')

            if line.startswith("country:") or line.startswith("Country:"):
                parts = line.strip().split(":")
                cc_tmp_list.append(parts[1].strip())

            if line.startswith("descr:") or line.startswith("OrgName") or line.startswith("owner:"):
                parts = line.strip().split(":")
                desc_tmp_list.append(parts[1].strip())

        # usually there is more than one line matching the current
        # pattern, but I want only the first ones
        countrycode = cc_tmp_list[0]
        description = desc_tmp_list[0]

        # write countrycode and description to the file for the results
        outputfile.write("\"{}\",\"{}\"\n".format(countrycode, description))

        # Setting the variables to "None" again, in case an incorrect ip-address is queried
        # otherwise the data of the previous ip-address would be written again
        countrycode = None
        description = None

        # wait for 3 seconds in order not to get blocked - hopefully
        time.sleep(3)

# close the file for the results
outputfile.close()
