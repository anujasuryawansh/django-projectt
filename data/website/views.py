from django.shortcuts import render,HttpResponse
from website import urls
from django.shortcuts import render, HttpResponse
from website import urls
import pickle
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
import sklearn

# Create your views here.
def home(request):
    return HttpResponse("hi from Data Science Project")


# Create your views here.
def hello(request):
    if request.method == 'GET':
        return render(request, "form.html")
    else:
        # Fetch data from the form
        gender = request.POST.get('gender')
        ssc_percentage = request.POST.get('ssc_percentage')
        ssc_board = request.POST.get('ssc_board')
        hsc_percentage = request.POST.get('hsc_percentage')
        hsc_board = request.POST.get('hsc_board')
        hsc_subject = request.POST.get('hsc_subject')
        hsc_subject = request.POST.get('hsc_subject')
        degree_percentage = request.POST.get('degree_percentage')
        undergrad_degree = request.POST.get('undergrad_degree')
        work_experience = request.POST.get('work_experience')
        emp_test_percentage = request.POST.get('emp_test_percentage')
        specialisation = request.POST.get('specialisation')
        mba_percent = request.POST.get('mba_percent')

        ct=pickle.load(open("coltransformer.pkl","rb"))
        lr=pickle.load(open("logistic_regression.pkl","rb"))

        input_df=pd.DataFrame(data=[[gender,ssc_percentage,ssc_board,hsc_percentage,hsc_board,hsc_subject,degree_percentage,
         undergrad_degree,work_experience,emp_test_percentage,specialisation,mba_percent]],columns=['gender', 'ssc_percentage', 'ssc_board', 'hsc_percentage', 'hsc_board',
       'hsc_subject', 'degree_percentage', 'undergrad_degree',
       'work_experience', 'emp_test_percentage', 'specialisation',
       'mba_percent'])

        input_df = ct.transform(input_df)
        ans=lr.predict(input_df)[0]
        if ans==1:
            return HttpResponse("<h1>YOU WILL GET A JOB</h1>")
        else:
            return HttpResponse("<h1>YOU WILL NOT GET A JOB</h>")

        return HttpResponse("Data Fetched Successfully !!")
def predictinpdata(input_df):
    ct=pickle.load(open("coltransformer.pkl","rb"))
    lr=pickle.load(open("logistic_regression","rb"))
    x=ct.fit_transform(input_df)
    ans=lr.predict(x)[0]
    if ans==1:
        return "YOU WILL GET A JOB"
    else:
        return "YOU WILL NOT GET A JOB"