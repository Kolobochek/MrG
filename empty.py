import sys
output=""
with open("tq.txt") as f:
    for line in f:
        if not line.isspace():
            output+=line

f= open("tq.txt","w")
f.write(output)

output=""
with open("tq.txt") as f:
    for line in f:
        if "@" not in line:
            output+=line

f= open("tq.txt","w")
f.write(output)

output=""
with open("tq.txt") as f:
    for line in f:
        if "/" not in line:
            output+=line

f= open("tq.txt","w")
f.write(output)