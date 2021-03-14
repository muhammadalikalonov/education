from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
# from .forms import *
import telebot

token = "1092503127:AAEY5BgQR0IAv6lSzwuOJzrMW8K186QRItM"

bot = telebot.TeleBot(token)


# Create your views here.


def contacts(request):
    # message = Contact.objects.all().first()
    # form = ContactFormForm()
    #
    # if request.method == 'POST':
    #     form = ContactFormForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         try:
    #             message_name = request.POST['name']
    #             message_phone = request.POST['phone']
    #             message_text = request.POST['content']
    #             sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎️ Telefon raqami: {message_phone} \n✉️ Xabar: {message_text}'
    #             bot.send_message(196862960, sms)
    #             return redirect('error')
    #
    #         except:
    #             message_name = request.POST['name']
    #             message_phone = request.POST['phone']
    #             sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎️ Telefon raqami: {message_phone} '
    #             bot.send_message(196862960, sms)
    #             return redirect('error')
    #
    # context = {
    #     'form': form,
    #     'message': message,
    #
    # }
    return render(request, 'top/contacts.html')





