from tkinter import *
import mysql.connector as rajjo
from tkinter.font import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import csv
import os
import shutil






def reset_data():
    ansr=messagebox.askquestion("Reset","Are you sure you want to reset all data of this project?")
    if(ansr=="yes"):
        try:
            shutil.rmtree("Data")
            s="DROP DATABASE class_management"
            cur.execute(s)
        except:
            pass
        root.quit()



def reset():
    all_frames=[sec_view_part_sub_res_frame,first_view_part_sub_res_frame,sec_add_part_sub_res_frame,first_add_part_sub_res_frame,add_part_sub_res_frame,view_sec_result_list_frame,view_sec_result_frame,view_first_result_list_frame,view_first_result_frame,add_first_result_list_frame,add_sec_result_list_frame,add_first_result_frame,add_sec_result_frame,result_inner_frame,result_frame,result_outer_frame,view_this_attendance_btn_frame,view_this_attendance_frame,view_this_attendance_outer_frame,view_attendance_btn_frame,view_attendance_frame,view_attendance_outer_frame,add_attendance_btn_frame,add_attendance_frame,add_attendance_outer_frame,attendance_frame,attendance_outer_frame,view_this_daily_activities_btn_frame,view_this_daily_activities_outer_frame,view_this_daily_activities_frame,view_daily_activities_btn_frame,view_daily_activities_outer_frame,view_daily_activities_frame,add_daily_activities_btn_frame,add_daily_activities_outer_frame,add_daily_activities_frame,daily_activities_frame,daily_activities_outer_frame,edit_this_student_frame,edit_students_outer_frame,edit_students_frame,edit_students_list_frame,edit_this_teacher_frame,edit_teachers_outer_frame,edit_teachers_frame,edit_teachers_list_frame,remove_teachers_list_frame,view_teachers_list_frame,remove_students_list_frame,view_students_list_frame,view_this_teacher_frame,view_teachers_outer_frame,view_teachers_frame,remove_teachers_outer_frame,remove_teachers_frame,remove_students_outer_frame,remove_students_frame,remove_this_student_frame,view_this_student_frame,view_students_outer_frame,view_students_frame,routine_outer_frame,empty_routine_frame,read_routine_frame,write_routine_frame,teachers_frame,teachers_btn_frame,students_frame,students_btn_frame,students_outer_frame,teachers_outer_frame,login_frame,choice_outer_frame,choice_frame,login_outer_frame,add_students_frame,add_students_outer_frame,add_students_btn_frame,add_teachers_outer_frame,add_teachers_frame,add_teachers_btn_frame]
    for frame in all_frames:
        for widget in frame.winfo_children():
            if widget not in all_frames:
                widget.destroy()
        frame.pack_forget()  



def show_attendance_frame():
    reset()
    
    def show_add_attendance_frame():
        reset()
        label=Label(add_attendance_outer_frame,image=attendance_banner,bd=0).pack(side=TOP)
        for i in range(3):
            add_attendance_frame.rowconfigure(i,weight=1)
        for j in range(3):
            add_attendance_frame.columnconfigure(j,weight=1)
        myfont=("Comic Sans MS",15)
        present_stu=[]
        tpre=len(present_stu)
        absent_stu=[]
        tabsnt=len(absent_stu)
        dt=DateEntry(add_attendance_frame,date_pattern="dd-MM-yyyy",width=28,font=myfont,selectmode="day",justify=CENTER)
        dt.grid(row=0,column=0,columnspan=3)
        lab=Label(add_attendance_frame,text="Present",font=myfont,bg="#92A0D1",bd=0).grid(row=1,column=0)
        lab=Label(add_attendance_frame,text="Student",font=myfont,bg="#92A0D1",bd=0).grid(row=1,column=1)
        lab=Label(add_attendance_frame,text="Absent",font=myfont,bg="#92A0D1",bd=0).grid(row=1,column=2)
        s="SELECT * FROM students"
        cur.execute(s)
        data=cur.fetchall()
        lfont=Font(family="comic sans ms",size=15)
        present_list=Listbox(add_attendance_frame,width=30,height=10,font=lfont)
        present_list.grid(row=2,column=0)
        student_list=Listbox(add_attendance_frame,width=30,height=10,font=lfont)
        student_list.grid(row=2,column=1)
        absent_list=Listbox(add_attendance_frame,width=30,height=10,font=lfont)
        absent_list.grid(row=2,column=2)
        student_list.configure(background="black",foreground="white")
        present_list.configure(background="black",foreground="white")
        absent_list.configure(background="black",foreground="white")
        
        for i in range(len(data)):
            if len(str(data[i][2]))==1:
                s=str(data[i][2])+str("    ")+str(data[i][0])
            elif len(str(data[i][2]))==2:
                s=str(data[i][2])+str("   ")+str(data[i][0])
            elif len(str(data[i][2]))==3:
                s=str(data[i][2])+str("  ")+str(data[i][0])
            else:
                s=str(data[i][2])+str("    ")+str(data[i][0])
            student_list.insert(i,s)

        def present_act():
            try:
                global tpre
                Clicked_items=student_list.curselection()
                sel=Clicked_items[0]
                ins=student_list.get(sel)
                student_list.delete(sel)
                present_list.insert(0,ins)
                pri=""
                for i in ins:
                    pri+=i
                present_stu.append(pri)
                tpre=len(present_stu)
            except:
                messagebox.showwarning("Warning","Select the student first!")
        def absent_act():
            try:
                global tabsnt
                Clicked_items=student_list.curselection()
                sel=Clicked_items[0]
                ins=student_list.get(sel)
                student_list.delete(sel)
                absent_list.insert(0,ins)
                pri=""
                for i in ins:
                    pri+=i
                absent_stu.append(pri)
                tabsnt=len(absent_stu)
            except:
                messagebox.showwarning("Warning","Select the student first!")
        def set_act():
            gotdb=dt.get_date()
            gotdb1=gotdb.strftime("%d-%m-%Y")
            filenamed="Data\\Attendance\\" + str(gotdb1) +".csv"
            f=open(filenamed,"w")
            write=csv.writer(f)
            write.writerow(present_stu)
            write.writerow(absent_stu)
            f.close()
            messagebox.showinfo("Added",f"Attendance added successfully!\nTotal Present : {len(present_stu)}\nTotal Absent : {len(absent_stu)}")
            show_attendance_frame()
        
        for i in range(5):
            add_attendance_btn_frame.columnconfigure(i,weight=1)
        add_attendance_btn_frame.rowconfigure(0,weight=1)
        saveact=Button(add_attendance_btn_frame,image=set_btn,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=set_act).grid(row=0,column=2)
        gobck=Button(add_attendance_btn_frame,image=goback_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=show_attendance_frame).grid(row=0,column=0)
        present=Button(add_attendance_btn_frame,image=present_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=present_act).grid(row=0,column=1)
        absent=Button(add_attendance_btn_frame,image=absent_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=absent_act).grid(row=0,column=3)
        close=Button(add_attendance_btn_frame,image=close_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=show_choice_frame).grid(row=0,column=4)
        
        add_attendance_frame.pack(expand=True,fill="both")
        add_attendance_frame.tkraise()
        add_attendance_btn_frame.pack(expand=True,fill="both",side=BOTTOM,pady=15)
        add_attendance_btn_frame.tkraise()
        add_attendance_outer_frame.pack(expand=True,fill="both")
        add_attendance_outer_frame.tkraise()

    def show_view_attendance_frame():
        reset()
        label=Label(view_attendance_outer_frame,image=attendance_banner,bd=0).pack(side=TOP)
        for i in range(2):
            view_attendance_frame.rowconfigure(i,weight=1)
        view_attendance_frame.columnconfigure(0,weight=1)
        myfont=("Comic Sans MS",15)
        dt=DateEntry(view_attendance_frame,date_pattern="dd-MM-yyyy",width=28,font=myfont,selectmode="day",justify=CENTER)
        dt.grid(row=0,column=0)
        btn=Button(view_attendance_frame,bd=0,bg="#92A0D1",activebackground="#92A0D1",image=view_photo,command=lambda:show_this_attendance_frame(dt.get_date()))
        btn.grid(row=1,column=0)
        for i in range(2):
            view_attendance_btn_frame.columnconfigure(i,weight=1)
        view_attendance_btn_frame.rowconfigure(0,weight=1)
        
        gobck=Button(view_attendance_btn_frame,image=goback_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=show_attendance_frame).grid(row=0,column=0)
        close=Button(view_attendance_btn_frame,image=close_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=show_choice_frame).grid(row=0,column=1)
        
        view_attendance_frame.pack(expand=True,fill="both")
        view_attendance_frame.tkraise()
        view_attendance_btn_frame.pack(expand=True,fill="both",side=BOTTOM,pady=15)
        view_attendance_btn_frame.tkraise()
        view_attendance_outer_frame.pack(expand=True,fill="both")
        view_attendance_outer_frame.tkraise()
    
    def show_this_attendance_frame(dt):
        try:
            gotdb1=dt.strftime("%d-%m-%Y")
            filenamed="Data\\Attendance\\" + str(gotdb1) +".csv"
            f=open(filenamed,"r")
            reset()
            myfont=("Comic Sans MS",20)
            label=Label(view_this_attendance_outer_frame,image=attendance_banner,bd=0).pack(side=TOP)
            for i in range(2):
                view_this_attendance_frame.columnconfigure(i,weight=1)
            for i in range(3):
                view_this_attendance_frame.rowconfigure(i,weight=1)
            lab=Label(view_this_attendance_frame,text="Present",font=myfont,bg="#92A0D1",bd=0).grid(row=0,column=0)
            lab=Label(view_this_attendance_frame,text="Absent",font=myfont,bg="#92A0D1",bd=0).grid(row=0,column=1)
            filenamed="Data\\Attendance\\" + str(gotdb1) +".csv"
            f=open(filenamed,"r")
            read=csv.reader(f)
            L=[]
            m=0
            for i in read:
                if m%2==0:
                    L.append(i)
                m+=1
            f.close()
            pre_stu=""
            abs_stu=""

            for i in L[0]:
                pre_stu+=i
                pre_stu+="\n"
            for i in L[1]:
                abs_stu+=i
                abs_stu+="\n"
            myfont=("Comic Sans MS",15)
            lab=Label(view_this_attendance_frame,text=pre_stu,font=myfont,bg="#92A0D1",bd=0).grid(row=1,column=0)
            lab=Label(view_this_attendance_frame,text=abs_stu,font=myfont,bg="#92A0D1",bd=0).grid(row=1,column=1)
            lab=Label(view_this_attendance_frame,text=f"Total Present : {len(L[0])}",font=myfont,bg="#92A0D1",fg="yellow",bd=0).grid(row=2,column=0)
            lab=Label(view_this_attendance_frame,text=f"Total Absent : {len(L[1])}",font=myfont,bg="#92A0D1",fg="yellow",bd=0).grid(row=2,column=1)
            for i in range(2):
                view_this_attendance_btn_frame.columnconfigure(i,weight=1)
            view_this_attendance_btn_frame.rowconfigure(0,weight=1)
            gobck=Button(view_this_attendance_btn_frame,image=goback_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=show_view_attendance_frame).grid(row=0,column=0)
            close=Button(view_this_attendance_btn_frame,image=close_photo,bg="#92A0D1",bd=0,activebackground="#92A0D1",command=show_choice_frame).grid(row=0,column=1)
            view_this_attendance_frame.pack(expand=True,fill="both")
            view_this_attendance_frame.tkraise()
            view_this_attendance_btn_frame.pack(expand=True,fill="both",side=BOTTOM,pady=15)
            view_this_attendance_btn_frame.tkraise()
            view_this_attendance_outer_frame.pack(expand=True,fill="both")
            view_this_attendance_outer_frame.tkraise()
        except:
            messagebox.showerror("Error","No record found for this date!")
        


        

    label=Label(attendance_outer_frame,image=attendance_banner,bd=0).pack(side=TOP)
    for i in range(3):
        attendance_frame.rowconfigure(i,weight=1)
    attendance_frame.columnconfigure(0,weight=1)
    view=Button(attendance_frame,bg="#92A0D1",bd=0,image=view_photo,activebackground="#92A0D1",command=show_view_attendance_frame).grid(row=0,column=0)
    add=Button(attendance_frame,bg="#92A0D1",bd=0,image=add_photo,activebackground="#92A0D1",command=show_add_attendance_frame).grid(row=1,column=0)
    close=Button(attendance_frame,bg="#92A0D1",bd=0,image=close_photo,activebackground="#92A0D1",command=show_choice_frame).grid(row=2,column=0)
    
    attendance_frame.pack(expand=True,fill="both")
    attendance_frame.tkraise()
    attendance_outer_frame.pack(expand=True,fill="both")
    attendance_outer_frame.tkraise()




