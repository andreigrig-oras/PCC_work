usernames=("admin",'mark','anthony','maria','georgia')
new_users=["Mark","George","maria","rupert","harry", "admin"]

#username="mark"
#if usernames:
#    if username in usernames:
#        if username=="admin": print ("Hello Admin, would you like a status update?")
#        else: print (f"Hello {username.title()}, thank you for logging in again")
#else: print("We need users")
for new_user in new_users:
    if new_user.lower() in usernames:
        print (f"Please choose a different log in name, {new_user.title()}")
    else: print (f"This log in name is available, {new_user.title()}")