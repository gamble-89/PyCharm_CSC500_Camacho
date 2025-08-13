# OR Operator Example: Checking if a customer is eligible for a 10% discount (military, teacher, or first responder)
military_chk = input("Are you a military veteran? (yes/no): ").lower() == "yes"
teacher_chk = input("Are you an educator? (yes/no): ").lower() == "yes"
responder_chk = input("Are you a first responder? (yes/no): ").lower() == "yes"
if military_chk or teacher_chk or responder_chk:
    print("Discount of 10% will be applied, Thank you!")
else:
    print("Ineligible for discount")
