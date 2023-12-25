from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View

from .forms import CreateUserForm, LoginUserForm, ProfileForm, SearchForm
from django.http import JsonResponse
from .models import UserProfile
from .models import TermsOfService
from .models import Earnings, PendingPayments, WithdrawalRequest
from .forms import AcceptTOSForm, WithdrawalRequestForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePage(TemplateView):
    template_name = 'home.html'

class CreateUser(CreateView):
    template_name = 'sign_up.html'
    queryset = User.objects.all()
    form_class = CreateUserForm

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('/user_login')
        else:
            return render('Invalid Signup')

def Logout(request):
    logout(request)
    return redirect('/user_login')

class LoginView(CreateView):
    template_name = 'login.html'
    queryset = User.objects.all()
    form_class = LoginUserForm

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard_page')
        else:
            return render({'details':'Not Found'}, self.template_name)

class CreateProfile(LoginRequiredMixin, CreateView):
    template_name = 'create_profile.html'
    queryset = UserProfile.objects.all
    form_class = ProfileForm
    success_url = '/user_profile'
    login_url = '/user_login'
    

class UserProfileView(LoginRequiredMixin, ListView):
    template_name = 'user_profile.html'
    queryset = UserProfile.objects.all()
    context_object_name = 'user'
    login_url = '/user_login'

    # def get(request):
    #     user_data = UserProfile.objects.filter(user=request.user)
    #     return render(request, self.template_name, {'user':user_data})

class UpdateProfile(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    queryset = UserProfile.objects.all()
    form_class = ProfileForm
    success_url = '/user_profile'
    login_url = '/user_login'

class DeleteUser(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = UserProfile.objects.all()
    context_object_name = 'delete'
    success_url = '/user_profile'
    login_url = '/user_login'

def search_view(request):
    query = request.GET.get('q')

    if query:
        results = UserProfile.objects.filter(title__icontains=query)
        # Adjust 'your_field' to the field you want to search on

        return render(request, 'search_results.html', {'results': results})
    else:
        return render(request, 'search_results.html', {'results': []})

def user_search(request):
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        users = userprofile.objects.filter(title__icontains=search_query)
        return render(request, 'user_search.html', {'users': users})
    else:
        return render(request, 'user_search.html', {})



def geolocation_view(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Process latitude and longitude (e.g., store in the database)
        # Implement your logic here

        return JsonResponse({'message': 'Geolocation received and processed successfully'})

    return JsonResponse({'error': 'Invalid request method'})



class Dashbord(TemplateView):
    template_name = 'dashboard.html'
    login_url = '/user_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_details'] = UserProfile.objects.all()
        return context


class AboutPage(TemplateView):
    template_name = 'about.html'
    login_url = '/user_login'

class ContactPage(TemplateView):
    template_name = 'contact.html'
    login_url = '/user_login'

class TestimonialsPage(TemplateView):
    template_name = 'testimonials.html'
    login_url = '/user_login'

def terms_of_service(request):
    tos = TermsOfService.objects.latest('date_updated')
    return render(request, 'terms_of_service.html', {'tos': tos})

def accept_terms(request):
    form = AcceptTOSForm(request.POST or None)
    if form.is_valid():
        # Process user acceptance here (e.g., set a flag in user profile)
        return redirect('home')  # Redirect to home page or another view

    return render(request, 'accept_terms.html', {'form': form})


def job_count(request):
    ongoing_status_criteria = ['in_progress', 'processing', 'active']
    ongoing_jobs_count = UserProfile.objects.filter(status__in=ongoing_status_criteria).count()
    return render(request, 'job_count.html', {'ongoing_jobs_count': ongoing_jobs_count})

def account_status(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'account_status.html', {'user_profile': user_profile})

class PrivacyPolicyPage(TemplateView):
    template_name = 'privacy_policy.html'
    login_url = '/user_login'

class FaqPage(TemplateView):
    template_name = 'faq.html'
    login_url = '/user_login'

class HowItWorksPage(TemplateView):
    template_name = 'functioning.html'
    login_url = '/user_login'


@login_required
def make_payment(request):
    if request.method == 'POST':
        # Process payment logic using Stripe or your chosen gateway
        # Handle payment form submission
        amount = 1000  # Amount in cents
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
        )
        return render(request, 'payment_confirmation.html', {'client_secret': intent.client_secret})
    return render(request, 'payment.html')

def earnings_view(request):
    user_earnings = Earnings.objects.filter(user=request.user)
    return render(request, 'earnings.html', {'user_earnings': user_earnings})

def pending_payments_view(request):
    user_pending_payments = PendingPayments.objects.filter(user=request.user)
    return render(request, 'pending_payments.html', {'user_pending_payments': user_pending_payments})

def withdrawal_requests_view(request):
    pending_withdrawal_requests = WithdrawalRequest.objects.filter(user=request.user, is_approved=False)
    if request.method == 'POST':
        form = WithdrawalRequestForm(request.POST)
        if form.is_valid():
            withdrawal = form.save()
            return redirect('success_page')
    else:
        form = WithdrawalRequestForm()
    return render(request, 'withdrawal_requests.html', {'form': form})

def ongoing_projects_view(request):
    ongoing_projects = UserProfile.objects.all()
    return render(request, 'ongoing_projects.html', {'ongoing_projects': ongoing_projects})