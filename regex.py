import pyperclip, re

# Create PhoneNumber regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                      # Area Code
    (\s|-|\.)?                              # Separator
    (\d{3})                                 #first 3 digits
    (\s|-|\.)                               # separator
    (\d{4})                                 # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# Create Email Regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                       # Username
    @                                       # @ symbol
    [a-zA-Z0-9.-]+                          # Domain name
    (\.[a-zA-Z]{2,4})                       # dot- something
    )''', re.VERBOSE)

    


# TODO: Find matches in the clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])
    

# TODO: Copy results to the clipboard.

if len(matches)> 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addrssed found.')
    
