from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def chain(request: HttpRequest, n: int):
	if n < 10:
		return redirect(reverse('chain', args=(n+1,)))
	return HttpResponse('OK THEN')


def selfref(request: HttpRequest):
	return redirect(reverse('selfref'))


def cycle(request: HttpRequest, n: int):
	if n < 10:
		return redirect(reverse('cycle', args=(n+1,)))
	return redirect(reverse('cycle', args=(1,)))


def infinite(request: HttpRequest):
	def iter():
		while True:
			yield 'z'*10000
	h = StreamingHttpResponse(iter())
	h.status_code = 303
	h['Location'] = '/normal/'
	return h


def normal(request: HttpRequest):
	return HttpResponse('OK GUY')
