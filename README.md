# 1. Phone Number and Email Extractor

# 📞📧 Phone Number and Email Address Extractor

This is a Python script that extracts phone numbers and email addresses from a block of text using regular expressions (regex). It is useful for scanning documents, webpages, or files to automatically collect contact details.

## Features

- Extracts phone numbers with or without country codes (e.g., +1 415-863-9900, 800-420-7240)
- Extracts email addresses (e.g., info@example.com)
- Supports common formats with dashes, spaces, parentheses, or dots
- Outputs results in a clean, labeled format

## Example Input

No Starch Press, Inc.  
Phone: 800-420-7240 or +1 415-863-9900  
Fax: +1 415-863-9950  

Emails:  
info@nostarch.com  
sales@nostarch.com

## Example Output

Phone: 800-420-7240  
Phone: +1-415-863-9900  
Phone: +1-415-863-9950  
Email: info@nostarch.com  
Email: sales@nostarch.com

## How It Works

- Uses Python’s `re` module to define patterns for phone numbers and email addresses
- Uses `.findall()` to locate all matches
- Formats and prints the results with labels


# 2. 🔐 Strong Password Validator

This Python script checks whether a given password is strong based on commonly accepted criteria. It uses regular expressions to validate the presence of lowercase and uppercase letters, digits, and enforces a minimum length.

---

## ✅ Password Strength Criteria

A strong password must:

- Be at least **8 characters long**
- Contain **at least one lowercase letter**
- Contain **at least one uppercase letter**
- Contain **at least one digit**

---

## ⚙️ How It Works

The script defines a function called `strongpassword()` that:

1. Prompts the user to enter a password
2. Uses the `re` (regular expressions) module to search for:
   - Lowercase letters `[a-z]`
   - Uppercase letters `[A-Z]`
   - Digits `\d`
3. Prints a specific error message if any condition fails
4. Confirms the password is strong if all rules pass

---



# 3📝 Random Quiz Generator

This Python script generates multiple randomized quiz files along with their answer keys. Each quiz tests knowledge of U.S. state capitals, with the order of the questions and answer options randomized to ensure each quiz is unique.

## 📌 Features

- Generates multiple quiz versions (default: 35)
- Creates separate answer keys for grading
- Randomizes:
  - The order of the states
  - The placement of the correct answer among the options
- Saves files neatly in a specified output directory

## 📂 File Output

Each run will generate:
- `capitalsquiz1.txt`, `capitalsquiz2.txt`, ..., `capitalsquiz35.txt` — quiz files
- `capitalsquiz_answer1.txt`, ..., `capitalsquiz_answer35.txt` — answer keys
