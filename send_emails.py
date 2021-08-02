# #!/usr/bin/env python3
import os, sys
import smtplib, time

if not os.path.isfile ("participants.txt"):
    print ("File participants.txt does not exists.")
    sys.exit(1)

if not os.path.isfile ("offers_to.txt"):
    print ("File offers_to.txt does not exists. Use shuffle.py.")
    sys.exit(1)

with open("participants.txt", 'r') as f:
    participants = [ p for p in f ]
with open("offers_to.txt", 'r') as f:
    offers_to = [ p for p in f ]

if len(participants) != len(offers_to):
    print ("The lists do not have the same length. Did you use shuffle.py correctly?")
    sys.exit(1)

smtp = smtplib.SMTP ('mail.domain.com')

fromaddr = "Santa Claus <santa.claus@domain.com>"

bodyTpl = """Oh oh oh, hello {0} !

My little elves are overbooked this year, uh-oh!
Would you mind helping me? If you could buy {1} a little something, it would for sure save Christmas!

Oh oh oh !

Santa Clauss"""

subject = "Santa Class needs you!"

for src, dst in zip(participants, offers_to):
    participant = src.split(',')[0]
    toaddr = src.split(',')[1]
    if toaddr[-1] == "\n": toaddr = toaddr[:-1]
    toaddr = participant+" <"+toaddr+">"
    offer_to = dst.split(',')[0]
    offer_toaddr = dst.split(',')[1].strip()

    msg = ("From: {}\nTo: {}\nSubject: {}\nContent-Type: text/plain; charset=utf-8\n".format(fromaddr,toaddr,subject,'UTF-8'))
    msg += bodyTpl.format(participant, offer_to, 'UTF-8')

    # print(msg)
    res = smtp.sendmail(fromaddr, [toaddr], msg.encode("utf8")) #
    if res: print(res)
    time.sleep(1)

smtp.quit()
