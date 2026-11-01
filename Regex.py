# REGEX QUESTIONS PRACTICE SUBTOPICS WISE 
# SUBTOPIC 1
# RE module basics
# q1
import re
text = "Python is fun. I love Python programming."
resultoftext = re.search("Python",text)
print(resultoftext)
print(re.fullmatch("Python", "Python"))
print(re.match("Python", text))
resultoftext = re.search("Java",text)
if resultoftext:
    print("FOUND")
else:
    print("NONE")
resultoftext = re.search("fun", text)
print(resultoftext.start())
print(resultoftext.end())
resultoftext = re.findall("Python",text)
print(len(resultoftext))

# SUBTOPIC 2: RAW STRINGS + LITERAL MATCHING
# q1
text = "Price is 3.14 or 3x14"
result = re.findall(r"3\.14",text)
print(result)
# q2
text = "Price is 3.14 or 3x14"
resultt = re.findall("3.14",text)
print(resultt)
# q3
words = "C:\new\table"
print(words)
W = r"C:\new\table"
print(W)
# q4
text = "Total: $50 (approx)"
res = re.search(r"\$50",text)
print(res)
R = re.search(r"\(approx\)",text)
print(R)
# q5
text = "Python python PYTHON"
T = re.findall("python",text)
print(T)

# SUBTOPIC 3: . ^ $
# q1
import re
text = "cat cot cut ct cart"
print(re.findall(r"c.t",text))

# q2
text = "Python is fun"
print(re.search(r"^Python",text))

# q3 1part
text = "Python is fun"
resulttt = re.search(r"fun$",text)
if resulttt :
    print("found")
else:
    print("not found")

# q3 part2 
text = "Python is fun"
RESULT = re.search(r"Python$",text)
if RESULT:
    print("found")
else:
    print("not found")

# q4 part1
text1 = "hello"
print(re.search(r"^.....$",text1))

# q4 part2
text2 = "hi"
print(re.search(r"^.....$",text2))

# q4 part3
text3 = "hello!"
print(re.search(r"^.....$",text3))

# q5
TEXT = text = "abc a.c"
print(re.findall(r"a\.c",TEXT))

# SUBTOPIC 4: CHARACTER CLASSES [ ]
# q1
import re
teXT = "Hello World, I am Learning Python"
print(re.findall(r"[aeiouAEIOU]",teXT))

# q2
tExt = "Order 2026 shipped"
print(re.findall(r"[0-9]",tExt))

# q3
texxt = "gray grey groy graY"
print(re.findall(r"gr[ae]y",texxt))

# q4
TEXXXT = "Hi! How are you? 100%"
print(re.findall(r"[^a-zA-Z0-9 ]",TEXXXT))

# q5
Teext = text = "a.b,c;d"
print(re.findall(r"[.,;]",Teext))

# q6
texTT = "a.b"
print(re.findall(r".", texTT))
print(re.findall(r"[.]", texTT))
print(re.findall(r"[\.]", texTT))

# SUBTOPIC 5 SHORTHAND CLASSES
# q1
import re
text = "Order 66 on 12 Oct 2026"
print(re.findall(r"\d",text))

# q2
text = "Hi! Ready? 2026"
print(re.findall(r"\W", text))

# q3
text = "a b\tc\nd"
print(re.findall(r"\s", text))

# q4
text = "cat concat cat. category"
print(re.findall(r"\bcat\b", text))
print(re.findall(r"cat", text))

# q5
text = "Total 3.14 and 2.5"
print(re.findall(r"[\d.]", text))

# SUBTOPIC 6: QUANTIFIERS
# q1
import re
text = "Order 66 on 12 Oct 2026"
print(re.findall(r"\d+", text))

# q2
text = "color colour colouur"
print(re.findall(r"colou?r", text))

# q3
text = "Call 9876543210 or 12345 or 98765432101"
print(re.findall(r"\b\d{10}\b",text))


# q4
text = "Hello, world 2026! Python_3"
print(re.findall(r"\w+", text))

# q5
text = "5kg 10 kg 7  kg 3Kg"
print(re.findall(r"\d+\s*kg",text))

# SUBTOPIC 7: GREEDY vs LAZY
# q1 part1 
text = "<p>Hello</p><p>World</p>"
print(re.findall(r"<p>.+</p>", text))

