#!python3

# Project :- Reading data from a Spreadsheet

import openpyxl, pprint
print('Opening workbook')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

for row in range(2,sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # make sure the key for this state exists
    countyData.setdefault(state, {})

    # Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts':0, 'pop':0})

    # Each row represents 1 census tract
    countyData[state][county]['tracts'] += 1

    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

print('Writing Results')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
