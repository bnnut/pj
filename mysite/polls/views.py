from django.shortcuts import render
from django.shortcuts import redirect
from .forms import Crayfishform
from .forms import Crayfishform2
from sklearn import linear_model
from sklearn.externals import joblib
import json, threading
from django.http import HttpResponse
from .models import *


# *********  machine learning methods ***********

def buildModel():
    model = linear_model.LinearRegression()
    # load
    X, Y = [], []
    records = Crayfish.objects.all()
    for c in records:
        X.append(c.size)
        Y.append(c.price)
    model.fit(X, Y)
    # save model
    joblib.dump(model, 'model.pkl')


def evaluate(size):
    model = joblib.load('model.pkl')
    score = model.predict(size)
    return score

# ***********************************************
#

def index(request):
    return render(request, 'polls/index.html', {})


def getprice(request):
    if request.method == "POST":
        try:
            result = evaluate(float(request.POST['size']))
            return render(request, 'polls/result.html', {'result': float(result)})
        except:
            pass
            result2 = "Not enough data available"
            return render(request, 'polls/result.html', {'result': result2})
    else:
        form = Crayfishform2()
    return render(request, 'polls/getprice.html', {'form': form})


def savedat(request):
    if request.method == "POST":
        form = Crayfishform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            threading.Thread(None, buildModel, None, ()).start()
            return redirect('index')
    else:
        form = Crayfishform()
    return render(request, 'polls/savedat.html', {'form': form})

