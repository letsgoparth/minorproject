from django.shortcuts import render
import plotly.express as px

# Create your views here.

# def viewfunction(request):
#     return render(request,"home.html") 

# Create your views here.
def viewfunction(request):

    fig = px.line(
        x=[2018,2019,2020,2021,2022],
        y=[4,7,4,6,7],
        title="CO2 PPM",
        labels={'x': 'Date', 'y': 'CO2 PPM'}
    )
    
    fig2 = px.line(
        x=[3018,3019,3020,3021,3022],
        y=[9,13,43,6,56],
        title="CO2 PPM",
        labels={'x': 'Date', 'y': 'CO2 PPM'}
    )

    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
            
    })
    chart = fig.to_html()
    chart2 = fig2.to_html()
    context = {'chart': chart,'chart2':chart2}
    return render(request, 'chart.html', context)