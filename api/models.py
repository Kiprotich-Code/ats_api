from django.db import models

# Create your models here.
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]

    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    applied_on = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    result = models.TextField(blank=True, null=True)  # Optional, for interview results
    application_deadline = models.DateField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"