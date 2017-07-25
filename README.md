# whois-helper
Python-script for making whois-queries of ip-addresses stored in a textfile. Produces a csv-file as output.<br>
Needs the program 'whois' to be installed on Linux!

# Introduction
Let's assume you have a look in your website's logfiles and you are interested in which ip-addresses can be found there, how often they occur and of course where they come from.

This is a task that can be completely done using the linux-bash. At first you have to extract the ip-addresses using 'egrep' followed by 'sort' and 'uniq' respectively 'uniq -c'. Then you have to use 'awk' (at least this is how I would do that) to perform a whois-query for every ip-address found. And in the end, you need a way to look through your results.

This little python-script can offer some help.

# Usage
As written above this script is intended to be used under Linux with the program 'whois' installed and usable. You must have a document containing the frequency and the corresponding ip-address (one per line). This is how the output looks like when you perform the steps noted above (egrep, sort, uniq -c).

Now you can use the script via:<br>
python3 whois-helper.py addresses.txt

In this example the file 'addresses.txt' contains the ip-addresses. If you forget to specify an input-file the script tells you about that and terminates.

# What you get
The result of the script will be a csv-file called 'results.csv'. I contains the frequency as column no. 1, the ip-address as column no. 2, the country-code as column no. 3 and the description of the owner of the ip-address als column no. 4.

I have tested the script with different ip-addresses from RIPE, ARIN, LACNIC, APNIC an AFRINIC, as the results of the whois-queries are slightly different. But the script should match in every case. At least it did during my tests.

If an ip-address is checked which is not valid, you will see 'None' as entry for the country-code and description of the owner of the ip-address.
