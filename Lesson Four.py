from tkinter import Tk # احضار المكتبة التي نعمل عليها
from PIL import ImageTk , Image
root = Tk() # انشاء نافذة
root.geometry('500x500+450+100') # تغير مكان وحجم ضهور النافذة
root.title('Tkinter With Mohammed') # اضافة عنوان للنافذة 
root.configure(background='#262626') # تغير لون خلفية البرنامج
# root.iconbitmap('icon.ico') # هذه الأمر لتغير الأيقونة ولكن يدعم فقط امتداد ico
photo_app = ImageTk.PhotoImage(Image.open('python.png')) # فتح الصورة وتجهيدزها للأستعمال داخل البرنامج
root.iconphoto(True, photo_app) # تعين الصور كايقونة للبرنامج 
root.mainloop() # تكرار عدد فريمات النافذة 
