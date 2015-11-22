from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def ad_timeline(request): 
	""" Home View: Timeline/Feed """ 
	return render(request, 'ads/timeline.html', {})

def ad_info(request):
	""" This view should accept an advertisement_id and render its info """ 
	return render(request, 'ads/info.html', {})