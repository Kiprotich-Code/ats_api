from rest_framework import serializers
from .models import JobApplication


# serializers 
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job_title', 'company', 'applied_on', 'status', 'result', 'application_deadline', ]