def show_messages(messages):
    print(f"Here is a list of your messages:")
    for message in messages:
        print(message)
def send_messages (messages,sent_messages):
    while messages:
        message=messages.pop()
        sent_messages.append(message)


message_list=["oh wow",'this is cool',"isn't it?"]
sent_list=[]

send_messages(message_list[:],sent_list)
print("Message list:")
show_messages(message_list)
print("Sent message list:")
show_messages(sent_list)