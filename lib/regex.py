
import re

my_regex = re.compile(
    r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
)

def match_string(string):
    return my_regex.fullmatch(string)
