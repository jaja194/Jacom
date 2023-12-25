from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import Customer
from .models import TermsOfService
from .models import Earnings, PendingPayments, WithdrawalRequest


admin.site.register(UserProfile)
admin.site.register(Customer)
admin.site.register(TermsOfService)
admin.site.register(Earnings), (PendingPayments), (WithdrawalRequest)
