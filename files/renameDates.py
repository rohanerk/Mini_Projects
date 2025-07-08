import shutil,os,re

datePattern = re.compile(r"""^(.*?)   # ALL text before the date
                ((0|1)?\d)-           # one or two digits for the month
                ((0|1|2|3)?\d)-       # one or two digits for the day
                ((19|20)\d\d)         # four digits for the year
                (.*?)$                # all the text after the date
                """,re.VERBOSE)


# Loop over the files in the working directory

for filename in os.listdir('.'):
    mo = datePattern.search(filename)

    # Skip files without a date
    if mo == None:
        continue
    # Get the different parts of the filename.

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename

    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart '-'+ afterPart

    absWorkingDir = os.path.abspath('.')
    filename = os.path.join(absWorkingDir,filename)
    euroFileName = os.path.join(absWorkingDir,euroFileName)

    # Rename the files

    print('Renaming "%s" to "%s"...' % (filename,euroFileName))
    shutil.move(filename,euroFileName)
