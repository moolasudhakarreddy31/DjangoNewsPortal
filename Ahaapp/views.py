from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'Ahaapp/index.html')


def moviesinfo(request):
    head_msg='Leatest Movie Updates Hear..!'
    msg1='Raviteja Fixed In A Loop With Bollywood Hero?'
    msg2='Salman Khan To Launch Jr NTR First?'
    msg3='Poster: Lord Hanuman From Adipurush'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'Ahaapp/news.html',context=my_dict)


def sportsinfo(request):
    head_msg='Leatest Sports Updates Hear..!'
    msg1='Watch: KKR captain Nitish Rana and coach Chandrakant Pandit take blessings at Kalighat temple ahead of RCB vs KKR. '
    msg2='Suryakumar Yadav will have to forget the expectations on him: AB de Villiers.'
    msg3='s per reports, Frank Lampard accepts Chelsea interim coaching role'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'Ahaapp/news.html',context=my_dict)


def politicsinfo(request):
    head_msg='Leatest Politics Updates Hear..!'
    msg1='Lok Sabha Budget session ends, House adjourned sine die'
    msg2='Karnataka polls: Cong releases second list of 41 candidates, marks one seat for Sarvodaya Karnataka Party'
    msg3='Monopolies in various sectors pushing prices higher: Jairam Ramesh'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'Ahaapp/news.html',context=my_dict)
















