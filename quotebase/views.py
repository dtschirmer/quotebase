# views

from django.template.loader import get_template
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import Context, RequestContext
from quotebase.forms import QuoteForm, CostForm, LoginForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.shortcuts import render, redirect, render_to_response
import MySQLdb
from quotebase.quotes.models import Quote, Cost

def test(request):
    return render(request, 'test.html')

def login_user(request):
    logout(request)
    form = LoginForm(request.POST)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user) 
                messages.success(request, 'You are now logged in.')
                return redirect('/quotes/', {'messages': messages})
        else:
            messages.error(request, 'Username and/or password are incorrect')
            return redirect('/login/', {'messages': messages, 'form': form})
    return render(request, 'login.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('/login/', {'messages': messages})

@login_required
def main(request):
    quote_list = Quote.objects.order_by('date').all()
    paginator = Paginator(quote_list, 5)
    page = request.GET.get('page')
    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)
    return render(request, 'main.html', {'quotes': quotes})

@login_required
def quote_detail(request, quote_id):
    one_quote = Quote.objects.get(pk=quote_id)
    #assoc_costs = Cost.objects.filter()
    return render(request, 'quote_detail.html', {'q_detail': one_quote, 'quote_id': quote_id})

@login_required
def new_quote(request):
    if request.method == 'POST': 
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New quote successfully added!')        
            return redirect('main', {'messages': messages})
    else:
        form = QuoteForm()    
    return render(request, 'quote_form.html', {'form': form})
    
@login_required
def edit_quote(request, quote_id):
    one_quote = Quote.objects.get(pk=quote_id)
    data = {
        'id': one_quote.id,
        'date': one_quote.date, 
        'assigned': one_quote.assigned, 
        'lead_type': one_quote.lead_type,
        'lead_contact': one_quote.lead_contact,
        'coordinator': one_quote.coordinator,
        'coord_email': one_quote.coord_email,
        'coord_phone': one_quote.coord_phone,
        'relo_company': one_quote.relo_company,
        'customer': one_quote.customer,
        'cust_email': one_quote.cust_email,
        'cust_phone': one_quote.cust_phone,
        'cust_company': one_quote.cust_company,
        'other_contact': one_quote.other_contact,
        'other_email': one_quote.other_email,
        'other_phone': one_quote.other_phone,
        'other_company': one_quote.other_company,
        'o_city': one_quote.o_city,
        'o_st_pr': one_quote.o_st_pr,
        'o_country': one_quote.o_country,
        'd_city': one_quote.d_city,
        'd_st_pr': one_quote.d_st_pr,
        'd_country': one_quote.d_country,
        'pets': one_quote.pets,
        'pet_notes': one_quote.pet_notes,
        'total_costs': one_quote.total_costs,   
        'contingency': one_quote.contingency,      
        'incentive': one_quote.incentive,          
        'referral_fee': one_quote.referral_fee,    
        'cc_fee': one_quote.cc_fee,                
        'markup': one_quote.markup,                
        'total_quote': one_quote.total_quote,      
        'prc_approved': one_quote.prc_approved,    
        'prc_appvd_date': one_quote.prc_appvd_date,
        'sent_date': one_quote.sent_date,          
        'convert_date': one_quote.convert_date,    
        'prc': one_quote.prc,                      
        'notes': one_quote.notes                   
   } 
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_form = form
            new_form.save()
            messages.success(request, 'Quote successfully modified')        
            return redirect('/quotes/', {'messages': messages, 'quote_id': quote_id})
    else:
        form = QuoteForm(initial=data)    
    return render(request, 'quote_form.html', {'form': form, 'quote_id': quote_id})

@login_required
def main_costs(request):
    costs = Cost.objects.all()
    return render(request, 'costs.html', {'cost_list': costs})

@login_required
def new_cost(request):
    if request.method == 'POST': 
        form = CostForm(request.POST)
        if form.is_valid():
            new_obj = form.save(commit=False)    
            new_obj.save()
            messages.success(request, 'New cost successfully added!')        
            return redirect('/quotes/', {'messages': messages})
    
    else:
        form = CostForm()
        
    return render(request, 'cost_form_table.html', {
                'form': form,
               })        
def reference(request):
    return render(request, 'Here is the reference page')    
