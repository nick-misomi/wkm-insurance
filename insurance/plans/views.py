from django.shortcuts import render

# insurance plans
def pension(request):
    return render(request, 'plans/pension.html')

def motor_insurance(request):
    return render(request, 'plans/motor_insurance.html')

def health_insurance(request):
    return render(request, 'plans/health_insurance.html')

def life_insurance(request):
    return render(request, 'plans/life_insurance.html')

def comprehesive_detail(request):
    return render(request, 'plans/comprehesive_detail.html')

def third_party(request):
    return render(request, 'plans/third_party_detail.html')

def motor_commercial(request):
    return render(request, 'plans/motor_commercial_detail.html')

