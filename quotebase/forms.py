from django import forms
from quotebase.quotes.models import Quote, Cost
from quotebase.contacts.models import User, Partner, Agent, Relo_Company
from quotebase.reference.models import Airline, Currency

class CustomDateField(forms.DateField):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('input_formats', ("%d/%m/%Y",))
    super(CustomDateField, self).__init__(*args, **kwargs)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields =['date', 'assigned', 'lead_type', 'lead_contact', \
                'coordinator', 'coord_email', 'coord_phone', 'relo_company', \
                'customer', 'cust_email', 'cust_phone', 'cust_company', \
                'other_contact', 'other_email', 'other_phone', 'other_company', \
                'o_city', 'o_st_pr', 'o_country', 'd_city', 'd_st_pr', 'd_country', 'pets', 'pet_notes', \
                'total_costs', 'contingency', 'incentive', 'referral_fee', 'cc_fee', 'markup', 'total_quote', \
                'prc_approved', 'prc_appvd_date', 'sent_date', 'convert_date', 'prc', 'notes']


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['quotes', 'date', 'agent', 'estimated', 'currency', 'exchange_rate', 'service_point', 'airline', 'o_airport', \
                'd_airport', 'af_cost', 'af_cost_lcl', 'af_fee', 'af_fee_lcl', 'ap_fee_customs', \
                'ap_fee_lcl', 'ap_cust_notes', 'transportation', 'trans_lcl', 'trans_notes', \
                'travel_kennel', 'tk_lcl', 'tk_notes', 'vaccination', 'vcn_lcl', 'vcn_notes', \
                'parasite', 'para_lcl', 'para_notes', 'health_cert', 'hc_lcl', 'hc_notes', 'hc_2', 'hc_2_lcl', 'hc_2_notes', \
                'gov_endorse', 'gov_end_lcl', 'gov_end_notes', 'gov_permit', 'gov_perm_lcl', 'gov_perm_notes', \
                'postage', 'post_lcl', 'post_notes', 'quarantine', 'q_lcl', 'q_notes', 'boarding', 'board_lcl', 'board_notes', \
                'other_name', 'other_cost', 'other_lcl', 'other_notes', 'total_cost', 'total_lcl', 'notes']

class DestinationCostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['date', 'agent', 'estimated', 'currency', 'exchange_rate', 'service_point', \
                'af_fee', 'af_fee_lcl', 'ap_fee_customs', 'transportation', 'trans_lcl', 'trans_notes', \
                'gov_endorse', 'gov_end_lcl', 'gov_end_notes', 'gov_permit', 'gov_perm_lcl', 'gov_perm_notes', \
                'quarantine', 'q_lcl', 'q_notes', 'boarding', 'board_lcl', 'board_notes', \
                'other_name', 'other_cost', 'other_lcl', 'other_notes', 'total_cost', 'total_lcl', 'notes']

class GroundCostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['date', 'agent', 'estimated', 'currency', 'exchange_rate', 'service_point', \
                'transportation', 'trans_lcl', 'trans_notes', 'other_name', 'other_cost', 'other_lcl', 'other_notes', \
                'total_cost', 'total_lcl', 'notes']

class AirFreightCostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['date', 'agent', 'estimated', 'currency', 'exchange_rate', 'service_point', \
                'airline', 'o_airport', 'd_airport', 'af_cost', 'af_cost_lcl', 'af_fee', 'af_fee_lcl']

class OtherCostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['date', 'agent', 'estimated', 'currency', 'exchange_rate', 'service_point', \
        'vcn_lcl', 'vcn_notes', 'parasite', 'para_lcl', 'para_notes', 'health_cert', 'hc_lcl', \
        'hc_notes', 'hc_2', 'hc_2_lcl', 'hc_2_notes', 'gov_endorse', 'gov_end_lcl', 'gov_end_notes', \
        'gov_permit', 'gov_perm_lcl', 'gov_perm_notes', \
        'other_name', 'other_cost', 'other_lcl', 'other_notes', 'total_cost', 'total_lcl', 'notes']

class UserForm(forms.ModelForm):
    class Meta:
        model = User

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent

class ReloCompanyForm(forms.ModelForm):
    class Meta:
        model = Relo_Company

class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline

class Currency(forms.ModelForm):
    class Meta:
        model = Currency
