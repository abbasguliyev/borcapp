from django.shortcuts import render
from django.views.generic import TemplateView
from loan.models import Loan, Borrower, Deposit, Depositor, Donation, LoanReferances, Referance, Pool

class HomeView(TemplateView):
    template_name = "debts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loans"] = Loan.objects.select_related("borrower").all()
        return context
    