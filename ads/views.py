from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *


@login_required
def ad_timeline(request): 
	""" Home View: Timeline/Feed """ 
	items = Item.objects.all()
	return render(request, 'ads/timeline.html', {
		'items': items
		})

@login_required
def ad_info(request):
	""" This view should accept an advertisement_id and render its info """ 
	return render(request, 'ads/info.html', {})

def create_ad(request):
	item_form = AddItemForm(request.POST or None, request.FILES or None)
	if item_form.is_valid():
		print item_form.cleaned_data
		item_form.save()
		return HttpResponseRedirect(reverse('timeline'))
	return render(request, 'ads/create_ad.html', {'form': item_form})