def show_result_frame():
    reset()
    def show_add_result_inner_frame():
        reset()
        label=Label(result_outer_frame,image=results_banner,bd=0).pack(side=TOP)
        result_inner_frame.columnconfigure(0,weight=1)
        for i in range(4):
            result_inner_frame.rowconfigure(i,weight=1)
        fst_btn=Button(result_inner_frame,image=first_term_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_add_first_result_frame).grid(row=0,column=0)
        sec_btn=Button(result_inner_frame,image=sec_term_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_add_sec_result_frame).grid(row=1,column=0)
        goback_btn=Button(result_inner_frame,image=goback_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_result_frame).grid(row=2,column=0)
        close_btn=Button(result_inner_frame,image=close_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_choice_frame).grid(row=3,column=0)
        result_outer_frame.pack(expand=True,fill="both")
        result_outer_frame.tkraise()
        result_inner_frame.pack(expand=True,fill="both",side=BOTTOM)
        result_inner_frame.tkraise()


    def show_view_result_inner_frame():
        reset()
        label=Label(result_outer_frame,image=results_banner,bd=0).pack(side=TOP)
        result_inner_frame.columnconfigure(0,weight=1)
        for i in range(4):
            result_inner_frame.rowconfigure(i,weight=1)
        fst_btn=Button(result_inner_frame,image=first_term_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_view_first_result_frame).grid(row=0,column=0)
        sec_btn=Button(result_inner_frame,image=sec_term_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_view_sec_result_frame).grid(row=1,column=0)
        goback_btn=Button(result_inner_frame,image=goback_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_result_frame).grid(row=2,column=0)
        close_btn=Button(result_inner_frame,image=close_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_choice_frame).grid(row=3,column=0)
        result_outer_frame.pack(expand=True,fill="both")
        result_outer_frame.tkraise()
        result_inner_frame.pack(expand=True,fill="both",side=BOTTOM)
        result_inner_frame.tkraise()

    def show_first_add_part_sub_res_frame(sb,mm):
        try:
            mmi=float(mm)
            reset()
            def add_first_marks(rno,mo):
                try:
                    moi=float(mo)
                    if moi>mmi:
                        b=1/0
                    s="SELECT * FROM students"
                    cur.execute(s)
                    data=cur.fetchall()
                    for i in data:
                        if i[2]==int(rno):
                            break
                    else:
                        b=1/0
                    f=open(f"Data\\Results\\Term 1\\Roll {rno}.csv","a",newline="")
                    f1s=open(f"Data\\Results\\Term 1\\{sb}.csv","a",newline="")
                    write=csv.writer(f)
                    write1s=csv.writer(f1s)
                    write.writerow((sb,moi,mmi))
                    write1s.writerow((rno,moi))
                    f.close()
                    f1s.close()
                    show_first_add_part_sub_res_frame(sb,mm)

                except:
                    messagebox.showerror("Error","Something went wrong!")

            label=Label(result_outer_frame,image=first_trm_banner,bd=0).pack(side=TOP)
            for i in range(7):
                first_add_part_sub_res_frame.rowconfigure(i,weight=1)
            for i in range(2):
                first_add_part_sub_res_frame.columnconfigure(i,weight=1)
            myfont=("comic sans ms",20)
            sub_label=Label(first_add_part_sub_res_frame,text=sb,fg="pink",font=("comic sans ms",40),bg="#3256A8",bd=0).grid(row=0,columnspan=2)
            mm_label=Label(first_add_part_sub_res_frame,text=f"Maximum Marks : {mmi}",fg="white",font=("Comic Sans ms",10),bg="#3256A8",bd=0).grid(row=1,columnspan=2)
            try:
                f1r=open(f"Data\\Results\\Term 1\\{sb}.csv","r")
                read1r=csv.reader(f1r)
                L={}
                for i in read1r:
                    L.update({i[0]:i[1]})
                f1r.close()
                sttr=""
                c=0
                for i in L:
                    c+=1
                    if c%10==0:
                        sttr+=str(f"{i}:{L[i]}      ")+"\n"
                    else:
                        sttr+=str(f"{i}:{L[i]}      ")
                coll_label=Label(first_add_part_sub_res_frame,text=sttr,font=("Comic Sans ms",10),fg="white",bg="#3256A8",bd=0).grid(row=2,columnspan=2)
            except:
                pass
            roll_label=Label(first_add_part_sub_res_frame,text="Roll no.",font=("Comic Sans ms",20),bg="#3256A8",bd=0).grid(row=3,column=0)
            marks_label=Label(first_add_part_sub_res_frame,text="Marks Obtained",font=myfont,bg="#3256A8",bd=0).grid(row=3,column=1)
            roll_label_entry=Entry(first_add_part_sub_res_frame,font=myfont,width=30,justify=CENTER)
            roll_label_entry.grid(row=4,column=0)
            marks_label_entry=Entry(first_add_part_sub_res_frame,font=myfont,width=30,justify=CENTER)
            marks_label_entry.grid(row=4,column=1)
            add_button=Button(first_add_part_sub_res_frame,image=add_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=lambda:add_first_marks(roll_label_entry.get(),marks_label_entry.get())).grid(row=5,columnspan=2)
            goback_button=Button(first_add_part_sub_res_frame,image=goback_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_add_first_result_frame).grid(row=6,column=0)
            close_button=Button(first_add_part_sub_res_frame,image=close_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_result_frame).grid(row=6,column=1)
            first_add_part_sub_res_frame.pack(expand=True,fill="both")
            first_add_part_sub_res_frame.tkraise()
            result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
            result_outer_frame.tkraise()
        except:
            messagebox.showerror("Error","Invalid input")
    def show_sec_add_part_sub_res_frame(sb,mm):
        try:
            mmi=float(mm)
            reset()
            def add_sec_marks(rno,mo):
                try:
                    moi=float(mo)
                    if moi>mmi:
                        b=1/0
                    s="SELECT * FROM students"
                    cur.execute(s)
                    data=cur.fetchall()
                    for i in data:
                        if i[2]==int(rno):
                            break
                    else:
                        b=1/0
                    f=open(f"Data\\Results\\Term 2\\Roll {rno}.csv","a",newline="")
                    f1s=open(f"Data\\Results\\Term 2\\{sb}.csv","a",newline="")
                    write=csv.writer(f)
                    write1s=csv.writer(f1s)
                    write.writerow((sb,moi,mmi))
                    write1s.writerow((rno,moi))
                    f.close()
                    f1s.close()
                    show_sec_add_part_sub_res_frame(sb,mm)

                except:
                    messagebox.showerror("Error","Something went wrong!")

            label=Label(result_outer_frame,image=sec_trm_banner,bd=0).pack(side=TOP)
            for i in range(7):
                sec_add_part_sub_res_frame.rowconfigure(i,weight=1)
            for i in range(2):
                sec_add_part_sub_res_frame.columnconfigure(i,weight=1)
            myfont=("comic sans ms",20)
            sub_label=Label(sec_add_part_sub_res_frame,text=sb,fg="pink",font=("comic sans ms",40),bg="#3256A8",bd=0).grid(row=0,columnspan=2)
            mm_label=Label(sec_add_part_sub_res_frame,text=f"Maximum Marks : {mmi}",fg="white",font=("Comic Sans ms",10),bg="#3256A8",bd=0).grid(row=1,columnspan=2)
            try:
                f1r=open(f"Data\\Results\\Term 2\\{sb}.csv","r")
                read1r=csv.reader(f1r)
                L={}
                for i in read1r:
                    L.update({i[0]:i[1]})
                f1r.close()
                sttr=""
                c=0
                for i in L:
                    c+=1
                    if c%10==0:
                        sttr+=str(f"{i}:{L[i]}      ")+"\n"
                    else:
                        sttr+=str(f"{i}:{L[i]}      ")
                coll_label=Label(sec_add_part_sub_res_frame,text=sttr,font=("Comic Sans ms",10),fg="white",bg="#3256A8",bd=0).grid(row=2,columnspan=2)
            except:
                pass
            roll_label=Label(sec_add_part_sub_res_frame,text="Roll no.",font=("Comic Sans ms",20),bg="#3256A8",bd=0).grid(row=3,column=0)
            marks_label=Label(sec_add_part_sub_res_frame,text="Marks Obtained",font=myfont,bg="#3256A8",bd=0).grid(row=3,column=1)
            roll_label_entry=Entry(sec_add_part_sub_res_frame,font=myfont,width=30,justify=CENTER)
            roll_label_entry.grid(row=4,column=0)
            marks_label_entry=Entry(sec_add_part_sub_res_frame,font=myfont,width=30,justify=CENTER)
            marks_label_entry.grid(row=4,column=1)
            add_button=Button(sec_add_part_sub_res_frame,image=add_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=lambda:add_sec_marks(roll_label_entry.get(),marks_label_entry.get())).grid(row=5,columnspan=2)
            goback_button=Button(sec_add_part_sub_res_frame,image=goback_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_add_sec_result_frame).grid(row=6,column=0)
            close_button=Button(sec_add_part_sub_res_frame,image=close_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_result_frame).grid(row=6,column=1)
            sec_add_part_sub_res_frame.pack(expand=True,fill="both")
            sec_add_part_sub_res_frame.tkraise()
            result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
            result_outer_frame.tkraise()
        except:
            messagebox.showerror("Error","Invalid input")
    def show_add_first_result_frame():
        reset()
        def close_fun():
            show_result_frame()
        def goback_fun():
            show_add_result_inner_frame()

        label=Label(result_outer_frame,image=first_trm_banner,bd=0).pack(side=TOP)
        for i in range(4):
            add_first_result_frame.rowconfigure(i,weight=1)
        for i in range(2):
            add_first_result_frame.columnconfigure(i,weight=1)
        myfont=("comic sans ms",20)
        sub_label=Label(add_first_result_frame,text="Subject",font=("comic sans ms",20),bg="#3256A8",bd=0).grid(row=0,column=0)
        max_marks_label=Label(add_first_result_frame,text="Maximum Marks",font=myfont,bg="#3256A8",bd=0).grid(row=0,column=1)
        sub_label_entry=Entry(add_first_result_frame,font=myfont,width=30,justify=CENTER)
        sub_label_entry.grid(row=1,column=0)
        max_marks_label_entry=Entry(add_first_result_frame,font=myfont,width=30,justify=CENTER)
        max_marks_label_entry.grid(row=1,column=1)
        pro_button=Button(add_first_result_frame,image=proceed_image,activebackground="#3256A8",bg="#3256A8",bd=0,command=lambda:show_first_add_part_sub_res_frame(sub_label_entry.get().upper(),max_marks_label_entry.get())).grid(row=2,columnspan=2)
        goback_button=Button(add_first_result_frame,image=goback_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=goback_fun).grid(row=3,column=0)
        close_button=Button(add_first_result_frame,image=close_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=close_fun).grid(row=3,column=1)
        
        add_first_result_frame.pack(expand=True,fill="both")
        add_first_result_frame.tkraise()
        result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
        result_outer_frame.tkraise()

    def show_add_sec_result_frame():
        reset()
        def close_fun():
            show_result_frame()
        def goback_fun():
            show_add_result_inner_frame()

        label=Label(result_outer_frame,image=sec_trm_banner,bd=0).pack(side=TOP)
        for i in range(4):
            add_sec_result_frame.rowconfigure(i,weight=1)
        for i in range(2):
            add_sec_result_frame.columnconfigure(i,weight=1)
        myfont=("comic sans ms",20)
        sub_label=Label(add_sec_result_frame,text="Subject",font=("comic sans ms",20),bg="#3256A8",bd=0).grid(row=0,column=0)
        max_marks_label=Label(add_sec_result_frame,text="Maximum Marks",font=myfont,bg="#3256A8",bd=0).grid(row=0,column=1)
        sub_label_entry=Entry(add_sec_result_frame,font=myfont,width=30,justify=CENTER)
        sub_label_entry.grid(row=1,column=0)
        max_marks_label_entry=Entry(add_sec_result_frame,font=myfont,width=30,justify=CENTER)
        max_marks_label_entry.grid(row=1,column=1)
        pro_button=Button(add_sec_result_frame,image=proceed_image,activebackground="#3256A8",bg="#3256A8",bd=0,command=lambda:show_sec_add_part_sub_res_frame(sub_label_entry.get().upper(),max_marks_label_entry.get())).grid(row=2,columnspan=2)
        goback_button=Button(add_sec_result_frame,image=goback_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=goback_fun).grid(row=3,column=0)
        close_button=Button(add_sec_result_frame,image=close_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=close_fun).grid(row=3,column=1)
        
        add_sec_result_frame.pack(expand=True,fill="both")
        add_sec_result_frame.tkraise()
        result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
        result_outer_frame.tkraise()


    def show_view_first_result_frame():
        reset()
        def show_first_view_part_sub_res_frame():
            try:
                Clicked_items=l.curselection()
                for item in Clicked_items:
                    it=l.get(item)
                s=""
                for i in it[:4]:
                    if i.isdigit():
                        s+=i
                try:
                    f=open(f"Data\\Results\\Term 1\\Roll {s}.csv","r")
                    read=csv.reader(f)
                    c=0
                    L=[]
                    for i in read:
                        L+=(i,)
                        c+=1
                    reset()
                    label=Label(result_outer_frame,image=first_trm_banner,bd=0).pack(side=TOP)
                    for i in range(6):
                        first_view_part_sub_res_frame.columnconfigure(i,weight=1)
                    for i in range(6+c):
                        if i<=1 or i>2+c:
                            first_view_part_sub_res_frame.rowconfigure(i,weight=1)
                        else:
                            first_view_part_sub_res_frame.rowconfigure(i,weight=2)
                    selectdb="SELECT * FROM students"
                    cur.execute(selectdb)
                    data=cur.fetchall()
                    for i in data:
                        if i[2]==int(s):
                            name=i[0]
                            dob=i[4]
                            admno=i[3]
                            phone=i[10]

                    name_label=Label(first_view_part_sub_res_frame,text="Name : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=0,sticky=E)
                    name_a=Label(first_view_part_sub_res_frame,text=name,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=1,sticky=W)
                    class_label=Label(first_view_part_sub_res_frame,text="Class : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=2,sticky=E)
                    class_a=Label(first_view_part_sub_res_frame,text="12 'A'",fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=3,sticky=W)
                    dob_label=Label(first_view_part_sub_res_frame,text="D.O.B. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=4,sticky=E)
                    dob_label=Label(first_view_part_sub_res_frame,text=dob,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=5,sticky=W)
                    roll_label=Label(first_view_part_sub_res_frame,text="Roll no. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=0,sticky=E)
                    roll_a=Label(first_view_part_sub_res_frame,text=s,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=1,sticky=W)
                    admno_label=Label(first_view_part_sub_res_frame,text="Adm no. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=2,sticky=E)
                    admno_a_label=Label(first_view_part_sub_res_frame,text=admno,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=3,sticky=W)
                    phone_label=Label(first_view_part_sub_res_frame,text="Phone no. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=4,sticky=E)
                    phone_a=Label(first_view_part_sub_res_frame,text=phone,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=5,sticky=W)

                    sub_label=Label(first_view_part_sub_res_frame,text="Subject",font=("comic sans ms",25),fg="yellow",bg="#3256A8",bd=0).grid(row=2,column=0,columnspan=2)
                    marks_obt=Label(first_view_part_sub_res_frame,text="Marks Obtained",font=("comic sans ms",25),fg="yellow",bg="#3256A8",bd=0).grid(row=2,column=2,columnspan=2)
                    fm=Label(first_view_part_sub_res_frame,text="Maximum Marks",font=("comic sans ms",25),fg="yellow",bg="#3256A8",bd=0).grid(row=2,column=4,columnspan=2)
                    rows=3
                    tobt=0
                    tmax=0
                    for i in L:
                        columns=0
                        tobt+=float(i[1])
                        tmax+=float(i[2])
                        for j in i:
                            lab=Label(first_view_part_sub_res_frame,text=j,font=("comic sans ms",15),fg="light green",bg="#3256A8",bd=0).grid(row=rows,column=columns,columnspan=2)
                            columns+=2
                        rows+=1
                    marks_label=Label(first_view_part_sub_res_frame,text="Marks : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=0,sticky=E)
                    marks_a=Label(first_view_part_sub_res_frame,text=f"{tobt} / {tmax}",fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=1,sticky=W)
                    perc_label=Label(first_view_part_sub_res_frame,text="Percentage : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=4,sticky=E)
                    ppeer=tobt*100/tmax
                    perc_a=Label(first_view_part_sub_res_frame,text=str("{:.2f}".format(ppeer))+" %",fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=5,sticky=W)
                    result="Pass"
                    if 91<= float(tobt*100/tmax) <= 100 :
                        grade= "A1 (Outstanding)"
                    elif 81<= float(tobt*100/tmax) < 91 :
                        grade= "A2 (Excellent)"
                    elif 71<= float(tobt*100/tmax) < 81 :
                        grade= "B1 (Very Good)"
                    elif 61<= float(tobt*100/tmax) < 71 :
                        grade= "B1 (Good)"
                    elif 51<= float(tobt*100/tmax) < 61 :
                        grade= "C1 (Above Average)"
                    elif 41<= float(tobt*100/tmax) < 51 :
                        grade= "C1 (Average)"
                    elif 33<= float(tobt*100/tmax) < 41 :
                        grade= "D (Pass)"
                    elif 21<= float(tobt*100/tmax) < 33 :
                        grade= "E1 (Needs Improvement)"
                        result="Fail"
                    elif 0<= float(tobt*100/tmax) < 21 :
                        grade= "E2 (Needs Improvement)"
                        result="Fail"
                    else:
                        grade="Invalid"
                        result="Invalid"
                    grade_label=Label(first_view_part_sub_res_frame,text="Grade : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=0,sticky=E)
                    grade_a=Label(first_view_part_sub_res_frame,text=grade,fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=1,sticky=W)
                    result_label=Label(first_view_part_sub_res_frame,text="Result : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=4,sticky=E)
                    result_a=Label(first_view_part_sub_res_frame,text=result,fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=5,sticky=W)
                    goback_button=Button(first_view_part_sub_res_frame,image=goback_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_view_first_result_frame).grid(row=5+c,column=0,columnspan=2)
                    close_button=Button(first_view_part_sub_res_frame,image=close_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_result_frame).grid(row=5+c,column=4,columnspan=2)

                    first_view_part_sub_res_frame.pack(expand=True,fill="both")
                    first_view_part_sub_res_frame.tkraise()
                    result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
                    result_outer_frame.tkraise()
                except:
                    messagebox.showerror("Error","No record found!")
            except:
                messagebox.showerror("Error","Select the student first")
        
        
        
        def gob():
            show_view_result_inner_frame()
        label=Label(result_outer_frame,image=first_trm_banner,bd=0).pack(side=TOP)
        #add_first_result_frame
        for i in range(2):
            view_first_result_frame.columnconfigure(i,weight=1)
        for i in range(2):
            view_first_result_frame.rowconfigure(i,weight=1)
        s="SELECT * FROM students"
        cur.execute(s)
        data=cur.fetchall()
        lfont=Font(family="comic sans ms",size=15)
        l=Listbox(view_first_result_list_frame,width=25,height=10,selectmode=SINGLE,font=lfont)
        l.pack(side=LEFT,fill=BOTH)
        scrollbar=Scrollbar(view_first_result_list_frame)
        scrollbar.pack(side=RIGHT,fill=BOTH)
        for i in range(len(data)):
            if len(str(data[i][2]))==1:
                s=str(data[i][2])+str("    ")+str(data[i][0])
            elif len(str(data[i][2]))==2:
                s=str(data[i][2])+str("   ")+str(data[i][0])
            elif len(str(data[i][2]))==3:
                s=str(data[i][2])+str("  ")+str(data[i][0])
            else:
                s=str(data[i][2])+str("    ")+str(data[i][0])
            l.insert(i,s)
        l.config(yscrollcommand=scrollbar.set)
        l.configure(background="black",foreground="white")
        scrollbar.config(command=l.yview)
        view_first_result_list_frame.grid(row=0,columnspan=2)
        goback_btn=Button(view_first_result_frame,image=goback_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=gob).grid(row=1,column=0)
        pro_btn=Button(view_first_result_frame,image=proceed_image,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_first_view_part_sub_res_frame).grid(row=1,column=1)


        view_first_result_list_frame.tkraise()
        view_first_result_frame.pack(expand=True,fill="both")
        view_first_result_frame.tkraise()
        result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
        result_outer_frame.tkraise()



    def show_view_sec_result_frame():
        reset()
        def show_sec_view_part_sub_res_frame():
            try:
                Clicked_items=l.curselection()
                for item in Clicked_items:
                    it=l.get(item)
                s=""
                for i in it[:4]:
                    if i.isdigit():
                        s+=i
                try:
                    f=open(f"Data\\Results\\Term 2\\Roll {s}.csv","r")
                    read=csv.reader(f)
                    c=0
                    L=[]
                    for i in read:
                        L+=(i,)
                        c+=1
                    reset()
                    label=Label(result_outer_frame,image=sec_trm_banner,bd=0).pack(side=TOP)
                    for i in range(6):
                        sec_view_part_sub_res_frame.columnconfigure(i,weight=1)
                    for i in range(6+c):
                        if i<=1 or i>2+c:
                            sec_view_part_sub_res_frame.rowconfigure(i,weight=1)
                        else:
                            sec_view_part_sub_res_frame.rowconfigure(i,weight=2)
                    selectdb="SELECT * FROM students"
                    cur.execute(selectdb)
                    data=cur.fetchall()
                    for i in data:
                        if i[2]==int(s):
                            name=i[0]
                            dob=i[4]
                            admno=i[3]
                            phone=i[10]

                    name_label=Label(sec_view_part_sub_res_frame,text="Name : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=0,sticky=E)
                    name_a=Label(sec_view_part_sub_res_frame,text=name,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=1,sticky=W)
                    class_label=Label(sec_view_part_sub_res_frame,text="Class : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=2,sticky=E)
                    class_a=Label(sec_view_part_sub_res_frame,text="12 'A'",fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=3,sticky=W)
                    dob_label=Label(sec_view_part_sub_res_frame,text="D.O.B. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=4,sticky=E)
                    dob_label=Label(sec_view_part_sub_res_frame,text=dob,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=0,column=5,sticky=W)
                    roll_label=Label(sec_view_part_sub_res_frame,text="Roll no. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=0,sticky=E)
                    roll_a=Label(sec_view_part_sub_res_frame,text=s,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=1,sticky=W)
                    admno_label=Label(sec_view_part_sub_res_frame,text="Adm no. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=2,sticky=E)
                    admno_a_label=Label(sec_view_part_sub_res_frame,text=admno,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=3,sticky=W)
                    phone_label=Label(sec_view_part_sub_res_frame,text="Phone no. : ",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=4,sticky=E)
                    phone_a=Label(sec_view_part_sub_res_frame,text=phone,fg="white",font=("comic sans ms",15),bg="#3256A8",bd=0).grid(row=1,column=5,sticky=W)

                    sub_label=Label(sec_view_part_sub_res_frame,text="Subject",font=("comic sans ms",25),fg="yellow",bg="#3256A8",bd=0).grid(row=2,column=0,columnspan=2)
                    marks_obt=Label(sec_view_part_sub_res_frame,text="Marks Obtained",font=("comic sans ms",25),fg="yellow",bg="#3256A8",bd=0).grid(row=2,column=2,columnspan=2)
                    fm=Label(sec_view_part_sub_res_frame,text="Maximum Marks",font=("comic sans ms",25),fg="yellow",bg="#3256A8",bd=0).grid(row=2,column=4,columnspan=2)
                    rows=3
                    tobt=0
                    tmax=0
                    for i in L:
                        columns=0
                        tobt+=float(i[1])
                        tmax+=float(i[2])
                        for j in i:
                            lab=Label(sec_view_part_sub_res_frame,text=j,font=("comic sans ms",15),fg="light green",bg="#3256A8",bd=0).grid(row=rows,column=columns,columnspan=2)
                            columns+=2
                        rows+=1
                    marks_label=Label(sec_view_part_sub_res_frame,text="Marks : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=0,sticky=E)
                    marks_a=Label(sec_view_part_sub_res_frame,text=f"{tobt} / {tmax}",fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=1,sticky=W)
                    perc_label=Label(sec_view_part_sub_res_frame,text="Percentage : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=4,sticky=E)
                    ppeer=tobt*100/tmax
                    perc_a=Label(sec_view_part_sub_res_frame,text=str("{:.2f}".format(ppeer))+" %",fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=3+c,column=5,sticky=W)
                    result="Pass"
                    if 91<= float(tobt*100/tmax) <= 100 :
                        grade= "A1 (Outstanding)"
                    elif 81<= float(tobt*100/tmax) < 91 :
                        grade= "A2 (Excellent)"
                    elif 71<= float(tobt*100/tmax) < 81 :
                        grade= "B1 (Very Good)"
                    elif 61<= float(tobt*100/tmax) < 71 :
                        grade= "B1 (Good)"
                    elif 51<= float(tobt*100/tmax) < 61 :
                        grade= "C1 (Above Average)"
                    elif 41<= float(tobt*100/tmax) < 51 :
                        grade= "C1 (Average)"
                    elif 33<= float(tobt*100/tmax) < 41 :
                        grade= "D (Pass)"
                    elif 21<= float(tobt*100/tmax) < 33 :
                        grade= "E1 (Needs Improvement)"
                        result="Fail"
                    elif 0<= float(tobt*100/tmax) < 21 :
                        grade= "E2 (Needs Improvement)"
                        result="Fail"
                    else:
                        grade="Invalid"
                        result="Invalid"
                    grade_label=Label(sec_view_part_sub_res_frame,text="Grade : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=0,sticky=E)
                    grade_a=Label(sec_view_part_sub_res_frame,text=grade,fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=1,sticky=W)
                    result_label=Label(sec_view_part_sub_res_frame,text="Result : ",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=4,sticky=E)
                    result_a=Label(sec_view_part_sub_res_frame,text=result,fg="white",font=("comic sans ms",17),bg="#3256A8",bd=0).grid(row=4+c,column=5,sticky=W)
                    goback_button=Button(sec_view_part_sub_res_frame,image=goback_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_view_sec_result_frame).grid(row=5+c,column=0,columnspan=2)
                    close_button=Button(sec_view_part_sub_res_frame,image=close_photo,activebackground="#3256A8",bg="#3256A8",bd=0,command=show_result_frame).grid(row=5+c,column=4,columnspan=2)

                    sec_view_part_sub_res_frame.pack(expand=True,fill="both")
                    sec_view_part_sub_res_frame.tkraise()
                    result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
                    result_outer_frame.tkraise()
                except:
                    messagebox.showerror("Error","No record found!")
            except:
                messagebox.showerror("Error","Select the student first")
        
        def gob():
            show_view_result_inner_frame()
        label=Label(result_outer_frame,image=sec_trm_banner,bd=0).pack(side=TOP)
        #add_sec_result_frame
        for i in range(2):
            view_sec_result_frame.columnconfigure(i,weight=1)
        for i in range(2):
            view_sec_result_frame.rowconfigure(i,weight=1)

        s="SELECT * FROM students"
        cur.execute(s)
        data=cur.fetchall()
        lfont=Font(family="comic sans ms",size=15)
        l=Listbox(view_sec_result_list_frame,width=25,height=10,selectmode=SINGLE,font=lfont)
        l.pack(side=LEFT,fill=BOTH)
        scrollbar=Scrollbar(view_sec_result_list_frame)
        scrollbar.pack(side=RIGHT,fill=BOTH)
        for i in range(len(data)):
            if len(str(data[i][2]))==1:
                s=str(data[i][2])+str("    ")+str(data[i][0])
            elif len(str(data[i][2]))==2:
                s=str(data[i][2])+str("   ")+str(data[i][0])
            elif len(str(data[i][2]))==3:
                s=str(data[i][2])+str("  ")+str(data[i][0])
            else:
                s=str(data[i][2])+str("    ")+str(data[i][0])
            l.insert(i,s)
        l.config(yscrollcommand=scrollbar.set)
        l.configure(background="black",foreground="white")
        scrollbar.config(command=l.yview)
        view_sec_result_list_frame.grid(row=0,columnspan=5)
        goback_btn=Button(view_sec_result_frame,image=goback_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=gob).grid(row=1,column=0)
        pro_btn=Button(view_sec_result_frame,image=proceed_image,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_sec_view_part_sub_res_frame).grid(row=1,column=1)
        view_sec_result_list_frame.tkraise()
        view_sec_result_frame.pack(expand=True,fill="both")
        view_sec_result_frame.tkraise()
        result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
        result_outer_frame.tkraise()

    label=Label(result_outer_frame,image=results_banner,bd=0).pack(side=TOP)
    result_frame.columnconfigure(0,weight=1)
    for i in range(3):
        result_frame.rowconfigure(i,weight=1)
    add_btn=Button(result_frame,image=add_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_add_result_inner_frame).grid(row=0,column=0)
    view_btn=Button(result_frame,image=view_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_view_result_inner_frame).grid(row=1,column=0)
    close_btn=Button(result_frame,image=close_photo,bd=0,bg="#3256A8",activebackground="#3256A8",command=show_choice_frame).grid(row=2,column=0)
    
    result_frame.pack(expand=True,fill="both")
    result_frame.tkraise()
    result_outer_frame.pack(expand=True,fill="both",side=BOTTOM)
    result_outer_frame.tkraise()







def show_daily_activities_frame():
    reset()
    def show_add_daily_activities_frame():
        reset()
        label=Label(add_daily_activities_outer_frame,image=daily_activities_banner,bd=0).pack(side=TOP)
        for i in range(3):
            add_daily_activities_frame.rowconfigure(i,weight=1)
        for j in range(5):
            add_daily_activities_frame.columnconfigure(j,weight=1)
        myfont=("Comic Sans MS",15)
        dt=DateEntry(add_daily_activities_frame,date_pattern="dd-MM-yyyy",width=28,font=myfont,selectmode="day",justify=CENTER)
        dt.grid(row=0,column=0,columnspan=5)
        lab=Label(add_daily_activities_frame,text="Period",font=myfont,bg="#876ecc",bd=0).grid(row=1,column=0)
        lab=Label(add_daily_activities_frame,text="Subject",font=myfont,bg="#876ecc",bd=0).grid(row=1,column=1)
        lab=Label(add_daily_activities_frame,text="Activity",font=myfont,bg="#876ecc",bd=0).grid(row=1,column=2)
        lab=Label(add_daily_activities_frame,text="Homework",font=myfont,bg="#876ecc",bd=0).grid(row=1,column=3)
        lab=Label(add_daily_activities_frame,text="Teacher Code",font=myfont,bg="#876ecc",bd=0).grid(row=1,column=4)

        per=Entry(add_daily_activities_frame,justify=CENTER,font=myfont)
        per.grid(row=2,column=0)
        sub=Entry(add_daily_activities_frame,justify=CENTER,font=myfont)
        sub.grid(row=2,column=1)
        act=Entry(add_daily_activities_frame,justify=CENTER,font=myfont)
        act.grid(row=2,column=2)
        hw=Entry(add_daily_activities_frame,justify=CENTER,font=myfont)
        hw.grid(row=2,column=3)
        tc=Entry(add_daily_activities_frame,justify=CENTER,font=myfont)
        tc.grid(row=2,column=4)


        def set_act():
            s="SELECT * FROM teachers"
            cur.execute(s)
            data=cur.fetchall()
            gotdb=dt.get_date()
            gotdb1=gotdb.strftime("%d-%m-%Y")
            filenamed="Data\\Daily activities\\" + str(gotdb1) +".csv"
            f=open(filenamed,"a")
            write=csv.writer(f)
            for i in data:
                if i[11]==int(tc.get()):
                    tname=i[0]
                    break
            try:
                listact=[per.get(),sub.get(),act.get(),hw.get(),tname]
                write.writerow(listact)
                f.close()
                messagebox.showinfo("Added","Activity added successfully!")
                show_daily_activities_frame()
            except:
                messagebox.showerror("Error","Something went wrong!")
        
        for i in range(3):
            add_daily_activities_btn_frame.columnconfigure(i,weight=1)
        add_daily_activities_btn_frame.rowconfigure(0,weight=1)
        saveact=Button(add_daily_activities_btn_frame,image=set_btn,bg="#876ecc",bd=0,activebackground="#876ecc",command=set_act).grid(row=0,column=1)
        gobck=Button(add_daily_activities_btn_frame,image=goback_photo,bg="#876ecc",bd=0,activebackground="#876ecc",command=show_daily_activities_frame).grid(row=0,column=0)
        close=Button(add_daily_activities_btn_frame,image=close_photo,bg="#876ecc",bd=0,activebackground="#876ecc",command=show_choice_frame).grid(row=0,column=2)
        
        add_daily_activities_frame.pack(expand=True,fill="both")
        add_daily_activities_frame.tkraise()
        add_daily_activities_btn_frame.pack(expand=True,fill="both",side=BOTTOM,pady=15)
        add_daily_activities_btn_frame.tkraise()
        add_daily_activities_outer_frame.pack(expand=True,fill="both")
        add_daily_activities_outer_frame.tkraise()

    def show_view_daily_activities_frame():
        reset()
        label=Label(view_daily_activities_outer_frame,image=daily_activities_banner,bd=0).pack(side=TOP)
        for i in range(2):
            view_daily_activities_frame.rowconfigure(i,weight=1)
        view_daily_activities_frame.columnconfigure(0,weight=1)
        myfont=("Comic Sans MS",15)
        dt=DateEntry(view_daily_activities_frame,date_pattern="dd-MM-yyyy",width=28,font=myfont,selectmode="day",justify=CENTER)
        dt.grid(row=0,column=0)
        btn=Button(view_daily_activities_frame,bd=0,bg="#876ecc",activebackground="#876ecc",image=view_photo,command=lambda:show_this_activity_frame(dt.get_date()))
        btn.grid(row=1,column=0)
        for i in range(2):
            view_daily_activities_btn_frame.columnconfigure(i,weight=1)
        view_daily_activities_btn_frame.rowconfigure(0,weight=1)
        
        gobck=Button(view_daily_activities_btn_frame,image=goback_photo,bg="#876ecc",bd=0,activebackground="#876ecc",command=show_daily_activities_frame).grid(row=0,column=0)
        close=Button(view_daily_activities_btn_frame,image=close_photo,bg="#876ecc",bd=0,activebackground="#876ecc",command=show_choice_frame).grid(row=0,column=1)
        
        view_daily_activities_frame.pack(expand=True,fill="both")
        view_daily_activities_frame.tkraise()
        view_daily_activities_btn_frame.pack(expand=True,fill="both",side=BOTTOM,pady=15)
        view_daily_activities_btn_frame.tkraise()
        view_daily_activities_outer_frame.pack(expand=True,fill="both")
        view_daily_activities_outer_frame.tkraise()
    
    def show_this_activity_frame(dt):
        try:
            gotdb1=dt.strftime("%d-%m-%Y")
            filenamed="Data\\Daily activities\\" + str(gotdb1) +".csv"
            f=open(filenamed,"r")
            reset()
            myfont=("Comic Sans MS",20)
            label=Label(view_this_daily_activities_outer_frame,image=daily_activities_banner,bd=0).pack(side=TOP)
            for i in range(5):
                view_this_daily_activities_frame.columnconfigure(i,weight=1)
            for i in range(9):
                view_this_daily_activities_frame.rowconfigure(i,weight=1)
            lab=Label(view_this_daily_activities_frame,text="Period",font=myfont,bg="#876ecc",bd=0).grid(row=0,column=0)
            lab=Label(view_this_daily_activities_frame,text="Subject",font=myfont,bg="#876ecc",bd=0).grid(row=0,column=1)
            lab=Label(view_this_daily_activities_frame,text="Activity",font=myfont,bg="#876ecc",bd=0).grid(row=0,column=2)
            lab=Label(view_this_daily_activities_frame,text="Homework",font=myfont,bg="#876ecc",bd=0).grid(row=0,column=3)
            lab=Label(view_this_daily_activities_frame,text="Teacher",font=myfont,bg="#876ecc",bd=0).grid(row=0,column=4)
            filenamed="Data\\Daily activities\\" + str(gotdb1) +".csv"
            f=open(filenamed,"r")
            read=csv.reader(f)
            L=[]
            m=0
            for i in read:
                if m%2==0:
                    L.append(i)
                m+=1
            f.close()
            r=0
            myfont=("Comic Sans MS",15)
            for i in L:
                c=0
                r+=1
                for j in i:
                    lab=Label(view_this_daily_activities_frame,text=j,fg="white",bg="#876ecc",font=myfont,bd=0)
                    lab.grid(row=r,column=c)
                    c+=1
            for i in range(2):
                view_this_daily_activities_btn_frame.columnconfigure(i,weight=1)
            view_this_daily_activities_btn_frame.rowconfigure(0,weight=1)
            gobck=Button(view_this_daily_activities_btn_frame,image=goback_photo,bg="#876ecc",bd=0,activebackground="#876ecc",command=show_view_daily_activities_frame).grid(row=0,column=0)
            close=Button(view_this_daily_activities_btn_frame,image=close_photo,bg="#876ecc",bd=0,activebackground="#876ecc",command=show_choice_frame).grid(row=0,column=1)
            view_this_daily_activities_frame.pack(expand=True,fill="both")
            view_this_daily_activities_frame.tkraise()
            view_this_daily_activities_btn_frame.pack(expand=True,fill="both",side=BOTTOM,pady=15)
            view_this_daily_activities_btn_frame.tkraise()
            view_this_daily_activities_outer_frame.pack(expand=True,fill="both")
            view_this_daily_activities_outer_frame.tkraise()
        except:
            messagebox.showerror("Error","No activity found for this date!")
        


        

    label=Label(daily_activities_outer_frame,image=daily_activities_banner,bd=0).pack(side=TOP)
    for i in range(3):
        daily_activities_frame.rowconfigure(i,weight=1)
    daily_activities_frame.columnconfigure(0,weight=1)
    view=Button(daily_activities_frame,bg="#876ecc",bd=0,image=view_photo,activebackground="#876ecc",command=show_view_daily_activities_frame).grid(row=0,column=0)
    add=Button(daily_activities_frame,bg="#876ecc",bd=0,image=add_photo,activebackground="#876ecc",command=show_add_daily_activities_frame).grid(row=1,column=0)
    close=Button(daily_activities_frame,bg="#876ecc",bd=0,image=close_photo,activebackground="#876ecc",command=show_choice_frame).grid(row=2,column=0)
    
    daily_activities_frame.pack(expand=True,fill="both")
    daily_activities_frame.tkraise()
    daily_activities_outer_frame.pack(expand=True,fill="both")
    daily_activities_outer_frame.tkraise()





def show_routine_frame():
    reset()
    #label=Label(routine_outer_frame,image=routine_banner,bd=0).pack(side=TOP)
    def show_write_routine_frame():
                rfont=("comic sans ms",20)
                reset()
                label=Label(routine_outer_frame,image=routine_banner,bd=0).pack(side=TOP)
                for row in range(0,8):
                    write_routine_frame.rowconfigure(row,weight=1)
                for col in range(0,9):
                    write_routine_frame.columnconfigure(col,weight=1)
                emp_label=Label(write_routine_frame,text="",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=0)
                emp_label=Label(write_routine_frame,text="Mon",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=1,column=0)
                emp_label=Label(write_routine_frame,text="Tue",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=2,column=0)
                emp_label=Label(write_routine_frame,text="Wed",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=3,column=0)
                emp_label=Label(write_routine_frame,text="Thu",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=4,column=0)
                emp_label=Label(write_routine_frame,text="Fri",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=5,column=0)
                emp_label=Label(write_routine_frame,text="Sat",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=6,column=0)

                emp_label=Label(write_routine_frame,text="1",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=1)
                emp_label=Label(write_routine_frame,text="2",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=2)
                emp_label=Label(write_routine_frame,text="3",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=3)
                emp_label=Label(write_routine_frame,text="4",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=4)
                emp_label=Label(write_routine_frame,text="5",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=5)
                emp_label=Label(write_routine_frame,text="6",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=6)
                emp_label=Label(write_routine_frame,text="7",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=7)
                emp_label=Label(write_routine_frame,text="8",font=rfont,bg="#52c798",bd=0)
                emp_label.grid(row=0,column=8)



                rfont=("comic sans ms",15)

                m1=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m1.grid(row=1,column=1)
                m2=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m2.grid(row=1,column=2)
                m3=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m3.grid(row=1,column=3)
                m4=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m4.grid(row=1,column=4)
                m5=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m5.grid(row=1,column=5)
                m6=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m6.grid(row=1,column=6)
                m7=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m7.grid(row=1,column=7)
                m8=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                m8.grid(row=1,column=8)

                t1=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t1.grid(row=2,column=1)
                t2=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t2.grid(row=2,column=2)
                t3=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t3.grid(row=2,column=3)
                t4=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t4.grid(row=2,column=4)
                t5=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t5.grid(row=2,column=5)
                t6=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t6.grid(row=2,column=6)
                t7=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t7.grid(row=2,column=7)
                t8=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                t8.grid(row=2,column=8)

                w1=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w1.grid(row=3,column=1)
                w2=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w2.grid(row=3,column=2)
                w3=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w3.grid(row=3,column=3)
                w4=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w4.grid(row=3,column=4)
                w5=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w5.grid(row=3,column=5)
                w6=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w6.grid(row=3,column=6)
                w7=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w7.grid(row=3,column=7)
                w8=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                w8.grid(row=3,column=8)

                th1=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th1.grid(row=4,column=1)
                th2=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th2.grid(row=4,column=2)
                th3=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th3.grid(row=4,column=3)
                th4=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th4.grid(row=4,column=4)
                th5=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th5.grid(row=4,column=5)
                th6=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th6.grid(row=4,column=6)
                th7=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th7.grid(row=4,column=7)
                th8=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                th8.grid(row=4,column=8)

                f1=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f1.grid(row=5,column=1)
                f2=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f2.grid(row=5,column=2)
                f3=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f3.grid(row=5,column=3)
                f4=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f4.grid(row=5,column=4)
                f5=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f5.grid(row=5,column=5)
                f6=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f6.grid(row=5,column=6)
                f7=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f7.grid(row=5,column=7)
                f8=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                f8.grid(row=5,column=8)

                s1=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s1.grid(row=6,column=1)
                s2=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s2.grid(row=6,column=2)
                s3=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s3.grid(row=6,column=3)
                s4=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s4.grid(row=6,column=4)
                s5=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s5.grid(row=6,column=5)
                s6=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s6.grid(row=6,column=6)
                s7=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s7.grid(row=6,column=7)
                s8=Entry(write_routine_frame,justify=CENTER,font=rfont,width=10)
                s8.grid(row=6,column=8)
                def set_routine():
                    f=open("Data\\Routine\\routine.csv","w")
                    write=csv.writer(f)
                    mon=[m1.get(),m2.get(),m3.get(),m4.get(),m5.get(),m6.get(),m7.get(),m8.get()]
                    write.writerow(mon)
                    tue=[t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t7.get(),t8.get()]
                    write.writerow(tue)
                    wed=[w1.get(),w2.get(),w3.get(),w4.get(),w5.get(),w6.get(),w7.get(),w8.get()]
                    write.writerow(wed)
                    thu=[th1.get(),th2.get(),th3.get(),th4.get(),th5.get(),th6.get(),th7.get(),th8.get()]
                    write.writerow(thu)
                    fri=[f1.get(),f2.get(),f3.get(),f4.get(),f5.get(),f6.get(),f7.get(),f8.get()]
                    write.writerow(fri)
                    sat=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get(),s7.get(),s8.get()]
                    write.writerow(sat)
                    f.flush()
                    f.close()
                    messagebox.showinfo("Success","New Routine is set!")


                set_r_btn=Button(write_routine_frame,image=set_btn,bd=0,bg="#52c798",activebackground="#52c798",command=set_routine)
                set_r_btn.grid(row=7,column=5,columnspan=4)
                close_btn=Button(write_routine_frame,image=close_photo,bg="#52c798",bd=0,activebackground="#52c798",command=show_routine_frame)
                close_btn.grid(row=7,column=0,columnspan=4)



                write_routine_frame.pack(expand=True,fill="both")
                write_routine_frame.tkraise()
                routine_outer_frame.pack(expand=True,fill="both")
                routine_outer_frame.tkraise()
    def show_read_routine_frame():
            rfont=("comic sans ms",20)
            reset()
            label=Label(routine_outer_frame,image=routine_banner,bd=0).pack(side=TOP)
            for row in range(0,8):
                read_routine_frame.rowconfigure(row,weight=1)
            for col in range(0,9):
                read_routine_frame.columnconfigure(col,weight=1)
            emp_label=Label(read_routine_frame,text="",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=0)
            emp_label=Label(read_routine_frame,text="Mon",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=1,column=0)
            emp_label=Label(read_routine_frame,text="Tue",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=2,column=0)
            emp_label=Label(read_routine_frame,text="Wed",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=3,column=0)
            emp_label=Label(read_routine_frame,text="Thu",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=4,column=0)
            emp_label=Label(read_routine_frame,text="Fri",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=5,column=0)
            emp_label=Label(read_routine_frame,text="Sat",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=6,column=0)

            emp_label=Label(read_routine_frame,text="1",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=1)
            emp_label=Label(read_routine_frame,text="2",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=2)
            emp_label=Label(read_routine_frame,text="3",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=3)
            emp_label=Label(read_routine_frame,text="4",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=4)
            emp_label=Label(read_routine_frame,text="5",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=5)
            emp_label=Label(read_routine_frame,text="6",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=6)
            emp_label=Label(read_routine_frame,text="7",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=7)
            emp_label=Label(read_routine_frame,text="8",font=rfont,bg="#52c798",bd=0)
            emp_label.grid(row=0,column=8)

            rfont=("comic sans ms",15)
            read=csv.reader(f)
            subs=[]
            for j in read:
                subs.append(j)
            [mon,yuk,tue,yuk,wed,yuk,thu,yuk,fri,yuk,sat,yuk]=subs
            def sub(day,rw):
                for i in range(0,8):
                    label=Label(read_routine_frame,text=day[i],fg="#404040",font=rfont,bg="#52c798",bd=0).grid(row=rw,column=i+1)
            col=1
            for i in range(0,12,2):
                sub(subs[i],col)
                col+=1

            f.close()
            set_r_btn=Button(read_routine_frame,image=set_routine_btn_photo,bd=0,bg="#52c798",activebackground="#52c798",command=show_write_routine_frame)
            set_r_btn.grid(row=7,column=5,columnspan=4)
            close_btn=Button(read_routine_frame,image=close_photo,bg="#52c798",bd=0,activebackground="#52c798",command=show_choice_frame)
            close_btn.grid(row=7,column=0,columnspan=4)
            read_routine_frame.pack(expand=True,fill="both")
            read_routine_frame.tkraise()
            routine_outer_frame.pack(expand=True,fill="both")
            routine_outer_frame.tkraise()


    def show_empty_routine_frame():
            reset()
            label=Label(routine_outer_frame,image=routine_banner,bd=0).pack(side=TOP)
            set_r_btn=Button(empty_routine_frame,image=set_routine_btn_photo,bd=0,bg="#52c798",activebackground="#52c798",command=show_write_routine_frame).place(relx=0.5,rely=0.4,anchor=CENTER)
            close_btn=Button(empty_routine_frame,image=close_photo,bd=0,bg="#52c798",activebackground="#52c798",command=show_choice_frame).place(relx=0.5,rely=0.6,anchor=CENTER)
            empty_routine_frame.pack(expand=True,fill="both")
            empty_routine_frame.tkraise()
            routine_outer_frame.pack(expand=True,fill="both")
            routine_outer_frame.tkraise()
    
    try:
        f=open("Data\\Routine\\routine.csv","r")
        show_read_routine_frame()
    except FileNotFoundError:
        show_empty_routine_frame()
    routine_outer_frame.pack(expand=True,fill="both")
    routine_outer_frame.tkraise()
        
def logout():
        ansr=messagebox.askquestion("Log Out","Do you really want to Log Out?")
        if(ansr=="yes"):
            show_login_frame()



def show_view_teachers_frame():
    reset()
    label=Label(view_teachers_outer_frame,image=teachers_banner,bd=0).pack(side=TOP,pady=5)
    s="SELECT * FROM teachers"
    cur.execute(s)
    data=cur.fetchall()
    lfont=Font(family="comic sans ms",size=15)
    for i in range(2):
        view_teachers_frame.rowconfigure(i,weight=1)
    for i in range(5):
        view_teachers_frame.columnconfigure(i,weight=1)
    l=Listbox(view_teachers_list_frame,width=30,height=15,selectmode=SINGLE,font=lfont)
    l.pack(side=LEFT,fill=BOTH)
    scrollbar=Scrollbar(view_teachers_list_frame)
    scrollbar.pack(side=RIGHT,fill=BOTH)
    for i in range(len(data)):
        s=str(data[i][11])+str("   ")+str(data[i][0])
        l.insert(i,s)
    l.config(yscrollcommand=scrollbar.set)
    l.configure(background="black",foreground="white")
    scrollbar.config(command=l.yview)
    view_teachers_list_frame.grid(row=0,columnspan=5)

    def show_edit_this_teacher_frame(st):
        reset()
        label=Label(edit_teachers_outer_frame,image=edit_teachers_banner,bd=0).pack(side=TOP,pady=20)
        edit_teachers_outer_frame.pack(fill="both")
        #configuring rows and columns
        for i in range(0,4):
            edit_this_teacher_frame.columnconfigure(i,weight=1)
        for i in range(0,10):
            edit_this_teacher_frame.rowconfigure(i,weight=1)
        edit_this_teacher_frame.rowconfigure(10,weight=2)
        #main
        myfont=("Comic Sans MS",15)
        fullname=Label(edit_this_teacher_frame,text="Full Name*",bd=0,bg="#5e223b",fg="white",font=myfont)
        fullname.grid(row=0,column=0,sticky=E)
        s=StringVar()
        fullname_entry=Entry(edit_this_teacher_frame,textvariable=s,font=myfont,justify=CENTER)
        s.set(str(st[0][0]))
        fullname_entry.grid(row=0,column=1,padx=20,sticky=W)
        gender=Label(edit_this_teacher_frame,text="Gender",bd=0,bg="#5e223b",fg="white",font=myfont)
        gender.grid(row=1,column=0,sticky=E)
        gender_combo=Combobox(edit_this_teacher_frame,state="readonly",values=["Male","Female","Other"],width=19,justify=CENTER,font=myfont)
        gender_combo.set(str(st[0][1]))
        gender_combo.grid(row=1,column=1,padx=20,sticky=W)
        
        
        dob=Label(edit_this_teacher_frame,text="Date of birth",bd=0,bg="#5e223b",fg="white",font=myfont)
        dob.grid(row=2,column=0,sticky=E)
        s=StringVar()
        # dob_entry=Entry(edit_this_teacher_frame,textvariable=s,font=myfont,justify=CENTER)
        # s.set(str(st[0][2]))
        # dob_entry.grid(row=2,column=1,padx=20,sticky=W)
        dob_entry=DateEntry(edit_this_teacher_frame,date_pattern="dd-MM-yyyy",width=19,font=myfont,selectmode="day",year=int(st[0][2][6:10]),month=int(st[0][2][3:5]),day=int(st[0][2][0:2]),justify=CENTER)
        dob_entry.grid(row=2,column=1,padx=20,sticky=W)
        
        blood=Label(edit_this_teacher_frame,text="Blood Group",bd=0,bg="#5e223b",fg="white",font=myfont)
        blood.grid(row=3,column=0,sticky=E)
        blood_combo=Combobox(edit_this_teacher_frame,state="readonly",values=["A+","A-","B+","B-","O+","O-","AB+","AB-"],width=19,justify=CENTER,font=myfont)
        blood_combo.set(str(st[0][3]))
        blood_combo.grid(row=3,column=1,padx=20,sticky=W)

        email=Label(edit_this_teacher_frame,text="Email Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        email.grid(row=4,column=0,sticky=E)
        s=StringVar()
        email_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][4]))
        email_entry.grid(row=4,column=1,padx=20,sticky=W)

        phone=Label(edit_this_teacher_frame,text="Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        phone.grid(row=0,column=2,sticky=E)
        s=StringVar()
        phone_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][5]))
        phone_entry.grid(row=0,column=3,padx=20,sticky=W)

        qualifications=Label(edit_this_teacher_frame,text="Qualifications",bd=0,bg="#5e223b",fg="white",font=myfont)
        qualifications.grid(row=1,column=2,sticky=E)
        t=StringVar()
        qualifications_entry=Entry(edit_this_teacher_frame,textvariable=t,justify=CENTER,font=myfont)
        t.set(str(st[0][6]))
        qualifications_entry.grid(row=1,column=3,padx=20,sticky=W)

        whatsappno=Label(edit_this_teacher_frame,text="Whatsapp no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        whatsappno.grid(row=2,column=2,sticky=E)
        s=StringVar()
        whatsappno_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][7]))
        whatsappno_entry.grid(row=2,column=3,padx=20,sticky=W)

        address=Label(edit_this_teacher_frame,text="Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        address.grid(row=3,column=2,sticky=E)
        s=StringVar()
        address_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][8]))
        address_entry.grid(row=3,column=3,padx=20,sticky=W)

        pincode=Label(edit_this_teacher_frame,text="Pin Code",bd=0,bg="#5e223b",fg="white",font=myfont)
        pincode.grid(row=4,column=2,sticky=E)
        s=StringVar()
        pincode_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][9]))
        pincode_entry.grid(row=4,column=3,padx=20,sticky=W)

        subject=Label(edit_this_teacher_frame,text="Subject",bd=0,bg="#5e223b",fg="white",font=myfont)
        subject.grid(row=5,column=0,sticky=E)
        s=StringVar()
        subject_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][10]))
        subject_entry.grid(row=5,column=1,padx=20,sticky=W)

        teacher_code=Label(edit_this_teacher_frame,text="Teacher code*",bd=0,bg="#5e223b",fg="white",font=myfont)
        teacher_code.grid(row=5,column=2,sticky=E)
        s=StringVar()
        teacher_code_entry=Entry(edit_this_teacher_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][11]))
        global xr
        xr=st[0][11]
        teacher_code_entry.grid(row=5,column=3,padx=20,sticky=W)

        def update_teacher():
            try:
                gotdb=dob_entry.get_date()
                gotdb1=gotdb.strftime("%d-%m-%Y")
                s="update teachers set fullname = %s,gender=%s ,dob=%s,blood=%s,email=%s,phone=%s,qualifications=%s,whatsappno=%s,address=%s,pincode=%s,subject=%s,teacher_code=%s where teacher_code=%s"
                b=(fullname_entry.get(),gender_combo.get(),gotdb1,blood_combo.get(),email_entry.get(),phone_entry.get(),qualifications_entry.get(),whatsappno_entry.get(),address_entry.get(),pincode_entry.get(),subject_entry.get(),int(teacher_code_entry.get()),xr)
                cur.execute(s,b)
                mydb.commit()
                messagebox.showinfo("Success","Details Updated!")
                s=f"SELECT * FROM teachers WHERE teacher_code={int(teacher_code_entry.get())}"
                cur.execute(s)
                st=cur.fetchall()
                show_view_teachers_frame()
            except:
                messagebox.showerror("Error","Something went wrong!")


        
        goback_btn=Button(edit_this_teacher_frame,image=goback_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_view_teachers_frame)
        goback_btn.grid(row=10,column=0,sticky=E)
        set_bttn=Button(edit_this_teacher_frame,image=set_btn,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=update_teacher)
        set_bttn.grid(row=10,column=1,columnspan=2)
        close_btn=Button(edit_this_teacher_frame,image=close_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_choice_frame)
        close_btn.grid(row=10,column=3,sticky=W)
        edit_this_teacher_frame.pack(expand=True,fill="both")
        edit_this_teacher_frame.tkraise()
        
        edit_teachers_outer_frame.tkraise()


    def select_remove():
        clicked_item=l.curselection()
        try:
            sel=data[clicked_item[0]][11]
            s=f"DELETE FROM teachers WHERE teacher_code={sel}"
            cur.execute(s)
            mydb.commit()
            show_view_teachers_frame()
        except:
            messagebox.showwarning("Warning","Select the teacher first!")
    
    
    
    def select_edit():
        clicked_item=l.curselection()
        try:
            sel=data[clicked_item[0]][11]
            s=f"SELECT * FROM teachers WHERE teacher_code={sel}"
            cur.execute(s)
            st=cur.fetchall()
            show_edit_this_teacher_frame(st)
        except:
            messagebox.showwarning("Warning","Select the teacher first!")

    
    
    
    
    
    def show_view_this_teacher_frame(st):
        reset()
        label=Label(view_teachers_outer_frame,image=view_teachers_banner,bd=0).pack(side=TOP,pady=5)
        view_teachers_outer_frame.pack(fill="both")
        #configuring rows and columns
        for i in range(0,4):
            view_this_teacher_frame.columnconfigure(i,weight=1)
        for i in range(0,10):
            view_this_teacher_frame.rowconfigure(i,weight=1)
        view_this_teacher_frame.rowconfigure(10,weight=2)
        #main
        myfont=("Comic Sans MS",15)
        fullname=Label(view_this_teacher_frame,text="Full Name",bd=0,bg="#5e223b",fg="white",font=myfont)
        fullname.grid(row=0,column=0,sticky=E)
        fullname_entry=Label(view_this_teacher_frame,text=str(st[0][0]),bd=0,bg="#5e223b",fg="white",font=myfont)
        fullname_entry.grid(row=0,column=1,padx=20,sticky=W)
        gender=Label(view_this_teacher_frame,text="Gender",bd=0,bg="#5e223b",fg="white",font=myfont)
        gender.grid(row=1,column=0,sticky=E)
        gender_entry=Label(view_this_teacher_frame,text=str(st[0][1]),bd=0,bg="#5e223b",fg="white",font=myfont)
        gender_entry.grid(row=1,column=1,padx=20,sticky=W)
        dob=Label(view_this_teacher_frame,text="Date of birth",bd=0,bg="#5e223b",fg="white",font=myfont)
        dob.grid(row=2,column=0,sticky=E)
        dob_entry=Label(view_this_teacher_frame,text=str(st[0][2]),bd=0,bg="#5e223b",fg="white",font=myfont)
        dob_entry.grid(row=2,column=1,padx=20,sticky=W)

        blood=Label(view_this_teacher_frame,text="Blood Group",bd=0,bg="#5e223b",fg="white",font=myfont)
        blood.grid(row=3,column=0,sticky=E)
        blood_combo=Label(view_this_teacher_frame,text=str(st[0][3]),bd=0,bg="#5e223b",fg="white",font=myfont)
        blood_combo.grid(row=3,column=1,padx=20,sticky=W)

        email=Label(view_this_teacher_frame,text="Email Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        email.grid(row=4,column=0,sticky=E)
        email_entry=Label(view_this_teacher_frame,text=str(st[0][4]),bd=0,bg="#5e223b",fg="white",font=myfont)
        email_entry.grid(row=4,column=1,padx=20,sticky=W)

        phone=Label(view_this_teacher_frame,text="Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        phone.grid(row=0,column=2,sticky=E)
        phone_entry=Label(view_this_teacher_frame,text=str(st[0][5]),bd=0,bg="#5e223b",fg="white",font=myfont)
        phone_entry.grid(row=0,column=3,padx=20,sticky=W)

        qualifications=Label(view_this_teacher_frame,text="Qualifications",bd=0,bg="#5e223b",fg="white",font=myfont)
        qualifications.grid(row=1,column=2,sticky=E)
        qualifications_entry=Label(view_this_teacher_frame,text=str(st[0][6]),bd=0,bg="#5e223b",fg="white",font=myfont)
        qualifications_entry.grid(row=1,column=3,padx=20,sticky=W)

        whatsappno=Label(view_this_teacher_frame,text="Whatsapp no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        whatsappno.grid(row=2,column=2,sticky=E)
        whatsappno_entry=Label(view_this_teacher_frame,text=str(st[0][7]),bd=0,bg="#5e223b",fg="white",font=myfont)
        whatsappno_entry.grid(row=2,column=3,padx=20,sticky=W)

        address=Label(view_this_teacher_frame,text="Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        address.grid(row=3,column=2,sticky=E)
        address_entry=Label(view_this_teacher_frame,text=str(st[0][8]),bd=0,bg="#5e223b",fg="white",font=myfont)
        address_entry.grid(row=3,column=3,padx=20,sticky=W)

        pincode=Label(view_this_teacher_frame,text="Pin Code",bd=0,bg="#5e223b",fg="white",font=myfont)
        pincode.grid(row=4,column=2,sticky=E)
        pincode_entry=Label(view_this_teacher_frame,text=str(st[0][9]),bd=0,bg="#5e223b",fg="white",font=myfont)
        pincode_entry.grid(row=4,column=3,padx=20,sticky=W)

        subject=Label(view_this_teacher_frame,text="Subject",bd=0,bg="#5e223b",fg="white",font=myfont)
        subject.grid(row=5,column=0,sticky=E)
        subject_entry=Label(view_this_teacher_frame,text=str(st[0][10]),bd=0,bg="#5e223b",fg="white",font=myfont)
        subject_entry.grid(row=5,column=1,padx=20,sticky=W)

        teacher_code=Label(view_this_teacher_frame,text="Teacher code",bd=0,bg="#5e223b",fg="white",font=myfont)
        teacher_code.grid(row=5,column=2,sticky=E)
        teacher_code_entry=Label(view_this_teacher_frame,text=str(st[0][11]),bd=0,bg="#5e223b",fg="white",font=myfont)
        teacher_code_entry.grid(row=5,column=3,padx=20,sticky=W)

        
        goback_btn=Button(view_this_teacher_frame,image=goback_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_view_teachers_frame)
        goback_btn.grid(row=10,column=0,columnspan=2)
        close_btn=Button(view_this_teacher_frame,image=close_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_choice_frame)
        close_btn.grid(row=10,column=2,columnspan=2)
        view_this_teacher_frame.pack(expand=True,fill="both")
        view_this_teacher_frame.tkraise()
        
        view_teachers_outer_frame.tkraise()


    def select_view():
        clicked_item=l.curselection()
        try:
            sel=data[clicked_item[0]][11]
            s=f"SELECT * FROM teachers WHERE teacher_code={sel}"
            cur.execute(s)
            st=cur.fetchall()
            show_view_this_teacher_frame(st)
        except:
            messagebox.showwarning("Warning","Select the teacher first!")
    add_details_btn=Button(view_teachers_frame,image=add_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=show_addteachers_frame).grid(row=1,column=0)
    view_details_btn=Button(view_teachers_frame,image=view_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=select_view).grid(row=1,column=1)
    edit_details_btn=Button(view_teachers_frame,image=edit_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=select_edit).grid(row=1,column=2)
    remove_details_btn=Button(view_teachers_frame,image=remove_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=select_remove).grid(row=1,column=3)
    close_btn=Button(view_teachers_frame,image=close_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=show_choice_frame).grid(row=1,column=4)
    view_teachers_frame.pack(expand=True,fill="both")
    view_teachers_frame.tkraise()
    view_teachers_outer_frame.pack(expand=True,fill="both")
    view_teachers_outer_frame.tkraise()


def show_addteachers_frame():

    reset()


    #banner
    label=Label(add_teachers_outer_frame,image=add_teachers_banner,bd=0).pack(side=TOP,pady=15)
    
    #configuring rows and columns

    for i in range(0,4):
        add_teachers_frame.columnconfigure(i,weight=1)
    for i in range(0,6):
        add_teachers_frame.rowconfigure(i,weight=1)

    myfont=("Comic Sans MS",15)
    
    fullname=Label(add_teachers_frame,text="Full Name*",bd=0,bg="#5e223b",fg="white",font=myfont)
    fullname.grid(row=0,column=0,sticky=E)
    fullname_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    fullname_entry.grid(row=0,column=1,padx=20,sticky=W)

    gender=Label(add_teachers_frame,text="Gender",bd=0,bg="#5e223b",fg="white",font=myfont)
    gender.grid(row=1,column=0,sticky=E)
    gender_combo=Combobox(add_teachers_frame,state="readonly",values=["Male","Female","Other"],font=myfont,justify=CENTER,width=28)
    #gender_combo.set("Gender")
    gender_combo.grid(row=1,column=1,padx=20,sticky=W)

    dob=Label(add_teachers_frame,text="Date of birth",bd=0,bg="#5e223b",fg="white",font=myfont)
    dob.grid(row=2,column=0,sticky=E)
    # dob_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    # dob_entry.grid(row=2,column=1,padx=20,sticky=W)
    dob_entry=DateEntry(add_teachers_frame,date_pattern="dd-MM-yyyy",width=28,font=myfont,selectmode="day",year=2000,month=1,day=1,justify=CENTER)
    dob_entry.grid(row=2,column=1,padx=20,sticky=W)



    blood=Label(add_teachers_frame,text="Blood Group",bd=0,bg="#5e223b",fg="white",font=myfont)
    blood.grid(row=3,column=0,sticky=E)
    blood_combo=Combobox(add_teachers_frame,state="readonly",values=["A+","A-","B+","B-","O+","O-","AB+","AB-"],font=myfont,justify=CENTER,width=28)
    blood_combo.set("")
    blood_combo.grid(row=3,column=1,padx=20,sticky=W)

    email=Label(add_teachers_frame,text="Email Address",bd=0,bg="#5e223b",fg="white",font=myfont)
    email.grid(row=4,column=0,sticky=E)
    email_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    email_entry.grid(row=4,column=1,padx=20,sticky=W)

    phone=Label(add_teachers_frame,text="Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
    phone.grid(row=0,column=2,sticky=E)
    phone_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    phone_entry.grid(row=0,column=3,padx=20,sticky=W)

    qualifications=Label(add_teachers_frame,text="Qualifications",bd=0,bg="#5e223b",fg="white",font=myfont)
    qualifications.grid(row=1,column=2,sticky=E)
    qualifications_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    qualifications_entry.grid(row=1,column=3,padx=20,sticky=W)

    whatsappno=Label(add_teachers_frame,text="Whatsapp no.",bd=0,bg="#5e223b",fg="white",font=myfont)
    whatsappno.grid(row=2,column=2,sticky=E)
    whatsappno_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    whatsappno_entry.grid(row=2,column=3,padx=20,sticky=W)

    address=Label(add_teachers_frame,text="Address",bd=0,bg="#5e223b",fg="white",font=myfont)
    address.grid(row=3,column=2,sticky=E)
    address_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    address_entry.grid(row=3,column=3,padx=20,sticky=W)

    pincode=Label(add_teachers_frame,text="Pin Code",bd=0,bg="#5e223b",fg="white",font=myfont)
    pincode.grid(row=4,column=2,sticky=E)
    pincode_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    pincode_entry.grid(row=4,column=3,padx=20,sticky=W)

    subject=Label(add_teachers_frame,text="Subject",bd=0,bg="#5e223b",fg="white",font=myfont)
    subject.grid(row=5,column=0,sticky=E)
    subject_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    subject_entry.grid(row=5,column=1,padx=20,sticky=W)

    teacher_code=Label(add_teachers_frame,text="Teacher code*",bd=0,bg="#5e223b",fg="white",font=myfont)
    teacher_code.grid(row=5,column=2,sticky=E)
    teacher_code_entry=Entry(add_teachers_frame,width=30,font=myfont,justify=CENTER)
    teacher_code_entry.grid(row=5,column=3,padx=20,sticky=W)

    def ins_teachers():
        try:
            gotdb=dob_entry.get_date()
            gotdb1=gotdb.strftime("%d-%m-%Y")
            s="INSERT INTO teachers VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            b=(fullname_entry.get(),gender_combo.get(),gotdb1,blood_combo.get(),email_entry.get(),phone_entry.get(),qualifications_entry.get(),whatsappno_entry.get(),address_entry.get(),pincode_entry.get(),subject_entry.get(),teacher_code_entry.get())
            cur.execute(s,b)
            mydb.commit()
            messagebox.showinfo("Added","Teacher added!")
            show_addteachers_frame()
        except:
            messagebox.showerror("Error","Something went wrong!")

    #configuring columns

    for i in range(0,3):
        add_teachers_btn_frame.columnconfigure(i,weight=1)
    add_teachers_btn_frame.rowconfigure(0,weight=1)

        
    #adding buttons
    
    add_button=Button(add_teachers_btn_frame,image=add_photo,bd=0,activebackground="#5e223b",bg="#5e223b",command=ins_teachers).grid(row=0,column=1)
    back_button=Button(add_teachers_btn_frame,image=goback_photo,bd=0,activebackground="#5e223b",bg="#5e223b",command=show_view_teachers_frame).grid(row=0,column=0)
    close_button=Button(add_teachers_btn_frame,image=close_photo,bd=0,activebackground="#5e223b",bg="#5e223b",command=show_choice_frame).grid(row=0,column=2)
    
    add_teachers_frame.pack(expand=True,fill="both")
    add_teachers_btn_frame.pack(expand=True,fill="both")
    add_teachers_frame.tkraise()
    add_teachers_btn_frame.tkraise()
    add_teachers_outer_frame.pack(expand=True,fill="both")
    add_teachers_outer_frame.tkraise()


def show_view_students_frame():
    reset()
    label=Label(view_students_outer_frame,image=students_banner,bd=0).pack(side=TOP,pady=5)
    s="SELECT * FROM students"
    cur.execute(s)
    data=cur.fetchall()
    lfont=Font(family="comic sans ms",size=15)
    for i in range(2):
        view_students_frame.rowconfigure(i,weight=1)
    for i in range(5):
        view_students_frame.columnconfigure(i,weight=1)
    l=Listbox(view_students_list_frame,width=30,height=15,selectmode=SINGLE,font=lfont)
    l.pack(side=LEFT,fill=BOTH)
    scrollbar=Scrollbar(view_students_list_frame)
    scrollbar.pack(side=RIGHT,fill=BOTH)
    for i in range(len(data)):
        if len(str(data[i][2]))==1:
            s=str(data[i][2])+str("    ")+str(data[i][0])
        elif len(str(data[i][2]))==2:
            s=str(data[i][2])+str("   ")+str(data[i][0])
        elif len(str(data[i][2]))==3:
            s=str(data[i][2])+str("  ")+str(data[i][0])
        else:
            s=str(data[i][2])+str("    ")+str(data[i][0])
        l.insert(i,s)
    l.config(yscrollcommand=scrollbar.set)
    l.configure(background="black",foreground="white")
    scrollbar.config(command=l.yview)
    view_students_list_frame.grid(row=0,columnspan=5)
    
    def show_edit_this_student_frame(st):
        reset()
        label=Label(edit_students_outer_frame,image=edit_students_banner,bd=0).pack(side=TOP,pady=20)
        edit_students_outer_frame.pack(fill="both")
        for i in range(0,4):
            edit_this_student_frame.columnconfigure(i,weight=1)
        for i in range(0,10):
            edit_this_student_frame.rowconfigure(i,weight=1)
        edit_this_student_frame.rowconfigure(10,weight=2)
        #main
        myfont=("Comic Sans MS",15)
        fullname=Label(edit_this_student_frame,text="Full Name*",bd=0,bg="#5e223b",fg="white",font=myfont)
        fullname.grid(row=0,column=0,sticky=E)
        s=StringVar()
        fullname_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][0]))
        fullname_entry.grid(row=0,column=1,padx=20,sticky=W)
        gender=Label(edit_this_student_frame,text="Gender",bd=0,bg="#5e223b",fg="white",font=myfont)
        gender.grid(row=1,column=0,sticky=E)
        gender_combo=Combobox(edit_this_student_frame,state="readonly",values=["Male","Female","Other"],width=19,justify=CENTER,font=myfont)
        gender_combo.set(str(st[0][1]))
        gender_combo.grid(row=1,column=1,padx=20,sticky=W)
        rollno=Label(edit_this_student_frame,text="Roll no.*",bd=0,bg="#5e223b",fg="white",font=myfont)
        rollno.grid(row=2,column=0,sticky=E)
        s=StringVar()
        rollno_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][2]))
        global rx
        rx=st[0][2]
        rollno_entry.grid(row=2,column=1,padx=20,sticky=W)
        admno=Label(edit_this_student_frame,text="Admission no.*",bd=0,bg="#5e223b",fg="white",font=myfont)
        admno.grid(row=3,column=0,sticky=E)
        s=StringVar()
        admno_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][3]))
        admno_entry.grid(row=3,column=1,padx=20,sticky=W)
        
        
        dob=Label(edit_this_student_frame,text="Date of birth",bd=0,bg="#5e223b",fg="white",font=myfont)
        dob.grid(row=4,column=0,sticky=E)
        s=StringVar()
        dob_entry=DateEntry(edit_this_student_frame,date_pattern="dd-MM-yyyy",width=19,font=myfont,selectmode="day",year=int(st[0][4][6:10]),month=int(st[0][4][3:5]),day=int(st[0][4][0:2]),justify=CENTER)
        dob_entry.grid(row=4,column=1,padx=20,sticky=W)
        
        blood=Label(edit_this_student_frame,text="Blood Group",bd=0,bg="#5e223b",fg="white",font=myfont)
        blood.grid(row=5,column=0,sticky=E)
        blood_combo=Combobox(edit_this_student_frame,state="readonly",width=19,values=["A+","A-","B+","B-","O+","O-","AB+","AB-"],justify=CENTER,font=myfont)
        blood_combo.set(str(st[0][5]))
        blood_combo.grid(row=5,column=1,padx=20,sticky=W)
        mode_transport=Label(edit_this_student_frame,text="Mode of transport",bd=0,bg="#5e223b",fg="white",font=myfont)
        mode_transport.grid(row=6,column=0,sticky=E)
        mode_transport_combo=Combobox(edit_this_student_frame,state="readonly",width=19,values=["Bike","Bicycle","Auto-Rikshaw","Foot","Bus"],justify=CENTER,font=myfont)
        #mode_transport_combo.set("Mode of transport")
        mode_transport_combo.set(str(st[0][6]))
        mode_transport_combo.grid(row=6,column=1,padx=20,sticky=W)
        vehicleno=Label(edit_this_student_frame,text="Vehicle No.",bd=0,fg="white",bg="#5e223b",font=myfont)
        vehicleno.grid(row=7,column=0,sticky=E)
        s=StringVar()
        vehicleno_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][7]))
        vehicleno_entry.grid(row=7,column=1,padx=20,sticky=W)
        studentemail=Label(edit_this_student_frame,text="Student's Email Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        studentemail.grid(row=8,column=0,sticky=E)
        t=StringVar()
        studentemail_entry=Entry(edit_this_student_frame,textvariable=t,justify=CENTER,font=myfont)
        t.set(str(st[0][8]))
        studentemail_entry.grid(row=8,column=1,padx=20,sticky=W)
        fathersname=Label(edit_this_student_frame,text="Father's Name",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersname.grid(row=9,column=0,sticky=E)
        t=StringVar()
        fathersname_entry=Entry(edit_this_student_frame,textvariable=t,justify=CENTER,font=myfont)
        t.set(str(st[0][9]))
        fathersname_entry.grid(row=9,column=1,padx=20,sticky=W)
        fathersphone=Label(edit_this_student_frame,text="Father's Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersphone.grid(row=0,column=2,sticky=E)
        s=StringVar()
        fathersphone_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][10]))
        fathersphone_entry.grid(row=0,column=3,padx=20,sticky=W)
        fathersemail=Label(edit_this_student_frame,text="Father's Email",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersemail.grid(row=1,column=2,sticky=E)
        s=StringVar()
        fathersemail_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][11]))
        fathersemail_entry.grid(row=1,column=3,padx=20,sticky=W)
        fathersocc=Label(edit_this_student_frame,text="Father's Occupation",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersocc.grid(row=2,column=2,sticky=E)
        s=StringVar()
        fathersocc_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][12]))
        fathersocc_entry.grid(row=2,column=3,padx=20,sticky=W)
        mothersname=Label(edit_this_student_frame,text="Mother's Name",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersname.grid(row=3,column=2,sticky=E)
        s=StringVar()
        mothersname_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][13]))
        mothersname_entry.grid(row=3,column=3,padx=20,sticky=W)
        mothersphone=Label(edit_this_student_frame,text="Mother's Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersphone.grid(row=4,column=2,sticky=E)
        s=StringVar()
        mothersphone_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][14]))
        mothersphone_entry.grid(row=4,column=3,padx=20,sticky=W)
        mothersemail=Label(edit_this_student_frame,text="Mother's Email",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersemail.grid(row=5,column=2,sticky=E)
        s=StringVar()
        mothersemail_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][15]))
        mothersemail_entry.grid(row=5,column=3,padx=20,sticky=W)
        mothersocc=Label(edit_this_student_frame,text="Mother's Occupation",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersocc.grid(row=6,column=2,sticky=E)
        s=StringVar()
        mothersocc_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][16]))
        mothersocc_entry.grid(row=6,column=3,padx=20,sticky=W)
        whatsappno=Label(edit_this_student_frame,text="Whatsapp no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        whatsappno.grid(row=7,column=2,sticky=E)
        s=StringVar()
        whatsappno_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][17]))
        whatsappno_entry.grid(row=7,column=3,padx=20,sticky=W)
        address=Label(edit_this_student_frame,text="Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        address.grid(row=8,column=2,sticky=E)
        t=StringVar()
        address_entry=Entry(edit_this_student_frame,textvariable=t,justify=CENTER,font=myfont)
        t.set(str(st[0][18]))
        address_entry.grid(row=8,column=3,padx=20,sticky=W)
        pincode=Label(edit_this_student_frame,text="Pin Code",bd=0,bg="#5e223b",fg="white",font=myfont)
        pincode.grid(row=9,column=2,sticky=E)
        s=StringVar()
        pincode_entry=Entry(edit_this_student_frame,textvariable=s,justify=CENTER,font=myfont)
        s.set(str(st[0][19]))
        pincode_entry.grid(row=9,column=3,padx=20,sticky=W)

        def update_student():
            try:
                gotdb=dob_entry.get_date()
                gotdb1=gotdb.strftime("%d-%m-%Y")
                s="update students set fullname = %s,gender=%s ,rollno=%s,admno=%s,dob=%s,blood=%s,mode_transport=%s,vehicleno=%s,studentemail=%s,fathersname=%s,fathersphone=%s,fathersemail=%s,fathersocc=%s,mothersname=%s,mothersphone=%s,mothersemail=%s,mothersocc=%s,whatsappno=%s,address=%s,pincode=%s where rollno=%s"
                b=(fullname_entry.get(),gender_combo.get(),int(rollno_entry.get()),int(admno_entry.get()),gotdb1,blood_combo.get(),mode_transport_combo.get(),vehicleno_entry.get(),studentemail_entry.get(),fathersname_entry.get(),fathersphone_entry.get(),fathersemail_entry.get(),fathersocc_entry.get(),mothersname_entry.get(),mothersphone_entry.get(),mothersemail_entry.get(),mothersocc_entry.get(),whatsappno_entry.get(),address_entry.get(),pincode_entry.get(),rx)
                cur.execute(s,b)
                mydb.commit()
                messagebox.showinfo("Success","Details Updated!")
                s=f"SELECT * FROM students WHERE rollno={rx}"
                cur.execute(s)
                st=cur.fetchall()
                show_view_students_frame()
            except:
                messagebox.showerror("Error","Something went wrong!")


        
        goback_btn=Button(edit_this_student_frame,image=goback_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_view_students_frame)
        goback_btn.grid(row=10,column=0,sticky=E)
        set_bttn=Button(edit_this_student_frame,image=set_btn,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=update_student)
        set_bttn.grid(row=10,column=1,columnspan=2)
        close_btn=Button(edit_this_student_frame,image=close_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_choice_frame)
        close_btn.grid(row=10,column=3,sticky=W)
        edit_this_student_frame.pack(expand=True,fill="both")
        edit_this_student_frame.tkraise()
        #edit_students_outer_frame.pack(expand=True,fill="both")
        edit_students_outer_frame.tkraise()

    def select_remove():
        clicked_item=l.curselection()
        try:
            sel=data[clicked_item[0]][2]
            s=f"DELETE FROM students WHERE rollno={sel}"
            cur.execute(s)
            mydb.commit()
            show_view_students_frame()
        except:
            messagebox.showwarning("Warning","Select the student first!")
    


    def select_edit():
        clicked_item=l.curselection()
        try:
            sel=data[clicked_item[0]][2]
            s=f"SELECT * FROM students WHERE rollno={sel}"
            cur.execute(s)
            st=cur.fetchall()
            show_edit_this_student_frame(st)
        except:
            messagebox.showwarning("Warning","Select the student first!")
    


    
    def show_view_this_student_frame(st):
        reset()
        label=Label(view_students_outer_frame,image=view_students_banner,bd=0).pack(side=TOP,pady=5)
        view_students_outer_frame.pack(fill="both")
        #configuring rows and columns
        for i in range(0,4):
            view_this_student_frame.columnconfigure(i,weight=1)
        for i in range(0,10):
            view_this_student_frame.rowconfigure(i,weight=1)
        view_this_student_frame.rowconfigure(10,weight=2)
        #main
        myfont=("Comic Sans MS",15)
        fullname=Label(view_this_student_frame,text="Full Name",bd=0,bg="#5e223b",fg="white",font=myfont)
        fullname.grid(row=0,column=0,sticky=E)
        fullname_entry=Label(view_this_student_frame,text=str(st[0][0]),bd=0,bg="#5e223b",fg="white",font=myfont)
        fullname_entry.grid(row=0,column=1,padx=20,sticky=W)
        gender=Label(view_this_student_frame,text="Gender",bd=0,bg="#5e223b",fg="white",font=myfont)
        gender.grid(row=1,column=0,sticky=E)
        gender_entry=Label(view_this_student_frame,text=str(st[0][1]),bd=0,bg="#5e223b",fg="white",font=myfont)
        gender_entry.grid(row=1,column=1,padx=20,sticky=W)
        rollno=Label(view_this_student_frame,text="Roll no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        rollno.grid(row=2,column=0,sticky=E)
        rollno_entry=Label(view_this_student_frame,text=str(st[0][2]),bd=0,bg="#5e223b",fg="white",font=myfont)
        rollno_entry.grid(row=2,column=1,padx=20,sticky=W)
        admno=Label(view_this_student_frame,text="Admission no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        admno.grid(row=3,column=0,sticky=E)
        admno_entry=Label(view_this_student_frame,text=str(st[0][3]),bd=0,bg="#5e223b",fg="white",font=myfont)
        admno_entry.grid(row=3,column=1,padx=20,sticky=W)
        dob=Label(view_this_student_frame,text="Date of birth",bd=0,bg="#5e223b",fg="white",font=myfont)
        dob.grid(row=4,column=0,sticky=E)
        dob_entry=Label(view_this_student_frame,text=str(st[0][4]),bd=0,bg="#5e223b",fg="white",font=myfont)
        dob_entry.grid(row=4,column=1,padx=20,sticky=W)
        blood=Label(view_this_student_frame,text="Blood Group",bd=0,bg="#5e223b",fg="white",font=myfont)
        blood.grid(row=5,column=0,sticky=E)
        blood_combo=Label(view_this_student_frame,text=str(st[0][5]),bd=0,bg="#5e223b",fg="white",font=myfont)
        blood_combo.grid(row=5,column=1,padx=20,sticky=W)
        mode_transport=Label(view_this_student_frame,text="Mode of transport",bd=0,bg="#5e223b",fg="white",font=myfont)
        mode_transport.grid(row=6,column=0,sticky=E)
        mode_transport_combo=Label(view_this_student_frame,text=str(st[0][6]),bd=0,bg="#5e223b",fg="white",font=myfont)
        #mode_transport_combo.set("Mode of transport")
        mode_transport_combo.grid(row=6,column=1,padx=20,sticky=W)
        vehicleno=Label(view_this_student_frame,text="Vehicle No.",bd=0,fg="white",bg="#5e223b",font=myfont)
        vehicleno.grid(row=7,column=0,sticky=E)
        vehicleno_entry=Label(view_this_student_frame,text=str(st[0][7]),bd=0,bg="#5e223b",fg="white",font=myfont)
        vehicleno_entry.grid(row=7,column=1,padx=20,sticky=W)
        studentemail=Label(view_this_student_frame,text="Student's Email Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        studentemail.grid(row=8,column=0,sticky=E)
        studentemail_entry=Label(view_this_student_frame,text=str(st[0][8]),bd=0,bg="#5e223b",fg="white",font=myfont)
        studentemail_entry.grid(row=8,column=1,padx=20,sticky=W)
        fathersname=Label(view_this_student_frame,text="Father's Name",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersname.grid(row=9,column=0,sticky=E)
        fathersname_entry=Label(view_this_student_frame,text=str(st[0][9]),bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersname_entry.grid(row=9,column=1,padx=20,sticky=W)
        fathersphone=Label(view_this_student_frame,text="Father's Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersphone.grid(row=0,column=2,sticky=E)
        fathersphone_entry=Label(view_this_student_frame,text=str(st[0][10]),bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersphone_entry.grid(row=0,column=3,padx=20,sticky=W)
        fathersemail=Label(view_this_student_frame,text="Father's Email",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersemail.grid(row=1,column=2,sticky=E)
        fathersemail_entry=Label(view_this_student_frame,text=str(st[0][11]),bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersemail_entry.grid(row=1,column=3,padx=20,sticky=W)
        fathersocc=Label(view_this_student_frame,text="Father's Occupation",bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersocc.grid(row=2,column=2,sticky=E)
        fathersocc_entry=Label(view_this_student_frame,text=str(st[0][12]),bd=0,bg="#5e223b",fg="white",font=myfont)
        fathersocc_entry.grid(row=2,column=3,padx=20,sticky=W)
        mothersname=Label(view_this_student_frame,text="Mother's Name",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersname.grid(row=3,column=2,sticky=E)
        mothersname_entry=Label(view_this_student_frame,text=str(st[0][13]),bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersname_entry.grid(row=3,column=3,padx=20,sticky=W)
        mothersphone=Label(view_this_student_frame,text="Mother's Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersphone.grid(row=4,column=2,sticky=E)
        mothersphone_entry=Label(view_this_student_frame,text=str(st[0][14]),bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersphone_entry.grid(row=4,column=3,padx=20,sticky=W)
        mothersemail=Label(view_this_student_frame,text="Mother's Email",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersemail.grid(row=5,column=2,sticky=E)
        mothersemail_entry=Label(view_this_student_frame,text=str(st[0][15]),bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersemail_entry.grid(row=5,column=3,padx=20,sticky=W)
        mothersocc=Label(view_this_student_frame,text="Mother's Occupation",bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersocc.grid(row=6,column=2,sticky=E)
        mothersocc_entry=Label(view_this_student_frame,text=str(st[0][16]),bd=0,bg="#5e223b",fg="white",font=myfont)
        mothersocc_entry.grid(row=6,column=3,padx=20,sticky=W)
        whatsappno=Label(view_this_student_frame,text="Whatsapp no.",bd=0,bg="#5e223b",fg="white",font=myfont)
        whatsappno.grid(row=7,column=2,sticky=E)
        whatsappno_entry=Label(view_this_student_frame,text=str(st[0][17]),bd=0,bg="#5e223b",fg="white",font=myfont)
        whatsappno_entry.grid(row=7,column=3,padx=20,sticky=W)
        address=Label(view_this_student_frame,text="Address",bd=0,bg="#5e223b",fg="white",font=myfont)
        address.grid(row=8,column=2,sticky=E)
        address_entry=Label(view_this_student_frame,text=str(st[0][18]),bd=0,bg="#5e223b",fg="white",font=myfont)
        address_entry.grid(row=8,column=3,padx=20,sticky=W)
        pincode=Label(view_this_student_frame,text="Pin Code",bd=0,bg="#5e223b",fg="white",font=myfont)
        pincode.grid(row=9,column=2,sticky=E)
        pincode_entry=Label(view_this_student_frame,text=str(st[0][19]),bd=0,bg="#5e223b",fg="white",font=myfont)
        pincode_entry.grid(row=9,column=3,padx=20,sticky=W)

        goback_btn=Button(view_this_student_frame,image=goback_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_view_students_frame)
        goback_btn.grid(row=10,column=0,columnspan=2)
        close_btn=Button(view_this_student_frame,image=close_photo,bd=0,bg="#5e223b",activebackground="#5e223b",fg="white",command=show_choice_frame)
        close_btn.grid(row=10,column=2,columnspan=2)
        view_this_student_frame.pack(expand=True,fill="both")
        view_students_list_frame.tkraise()
        view_this_student_frame.tkraise()
        view_students_outer_frame.tkraise()


    def select_view():
        clicked_item=l.curselection()
        try:
            sel=data[clicked_item[0]][2]
            s=f"SELECT * FROM students WHERE rollno={sel}"
            cur.execute(s)
            st=cur.fetchall()
            show_view_this_student_frame(st)
        except:
            messagebox.showwarning("Warning","Select the student first!")
    add_btn=Button(view_students_frame,image=add_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=show_addstudents_frame).grid(row=1,column=0)
    view_details_btn=Button(view_students_frame,image=view_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=select_view).grid(row=1,column=1)
    edit_details_btn=Button(view_students_frame,image=edit_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=select_edit).grid(row=1,column=2)
    remove_details_btn=Button(view_students_frame,image=remove_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=select_remove).grid(row=1,column=3)
    close_btn=Button(view_students_frame,image=close_photo,bd=0,bg="#5e223b",activebackground="#5e223b",command=show_choice_frame).grid(row=1,column=4)
    view_students_frame.pack(expand=True,fill="both")
    view_students_frame.tkraise()
    view_students_outer_frame.pack(expand=True,fill="both")
    view_students_outer_frame.tkraise()
    



def show_addstudents_frame():
    
    reset()
    
    
    #banner
    label=Label(add_students_outer_frame,image=add_students_banner,bd=0).pack(side=TOP,pady=20)

    #configuring rows and columns

    for i in range(0,4):
        add_students_frame.columnconfigure(i,weight=1)
    for i in range(0,10):
        add_students_frame.rowconfigure(i,weight=1)

    #main

    myfont=("Comic Sans MS",15)
    fullname=Label(add_students_frame,text="Full Name*",bd=0,bg="#5e223b",fg="white",font=myfont)
    fullname.grid(row=0,column=0,sticky=E)
    fullname_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    fullname_entry.grid(row=0,column=1,padx=20,sticky=W)

    gender=Label(add_students_frame,text="Gender",bd=0,bg="#5e223b",fg="white",font=myfont)
    gender.grid(row=1,column=0,sticky=E)
    gender_combo=Combobox(add_students_frame,state="readonly",values=["Male","Female","Other"],font=myfont,justify=CENTER,width=28)
    #gender_combo.set("Gender")
    gender_combo.grid(row=1,column=1,padx=20,sticky=W)

    rollno=Label(add_students_frame,text="Roll no.*",bd=0,bg="#5e223b",fg="white",font=myfont)
    rollno.grid(row=2,column=0,sticky=E)
    rollno_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    rollno_entry.grid(row=2,column=1,padx=20,sticky=W)


    admno=Label(add_students_frame,text="Admission no.*",bd=0,bg="#5e223b",fg="white",font=myfont)
    admno.grid(row=3,column=0,sticky=E)
    admno_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    admno_entry.grid(row=3,column=1,padx=20,sticky=W)

    dob=Label(add_students_frame,text="Date of birth",bd=0,bg="#5e223b",fg="white",font=myfont)
    dob.grid(row=4,column=0,sticky=E)
    dob_entry=DateEntry(add_students_frame,date_pattern="dd-MM-yyyy",width=28,font=myfont,selectmode="day",year=2000,month=1,day=1,justify=CENTER)
    dob_entry.grid(row=4,column=1,padx=20,sticky=W)
    

    blood=Label(add_students_frame,text="Blood Group",bd=0,bg="#5e223b",fg="white",font=myfont)
    blood.grid(row=5,column=0,sticky=E)
    blood_combo=Combobox(add_students_frame,state="readonly",values=["A+","A-","B+","B-","O+","O-","AB+","AB-"],font=myfont,justify=CENTER,width=28)
    blood_combo.set("")
    blood_combo.grid(row=5,column=1,padx=20,sticky=W)

    mode_transport=Label(add_students_frame,text="Mode of transport",bd=0,bg="#5e223b",fg="white",font=myfont)
    mode_transport.grid(row=6,column=0,sticky=E)
    mode_transport_combo=Combobox(add_students_frame,state="readonly",values=["Bike","Bicycle","Auto-Rikshaw","Foot","Bus"],font=myfont,width=28,justify=CENTER)
    #mode_transport_combo.set("Mode of transport")
    mode_transport_combo.grid(row=6,column=1,padx=20,sticky=W)

    vehicleno=Label(add_students_frame,text="Vehicle No.",bd=0,fg="white",bg="#5e223b",font=myfont)
    vehicleno.grid(row=7,column=0,sticky=E)
    vehicleno_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    vehicleno_entry.grid(row=7,column=1,padx=20,sticky=W)

    studentemail=Label(add_students_frame,text="Student's Email Address",bd=0,bg="#5e223b",fg="white",font=myfont)
    studentemail.grid(row=8,column=0,sticky=E)
    studentemail_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    studentemail_entry.grid(row=8,column=1,padx=20,sticky=W)
    
    fathersname=Label(add_students_frame,text="Father's Name",bd=0,bg="#5e223b",fg="white",font=myfont)
    fathersname.grid(row=9,column=0,sticky=E)
    fathersname_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    fathersname_entry.grid(row=9,column=1,padx=20,sticky=W)

    fathersphone=Label(add_students_frame,text="Father's Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
    fathersphone.grid(row=0,column=2,sticky=E)
    fathersphone_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    fathersphone_entry.grid(row=0,column=3,padx=20,sticky=W)

    fathersemail=Label(add_students_frame,text="Father's Email",bd=0,bg="#5e223b",fg="white",font=myfont)
    fathersemail.grid(row=1,column=2,sticky=E)
    fathersemail_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    fathersemail_entry.grid(row=1,column=3,padx=20,sticky=W)

    fathersocc=Label(add_students_frame,text="Father's Occupation",bd=0,bg="#5e223b",fg="white",font=myfont)
    fathersocc.grid(row=2,column=2,sticky=E)
    fathersocc_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    fathersocc_entry.grid(row=2,column=3,padx=20,sticky=W)

    mothersname=Label(add_students_frame,text="Mother's Name",bd=0,bg="#5e223b",fg="white",font=myfont)
    mothersname.grid(row=3,column=2,sticky=E)
    mothersname_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    mothersname_entry.grid(row=3,column=3,padx=20,sticky=W)

    mothersphone=Label(add_students_frame,text="Mother's Phone no.",bd=0,bg="#5e223b",fg="white",font=myfont)
    mothersphone.grid(row=4,column=2,sticky=E)
    mothersphone_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    mothersphone_entry.grid(row=4,column=3,padx=20,sticky=W)

    mothersemail=Label(add_students_frame,text="Mother's Email",bd=0,bg="#5e223b",fg="white",font=myfont)
    mothersemail.grid(row=5,column=2,sticky=E)
    mothersemail_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    mothersemail_entry.grid(row=5,column=3,padx=20,sticky=W)

    mothersocc=Label(add_students_frame,text="Mother's Occupation",bd=0,bg="#5e223b",fg="white",font=myfont)
    mothersocc.grid(row=6,column=2,sticky=E)
    mothersocc_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    mothersocc_entry.grid(row=6,column=3,padx=20,sticky=W)

    whatsappno=Label(add_students_frame,text="Whatsapp no.",bd=0,bg="#5e223b",fg="white",font=myfont)
    whatsappno.grid(row=7,column=2,sticky=E)
    whatsappno_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    whatsappno_entry.grid(row=7,column=3,padx=20,sticky=W)

    address=Label(add_students_frame,text="Address",bd=0,bg="#5e223b",fg="white",font=myfont)
    address.grid(row=8,column=2,sticky=E)
    address_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    address_entry.grid(row=8,column=3,padx=20,sticky=W)

    pincode=Label(add_students_frame,text="Pin Code",bd=0,bg="#5e223b",fg="white",font=myfont)
    pincode.grid(row=9,column=2,sticky=E)
    pincode_entry=Entry(add_students_frame,width=30,font=myfont,justify=CENTER)
    pincode_entry.grid(row=9,column=3,padx=20,sticky=W)


    def ins_students():
        try:
            gotdb=dob_entry.get_date()
            gotdb1=gotdb.strftime("%d-%m-%Y")
            s="INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            b=(fullname_entry.get(),gender_combo.get(),rollno_entry.get(),admno_entry.get(),gotdb1,blood_combo.get(),mode_transport_combo.get(),vehicleno_entry.get(),studentemail_entry.get(),fathersname_entry.get(),fathersphone_entry.get(),fathersemail_entry.get(),fathersocc_entry.get(),mothersname_entry.get(),mothersphone_entry.get(),mothersemail_entry.get(),mothersocc_entry.get(),whatsappno_entry.get(),address_entry.get(),pincode_entry.get())
            cur.execute(s,b)
            mydb.commit()
            messagebox.showinfo("Added","Student added!")
            show_addstudents_frame()
        except:
            messagebox.showerror("Error","Something went wrong!")
    
    #configuring columns

    for i in range(0,3):
        add_students_btn_frame.columnconfigure(i,weight=1)
    add_students_btn_frame.rowconfigure(0,weight=1)



        
    #adding buttons
    
    add_button=Button(add_students_btn_frame,image=add_photo,bd=0,activebackground="#5e223b",bg="#5e223b",command=ins_students).grid(row=0,column=1)
    back_button=Button(add_students_btn_frame,image=goback_photo,bd=0,activebackground="#5e223b",bg="#5e223b",command=show_view_students_frame).grid(row=0,column=0)
    close_button=Button(add_students_btn_frame,image=close_photo,bd=0,activebackground="#5e223b",bg="#5e223b",command=show_choice_frame).grid(row=0,column=2)
    
    add_students_frame.pack(expand=True,fill="both")
    add_students_btn_frame.pack(expand=True,fill="both")
    add_students_frame.tkraise()
    add_students_btn_frame.tkraise()
    add_students_outer_frame.pack(expand=True,fill="both")
    add_students_outer_frame.tkraise()




def show_choice_frame():

    reset()
    
    #Banner


    label=Label(choice_outer_frame,image=cls,bd=0,bg="#845C79",fg="#eddd64",font=("Lucida Handwriting",90)).pack(side=TOP)

    #configuring rows and columns    

    for i in range(0,3):
        choice_frame.columnconfigure(i,weight=1)
    
    for i in range(0,3):
        choice_frame.rowconfigure(i,weight=2)

    #for i in range(2,4):
        #choice_frame.rowconfigure(i,weight=1)
    

    #adding buttons

    students=Button(choice_frame,image=students_photo,bd=0,bg="#845C79",activebackground="#845C79",command=show_view_students_frame)
    students.grid(row=0,column=0)
    
    teachers=Button(choice_frame,image=teachers_photo,bd=0,bg="#845C79",activebackground="#845C79",command=show_view_teachers_frame)
    teachers.grid(row=0,column=1)

    #show_students=Button(choice_frame,image=show_students_photo,bd=0,bg="#845C79",activebackground="#845C79")
    #show_students.grid(row=0,column=2)

    #show_teachers=Button(choice_frame,image=show_teachers_photo,bd=0,bg="#845C79",activebackground="#845C79")
    #show_teachers.grid(row=0,column=3)

    attendance=Button(choice_frame,image=attendance_photo,bd=0,bg="#845C79",activebackground="#845C79",command=show_attendance_frame)
    attendance.grid(row=0,column=2)

    show_routine=Button(choice_frame,image=show_routine_photo,bd=0,bg="#845C79",activebackground="#845C79",command=show_routine_frame)
    show_routine.grid(row=1,column=0)

    daily_activities=Button(choice_frame,image=daily_activities_photo,bd=0,bg="#845C79",activebackground="#845C79",command=show_daily_activities_frame)
    daily_activities.grid(row=1,column=1)

    results=Button(choice_frame,image=results_photo,bd=0,bg="#845C79",activebackground="#845C79",command=show_result_frame)
    results.grid(row=1,column=2)

    logout_btn=Button(choice_frame,image=logout_photo,bd=0,bg="#845C79",activebackground="#845C79",command=logout)
    logout_btn.grid(row=2,columnspan=3)

    #frame packing

    choice_frame.pack(expand=True,fill="both")
    choice_outer_frame.pack(expand=True,fill="both")
    choice_outer_frame.tkraise()
    choice_frame.tkraise()



def show_login_frame():
    
    def check(c_user,c_pass):
        def right():
            def dbcreation(cur1):
                global mydb
                global cur
                try:
                    cur1.execute("CREATE DATABASE class_management")
                    mydb=rajjo.connect(host="localhost",user=c_user,password=c_pass,database="class_management")
                    cur=mydb.cursor()
                    s="CREATE TABLE students(fullname varchar(50) not null,gender varchar(20),rollno int primary key,admno int unique,dob varchar(50),blood varchar(5),mode_transport varchar(20),vehicleno varchar(50),studentemail varchar(70),fathersname varchar(50),fathersphone varchar(20),fathersemail varchar(70),fathersocc varchar(50),mothersname varchar(50),mothersphone varchar(20),mothersemail varchar(70),mothersocc varchar(50),whatsappno varchar(20),address varchar(100),pincode varchar(6))"
                    cur.execute(s)
                    s="CREATE TABLE teachers(fullname varchar(50) not null,gender varchar(20),dob varchar(20),blood varchar(5),email varchar(70),phone varchar(20),qualifications varchar(50),whatsappno varchar(20),address varchar(100),pincode varchar(6),subject varchar(50),teacher_code int(10) primary key)"
                    cur.execute(s)
                    show_choice_frame()
                except:
                    mydb=rajjo.connect(host="localhost",user=c_user,password=c_pass,database="class_management")
                    cur=mydb.cursor()
                    show_choice_frame()
            try:
                global mydb
                mydb=rajjo.connect(host="localhost",user=c_user,password=c_pass)
                #obtaining cursor
                cur1=mydb.cursor()
                dbcreation(cur1)
            except:
                messagebox.showerror("Error","Wrong username or password!")
        right()

    def ask_quit():
        ansr=messagebox.askquestion("Exit","Do you really want to exit?")
        if(ansr=="yes"):
            root.quit()

    #login_frame
        
    reset()

    #Banner
    
    label=Label(login_outer_frame,image=my_img,bd=0).pack(side=TOP)

    #configuring rows and columns

    login_frame.columnconfigure(0,weight=1)
    for i in range(0,7):
        login_frame.rowconfigure(i,weight=1)
    
    #adding widgets

    uname=Label(login_frame,text="Username",bg="#081b29",fg="white",font=("Comic Sans MS",25))
    pswd=Label(login_frame,text="Password",bg="#081b29",fg="white",font=("Comic Sans MS",25))
    entry1=Entry(login_frame,width=30,font=('Comic Sans MS',20),justify=CENTER)
    entry2=Entry(login_frame,show="*",width=30,font=('Comic Sans MS',20),justify=CENTER)
    uname.grid(row=0,column=0)
    entry1.grid(row=1,column=0)
    pswd.grid(row=2,column=0)
    entry2.grid(row=3,column=0)
    def developer():
        messagebox.showinfo("Developer","This software is developed by Rajnath Prasad of DAV Public School,Sawang of Class 12 A (2021-22).")
    forgot_btn=Button(login_frame,text="About The Developer",bd=0,bg="#081b29",fg="white",activebackground="#081b29",font=('Comic Sans MS',12),command=developer)
    forgot_btn.grid(row=4,column=0)
    log_btn=Button(login_frame,image=login_photo,bd=0,bg="#081b29",activebackground="#081b29",command=lambda:check(entry1.get(),entry2.get()))
    log_btn.grid(row=5,column=0)
    quit_btn=Button(login_frame,image=quit_photo,bd=0,bg="#081b29",activebackground="#081b29",command=ask_quit)
    quit_btn.grid(row=6,column=0)

    #packing frames

    login_frame.pack(expand=True,fill="both")
    login_outer_frame.pack(expand=True,fill="both")
    login_outer_frame.tkraise()
    login_frame.tkraise()
    
#Main
root=Tk()
root.title("Class Management")
root.configure(background="#081b29")
root.state("zoomed")

#Loading photos

add_photo=PhotoImage(file="files\\add.png")
reset_photo=PhotoImage(file="files\\reset b.png")
close_photo=PhotoImage(file="files\\close.png")
goback_photo=PhotoImage(file="files\\go back.png")
view_photo=PhotoImage(file="files\\view.png")
remove_photo=PhotoImage(file="files\\remove.png")
edit_photo=PhotoImage(file="files\\edit.png")
present_photo=PhotoImage(file="files\\present.png")
absent_photo=PhotoImage(file="files\\absent.png")
first_term_photo=PhotoImage(file="files\\first terminal.png")
sec_term_photo=PhotoImage(file="files\\second terminal.png")
proceed_image=PhotoImage(file="files\\proceed.png")
image=Image.open("files\\routine banner.png")
image=image.resize((600,120),Image.Resampling.LANCZOS)
routine_banner=ImageTk.PhotoImage(image)

set_routine_btn_photo=PhotoImage(file="files\\set routine.png")

image=Image.open("files\\students label.png")
image=image.resize((550,120),Image.Resampling.LANCZOS)
students_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\first terminal banner.png")
image=image.resize((800,120),Image.Resampling.LANCZOS)
first_trm_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\second terminal banner.png")
image=image.resize((800,120),Image.Resampling.LANCZOS)
sec_trm_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\results label.png")
image=image.resize((550,120),Image.Resampling.LANCZOS)
results_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\teachers label.png")
image=image.resize((550,120),Image.Resampling.LANCZOS)
teachers_banner=ImageTk.PhotoImage(image)

login_photo=PhotoImage(file="files\\login.png")
quit_photo=PhotoImage(file="files\\quit.png")
set_btn=PhotoImage(file="files\\set.png")
logout_photo=PhotoImage(file="files\\logout.png")

image=Image.open("files\\adding students banner.png")
image=image.resize((720,120),Image.Resampling.LANCZOS)
add_students_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\view students banner.png")
image=image.resize((720,100),Image.Resampling.LANCZOS)
view_students_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\edit students banner.png")
image=image.resize((720,100),Image.Resampling.LANCZOS)
edit_students_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\DAV.png")
image=image.resize((800,170),Image.Resampling.LANCZOS)
my_img=ImageTk.PhotoImage(image)

class12a=Image.open("files\\class 12a.png")
class12a=class12a.resize((690,120),Image.Resampling.LANCZOS)
cls=ImageTk.PhotoImage(class12a)

image=Image.open("files\\adding teachers banner.png")
image=image.resize((720,120),Image.Resampling.LANCZOS)
add_teachers_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\attendance banner.png")
image=image.resize((720,120),Image.Resampling.LANCZOS)
attendance_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\view teachers banner.png")
image=image.resize((720,100),Image.Resampling.LANCZOS)
view_teachers_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\edit teachers banner.png")
image=image.resize((720,100),Image.Resampling.LANCZOS)
edit_teachers_banner=ImageTk.PhotoImage(image)

image=Image.open("files\\students.png")
image=image.resize((200,200),Image.Resampling.LANCZOS)
students_photo=ImageTk.PhotoImage(image)

image=Image.open("files\\teachers.png")
image=image.resize((200,200),Image.Resampling.LANCZOS)
teachers_photo=ImageTk.PhotoImage(image)

image=Image.open("files\\daily activities banner.png")
image=image.resize((720,120),Image.Resampling.LANCZOS)
daily_activities_banner=ImageTk.PhotoImage(image)


image=Image.open("files\\attendance.png")
image=image.resize((200,200),Image.Resampling.LANCZOS)
attendance_photo=ImageTk.PhotoImage(image)

image=Image.open("files\\show routine.png")
image=image.resize((200,200),Image.Resampling.LANCZOS)
show_routine_photo=ImageTk.PhotoImage(image)

image=Image.open("files\\daily activities.png")
image=image.resize((200,200),Image.Resampling.LANCZOS)
daily_activities_photo=ImageTk.PhotoImage(image)

image=Image.open("files\\results.png")
image=image.resize((200,200),Image.Resampling.LANCZOS)
results_photo=ImageTk.PhotoImage(image)


#Adding frames

login_outer_frame=Frame(root,bg="#081b29")
login_frame=Frame(login_outer_frame,bg="#081b29")
choice_outer_frame=Frame(root,bg="#845C79")
choice_frame=Frame(choice_outer_frame,bg="#845C79")
students_outer_frame=Frame(root,bg="#845C79")
teachers_outer_frame=Frame(root,bg="#845C79")
students_frame=Frame(students_outer_frame,bg="#845C79")
view_teachers_outer_frame=Frame(root,bg="#5e223b")
view_students_outer_frame=Frame(root,bg="#5e223b")
view_students_frame=Frame(view_students_outer_frame,bg="#5e223b")
view_students_list_frame=Frame(view_students_frame,bg="#5e223b")
view_this_student_frame=Frame(root,bg="#5e223b")
view_this_teacher_frame=Frame(root,bg="#5e223b")
remove_students_outer_frame=Frame(root,bg="#5e223b")
remove_students_frame=Frame(remove_students_outer_frame,bg="#5e223b")
remove_students_list_frame=Frame(remove_students_frame,bg="#5e223b")
remove_teachers_outer_frame=Frame(root,bg="#5e223b")
remove_teachers_frame=Frame(remove_teachers_outer_frame,bg="#5e223b")
remove_teachers_list_frame=Frame(remove_teachers_frame,bg="#5e223b")
edit_students_outer_frame=Frame(root,bg="#5e223b")
edit_students_frame=Frame(edit_students_outer_frame,bg="#5e223b")
edit_this_student_frame=Frame(root,bg="#5e223b")
edit_students_list_frame=Frame(edit_students_frame,bg="#5e223b")
edit_teachers_outer_frame=Frame(root,bg="#5e223b")
edit_teachers_frame=Frame(edit_teachers_outer_frame,bg="#5e223b")
edit_this_teacher_frame=Frame(root,bg="#5e223b")
edit_teachers_list_frame=Frame(edit_teachers_frame,bg="#5e223b")
remove_this_student_frame=Frame(root,bg="#5e223b")
view_teachers_frame=Frame(view_teachers_outer_frame,bg="#5e223b")
view_teachers_list_frame=Frame(view_teachers_frame,bg="#5e223b")
students_btn_frame=Frame(students_outer_frame,bg="#845C79")
teachers_frame=Frame(teachers_outer_frame,bg="#845C79")
teachers_btn_frame=Frame(teachers_outer_frame,bg="#845C79")
add_students_outer_frame=Frame(root,bg="#5e223b")
add_students_frame=Frame(add_students_outer_frame,bg="#5e223b")
add_students_btn_frame=Frame(add_students_outer_frame,bg="#5e223b")
add_teachers_outer_frame=Frame(root,bg="#5e223b")
add_teachers_frame=Frame(add_teachers_outer_frame,bg="#5e223b")
add_teachers_btn_frame=Frame(add_teachers_outer_frame,bg="#5e223b")
routine_outer_frame=Frame(root,bg="#52c798")
empty_routine_frame=Frame(routine_outer_frame,bg="#52c798")
read_routine_frame=Frame(routine_outer_frame,bg="#52c798")
write_routine_frame=Frame(routine_outer_frame,bg="#52c798")
daily_activities_outer_frame=Frame(root,bg="#876ecc")
daily_activities_frame=Frame(daily_activities_outer_frame,bg="#876ecc")
add_daily_activities_outer_frame=Frame(root,bg="#876ecc")
add_daily_activities_frame=Frame(add_daily_activities_outer_frame,bg="#876ecc")
add_daily_activities_btn_frame=Frame(add_daily_activities_outer_frame,bg="#876ecc")
view_daily_activities_outer_frame=Frame(root,bg="#876ecc")
view_daily_activities_frame=Frame(view_daily_activities_outer_frame,bg="#876ecc")
view_daily_activities_btn_frame=Frame(view_daily_activities_outer_frame,bg="#876ecc")
view_this_daily_activities_outer_frame=Frame(root,bg="#876ecc")
view_this_daily_activities_frame=Frame(view_this_daily_activities_outer_frame,bg="#876ecc")
view_this_daily_activities_btn_frame=Frame(view_this_daily_activities_outer_frame,bg="#876ecc")
attendance_outer_frame=Frame(root,bg="#92A0D1")
attendance_frame=Frame(attendance_outer_frame,bg="#92A0D1")
add_attendance_outer_frame=Frame(root,bg="#92A0D1")
add_attendance_frame=Frame(add_attendance_outer_frame,bg="#92A0D1")
add_attendance_btn_frame=Frame(add_attendance_outer_frame,bg="#92A0D1")
view_attendance_outer_frame=Frame(root,bg="#92A0D1")
view_attendance_frame=Frame(view_attendance_outer_frame,bg="#92A0D1")
view_attendance_btn_frame=Frame(view_attendance_outer_frame,bg="#92A0D1")
view_this_attendance_outer_frame=Frame(root,bg="#92A0D1")
view_this_attendance_frame=Frame(view_this_attendance_outer_frame,bg="#92A0D1")
view_this_attendance_btn_frame=Frame(view_this_attendance_outer_frame,bg="#92A0D1")

result_outer_frame=Frame(root,bg="#3256A8")
result_frame=Frame(result_outer_frame,bg="#3256A8")
result_inner_frame=Frame(result_outer_frame,bg="#3256A8")
add_first_result_frame=Frame(result_outer_frame,bg="#3256A8")
add_first_result_list_frame=Frame(add_first_result_frame,bg="#3256A8")
add_sec_result_frame=Frame(result_outer_frame,bg="#3256A8")
add_sec_result_list_frame=Frame(add_sec_result_frame,bg="#3256A8")
add_res_sub_frame=Frame(result_outer_frame,bg="#3256A8")
view_first_result_frame=Frame(result_outer_frame,bg="#3256A8")
view_first_result_list_frame=Frame(view_first_result_frame,bg="#3256A8")
view_sec_result_frame=Frame(result_outer_frame,bg="#3256A8")
view_sec_result_list_frame=Frame(view_sec_result_frame,bg="#3256A8")
add_part_sub_res_frame=Frame(result_outer_frame,bg="#3256A8")
first_add_part_sub_res_frame=Frame(result_outer_frame,bg="#3256A8")
sec_add_part_sub_res_frame=Frame(result_outer_frame,bg="#3256A8")
first_view_part_sub_res_frame=Frame(result_outer_frame,bg="#3256A8")
sec_view_part_sub_res_frame=Frame(result_outer_frame,bg="#3256A8")

#start


try:
    os.mkdir("Data")
except:
    pass


try:
    os.makedirs("Data\\Attendance\\")
    pass
except:
    pass


try:
    os.makedirs("Data\\Daily activities\\")
    pass
except:
    pass


try:
    os.makedirs("Data\\Results\\Term 1\\")
    pass
except:
    pass


try:
    os.makedirs("Data\\Results\\Term 2\\")
    pass
except:
    pass


try:
    os.makedirs("Data\\Routine\\")
    pass
except:
    pass

show_login_frame()


root.mainloop()
