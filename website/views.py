from django.shortcuts import render
from django.http import Http404
# Root Views

def index(request):
	return render(request, 'index.html')


# Fan views

def fan_signup(request):
	return render(request, 'fan/as-fan.html')

def fan1a(request):
	return render(request, 'fan/fan1a.html')

def fan1b(request):
	return render(request, 'fan/fan1b.html')

def fan1c(request):
	return render(request, 'fan/fan1c.html')

def fan2a(request):
	return render(request, 'fan/fan2a.html')

def fan2b(request):
	return render(request, 'fan/fan2b.html')

def fan2c(request):
	return render(request, 'fan/fan2c.html')	

def fan_pg1(request):
	return render(request, 'fan/fan_pg1.html')

def fan_pg10(request):
	return render(request, 'fan/fan_pg10.html')

def fan_pg11(request):
	return render(request, 'fan/fan_pg11.html')

def fan_pg12(request):
	return render(request, 'fan/fan_pg12.html')

def fan_pg2(request):
	return render(request, 'fan/fan_pg2.html')

def fan_pg3(request):
	return render(request, 'fan/fan_pg3.html')

def fan_pg4(request):
	return render(request, 'fan/fan_pg4.html')

def fan_pg5(request):
	return render(request, 'fan/fan_pg5.html')

def fan_pg6(request):
	return render(request, 'fan/fan_pg6.html')

def fan_pg7(request):
	return render(request, 'fan/fan_pg7.html')

def fan_pg8(request):
	return render(request, 'fan/fan_pg8.html')

def fan_pg9(request):
	return render(request, 'fan/fan_pg9.html')

# Coach views

def coach_signup(request):
	return render(request, 'coach/as-coach.html')

def coach2a(request):
	return render(request, 'coach/coach2a.html')

def coach2b(request):
	return render(request, 'coach/coach2b.html')	

def coach_pg1(request):
	return render(request, 'coach/coach_pg1.html')

def coach_pg10(request):
	return render(request, 'coach/coach_pg10.html')

def coach_pg12(request):
	return render(request, 'coach/coach_pg12.html')

def coach_pg2(request):
	return render(request, 'coach/coach_pg2.html')

def coach_pg3(request):
	return render(request, 'coach/coach_pg3.html')

def coach_pg4(request):
	return render(request, 'coach/coach_pg4.html')

def coach_pg5(request):
	return render(request, 'coach/coach_pg5.html')

def coach_pg6(request):
	return render(request, 'coach/coach_pg6.html')

def coach_pg7(request):
	return render(request, 'coach/coach_pg7.html')

def coach_pg8(request):
	return render(request, 'coach/coach_pg8.html')

def coach_pg9(request):
	return render(request, 'coach/coach_pg9.html')

# Inner views

def inner(request):
	return render(request, 'inner/inner1.html')

def inner10(request):
	return render(request, 'inner/inner10.html')

def inner11(request):
	return render(request, 'inner/inner11.html')	

def inner12_1(request):
	return render(request, 'inner/inner12-1.html')

def inner12_2(request):
	return render(request, 'inner/inner12-2.html')

def inner12(request):
	return render(request, 'inner/inner12.html')

def inner2(request):
	return render(request, 'inner/inner2.html')

def inner3(request):
	return render(request, 'inner/inner3.html')

def inner4(request):
	return render(request, 'inner/inner4.html')

def inner5(request):
	return render(request, 'inner/inner5.html')

def inner6(request):
	return render(request, 'inner/inner6.html')

def inner7_college_error(request):
	return render(request, 'inner/inner7-college-error.html')

def inner7_college(request):
	return render(request, 'inner/inner7-college.html')

def inner7_highschool_error(request):
	return render(request, 'inner/inner7-highschool-error.html')

def inner7_highschool(request):
	return render(request, 'inner/inner7-highschool.html')

def inner7(request):
	return render(request, 'inner/inner7.html')

def inner8(request):
	return render(request, 'inner/inner8.html')

def inner9(request):
	return render(request, 'inner/inner9.html')	

def innerc1(request):
	return render(request, 'inner/innerc1.html')

def innerc2(request):
	return render(request, 'inner/innerc2.html')

def innerc3(request):
	return render(request, 'inner/innerc3.html')

def innerc4(request):
	return render(request, 'inner/innerc4.html')

def innerc5(request):
	return render(request, 'inner/innerc5.html')

def innerc6(request):
	return render(request, 'inner/innerc6.html')


# Message views

def message(request):
	return render(request, 'message/message1.html')

def message2(request):
	return render(request, 'message/message2.html')

def message3(request):
	return render(request, 'message/message3.html')	

def message4(request):
	return render(request, 'message/message4.html')

def message4(request):
	return render(request, 'message/message5.html')


# Search views

def search(request):
	return render(request, 'search/search.html')

def search2(request):
	return render(request, 'fan/search2.html')

def search3(request):
	return render(request, 'fan/search3.html')