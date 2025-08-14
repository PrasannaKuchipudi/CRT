#14-08-2025 
#Regular Expressions - Collection of characters 
#1.[] - It represents characters.
#e.g:"[a-z]" 
#2. \ - It represents the special sequence. 
#e.g:"\r" 
#3. . - It signals that any character is present at some specific place. 
#e.g: "Ja.v." 
#4. ^ - It represents the pattern present at the begining of the string. 
#e.g: "^Python"
#5. $ - It represents the pattern present at the end of the string. 
#e.g: "python" 
#6. * - It represents zero or more occurence of a pattern in the string.
#e.g: "hello*" 
#7. + - It represents one or more occurence of a pattern in the string. 
#e.g: "hello+" 
#8. {} - The specified number of occurences of a pattern in the string. 
#e.g: "python{2}" 
#9. | - It represents either this or that character is present. 
#e.g: "hello | python*" 
#findall() - Search the given sentence from left to right
#Examples 
import re 
p=re.compile(r'\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
p=re.compile(r'\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
#Special Sequences 
#\A : It returns a match if the specified characters are present at the begining of the string. 
#\b : It returns a match if the specified characters are present at the begining of the string or the end of the string. 
#\B : It returns a match if the specified characters are present at the begining of the string but not at the end. 
#\d : It returns a match if the string contains digits [0-9].
#\D : It returns a match if the string doesn't contains digits [0-9].
#\s : It returns a match if the string contains any white space character. 
#\S : It returns a match if the string doesn't contain any white space character. 
#\w : It returns a match if the string contains any word characters. 
#\Z : Returns a match if the specified characters are at the end of the string.  
#[arn] : Returns a match if the string contains any of the specified characters in the set. 
#[a-n] : Returns a match if the string contains any of the characters between a to n. 
#[^arn] : Returns a match if the string contains the characters except a,r, and n. 
#[0123] : Returns a match if the string contains any of the specified digits. 
#[0-9] : Returns a match if the string contains any of the digits between 0 to 9. 
#[0-5] [0-9] : Returns a match if the string contains any digit between 00 and 59. 
import re 
p=re.compile(r'[a-e]') 
print(p.findall("Aye, said Mr. Gibenson Stark"))
import re 
p=re.compile(r'[A-z 0-9+]') 
print(p.findall("Aye, said Mr. Gibenson STARK 99"))
import re 
p=re.compile(r'[A-z 0-9]+') 
print(p.findall("Aye,said Mr. Gibenson STARK 99"))
import re 
p=re.compile(r'[A-z \d]+') 
print(p.findall("Aye,said Mr. Gibenson STARK 99"))  
#Example-1 : Match
import re 
def findMonthAndDate(string):
    regex=r"([a-zA-z]+) (\d+)"
    match=re.match(regex,string)
    if match==None:
        print("Not a valid date")
        return
    print(f"Given Data: {(match.group())}")
    print(f"Month: {(match.group(1))}")
    print(f"Day: {(match.group(2))}")
findMonthAndDate("Jun 24")
print('')
findMonthAndDate("I was born on Jun 24")
print('')
findMonthAndDate("Jun 12 2024")
#Example-2 :SEARCH
import re 
def findMonthAndDate(string):
    regex=r"([a-zA-z]+) (\d+)"
    match=re.search(regex,string)
    if match==None:
        print("Not a valid date")
        return
    print(f"Given Data: {(match.group())}")
    print(f"Month: {(match.group(1))}")
    print(f"Day: {(match.group(2))}")
findMonthAndDate("Jun 24")
print('')
findMonthAndDate("I was born on Jun 24")
print('')
findMonthAndDate("Jun 12 2024")
#Example-3:Search without function
import re 
regex=r"([a-zA-Z]+) (\d+)"
match=re.search(regex,"I was born on June 24")
if match is not None:
    print(f"Match at index {match.start()}, {match.end()}")
    print(f"Full match: {match.group()}")
    print(f"Month: {match.group(1)}")
    print(f"Date: {match.group(2)}")
else:
    print("The regex pattern does not match.")