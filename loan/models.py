from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Borrower(models.Model):
    """
    Borc alan şəxsin məlumatları
    """
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=15, blank=True, null=True)

class Referance(models.Model):
    """
    Referans məlumatları
    """
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=15, blank=True, null=True)

class Loan(models.Model):
    """
    Borc haqqında məlumatlar
    """
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="loans")
    amount = models.DecimalField(_("Loan Amount"), max_digits=10, decimal_places=2)
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    paid_date = models.DateField(_("End Date"))
    paid_status = models.BooleanField(default=False)

class LoanReferances(models.Model):
    """
    Borc Referansları
    """
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="referances")
    referance = models.ForeignKey(Referance, on_delete=models.CASCADE, related_name="loans")

class Donation(models.Model):
    """
    Sədəqə məlumatları
    """
    donor_name = models.CharField(_("Donor Name"), max_length=100)
    amount = models.DecimalField(_("Donation Amount"), max_digits=10, decimal_places=2)
    donation_date = models.DateField(_("Donation Date"), auto_now_add=True)

class Depositor(models.Model):
    """
    Əmanət edən şəxsin məlumatları
    """
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=15, blank=True, null=True)


class Deposit(models.Model):
    """
    Əmanət məlumatları
    """
    depositor_name = models.ForeignKey(Depositor, on_delete=models.CASCADE, related_name="deposits")
    amount = models.DecimalField(_("Deposit Amount"), max_digits=10, decimal_places=2)
    deposit_date = models.DateField(_("Deposit Date"), auto_now_add=True)
    return_date = models.DateField(_("Return Date"))


class Pool(models.Model):
    """
    Hovuz məlumatları
    """
    total_amount = models.DecimalField(_("Total Amount"), max_digits=15, decimal_places=2, default=0.0)