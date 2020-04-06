from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	response = HttpResponse()
	response.write("<em><p>NEVER</p></em>")
	response.write("<strong><p>GONNA</p></strong>")
	response.write("<b><p>GIVE</p></b>")
	response.write("<p>YOU</p>")
	response.write("<p>UP</p>")
	response.write("<p>NEVER</p>")
	response.write("<p>GONNA</p>")
	response.write("<p>LET</p>")
	response.write("<p>YOU</p>")
	response.write("<p>DOWN</p>")	

	return response

def options_calculator(request):
	return HttpResponse("Options Calculator")