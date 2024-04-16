# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def sent(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
#
# data = input()
# while data != "Stop":
#     sender, receiver, content = data.split()
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     data = input()
#
# indexes = [int(el) for el in input().split(", ")]
# for index, email in enumerate(emails):
#     if index in indexes:
#         emails[index].sent()
#     print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}")

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    data = input().split()
    if data[0] == "Stop":
        break

    sender, receiver, content = data
    email = Email(sender, receiver, content)
    emails.append(email)

indexes = [int(number) for number in input().split(", ")]
for index in indexes:
    if 0 <= index < len(emails):
        emails[index].sent()
for email in emails:
    print(email.get_info())