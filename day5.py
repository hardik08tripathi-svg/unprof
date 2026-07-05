import re

# Function to extract information
def extract_information(text):
    # Email Pattern
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    # Phone Number Pattern (supports +91, spaces, hyphens)
    phone_pattern = r'(?:\+91[- ]?)?[6-9]\d{9}'

    # Date Pattern (DD/MM/YYYY, DD-MM-YYYY, YYYY-MM-DD)
    date_pattern = r'\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})\b'

    # Find matches
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    dates = re.findall(date_pattern, text)

    # Clean phone numbers (remove spaces and hyphens)
    cleaned_phones = []
    for phone in phones:
        phone = re.sub(r'[- ]', '', phone)
        cleaned_phones.append(phone)

    # Display Results
    print("\n========== Extracted Information ==========")

    print("\nEmail Addresses:")
    if emails:
        for email in emails:
            print("-", email)
    else:
        print("No email addresses found.")

    print("\nPhone Numbers:")
    if cleaned_phones:
        for phone in cleaned_phones:
            print("-", phone)
    else:
        print("No phone numbers found.")

    print("\nDates:")
    if dates:
        for date in dates:
            print("-", date)
    else:
        print("No dates found.")

    print("\n===========================================")


# Main Program
def main():
    print("====== Text Information Extractor ======")
    print("Paste your text below.")
    print("Type 'END' on a new line when finished.\n")

    lines = []

    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)

    text = "\n".join(lines)

    extract_information(text)


if __name__ == "__main__":
    main()
