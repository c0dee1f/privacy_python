db_columns = ['user_id', 'raw_email', 'signup_date', 'ip_address', 'account_status']

# Isolate high-risk network PII in standalone variable
sensitive_field = db_columns.pop(3)

# Rename email column following use of sanitization script
db_columns[1] = "canonical_email"

# Add new column for compliance field to track user consent
db_columns.append("consent_status")

# Sort columns in reverse alphabetical order for engineering report documentation
db_columns.sort(reverse=True)

print("REPORT FINDINGS")
print("===============")
print(f"Total number of columns in database table: {len(db_columns)}")
print(f"Sorted list of columns: {db_columns}")
print(f"Isolated sensitive field: {sensitive_field}")