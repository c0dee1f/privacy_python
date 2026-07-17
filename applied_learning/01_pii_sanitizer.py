raw_email = "   ALICE.SMITH@Example.Org   "
raw_name = "   aLiCe sMiTh "
raw_phone = "(555) 019-2831 "

clean_email = raw_email.strip().lower()
clean_name = raw_name.strip().title()
clean_phone = (
    raw_phone.strip()
    .replace(" ", "")
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
)

print("Sanitization Results")
print("====================")
print(f"{raw_name} ==> {clean_name}")
print(f"{raw_email} ==> {clean_email}")
print(f"{raw_phone} ==> {clean_phone}")