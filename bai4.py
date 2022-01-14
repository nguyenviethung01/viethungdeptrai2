NameId = input("Tên và ID của em là:")
print ("", NameId);

import re
ID = re.sub(r'\D','', NameId);
print(ID)

sub_string = NameId[0:14]
print(sub_string)
