# certification/forms.py
from django import forms
from .models import EmployeeRequest, Feedback

class EmployeeRequestForm(forms.ModelForm):
    class Meta:
        model = EmployeeRequest
        fields = ['name', 'department', 'reason_for_request']

class HRFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['recipient_name', 'recipient_email', 'sent_date', 'department', 'feedback_text']