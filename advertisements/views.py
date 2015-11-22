from django.shortcuts import render


def ad_timeline(request): 
	""" Home View: Timeline/Feed """ 
	return render(request, 'advertisements/timeline.html', {})

def ad_info(request):
	""" This view should accept an advertisement_id and render its info """ 
	return render(request, 'advertisements/info.html', {})