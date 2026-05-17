def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

me=build_profile('andrei','grigoras',location='home',field='grass',funny='no')
print (me)