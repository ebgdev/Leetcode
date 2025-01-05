class Solution:
    def isNumber(self, s: str) -> bool:        
        try:
            float(s)
        except:
            return False
        else:
            forbiden = ["inf","-inf","+inf","Infinity","-Infinity","+Infinity","nan"]
            if s in forbiden:
                return False
            else:
                return True


# ---------------------------------------

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Strip any leading/trailing spaces
        s = s.strip()
        
        # Regex pattern to match a valid number
        # This pattern handles integer, decimal, and scientific notation (with 'e' or 'E')
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        
        return bool(re.match(pattern, s))

       