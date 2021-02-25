from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Stock
import numpy as np
import pandas as pd
import joblib

# Create your views here.


def index(request):
    if request.method == "POST":
        stock = Stock()
        stock.stocker = request.POST.get('s_n')
        stock.stock_date = request.POST.get('s_d')
        stock.stock_price = request.POST.get('s_o')
        stock.stock_high = request.POST.get('s_h')
        stock.stock_low = request.POST.get('s_l')
        stock.no_shares = request.POST.get('s_t')

        user_data = np.array(
            [
                [
                    stock.stock_price, stock.stock_high,
                    stock.stock_low, stock.no_shares
                ]
            ]).reshape(1, 4)

        model_path = 'ML/code/code folder/model.pkl'
        ar = joblib.load(open(model_path, 'rb'))
        prediction = ar.predict(user_data)

        stock.stock_final_price = round(prediction[0], 2)
        stock.save()

    return render(request, 'home/stock_market.html')


def stock_list(request, template_name='home/stock-list.html'):
    # noinspection PyUnresolvedReferences
    stock_lists = Stock.objects.all()
    paginator = Paginator(stock_lists, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name, {'object_list': stock_lists, 'page_obj': page_obj})
