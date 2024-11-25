from django.db import models

class Request(models.Model):
    DateTime = models.DateTimeField(auto_now_add=True)
    PlayerID = models.TextField()
    AccountTitle = models.TextField()
    AccountNumber = models.TextField()
    PaymentMethod = models.TextField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.TextField()
    def __str__(self):
        return f"Request {self.id} By User {self.PlayerID}"
