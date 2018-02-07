from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView,ListView
from .models import RestaurantLocation
# Create your views here.

'''def home(request, *args,**kwargs):
	query = RestaurantLocation.objects.all()
	context = {
	'object_list':query
	}
	print (args)
	return render(request,'home.html',context)

class SomeView(View):
	def get(self,request,*args,**kwargs):
		return render(request,'home.html',{'html_var':'fahad'}) 

	template_name='home.html'
	def get_context_data(self,*args,**kwargs):
		context =super(HomeView,self).get_context_data(*args,**kwargs)
		context = {'html_var':'optimus'}
		return context
'''
'''def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return render(request,'tryouts.html',{'html_var':message})
'''
def search(request):
	message = ''
	context={}
	if request.method == "POST":
		message = request.POST.get("q")
		query = RestaurantLocation.objects.filter(category__icontains=message)
		print (request.POST)
		print (message)
		context.update({
			'object_list':query
		})
	return render(request,'tryouts.html',context)

class HomeView(ListView):
	template_name='home.html'
	def get_queryset(self):
		print(self.kwargs.get("slug"))
		slug=self.kwargs.get("slug")
		if slug:
			query = RestaurantLocation.objects.filter(category__icontains=slug)
		else:
			query = RestaurantLocation.objects.all()
		return query
