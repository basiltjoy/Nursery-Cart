from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View 
from store.models.fertiliser import Fertilizer 

class care_necessities(View):
    def get(self, request):
        fertilizers = Fertilizer.objects.all()
        return render(request, 'care_necessities.html', {'fertilizers': fertilizers})
    
