import re

with open('how-we-help-you.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the escaped quotes
content = content.replace(r"\'How-we-help-you/Mastering Three Things_Earn More.jpg\'", "'How-we-help-you/Mastering Three Things_Earn More.jpg'")
content = content.replace(r"\'How-we-help-you/Mastering Three Things_Save More.jpg\'", "'How-we-help-you/Mastering Three Things_Save More.jpg'")
content = content.replace(r"\'How-we-help-you/Mastering Three Things_Spend Less.jpg\'", "'How-we-help-you/Mastering Three Things_Spend Less.jpg'")

content = content.replace(r"\'How-we-help-you/PYF Is Designed For.jpg\'", "'How-we-help-you/PYF Is Designed For.jpg'")

content = content.replace(r"\'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg\'", "'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg'")
content = content.replace(r"\'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg\'", "'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg'")
content = content.replace(r"\'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg\'", "'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg'")

with open('how-we-help-you.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed syntax error")
