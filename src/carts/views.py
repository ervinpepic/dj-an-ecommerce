# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def cart_home(request):
	return render(request, "carts/home.html", {})
