from models import *
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
import datetime
import sunlight

sunlight.config.API_KEY = "6d9a9a6b922a468a939482990814ca69"

def Main(request):
    meta = sunlight.openstates.state_metadata(state='ne')
    senators = sunlight.openstates.legislators(state='ne',active='true')
    bills = sunlight.openstates.bills(state='ne', session='104')[:20]
    committees = sunlight.openstates.committees(state='ne')


    dictionaries = { 'meta': meta, 'senators': senators, 'bills': bills, 'committees': committees, }
    return render_to_response('neleg/main.html', dictionaries)
    
def Bill(request, session, bill):
    bill = sunlight.openstates.bill_detail(state='ne', session=session, bill_id=bill)

    dictionaries = { 'bill': bill, }
    return render_to_response('neleg/bill.html', dictionaries)