from django.shortcuts import render, get_object_or_404, redirect
from bs4 import BeautifulSoup as bs

# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def result(requests):
    text = requests.POST['text']
    parsed = bs(text, 'html.parser')
    list = parsed.findAll('li')
    num = ['n'] * 100
    title = ['t'] *100
    discount = ['d'] *100
    price1 = ['x']*100
    price2 = ['p'] *100
    for a in list:
        try:
            number = a['item_id']
            title_tag = a.find('strong', 'tit_desc')
            try:
                discount2 = a.find('span', 'discount')
                prime = a.find('span', 'prime')
                discount[int(number)] = discount2.text
                price1[int(number)] = prime.text
            except:
                discount2 = 'no discount'
                discount[int(number)] = discount2
                prime = 'no prime'
                price1[int(number)] = prime

            price = a.find('span', 'sale')
            num[int(number)] = number
            title[int(number)] = title_tag.text
            price2[int(number)] = price.text

        except:
            continue

            final = ['f']*100
            for i in range(100):
                final[i] = num[i] +'\t' + title[i] +'\t' + discount[i] +'\t' +price1[i] +'\t' + price2[i]

    return render(requests, 'result.html', {'final':final})







