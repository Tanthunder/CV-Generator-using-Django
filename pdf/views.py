from django.shortcuts import render , redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
 
 
def accept_data(request):
    """Get/accept data from user."""
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work= request.POST.get("previous_work","")
        skills = request.POST.get("skills","")
 
        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('list')
    
    return render(request,'pdf/accept.html')


def download_resume(request,id):
    """view for downloading resume."""
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment ; filename = "resume.pdf"'
    return response
 
def resume_list(request):
    """Show list of all resumes available in db."""
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})

