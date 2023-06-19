from django.shortcuts import render
from django.http import HttpResponse
import datetime

conferences = [
{
  "id": 1,
  "name": "Artificial Intelligence in Agriculture",
  "date": "2023-05-20",
  "location": "Tech Hub X"
},
{
  "id": 2,
  "name": "Blockchain for Supply Chain Management",
  "date": "2023-09-15",
  "location": "Innovation Center Y"
},
{
  "id": 3,
  "name": "Cybersecurity in the Banking Sector",
  "date": "2023-06-30",
  "location": "Grand Hotel Z"
},
{
  "id": 4,
  "name": "Smart Cities and Sustainable Development",
  "date": "2023-11-10",
  "location": "Convention Center W"
},
{
  "id": 5,
  "name": "Future of Virtual Reality",
  "date": "2024-03-05",
  "location": "Tech Expo V"
}
    ]
def conferences_view(request):
    return render(request, 'conference/conferences.html', context={"conferences": conferences})

def create_conference_view(request):
    return render(request, "conference/createConference.html")

def conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/conference.html", context={"conference": conference })

def update_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/updateConference.html", context={"conference": conference})

def delete_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/delete_conference.html", context={"conference" : conference})

def confirm_delete_view(request, id):
    return render(request, "conference/confirm_delete.html")