# indexing = accessing elements of a sequence using []
# [begin:end:step] = slicing
# begin = start index (inclusive)
# end = end index (exclusive)
# step = how many characters to skip
# starting index is inclusive, ending index is exclusive
# indexing starts at 0
# negative indexing starts at -1

credit_card = "1234-5678-9012-3456"
print(credit_card[0])  # First character
print(credit_card[1])  # Second character
print(credit_card[-1])  # Last character
print(credit_card[-2])  # Second to last character
print(credit_card[0:4])  # First four characters
print(credit_card[5:9])  # Characters from index 5 to 8
print(credit_card[0:16:4])  # Every fourth character from the start
print(credit_card[::2])  # Every second character
print(credit_card[::-1])  # Reverse the string
print(credit_card[::])  # Copy the string

# Get the last four digits of the credit card number and display it in ****-****-****-3456 format
last_four = credit_card[-4:]  # Get the last four digits
masked_credit_card = "****-****-****-" + last_four
print(masked_credit_card)  # Display the masked credit card number