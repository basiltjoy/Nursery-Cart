from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
   

class care_necessities(View):
    def get(self, request):
         return render(request, 'care_necessities.html')