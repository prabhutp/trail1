#from django.shortcuts import render

# Create your views here.
# I have created this file- Prabhu T P

from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt

from wiecode.models import participants

# from django.shortcuts import render_to_response

# from django.template.loader import render_to_string

# from django.http import HttpResponse
import smtplib
import sys
import getpass
from email.mime.text import MIMEText


def index(request):
    return render(request, 'index.html')

# def about(request):
 #   return HttpResponse("about")


def contact(request):
    return render(request, 'contactUs.html')


def sendMail(request, leader_mail,leader_name):
    print("Python program to send a mail to your friend.")
    fromaddr = "prabhutp2@gmail.com"
    toaddr = leader_mail
    subject = "Mail from Wie code Website"
    # fromaddr = input("Enter the sender mail-id: ")
    # toaddr = input("Enter the receiver(Your friend's) mail-id: ")
    # subject = input("Enter the Subject for the mail: ")
    body = '''Hello '''+leader_name+'''!!!.

        This is a mail from wie code website.

     Thanks and Regards.
     IEEE SIT SB'''
    # print("Press 'Ctrl+Z'-for windows and 'Ctrl+D'-for other OS and 'Enter' key after the end of body of the mail.")
    # print("Enter the content for the body of the mail.")
    # msg = sys.stdin.readlines()
    # body = ""
    # for x in msg:
    #     body += x
    msg = MIMEText(body)
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    password = "Prabhutp@123"
    # password = input("Enter your password: ")
    #password = getpass.getpass(prompt='Enter your password: ')
    server.login(fromaddr, password)
    server.send_message(msg)
    print("Mail sent successfully...")
    server.quit()

# @csrf_exempt


def uregister(request):
    if request.method == "POST":
        print("Entered IF")
        # return render(request, 'index.html')
        # request.session["teamname"]=request.POST.get('teamname')
        # request.session["domains"]=request.POST.get('domains')
        # request.session["teamsize"]=request.POST.get('teamsize')
        # teamname=request.POST.get('teamname')
        # domain_info=request.POST.get('domains')
        teamsize = request.POST.get('teamsize')
        # print(teamname)
        # print(domain_info)
        print(teamsize)
        request.session["leader_name"] = request.POST.get('leader_name')
        # request.session["leader_mail"] = request.POST.get('leader_mail')
        # request.session["leader_number"] = request.POST.get('leader_number')
        # request.session["leader_clg"] = request.POST.get('leader_clg')
        leader_name = request.POST.get('leader_name')
        leader_mail = request.POST.get('leader_mail')
        leader_number = request.POST.get('leader_number')
        leader_clg = request.POST.get('leader_clg')
        print(request.session["leader_name"])
        # print(leader_mail)
        # print(leader_number)
        # print(leader_clg)
        # request.session["name1"]=request.POST.get('name1')
        # request.session["mail1"]=request.POST.get('mail1')
        # request.session["number1"]=request.POST.get('number1')
        # request.session["clg1"]=request.POST.get('clg1')
        name1 = request.POST.get('name1')
        mail1 = request.POST.get('mail1')
        number1 = request.POST.get('number1')
        clg1 = request.POST.get('clg1')
        # request.session["name2"]=request.POST.get('name2')
        # request.session["mail2"]=request.POST.get('mail2')
        # request.session["number2"]=request.POST.get('number2')
        # request.session["clg2"]=request.POST.get('clg2')
        name2 = request.POST.get('name2')
        mail2 = request.POST.get('mail2')
        number2 = request.POST.get('number2')
        clg2 = request.POST.get('clg2')
        # request.session["name3"]=request.POST.get('name3')
        # request.session["mail3"]=request.POST.get('mail3')
        # request.session["number3"]=request.POST.get('number3')
        # request.session["clg3"]=request.POST.get('clg3')
        name3 = request.POST.get('name3')
        mail3 = request.POST.get('mail3')
        number3 = request.POST.get('number3')
        clg3 = request.POST.get('clg3')
        # print(request.FILES)
        # abstractPdf = request.FILES['Abstract']
        first = participants(M1MailId=leader_mail, M1Name=request.session["leader_name"], M1College=leader_clg, M1Phone=leader_number,
                             M2MailId=mail1, M2Name=name1, M2College=clg1, M2Phone=number1,
                             M3MailId=mail2, M3Name=name2, M3College=clg2, M3Phone=number2,
                             M4MailId=mail3, M4Name=name3, M4College=clg3, M4Phone=number3,)
        first.save()
        # if(leader_mail!="none"):
        #     first.save()
        # extra = domains(M1MailId = leader_mail,domainName=domain_info,abstract=abstractPdf)
        # extra.save()
        print("conta")
        sendMail(request, leader_mail, leader_name)
        # return render(request, 'index.html')
        return redirect('/')
    else:
        return render(request, 'registration.html')
    return render(request, 'registration.html')

# def admins(request):
#     data = participants.objects.all().values()
#     print(data)
#     return render(request,'adminVerify.html', {"data": data})
# def register1(request):


@csrf_exempt
def admins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if(username == "ieee" and password == "ieeepassword"):
            data = participants.objects.all().values()
            return render(request, 'adminVerify.html', {"data": data})
        else:
            return render(request, 'adminLogin.html')
    else:
        return render(request, 'adminLogin.html')
