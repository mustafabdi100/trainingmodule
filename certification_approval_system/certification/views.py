# certification/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from .models import EmployeeRequest, Feedback,BondAgreement
from .forms import EmployeeRequestForm, HRFeedbackForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

employee_required = user_passes_test(is_employee, login_url='custom_login')

def is_hr(user):
    return user.groups.filter(name='HR').exists()

hr_required = user_passes_test(is_hr, login_url='custom_login')

def is_finance(user):
    return user.groups.filter(name='Finance').exists()

finance_required = user_passes_test(is_finance, login_url='custom_login')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Employee').exists():
                return redirect('employee_dashboard')
            elif user.groups.filter(name='HR').exists():
                return redirect('hr_dashboard')
            elif user.groups.filter(name='Finance').exists():
                return redirect('finance_dashboard')  # Replace with actual finance dashboard URL
        else:
            # Invalid login
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'certification/login.html')
    return render(request, 'certification/login.html')

@employee_required
def employee_dashboard(request):
    employee_requests = EmployeeRequest.objects.filter(status='Approved')
    
    # Dummy email to filter feedbacks (you can change it to any value you want)
    dummy_email = 'dummy@example.com'
    feedbacks = Feedback.objects.filter(recipient_email=dummy_email)
    
    context = {
        'employee_requests': employee_requests,
        'feedbacks': feedbacks,
    }
    return render(request, 'certification/employee_dashboard.html', context)

@employee_required
def approved_requests(request):
    approved_requests = EmployeeRequest.objects.filter(status='Approved')
    return render(request, 'certification/approved.html', {'approved_requests': approved_requests})

@employee_required
def pending_requests(request):
    requests = EmployeeRequest.objects.filter(status='Pending')
    return render(request, 'certification/pending.html', {'requests': requests})

@employee_required
def declined_requests(request):
    declined_requests = EmployeeRequest.objects.filter(status='Declined')
    return render(request, 'certification/declined.html', {'declined_requests': declined_requests})

@employee_required
def new_request(request):
    if request.method == 'POST':
        form = EmployeeRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pending_requests')  # Corrected URL pattern name
    else:
        form = EmployeeRequestForm()

    return render(request, 'certification/new_request.html', {'form': form})

@hr_required
def hr_dashboard(request):

  all_requests = EmployeeRequest.objects.all()  
  pending_requests = EmployeeRequest.objects.filter(status='Pending')
  approved_requests = EmployeeRequest.objects.filter(status='Approved')
  declined_requests = EmployeeRequest.objects.filter(status='Declined')

  context = {
    'all_requests': all_requests,
    'pending_requests': pending_requests,
    'approved_requests': approved_requests, 
    'declined_requests': declined_requests
  }

  return render(request, 'certification/hr_dashboard.html', context)

@hr_required
def hr_all_requests(request):
  all_requests = EmployeeRequest.objects.all()

  context = {
    'all_requests': all_requests
  }

  return render(request, 'certification/hr_all_requests.html', context)

@hr_required
def hr_pending_requests(request):
    # Get all pending requests
    pending_requests = EmployeeRequest.objects.filter(status='Pending')
    context = {
        'pending_requests': pending_requests,
    }
    return render(request, 'certification/hr_pending.html', context)

@hr_required
def hr_approve_request(request, request_id):
    # Get the certification request by id
    certification_request = get_object_or_404(EmployeeRequest, id=request_id)

    if request.method == 'POST':
        # Process the form submission for approval
        certification_request.status = 'Approved'
        certification_request.save()

        # Redirect back to HR pending requests
        return redirect('hr_pending_requests')

    context = {
        'request': certification_request,
    }
    return render(request, 'certification/hr_approve.html', context)

@hr_required
def hr_decline_request(request, request_id):
    # Get the certification request by id
    certification_request = get_object_or_404(EmployeeRequest, id=request_id)

    if request.method == 'POST':
        # Process the form submission for declining
        certification_request.status = 'Declined'
        certification_request.save()

        # Redirect back to HR pending requests
        return redirect('hr_pending_requests')

    context = {
        'request': certification_request,
    }
    return render(request, 'certification/hr_decline.html', context)

@hr_required
def hr_approved_requests(request):
  approved_requests = EmployeeRequest.objects.filter(status='Approved')

  context = {
    'approved_requests': approved_requests
  }

  return render(request, 'certification/hr_approved_requests.html', context)

@hr_required
def hr_declined_requests(request):
  declined_requests = EmployeeRequest.objects.filter(status='Declined')

  context = {
    'declined_requests': declined_requests
  }

  return render(request, 'certification/hr_declined_requests.html', context)

@hr_required
def send_bond_agreement(request, request_id):

  employee_request = get_object_or_404(EmployeeRequest, id=request_id)

  if request.method == 'POST':

    # Create BondAgreement 
    agreement = BondAgreement()
    agreement.employee_request = employee_request
    agreement.contract_terms = request.POST['contract_terms']
    agreement.save()

    return redirect('hr_approved_requests')

  else:

    context = {
      'employee_request': employee_request
    }

    return render(request, 'certification/send_agreement.html', context)

@employee_required
def view_bond_agreement(request, request_id):

  employee_request = get_object_or_404(EmployeeRequest, id=request_id)
  agreement = get_object_or_404(BondAgreement, employee_request=employee_request)

  if request.method == 'POST':
    
    decision = request.POST['decision']
    
    if decision == 'accept':
      agreement.sign_status = 'Signed'
      
    elif decision == 'decline':
      agreement.sign_status = 'Declined'
    
    agreement.save()
    
    return redirect('agreement_updated')

  context = {
    'employee_request': employee_request,
    'agreement': agreement
  }

  return render(request, 'certification/view_agreement.html', context)

@employee_required
def agreement_updated(request):

  context = {
    'message': 'Agreement updated successfully!' 
  }

  return render(request, 'certification/agreement_updated.html', context)

@hr_required
def declined_agreements(request):
    declined_agreements = BondAgreement.objects.filter(sign_status='Declined')
    
    context = {
        'declined_agreements': declined_agreements,
    }
    
    return render(request, 'certification/declined_agreements.html', context)

@hr_required
def accepted_agreements(request):
    accepted_agreements = BondAgreement.objects.filter(sign_status='Signed')
    
    context = {
        'accepted_agreements': accepted_agreements,
    }
    
    return render(request, 'certification/accepted_agreements.html', context)


