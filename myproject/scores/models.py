from django.db import models
import os
from twilio.rest import Client
# Create your models here.

class Score (models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = "ACc7e5f9c7b69dc3219b0c973c8b17aa6f"
            # Your Auth Token from twilio.com/console
            auth_token  = "007efaaa8be27c0dd907720791683f0a"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"Claim your Gcash Reward at https://www.facebook.com/61563448083479/videos/928556385699646",
                from_="+19787881931",
                to="+639630986870",
            )

            print(message.body)
        return super().save(*args, **kwargs)
