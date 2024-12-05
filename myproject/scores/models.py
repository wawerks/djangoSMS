from django.db import models
from twilio.rest import Client

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)
        
        if self.result >= 75:
            message = client.messages.create(
                body="You've Passed",
                from_="",
                to="",
            )
            print(message.body)
        elif self.result < 75: 
            message = client.messages.create(
                body="You've Failed",
                from_="",
                to="",
            )
            print(message.body)
        
        return super().save(*args, **kwargs)
