from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from project import assistant_code
from sqlsearchandadd import sqlsearch, sqladd



# Create your views here.

def members(request):
    return render(request, 'index.html') #can put html code in the brackets as well

def aboutus(request):
    return render(request, 'aboutus.html')

def assistant(request):
    return render(request, 'assistant.html')

def response(request):
    city_name = request.GET.get("city_name")
    from_date = request.GET.get("from_date")
    to_date = request.GET.get("to_date")
    hotel_name = request.GET.get("hotel_name")
    format = '%Y-%m-%d'
    to_date = datetime.strptime(to_date, format)
    from_date = datetime.strptime(from_date, format)
    answer, result_map = assistant_code(city_name, from_date, to_date, hotel_name)
    sqladd(city_name, from_date, to_date, hotel_name, answer)
    with open("driving_route_map.jpg", "wb") as img:
            for chunk in result_map:
                img.write(chunk)
    return HttpResponse(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Response</title>
</head>
<style>
    *{{
    box-sizing: border-box;
}}

body{{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    margin: 15px 30px;
    font-size: 17px;
    padding: 20px;
}}

.container{{
    background-color: #f2f2f2;
    padding: 5px 20px 15px 20px;
    border: 1px solid lightgray;
    border-radius: 4px;
}}

input[type="text"],
input[type="email"],
input[type="number"],
input[type="password"],
input[type="date"],
select,
textarea{{
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 5px;
}}
fieldset{{
    background-color: #fff;
    border: 1px solid #ccc;
}}

h1{{
    text-align: center;
    color: blue;
}}

h2{{
    text-align: center;
    color: orange;
}}

input[type="submit"]{{
    background-color: #4daea1;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 25%;
}}

input[type = "submit"]:hover{{
    background-color: #44fca4;
}}

    em{{
        font: italic;
        color: darkblue;
        background-color: azure;
    }}
</style>
<body>
    <h1>Creating the itinerary for {city_name} from {from_date} to {to_date} ...</h1>
    <hr>
    <p> {answer} </p>''')

def forum(request):
     return render(request, 'forum.html')

def newpost(request):
     return render(request, 'newpost.html')

def posted(request):
    city_name_forum = request.GET.get("city_name_forum")
    from_date_forum = request.GET.get("from_date_forum")
    to_date_forum = request.GET.get("to_date_forum")
    hotel_name_forum = request.GET.get("hotel_name_forum")
    review_itinerary = request.GET.get("itinerary_forum")
    sqladd(city_name_forum, from_date_forum, to_date_forum, hotel_name_forum, review_itinerary)
    params = {"city_name_forum": city_name_forum, "from_date_forum": from_date_forum, "to_date_forum": to_date_forum, "hotel_name_forum": hotel_name_forum, "review_itinerary": review_itinerary}
    print(params)
    return render(request, 'posted.html', params) #Change this to HttpResponse(the whole page)

def search(request):
     city_name = request.GET.get("city_name_search")
     records = sqlsearch(city_name)
     records = list(records)
     for i in range(len(records)):
        records[i] = list(records[i])
        records[i][4] = records[i][4].replace("<br>", "\n")
        records[i][4] = records[i][4].replace("<b>", "")
        records[i][4] = records[i][4].replace("</b>", "")
        records[i] = tuple(records[i])
     params = {"city_name": city_name, "from_date_1": records[0][1], "to_date_1": records[0][2], "hotel_name_1": records[0][3], "itinerary1": records[0][4], "from_date_2": records[1][1], "to_date_2": records[1][2], "hotel_name_2": records[1][3], "itinerary2": records[1][4], "from_date_3": records[2][1], "to_date_3": records[2][2], "hotel_name_3": records[2][3], "itinerary3": records[2][4], "from_date_4": records[3][1], "to_date_4": records[3][2], "hotel_name_4": records[3][3], "itinerary4": records[3][4], "from_date_5": records[4][1], "to_date_5": records[4][2], "hotel_name_5": records[4][3], "itinerary5": records[4][4]}
     return render(request, 'search.html', params)