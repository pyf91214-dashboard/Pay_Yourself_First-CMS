import re

with open('how-we-help-you.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Mastering Card 1
content = re.sub(
    r'<img src="How-we-help-you/Mastering Three Things_Earn More\.jpg"',
    r'<img :src="pageData.mastering.card1.image || \'How-we-help-you/Mastering Three Things_Earn More.jpg\'"',
    content
)

# 2. Mastering Card 2
content = re.sub(
    r'<img src="How-we-help-you/Mastering Three Things_Save More\.jpg"',
    r'<img :src="pageData.mastering.card2.image || \'How-we-help-you/Mastering Three Things_Save More.jpg\'"',
    content
)

# 3. Mastering Card 3
content = re.sub(
    r'<img src="How-we-help-you/Mastering Three Things_Spend Less\.jpg"',
    r'<img :src="pageData.mastering.card3.image || \'How-we-help-you/Mastering Three Things_Spend Less.jpg\'"',
    content
)

# 4. Designed For Main Image
content = re.sub(
    r'<img src="How-we-help-you/PYF Is Designed For\.jpg"',
    r'<img :src="pageData.designed_for.image || \'How-we-help-you/PYF Is Designed For.jpg\'"',
    content
)

# 5. Three Ways Card 1
content = re.sub(
    r'<img src="How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees\.jpg"',
    r'<img :src="pageData.three_ways.card1.image || \'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg\'"',
    content
)

# 6. Three Ways Card 2
content = re.sub(
    r'<img src="How-we-help-you/PYF Helps You Move Foward_save money on everyday living \.jpg"',
    r'<img :src="pageData.three_ways.card2.image || \'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg\'"',
    content
)

# 7. Three Ways Card 3
content = re.sub(
    r'<img src="How-we-help-you/PYF Helps You Move Foward_support for you home based business\.jpg"',
    r'<img :src="pageData.three_ways.card3.image || \'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg\'"',
    content
)

with open('how-we-help-you.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("regex replace complete")
