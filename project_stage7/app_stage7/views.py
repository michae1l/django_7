from django.shortcuts import render,redirect
from .models import hotel_recorde
# Create your views here.


def index(request):
     return render(request,"index/index.html")
  
def home(request):
     return render(request,"index/home.html")

def hotel_recorde(request):
        if request.method == 'POST':
           room_number = request.POST.get("room_number") 
           amount_paid = request.POST.get("amount_paid") 
           occupant_name = request.POST.get("occupant_name") 
           occupant_email = request.POST.get("occupant_email") 
           occupant_occupation = request.POST.get("occupant_occupation") 
           number_of_night = request.POST.get("number_of_night") 
           start_date = request.POST.get("start_date") 
           end_date = request.POST.get("end_date") 
           new_recorde =  hotel_recorde(room_number=room_number,amount_paid = amount_paid,occupant_name=occupant_name,occupant_email=occupant_email,occupant_occupation=occupant_occupation,number_of_night=number_of_night,start_date=start_date,end_date=end_date, )
           new_recorde.save()
           return redirect("index:home")
           return render(request,"index/")                       
