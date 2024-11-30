from django.db import models
from twilio.rest import Client

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        account_sid = "ACc7e5f9c7b69dc3219b0c973c8b17aa6f"
        auth_token = "007efaaa8be27c0dd907720791683f0a"
        client = Client(account_sid, auth_token)
        
        if self.result >= 75:
            message = client.messages.create(
                body="You've Passed",
                from_="+19787881931",
                to="+639630986870",
            )
            print(message.body)
        elif self.result < 75: 
            message = client.messages.create(
                body="You've Failed",
                from_="+19787881931",
                to="+639630986870",
            )
            print(message.body)
        
        return super().save(*args, **kwargs)
