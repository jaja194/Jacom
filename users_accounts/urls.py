from django.urls import path
from .views import HomePage, CreateUser, UserProfileView, UpdateProfile, DeleteUser, LoginView, Logout, AboutPage, ContactPage, CreateProfile, TestimonialsPage, FaqPage, PrivacyPolicyPage, HowItWorksPage, Dashbord, search_view
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users_accounts'

urlpatterns = [
    path('', HomePage.as_view(), name = 'homepage'),
    path('user_signup', CreateUser.as_view(), name = 'signup'),
    path('user_login', LoginView.as_view(), name = 'login'),
    path('user_logout', Logout, name = 'logout'),
    path('user_profile', UserProfileView.as_view(), name = 'profile'),
    path('create_profile', CreateProfile.as_view(), name = 'userprofile'),
    path('user_update/<pk>', UpdateProfile.as_view(), name = 'update'),
    path('user_delete/<pk>', DeleteUser.as_view(), name = 'delete'),
    path('about_us', AboutPage.as_view(), name = 'about'),
    path('contact_us', ContactPage.as_view(), name = 'contact'),
    path('testimonials',TestimonialsPage.as_view(), name = 'testimony'),
    # path('terms/',TermsOfService.as_view(), name = 'terms&service'),
    path('terms/', views.terms_of_service, name='terms_of_service'),
    path('faq', FaqPage.as_view(), name = 'faqpage'),
    path('privacy_policy', PrivacyPolicyPage.as_view(), name = 'privacy&policy'),
    path('functionl', HowItWorksPage.as_view(), name = 'functioning'),
    path('dashboard_page', Dashbord.as_view(), name = 'dashboard'),
    path('search_page', search_view, name='search'),
    path('user/search/', views.user_search, name='user_search'),
    path('geolocation/', views.geolocation_view, name='geolocation'),
    path('job_count/', views.job_count, name='job_count'),
    path('account/status/', views.account_status, name='account_status'),
    path('withdrawal_requests/', views.withdrawal_requests_view, name='withdrawals'),
    path('ongoing_projects/',views.ongoing_projects_view, name='ongoing_project'),
    #password reset
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),  name='password_reset_done'),
    path('reset/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]