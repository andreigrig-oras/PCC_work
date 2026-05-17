#what do you think of the change?
import re
text="reddit@mister.com"
def validate_email(email):
    if re.match(r'[\w\.-]+@[\w\.-]+.com',email)!=None: print ("it is an email address")
    else: print("it is not an email address")
validate_email(text)