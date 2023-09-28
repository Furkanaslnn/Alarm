from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pygame.mixer
import time

root = Tk()

root.geometry("420x400")
root.title("AlarmHat By OrangeHat")
root.resizable(width=False, height=False)
root.configure(background='black')

ikon_yolu = "Alarm\icon.ico"
root.iconbitmap(ikon_yolu)

dogrula = 0

def onayla():
	now = datetime.now()
	formatli_date = now.strftime("%H:%M-%d.%m.%Y")
	label_tarih.config(text='Şuanki Tarih:\n' + formatli_date)
	tarih_verisi = girilen_deger.get()
	label_alarm.configure(text='Şuanki Alarm:\n' + tarih_verisi)
	
	if dogrula == 0:
		alarm_cal()
	
	root.after(1000, onayla)

def alarm_cal():
	kullanici_girdisi = girilen_deger.get()
	now = datetime.now()
	formatli_date = now.strftime("%H:%M-%d.%m.%Y")
	if kullanici_girdisi == formatli_date:
		pygame.mixer.init()
		muzik_dosyasi = "C:/Users/FURKAN/Desktop/,/Alarm/ses.mp3"
		pygame.mixer.music.load(muzik_dosyasi)
		pygame.mixer.music.play()
		messagebox.showerror("AlarmHat", "Alarm Çalıyor!!")
		pygame.mixer.music.stop()
		
		global dogrula
		dogrula = 1

tarih_simdi = "Şuanki tarih:\n" 
tarih_alarm = "Alarm tarihi:\n"

label_baslik = Label(root, width=38, height=5, bg='black', fg='orange', text='--- AlarmHat ---', font=('Arial', 14))
label_baslik.grid(row=0, column=0)

label_tarih = Label(root, width=60, height=6, bg='black', fg='orange', text=tarih_simdi)
label_tarih.grid(row=1, column=0)

label_alarm = Label(root, width=60, height=6, bg='black', fg='orange', text=tarih_alarm)
label_alarm.grid(row=2, column=0)

girilen_deger = StringVar()
entry_alarm = Entry(root, width=35, textvariable=girilen_deger)
entry_alarm.grid(row=3, column=0)

label_buton = Label(root, width=35, height=6, bg='black')
label_buton.grid(row=4, column=0)

onay_buton = Button(label_buton, width=7, height=1, bg='orange', text='Onayla', font=('Arial'), command=onayla)
onay_buton.grid(row=0, column=0)

onayla()

dogrula = 0

root.mainloop()