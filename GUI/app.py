import tkinter as tk
from tkinter import filedialog, Text, Canvas, Radiobutton, Checkbutton, StringVar, IntVar
import os
import tkinter.ttk as ttk
from tkinter.ttk import Frame
from PIL import Image, ImageTk
import pickle
import numpy as np

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


root = tk.Tk()
maxWidth = 800
maxHeight = 800
root.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))

#var = tk.StringVar()



#python = skill_python.get()
#print(python)
	
#print(str(skill_python.get()))

def close_window():
	root.destroy()
	exit()

def clear_all():
	output.delete('0.0', tk.END)

def click():
	lst=[]
	lst2=[]
	output.delete(0.0, tk.END)

	#input_var = prediction(var)
	#output.insert(tk.END, input_var)

	j_type = int(selection1)
	m_type = int(selection2)

	lst.insert(0,int(j_type))
	lst.append(int(python))
	lst.append(sql)
	lst.append(ml)
	lst.append(r)
	lst.append(hadoop)
	lst.append(tableau)
	lst.append(sas)
	lst.append(spark)
	lst.append(java)
	lst.append(others)
	#print(lst)
	#lst.reshape(-1,1)
	#lst = np.reshape(lst, (1, 1))
	lst2.insert(0,lst)
	if m_type==1:
		loaded_model = pickle.load(open('lmmodel.sav', 'rb'))
		#result = loaded_model.score(X_test, Y_test)
		#print(result)
		op = str(loaded_model.predict(lst2))
		final=op[2:]
		final=final[:-2]
		text=str("\n Predicted Income Class: "+final)
		output.insert(tk.END, text)
	if m_type==2:
		loaded_model = pickle.load(open('digreg.sav', 'rb'))
		#result = loaded_model.score(X_test, Y_test)
		#print(result)
		op = str(loaded_model.predict(lst2))
		final=op[2:]
		final=final[:-2]
		text=str("\n Predicted Income Class: "+final)
		output.insert(tk.END, text)
	if m_type==3:
		loaded_model = pickle.load(open('clf.sav', 'rb'))
		#result = loaded_model.score(X_test, Y_test)
		#print(result)
		op = str(loaded_model.predict(lst2))
		final=op[2:]
		final=final[:-2]
		text=str("\n Predicted Income Class: "+final)
		output.insert(tk.END, text)


root.title("Income Class Prediction")
canvas_width = 800
canvas_height = 10
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")

head_label = tk.Label(root, text="Income Class Prediction", font="none 40 bold")
head_label.pack()
canvas_width = 800
canvas_height = 10
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")
w = Canvas(root, width=200, height=230)
w.place(x=230, y=75)

w.create_line(0, 0, 0, 230, fill="#476042", width=3)
#left side
lline1_label = tk.Label(root, text="This is a Classification", font="none 10")
lline1_label.place(x=10, y=90)
lline2_label = tk.Label(root, text="project. It classifies income", font="none 10")
lline2_label.place(x=10, y=110)
lline3_label = tk.Label(root, text="as Low, Medium, High based on", font="none 10")
lline3_label.place(x=10, y=130)
lline4_label = tk.Label(root, text="the skills and the job title.", font="none 10")
lline4_label.place(x=10, y=150)
lline4_label = tk.Label(root, text="There are 3 machine learning", font="none 10")
lline4_label.place(x=10, y=170)
lline5_label = tk.Label(root, text="models used:", font="none 10")
lline5_label.place(x=10, y=190)
lline6_label = tk.Label(root, text="1. Naive Bayes Classifier", font="none 10")
lline6_label.place(x=10, y=210)
lline7_label = tk.Label(root, text="2. Multinomial Regression", font="none 10")
lline7_label.place(x=10, y=230)
lline8_label = tk.Label(root, text="3. Decision Tree Classifier", font="none 10")
lline8_label.place(x=10, y=250)


#image side

load = Image.open("image2.jpeg")
render = ImageTk.PhotoImage(load)
img = tk.Label(root, image=render)
img.image = render
img.place(x=290, y=75)

w = Canvas(root, width=10, height=230)
w.place(x=570, y=75)

w.create_line(0, 0, 0, 230, fill="#476042", width=3)





w = Canvas(root, width=800, height=20)
w.place(x=0, y=300)

w.create_line(0, 0, 800, 0, fill="#476042", width=3)





selection1=0
selection2=0

def sel1():
	global selection1
	#print(str(job_type.get()))
	selection1 = str(job_type.get())

#print(selection1)

def sel2():
	global selection2
	#print(str(class_y.get()))
	selection2 = str(class_y.get())

python=0
sql=0
ml=0
r=0
hadoop=0
tableau=0
sas=0
spark=0
java=0
others=0

