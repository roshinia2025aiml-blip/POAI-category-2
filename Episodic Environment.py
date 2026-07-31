emails = [
    "Free Gift",
    "Project Meeting",
    "Lottery Winner",
    "Assignment Submission",
    "Discount Offer"
]

print("=== EMAIL FILTER ===")

for email in emails:

    if "Free" in email or "Lottery" in email or "Discount" in email:
        print(email, "-> SPAM")

    else:
        print(email, "-> SAFE")
