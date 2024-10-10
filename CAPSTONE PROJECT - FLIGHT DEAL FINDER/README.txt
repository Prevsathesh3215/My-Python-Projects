This is a readme explaining the project in detail: 

This project was done as a project in Day 40 of Dr. Angela Yu's 100 days of Python course. It involves finding the cheapest flight 
details from Kuala Lumpur to five locations, which are Paris, Frankfurt,Tokyo, Hong Kong, and Istanbul.

Requirements of project:
1. Find the cheapest flight deals from KUL to all five countries in a 3 day span starting from the current day. 
2. Once data obtained, process and send to Google Sheets spreadsheet for record-storing. 
3. If price of flight obtained lesser than data in spreadsheet record, send email to all emails saved in another spreadsheet. 

Packages used:
requests
pandas
gspread
smptlib
matplotlib.pyplot
datetime

APIs used:
Amadeus' Flight Offer API(Test environment)
