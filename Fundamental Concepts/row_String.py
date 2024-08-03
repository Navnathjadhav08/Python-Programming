import sys
sys.path.append(R'\Users\NAVNATH\OneDrive\Desktop\Py\assignments\modules')

"""Raw String
If you need to specify some strings where no special processing such as escape
sequences are handled, then what you need is to specify a raw string by prefixing r or
R to the string"""

"""
Always use raw strings when dealing with regular expressions.
Otherwise, a lot of backwhacking may be required. For example,
backreferences can be referred to as '\\1' or r'\1' ."""