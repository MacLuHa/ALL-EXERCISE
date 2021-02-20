import re
text="""Москва: 777, 999, 797.
        Тула: 071, 950, 112.."""
m=re.findall("\d",text,re.IGNORECASE)
print(m)
    
