from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from epms.models import Registrations,Info,Admin
# Create your views here.
def home(request):
	return render(request,'epms/index.html')

def login(request):
	if request.method == "POST":
		udata = [i for i in Registrations.objects.all() if ((request.POST['username']==i.Name) and (request.POST['password']==i.PassWord))]
		adata = [i for i in Admin.objects.all() if ((request.POST['username'])==i.Name and (request.POST['password'])==i.PassWord)]
		if len(udata) == 1:
			return redirect('/user/'+str(udata[0].id))
		elif len(adata)==1:
			return redirect('/adminu/'+str(adata[0].id))
	return render(request,'epms/login.html')

def register(request):
	if request.method == "POST":
		n = request.POST['username']
		pn = request.POST['phno']
		e = request.POST['email']
		a = request.POST['addr']
		p = request.POST['psswd']
		c = request.POST['cpsswd']
		if p != c :
			return HttpResponse("<script type='text/javascript'>alert('Given PassWord and Confirm PassWord are not same.')</script>")
		else:
			Registrations.objects.create(Name=n,PhNo=pn,EMail=e,Address=a,PassWord=p)
			send_mail('Registration Confirmation','Thanks for being Registered with us.','shaiksubhansaheb609@gmail.com',[e],fail_silently=False)
			return redirect('/login')
	return render(request,'epms/register.html')

def send(request):
	send_mail('Garbage Will be Colleted Regd.,','Your domestic waste will be replaced soon. For any queries contact +91 xxxxx xxxxx','shaiksubhansaheb609@gmail.com',[request.POST['email']],fail_silently=False)


def adminu(request,id):
	udata = Info.objects.all()
	adata = Admin.objects.get(id=id)
	if request.method == "POST":
		send(request)
	return render(request,'epms/admin.html/',{'name':adata.Name,'data':udata})

def user(request,id):
	data = Registrations.objects.get(id=id)
	n = [i for i in Info.objects.all() if i.Name == data.Name]
	if request.method == "POST" :
		n = request.POST['Name']
		m = request.POST['Material']
		q = request.POST['Quantity']
		p = request.POST['phno']
		e = request.POST['Email']
		a = request.POST['Address']
		ev = request.POST['ExpectedValue']
		mt = request.POST['MaterialType']
		Info.objects.create(Name=n,Material=m,Quantity=q,PhNo=p,EMail=e,Address=a,Value=ev,Type=mt)
		send_mail('Confirmation Mail','Your data is sent to authoities successfully. We will contact you soon.','shaiksubhansaheb609@gmail.com',[e],fail_silently=False)
		return HttpResponse("<script type='text/javascript'>alert('Your data stored successfully!!!')</script><h3>Click <a href='http://127.0.0.1:8000'>Here</a> to go homepage...</h3>")
	if len(n) !=0 :
		return render(request,'epms/user.html',{'data':data,'history':Info.objects.filter(Name=n[0].Name)})
	else:
		return render(request,'epms/user.html',{'data':data})