# q1 part 2
text = "<p>Hello</p><p>World</p>"
print(re.findall(r"<p>.+?</p>", text))

# q2
text = 'He said "hi" and "bye"'
print(re.findall(r'".*?"', text))

# q3
text = "aXbYbZb"
print(re.search(r"a.*b", text).group())
print(re.search(r"a.*?b", text).group())

# q4
text = "123456"
print(re.search(r"\d{2,4}", text))
print(re.search(r"\d{2,4}?",text))

# q5
text = "<b>one</b> <i>two</i> <u>three</u>"
print(re.findall(r"<.+?>", text))
print(re.findall(r"<[^>]+>", text))

# SUBTOPIC 8A: GROUPS ( ), CORE IDEA
# q1
text = "Call 555-1234 now"
textitem = re.search(r"(\d+)-(\d+)",text)
print(textitem.group())
print(textitem.group(1))
print(textitem.group(2))
print(textitem.groups())

# q2
text = "Date: 2026-10-18"
info = re.search(r"(\d{4})-(\d{2})-(\d{2})",text)
print(info.group(1))
print(info.group(2))
print(info.group(3))

# q3
text = "Name: Rahul Age: 25"
personalinfo = re.search(r"Name: (\w+) Age: (\d+)",text)
print(personalinfo)
print(personalinfo.group(1))
print(personalinfo.group(2))

# q4
text = "ababab"
print(re.search(r"ab+",text).group())
print(re.search(r"(ab)+",text).group())

# q5
text = "no number here"
T = re.search(r"(\w+)-(\w+)-(\w+)",text)
print(T)
if T:
    print(T.group(1))
else:
    print("NOT FOUND")

#  SUBTOPIC 8B: findall + GROUPS, NAMED, NON-CAPTURING
# q1
text = "a@x.com b@y.com"
print(re.findall(r"\w+@\w+\.com",text))
print(re.findall(r"(\w+)@\w+\.com",text))
print(re.findall(r"(\w+)@(\w+)", text))

# q2
text = "Name: Rahul Age: 25"
t = re.search(r"Name: (?P<Name>\w+) Age: (?P<Age>\d+)",text)
print(t)
print(t.group("Name"))
print(t.group("Age"))
print(t.groupdict())

# q3
text = "2026-10-18 and 2026-11-05"
m = re.findall(r"\d+-(\d{2})-\d+",text)
print(m)

# q4
text = "ababab abab"
x = re.findall(r"(ab)+",text)
y = re.findall(r"(?:ab)+",text)
print(x)
print(y)

# q5
text = "Call 555-1234 or 666-9876"
number = re.findall(r"(\d{3})-(\d{4})",text)
print(number)

# SUBTOPIC 9: ALTERNATION |
# q1
text = "I have a cat, a dog and a bird"
print(re.findall(r"cat|dog", text))

# q2
text = "gray grey groy"
print(re.findall(r"gr(?:a|e)y", text))
print(re.findall(r"[ae]", text))

# q3
text = "category cat"
print(re.search(r"cat|category", text).group())
print(re.search(r"category|cat", text).group())

# SUBTOPIC 10: sub, split, finditer, compile
# q1
text = "Call 555-1234 or 666-9876"
print(re.sub(r"\d", "X", text))

# q2
text = "apple,banana;cherry orange"
print(re.split(r"[,; ]",text))

# q3
text = "2026-10-29"
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})",r"\3/\2/\1", text))

# q4
text = "cat bat rat"
for words in re.finditer(r"(\w+)",text):
    print(words.groups(),words.start())

# q5
text = "a1 b22 c333"
pattern = re.compile(r"\d+")
print(pattern.findall(text))
print(pattern.sub("#",text))


# SUBTOPIC 11: FLAGS
# q1
text = "Python python PYTHON"
print(re.findall(r"Python",text,re.IGNORECASE))

# q2
text = "Cat cat CAT"
print(re.sub(r"cat","Dog",text,flags=re.I))

# q3
text = "Error: disk\nInfo: ok\nError: net"
print(re.findall(r"^Error.*",text,flags=re.M))

# q4
text = "a\nb"
print(re.search(r"a.b",text,flags=re.S))

# q5
text = "Cat\ncat\nCAT\ndog"
print(re.findall(r"^cat",text,flags=re.I | re.M))



























