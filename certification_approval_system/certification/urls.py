# certification/urls.py

from django.urls import path
from . import views
from .views import agreement_updated, declined_agreements, accepted_agreements

urlpatterns = [
     path('', views.custom_login, name='custom_login'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('new-request/', views.new_request, name='new_request'),
    path('pending-requests/', views.pending_requests, name='pending_requests'),
    path('approved-requests/', views.approved_requests, name='approved_requests'),
    path('declined-requests/', views.declined_requests, name='declined_requests'),
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('hr-pending/', views.hr_pending_requests, name='hr_pending_requests'),
    path('hr-approve/<int:request_id>/', views.hr_approve_request, name='hr_approve_request'),
    path('hr-decline/<int:request_id>/', views.hr_decline_request, name='hr_decline_request'),
    path('hr-all-requests/', views.hr_all_requests, name='hr_all_requests'),
    path('hr-approved-requests/', views.hr_approved_requests, name='hr_approved_requests'),
    path('hr-declined-requests/', views.hr_declined_requests, name='hr_declined_requests'),
    path('send-bond-agreement/<int:request_id>/', views.send_bond_agreement, name='send_bond_agreement'),
    path('view-bond-agreement/<int:request_id>/', views.view_bond_agreement, name='view_bond_agreement'),  
     path('agreement-updated/', agreement_updated, name='agreement_updated'),
     path('declined-agreements/', declined_agreements, name='declined_agreements'),
     path('accepted-agreements/', accepted_agreements, name='accepted_agreements'),
     
     
]