def input_skills():
	global python,sql,ml,r,hadoop, tableau, sas, spark, java, others

	#print(str(skill_python.get()))

	if str(skill_python.get())=='1':
		python=1
	else:
		python=0
	if str(skill_sql.get())=='1':
		sql=1
	else:
		sql=0
	if str(skill_ml.get())=='1':
		ml=1
	else:
		ml=0
	if str(skill_r.get())=='1':
		r=1
	else:
		r=0
	if str(skill_hadoop.get())=='1':
		hadoop=1
	else:
		hadoop=0
	if str(skill_tableau.get())=='1':
		tableau=1
	else:
		tableau=0
	if str(skill_sas.get())=='1':
		sas=1
	else:
		sas=0
	if str(skill_spark.get())=='1':
		spark=1
	else:
		spark=0
	if str(skill_java.get())=='1':
		java=1
	else:
		spark=0
	if str(skill_others.get())=='1':
		others=1
	else:
		others=0
	
	#print(python,sql,ml,r,hadoop, tableau, sas, spark, java, others)


head1_label = tk.Label(root, text="Choose Job Role:", font="none 15 bold")
head1_label.place(x=20, y=320)

#var = IntVar()
job_type = StringVar()
R1 = Radiobutton(root, text="Data Analyst", variable=job_type, value=1, command=sel1)
R1.place(x=220, y=325)
R2 = Radiobutton(root, text="Data Engineer", variable=job_type, value=2, command=sel1)
R2.place(x=350, y=325)
R3 = Radiobutton(root, text="Data Scientist", variable=job_type, value=3, command=sel1)
R3.place(x=500, y=325)


head2_label = tk.Label(root, text="Choose Skills:", font="none 15 bold")
head2_label.place(x=20, y=350)

skill_python = IntVar()
C1 = Checkbutton(root, text="Python", variable=skill_python,onvalue=1,offvalue=0,command=input_skills)
C1.place(x=220, y=355)
skill_python.set(0)

skill_sql = IntVar()
C2 = Checkbutton(root, text="SQL", variable=skill_sql, onvalue=1,offvalue=0, command=input_skills)
C2.place(x=290, y=355)
skill_sql.set(0)

skill_ml = IntVar()
C3 = Checkbutton(root, text="Machine Learning", variable=skill_ml, onvalue=1,offvalue=0, command=input_skills)
C3.place(x=330, y=355)
skill_ml.set(0)

skill_r = IntVar()
C4 = Checkbutton(root, text="R", variable=skill_r, onvalue=1,offvalue=0, command=input_skills) 
C4.place(x=460, y=355)
skill_r.set(0)


skill_hadoop = IntVar()
C5 = Checkbutton(root, text="Hadoop", variable=skill_hadoop, onvalue=1,offvalue=0, command=input_skills)
C5.place(x=500, y=355)
skill_hadoop.set(0)

skill_tableau = IntVar()
C6 = Checkbutton(root, text="Tableau", variable=skill_tableau, onvalue=1,offvalue=0, command=input_skills) 
C6.place(x=220, y=375)
skill_tableau.set(0)


skill_sas = IntVar()
C7 = Checkbutton(root, text="Sas", variable=skill_sas, onvalue=1,offvalue=0, command=input_skills)
C7.place(x=290, y=375)
skill_sas.set(0)


skill_spark = IntVar()
C8 = Checkbutton(root, text="Spark", variable=skill_spark, onvalue=1,offvalue=0, command=input_skills)
C8.place(x=330, y=375)
skill_spark.set(0)


skill_java = IntVar()
C9 = Checkbutton(root, text="Java", variable=skill_java, onvalue=1,offvalue=0, command=input_skills)
C9.place(x=385, y=375)
skill_java.set(0)


skill_others = IntVar()
C10 = Checkbutton(root, text="Others", variable=skill_others, onvalue=1,offvalue=0, command=input_skills)
C10.place(x=435, y=375)
skill_others.set(0)




head3_label = tk.Label(root, text="Choose Classifier:", font="none 15 bold")
head3_label.place(x=20, y=405)

#var = IntVar()
class_y = StringVar()
A1 = Radiobutton(root, text="Naive Bayes Classifier", variable=class_y, value=1, command=sel2)
A1.place(x=240, y=410)

A2 = Radiobutton(root, text="Multinomial Regression", variable=class_y, value=2, command=sel2)
A2.place(x=430, y=410)

A3 = Radiobutton(root, text="Decision Tree", variable=class_y, value=3, command=sel2)
A3.place(x=240, y=430)



convert = tk.Button(root, text="APPLY", padx=30, pady=15, fg="white", bg="#263D42", command=click)
convert.place(x=20, y=470)



head4_label = tk.Label(root, text="Prediction:", font="none 15 bold")
head4_label.place(x=20, y=525)

output = Text(root, width=40, height=5, font = "Calibri 17")
output.place(x=20, y=550)



exitbut = tk.Button(root, text="EXIT", padx=25, pady=10, fg="white", bg="#263D42", command=close_window)
exitbut.place(x=500, y=620)

clearbut = tk.Button(root, text="CLEAR", padx=30, pady=15, fg="white", bg="#263D42", command=clear_all)
clearbut.place(x=140, y=470)

root.mainloop()
