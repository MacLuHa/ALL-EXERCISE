import re
string="Привидение прошуршало и исчезло в лесу"
m=re.findall("[a-з]ло",string,re.IGNORECASE)
print(m)
