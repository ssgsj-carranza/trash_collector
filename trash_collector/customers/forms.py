from .models import Customer
from django import forms


class Forms(forms.Form):
    models = Customer
    fields = [
        "name",
        "user",
        "pickup_date",
        "one_time_pickup",
        "suspend_start_date",
        "suspend_end_date",
        "current_bill",
        "pick_up_charge_amount",
        "pick_up_zip"
    ]