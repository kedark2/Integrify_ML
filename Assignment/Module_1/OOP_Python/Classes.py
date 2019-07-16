class Mail:
    def __init__(self):
        self.inbox = 0
        self._sent = 0
        self._not_recommended_getter_var = 0

    @property
    def inbox(self):
        return self._inbox

    @inbox.setter
    def inbox(self, val):
        if val >= 0:
            self._inbox = val
        else :
            print("Please see the inbox email count to non-negative number!")

    def not_recommended_getter(self):
        return self._not_recommended_getter_var

    def send_mail(self, num=1):
        self._sent += num
        print(f"Message sent! You have {self.sent} mails in Sent")
    def receive_mail(self, num = 1):
        self._inbox += num
        print(f"New email! You have {self._inbox} emails")




a = 1
a_f = 1.0


