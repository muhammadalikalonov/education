from django.core import serializers
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import telebot
from django.contrib import messages
from django.core.serializers import serialize
from django.http import JsonResponse

token = "1715097196:AAGBr9vZEhRxT1x8PnhrnfZY-mDA6Cj94i0"

bot = telebot.TeleBot(token)

def error_404_view(request,exception):
    return render(request, 'others/404.html')


def page(request):



    if request.method == 'POST':
        try:
            form = PageForms(request.POST)
        except:
            form = PageFormsuz(request.POST)


        if form.is_valid():
            form.save()
            try:
                message_name = request.POST['name']
                message_phone = request.POST['phone']
                message_birth_date = request.POST['birth_date']
                message_city = request.POST['city']
                message_email = request.POST['email']
                message_english = request.POST['english']
                message_study = request.POST['study']
                message_description = request.POST['description']
                message_take_date = request.POST['take_date']
                message_surname = request.POST['surname']
                sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_birth_date}\n☎️ Telefon raqami: {message_study} \n✉️ Xabar: {message_english}'
                bot.send_message( 721237497, sms)
                messages.success(request, 'Xabaringiz qabul qilindi. Tez orada operator aloqaga chiqadi!!! ')
                print(sms)

                return redirect('index')
            except:
                return redirect('index')

    context = {


    }
    return render(request,'others/cons.html', context)



def contacts(request):

    form = ContactFormForm()

    if request.method == 'POST':

        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()

            message_name = request.POST['name']
            message_phone = request.POST['phone']
            message_text = request.POST['content']
            sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎️ Telefon raqami: {message_phone} \n✉️ Xabar: {message_text}'
            bot.send_message( 721237497, sms)
            messages.success(request, 'Xabaringiz qabul qilindi. Tez orada operator aloqaga chiqadi!!! ')
            print(sms)
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'others/contacts.html')


def contact_mobile(request):
    formi = ContactFormForm2()

    if request.method == 'POST':

        formi = ContactFormForm(request.POST)
        if formi.is_valid():
            formi.save()

            message_name = request.POST['name']
            message_phone = request.POST['phone']
            message_text = request.POST['content']
            sms = f'📩 Sizga xabar keldi\n\nIsmi: {message_name}\n☎️ Telefon raqami: {message_phone} \n✉️ Xabar: {message_text}'
            bot.send_message(721237497, sms)
            messages.success(request, 'Xabaringiz qabul qilindi. Tez orada operator aloqaga chiqadi!!! ')
            print(sms)
            return redirect('index')

    context = {
        'formi': formi,
    }
    return render(request, 'others/contacts.html')


