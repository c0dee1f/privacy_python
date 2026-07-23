all_columns = [
    'user_id', 'email_address', 'created_at', 'user_ip_address',
    'account_status', 'home_address', 'phone_number',
    'last_login_date', 'ssn_number', 'preferred_theme'
]
pii_keywords = ['email', 'ip', 'address', 'phone', 'ssn']
flagged_pii = []
public_fields = []

for column in all_columns:
    for keyword in pii_keywords:
        # If a keyword is found in the current column name, add
        # the column name to the flagged_pii list and break
        if keyword in column:
            flagged_pii.append(column)
            break    
    # If the flagged_pii list is empty or its last element doesn't match
    # our column name, add the column name to the public_fields list
    if not flagged_pii or flagged_pii[-1] != column:
        public_fields.append(column)

for field in flagged_pii:
    print(f"[WARNING] Flagged PII Field: {field}")

print(f"\nTotal number of Flagged PII Fields: {len(flagged_pii)}")
print(f"Total number of Safe Fields: {len(public_fields)}")