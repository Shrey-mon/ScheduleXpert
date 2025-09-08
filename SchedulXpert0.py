import tkinter as tk
from tkinter import *
from tkinter import messagebox
from scheduler6 import *
from tkinter import ttk
from set_info import *
from get_info import *
from faculty_info import FacultyInfo

root = Tk()
root.title("SchedulXpert")
img = tk.PhotoImage(file="C:/Users/Swadesh Sharma/Downloads/LNCT_Bhopal_Logo.png")
root.iconphoto(root, img)

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
rootw = int(sw // 1.2)
rooth = int(sh // 1.2)
xco = sw // 12
yco = sh // 15
root.geometry(f"{rootw}x{rooth}+{xco}+{yco}")

welcome_frame = tk.Frame(root, height=rooth * 0.96, width=rootw * 0.75, border=1, relief='solid', pady=20)
welcome_frame.pack_propagate(False)
welcome_frame.grid(row=0, column=1)

welcome_lbl1 = tk.Label(welcome_frame, text='Welcome To SchedulXpert', font=(None, 40), anchor='center', pady=50)
welcome_lbl1.pack()

welcome_lbl2 = tk.Label(welcome_frame, text='Your Schedule Management Application', font=(None, 15), justify='left',
                        anchor='w')
welcome_lbl2.pack()

navigation_frame = tk.Frame(root, bg='white', height=rooth * 0.96, width=rootw * 0.25, border=1, relief='solid',
                            pady=40,padx=20)

footer_frame = tk.Frame(root, width=rootw, height=rooth * 0.04, border=1, relief='solid', bg='lightgreen')
footer_frame.pack_propagate(False)
footer_frame.grid(row=1, column=0, columnspan=2)

credit_lbl = tk.Label(footer_frame, bg='lightgreen', text='Made By Swadesh K Sharma', font=(None, 11), anchor='e',
                      height=int(rooth * 0.04))
credit_lbl.pack(fill='both', side='right')

version_lbl = tk.Label(footer_frame, bg='lightgreen', text='Version: 0.0.1', font=(None, 11), anchor='w',
                       height=int(rooth * 0.04))
version_lbl.pack(fill='both', side='left')

faculty_info_frame = tk.Frame(root, height=rooth * 0.96, width=rootw * 0.75, border=1, relief='solid', padx=15, pady=20)
faculty_load_frame = tk.Frame(root, height=rooth * 0.96, width=rootw * 0.75, border=1, relief='solid', padx=15, pady=20)

navigation_frame.pack_propagate(False)
faculty_info_frame.pack_propagate(False)
faculty_load_frame.pack_propagate(False)

navigation_frame.grid(row=0, column=0)

logo = tk.Label(navigation_frame, bg='white')
logo.config(image=img)
logo.pack(fill='both')
lb1 = tk.Label(navigation_frame, text="SchedulXpert", font=("Times new roman", 22, "bold"), bg='white')
lb1.pack(fill='both')

faculty_info = fac_list
table = ttk.Treeview(faculty_info_frame, columns=('f_id', 'f_name', 'f_phone'), show='headings', height=15)

# frame for the entries
entry_frame = tk.LabelFrame(faculty_info_frame, text='Edit Information', height=rooth / 2, width=int(rootw * 0.75),
                            pady=10, padx=10)
entry_frame.grid_propagate(False)
fac_id_label = tk.Label(entry_frame, text='Faculty Id', height=2, width=20, anchor='w', font=(None, 10))
fac_name_label = tk.Label(entry_frame, text='Faculty name', height=2, width=20, anchor='w', font=(None, 10))
fac_phone_label = tk.Label(entry_frame, text='Phone Number', height=2, width=20, anchor='w', font=(None, 10))

f_id_entry = tk.Entry(entry_frame, width=50, font=(None, 10))
f_name_entry = tk.Entry(entry_frame, width=50, font=(None, 10))
f_phone_entry = tk.Entry(entry_frame, width=50, font=(None, 10))

current_frame = tk.Frame()


# frame1 Functions
def create_table():
    global table, entry_frame, current_frame
    current_frame.grid_forget()
    faculty_info_frame.grid(row=0, column=1)
    current_frame = faculty_info_frame
    table.heading('f_id', text='Faculty ID')
    table.heading('f_name', text='Faculty Name')
    table.heading('f_phone', text='Phone Number')
    table.column('f_id', anchor='center', width=200)
    table.column('f_phone', anchor='center', width=240)
    table.column('f_name', width=250)
    table.pack(fill='both')

    entry_frame.pack()

    fac_id_label.grid(row=1, column=0)
    f_id_entry.grid(row=1, column=1)

    fac_name_label.grid(row=3, column=0)
    f_name_entry.grid(row=3, column=1)

    fac_phone_label.grid(row=5, column=0)
    f_phone_entry.grid(row=5, column=1)

    show_entries()


def show_entries():
    global table, faculty_info
    table.delete(*table.get_children())
    for i in range(len(faculty_info)):
        fac = faculty_info[i]
        table.insert(parent='', index=i, values=(fac.getFId(), fac.getFName(), fac.getFPhone()))


options = []
all_fac = []


def item_select(_):
    global f_name_entry, f_id_entry, f_phone_entry
    f_id_entry.delete(0, END)
    f_name_entry.delete(0, END)
    f_phone_entry.delete(0, END)
    # table.update()
    for i in table.selection():
        l = list(table.item(i)['values'])
        f_id_entry.insert(END, l[0])
        f_name_entry.insert(END, l[1])
        f_phone_entry.insert(END, l[2])


def update_info():
    global faculty_info, f_id_entry, f_name_entry, f_phone_entry
    f_id = str(f_id_entry.get())
    f_name = str(f_name_entry.get())
    f_phone = str(f_phone_entry.get())
    update_faculty(f_id, f_name, f_phone)

    for i in range(len(faculty_info)):
        if faculty_info[i].getFId() == f_id:
            index = i
            faculty_info.remove(faculty_info[i])
            fac = FacultyInfo([f_id, f_name, f_phone])
            faculty_info.insert(i, fac)
            for id in table.get_children():
                if f_id == table.item(id)['values'][0]:
                    table.delete(id)
            table.insert(parent='', index=index, values=(f_id, f_name, f_phone))
            break


def add_fac():
    global faculty_info, f_id_entry, f_name_entry, f_phone_entry, options, all_fac
    if f_id_entry.get() == '':
        return
    if checkDuplication(f_id_entry.get()):
        pass
    else:
        setFacultyInfo(f_id_entry.get(), f_name_entry.get(), f_phone_entry.get())
        fac = FacultyInfo([f_id_entry.get(), f_name_entry.get(), f_phone_entry.get()])
        faculty_info.append(fac)
        table.insert(parent='', index=0, values=(fac.getFId(), fac.getFName(), fac.getFPhone()))
        options.append(fac.getFName())
        all_fac.append(fac)
        workbooks[fac.getFName()] = getFacWorkBook()
        faculty_sheets[fac.getFName()] = workbooks[fac.getFName()].active
        faculty_tt[fac.getFName()] = getTT()
    fac_dropdown_list['values'] = []
    fac_dropdown_list['values'] = options
    # show_entries(faculty_info)


def clear_entry():
    f_id_entry.delete(0, END)
    f_name_entry.delete(0, END)
    f_phone_entry.delete(0, END)


def delete_fac():
    global faculty_info, f_id_entry, options, all_fac
    f_id = f_id_entry.get()
    for fac in faculty_info:
        if fac.getFId() == f_id:
            faculty_info.remove(fac)
            options.remove(fac.getFName())
            all_fac.remove(fac)
            del workbooks[fac.getFName()]
            del faculty_sheets[fac.getFName()]
            del faculty_tt[fac.getFName()]
            break

    for id in table.get_children():
        if f_id == table.item(id)['values'][0]:
            table.delete(id)
            break
    fac_dropdown_list['values'] = []
    fac_dropdown_list['values'] = options
    delete_faculty(f_id)
    delete_fac_loads(f_id)


faculty_load_frame.grid_propagate(False)
fac_load_table_frame = tk.LabelFrame(faculty_load_frame, text='Load Table', height=int(rooth * 0.7),
                                     width=int(rootw * 0.75),
                                     padx=20, pady=20)
fac_load_table_frame.grid_propagate(False)
fac_load_table = ttk.Treeview(fac_load_table_frame, columns=('Section', 'Subject', 'Theory', 'Laboratory'),
                              show='headings',
                              height=5, )

for fac in faculty_info:
    all_fac.append(fac)
for fac in all_fac:
    options.append(fac.getFName())
fac_list_label = tk.Label(faculty_load_frame, text='Select Faculty', width=20, anchor='w')
fac_dropdown_list = ttk.Combobox(faculty_load_frame, state='readonly', width=30)

sub_list = []
for sub in cse_subjects:
    sub_list.append(sub)
for sub in aiml_subjects:
    sub_list.append(sub)
for sub in cy_subjects:
    sub_list.append(sub)

lbl_sub_combo = tk.Label(fac_load_table_frame, text='Select Subject', width=20, anchor='w', padx=2, pady=2)
lbl_sec_combo = tk.Label(fac_load_table_frame, text='Select Section', width=20, anchor='w', padx=2, pady=2)
select_sec_combo = ttk.Combobox(fac_load_table_frame, state='readonly', values=sections, width=30)
lbl_theory = tk.Label(fac_load_table_frame, text='Enter Theory Lectures', width=20, anchor='w', padx=2, pady=2)
lbl_lab = tk.Label(fac_load_table_frame, text='Enter Labs', width=20, anchor='w', padx=2, pady=2)
select_sub_combo = ttk.Combobox(fac_load_table_frame, state='readonly', values=sub_list, width=30)
theory_entry = tk.Entry(fac_load_table_frame, width=33)
lab_entry = tk.Entry(fac_load_table_frame, width=33)


def show_Load_frame():
    global faculty_load_frame, current_frame, options
    current_frame.grid_forget()
    faculty_load_frame.grid(row=0, column=1)
    current_frame = faculty_load_frame
    faculty_load_frame.grid_propagate(False)
    # fac_dropdown_list.delete(0, END)

    # for fac in all_fac:
    #     options.append(fac.getFName())
    fac_dropdown_list['values'] = []
    fac_dropdown_list['values'] = options
    fac_list_label.grid(row=0, column=0)
    fac_dropdown_list.grid(row=0, column=1)
    fac_load_table.heading('Section', text='Section')
    fac_load_table.heading('Subject', text='Subject')
    fac_load_table.heading('Theory', text='Theory')
    fac_load_table.heading('Laboratory', text='Laboratory')
    fac_load_table.column('Section', anchor='center', width=160)
    fac_load_table.column('Subject', anchor='center', width=160)
    fac_load_table.column('Theory', anchor='center', width=160)
    fac_load_table.column('Laboratory', anchor='center', width=160)
    fac_load_table.grid(row=0, column=0, columnspan=5)


def dropdown_selection(_):
    global fac_load_table, all_fac
    fac_load_table_frame.pack(side='bottom')
    fac_load_table.delete(*fac_load_table.get_children())
    # for fac in faculty_info:
    #     options.append(fac.getFName())
    # all_fac = []
    # for fac in faculty_info:
    #     all_fac.append(fac)
    for fac in all_fac:
        if fac.getFName() == fac_dropdown_list.get():
            c = 0
            load = fac.getFLoad()
            # print(load)
            for section, info in load.items():
                for j in info:
                    fac_load_table.insert(parent='', index=c, values=(section, j[0], j[2], j[3]))
                    c = c + 1
            break
    # fac_dropdown_list['values']=[]
    # for fac in all_fac:
    #     options.append(fac.getFName())
    tk.Label(fac_load_table_frame, height=4).grid(row=1, column=0)
    lbl_sub_combo.grid(row=2, column=0, sticky='w')
    select_sub_combo.grid(row=2, column=1)
    # lbl_sec_combo.config()
    lbl_sec_combo.grid(row=3, column=0, sticky='w')
    select_sec_combo.grid(row=3, column=1)
    lbl_theory.grid(row=4, column=0, sticky='w')
    theory_entry.grid(row=4, column=1)
    lbl_lab.grid(row=5, column=0, sticky='w')
    lab_entry.grid(row=5, column=1)
    load_insert_btn.grid(row=6, column=0)
    load_clear_btn.grid(row=6, column=1)
    load_delete_btn.grid(row=7,column=0,columnspan=2)


def load_insert():
    global faculty_info, all_fac
    sec = select_sec_combo.get()
    sub = select_sub_combo.get()
    th = theory_entry.get()
    lab = lab_entry.get()
    if len(sec)==0 or len(sub)==0 or len(th)==0 or len(lab)==0:
        return
    fac_name = fac_dropdown_list.get()
    for fac in faculty_info:
        if fac.getFName() == fac_name:
            f_id = fac.getFId()
            fac.setFLoad(sec, [sub, sec[-1], th, lab])
            if fac in av_fac:
                pass
            else:
                av_fac.append(fac)
            if fac not in all_fac:
                all_fac.append(fac)
    # fac_dropdown_list['values'] = []
    # for fac in all_fac:
    #     options.append(fac.getFName())

    fac_load_table.insert(parent='', index=END, values=(sec, sub, th, lab))
    add_fac_load(f_id, sub, sec[-1], th, lab)


def set_load_entry(_):
    global select_sub_combo, select_sec_combo, theory_entry, lab_entry
    theory_entry.delete(0,END)
    lab_entry.delete(0,END)
    id=fac_load_table.selection()
    l=fac_load_table.item(id)['values']
    select_sub_combo.set(l[1])
    select_sec_combo.set(l[0])
    theory_entry.insert(0,l[2])
    lab_entry.insert(0,l[3])


fac_load_table.bind('<Double-1>', set_load_entry)

def clear_load_entry():
    global select_sub_combo, select_sec_combo, theory_entry, lab_entry
    select_sub_combo.set('')
    select_sec_combo.set('')
    theory_entry.delete(0, END)
    lab_entry.delete(0, END)


def delete_load():
    global select_sub_combo, select_sec_combo, theory_entry, lab_entry,fac_dropdown_list
    f_name=fac_dropdown_list.get()
    id = fac_load_table.selection()

    sub=select_sub_combo.get()
    sec=select_sec_combo.get()
    # print(sec)
    th=theory_entry.get()
    lab=lab_entry.get()
    if len(sub)==0 or len(sec)==0 or len(th)==0 or len(lab)==0:
        return
    # f_id=''
    fac_load_table.delete(id)

    for fac in faculty_info:
        if fac.getFName()==f_name:
            f_id=fac.getFId()
            load=fac.getFLoad()[sec]
            for i in load:
                if i[0]==sub:
                    load.remove(i)
            break

    delete_fac_load(f_id,sub,sec[-1],th,lab)




load_insert_btn = tk.Button(fac_load_table_frame, text='Insert Load', width=20, command=load_insert, pady=3, padx=3)
load_clear_btn = tk.Button(fac_load_table_frame, text='Clear', width=20, command=clear_load_entry, padx=3, pady=3)
load_delete_btn=tk.Button(fac_load_table_frame,text='Delete', width=20, command=delete_load,padx=3,pady=3)
fac_dropdown_list.bind('<<ComboboxSelected>>', dropdown_selection)


def close_root():
    root.destroy()


update_btn = tk.Button(entry_frame, text='UPDATE', command=update_info, width=15)
update_btn.grid(row=7, column=0)

add_btn = tk.Button(entry_frame, text='ADD FACULTY', command=add_fac, width=15)
add_btn.grid(row=7, column=1)

clear_btn = tk.Button(entry_frame, text='CLEAR', command=clear_entry, width=15)
clear_btn.grid(row=8, column=0)

delete_btn = tk.Button(entry_frame, text='DELETE', command=delete_fac, width=15)
delete_btn.grid(row=8, column=1)

table.bind('<Double-1>', item_select)

lab_allotment_frame = tk.Frame(root, height=rooth * 0.96, width=rootw * 0.75, border=1, relief='solid', padx=15,
                               pady=20)
lab_allotment_frame.grid_propagate(False)
lbl_sec_combo_1 = tk.Label(lab_allotment_frame, text='Select Section', width=20, anchor='w', padx=2, pady=2)
select_sec_combo_1 = ttk.Combobox(lab_allotment_frame, state='readonly', values=sections, width=30)

sec_lab = section_labs.copy()
sec_lab_fac = section_lab_faculty.copy()

lab_allotment_table_frame = tk.LabelFrame(lab_allotment_frame, text='Load Table', height=int(rooth * 0.7),
                                          width=int(rootw * 0.75),
                                          padx=20, pady=20)
lab_allotment_table_frame.pack_propagate(False)
lab_allotment_frame.pack_propagate(False)
lab_allotment_table = ttk.Treeview(lab_allotment_table_frame, columns=('Subject', 'Laboratory', 'Faculty'),
                                   show='headings',
                                   height=7)


def show_lab_allotment_frame():
    global current_frame
    current_frame.grid_forget()
    current_frame = lab_allotment_frame
    lab_allotment_frame.grid(row=0, column=1)
    lab_allotment_frame.pack_propagate(False)
    lbl_sec_combo_1.pack(anchor='w')
    select_sec_combo_1.pack(anchor='w')
    lab_allotment_table_frame.pack_propagate(False)


# lab_allotment_table_frame.pack_propagate(False)
# lbl_sec_combo_2=tk.Label(lab_allotment_table_frame, text='Select Section', width=30)
# select_sec_combo_2=ttk.Combobox(lab_allotment_table_frame,)


def section_combobox_selection(_):
    lab_allotment_table_frame.pack(side='bottom')
    # lab_allotment_frame.pack_propagate(False)
    # lab_allotment_table_frame.pack_propagate(False)
    lab_allotment_table.pack()

    lab_allotment_table.heading('Subject', text='Subject')
    lab_allotment_table.heading('Laboratory', text='Laboratory')
    lab_allotment_table.heading('Faculty', text='Section')
    lab_allotment_table.column('Subject', anchor='center', width=120)
    lab_allotment_table.column('Laboratory', anchor='center', width=180)
    lab_allotment_table.column('Faculty', anchor='center', width=340)

    sec = select_sec_combo_1.get()
    lab_allotment_table.delete(*lab_allotment_table.get_children())
    labs = sec_lab[sec]
    fac = sec_lab_fac[sec]
    c = 0
    for i in labs.keys():
        if len(labs[i]) == 2:
            c=c+1
            lab_allotment_table.insert(parent='', index=(c), values=(i[0:5], labs[i][0], fac[i][0].getFName()))
            c=c+1
            lab_allotment_table.insert(parent='', index=(c), values=(i[6:], labs[i][1], fac[i][1].getFName()))
        else:
            c=c+1
            lab_allotment_table.insert(parent='', index=(c), values=(i, labs[i][0], fac[i][0].getFName()))


select_sec_combo_1.bind('<<ComboboxSelected>>', section_combobox_selection)


def start_scheduling():
    answer = messagebox.askyesno("Confirm", "Do you want to start Scheduling")
    if answer:
        # setTimeTables()
        # copy_tt_to_excel()
        set_sheets()
        messagebox.showinfo("Task Completion", "Scheduling Completed")
    else:
        pass


sub_names = get_sub_names()

sub_list_frame = tk.Frame(root, height=rooth * 0.96, width=rootw * 0.75, border=1, relief='solid', padx=15, pady=20)
sub_table = ttk.Treeview(sub_list_frame, columns=('Subject Code', 'Subject Name', 'Subject Type'), show='headings',
                         height=10)
sub_list_frame.grid_propagate(False)
lbl_sub_code = tk.Label(sub_list_frame, text='Enter Subject Code',anchor='w')
entry_sub_code = tk.Entry(sub_list_frame, width=40)
lbl_sub_name = tk.Label(sub_list_frame, text='Enter Subject Name',anchor='w')
entry_sub_name = tk.Entry(sub_list_frame, width=40)
lbl_sub_type = tk.Label(sub_list_frame, text='Select Subject Type',anchor='w')
combo_sub_type = ttk.Combobox(sub_list_frame, values=('B', 'L', 'T'), state='readonly', width=37)


def insert_sub():
    sub_code = entry_sub_code.get()
    sub_name = entry_sub_name.get()
    sub_type = combo_sub_type.get()

    if len(sub_code)==0:
        return

    add_subject(sub_code, sub_name, sub_type)
    sub_names[sub_code] = [sub_name, sub_type]

    index = len(sub_names) - 1
    sub_table.insert(parent='', index=index, values=[sub_code, sub_name, sub_type])


def update_sub():
    global entry_sub_name,entry_sub_code,combo_sub_type
    if len(entry_sub_code.get())==0:
        return

    sub_code=entry_sub_code.get()
    sub_name=entry_sub_name.get()
    sub_type=combo_sub_type.get()

    update_subject(sub_code, sub_name, sub_type)

    c=0
    for i in sub_table.selection():
        if sub_table.item(i)['values'][0]==sub_code:
            c = c + 1
            sub_table.delete(i)
            sub_table.insert(parent='',index=c, values=(sub_code,sub_name,sub_type))


def delete_subject():
    global entry_sub_name, entry_sub_code, combo_sub_type
    if len(entry_sub_code.get()) == 0:
        return

    sub_code = entry_sub_code.get()
    sub_name = entry_sub_name.get()
    sub_type = combo_sub_type.get()

    delete_sub(sub_code)
    for i in sub_table.selection():
        if sub_table.item(i)['values'][0] == sub_code:
            sub_table.delete(i)


def clear_entry_1():
    entry_sub_code.delete(0,END)
    entry_sub_name.delete(0,END)
    combo_sub_type.set('')


sub_insert_btn = tk.Button(sub_list_frame, width=30, text='Insert Subject', command=insert_sub,padx=6)
sub_update_btn = tk.Button(sub_list_frame, width=30, text='Update Subject', command=update_sub,padx=6)
sub_delete_btn = tk.Button(sub_list_frame,text='Delete Subject', width=30, command=delete_subject)
sub_entry_clear_btn= tk.Button(sub_list_frame, text='Clear', width=30,command=clear_entry_1)


def subject_item_select(_):
    global entry_sub_name,entry_sub_code,combo_sub_type
    entry_sub_name.delete(0, END)
    entry_sub_code.delete(0, END)
    sub_list_frame.grid_propagate(False)
    for i in sub_table.selection():
        l = list(sub_table.item(i)['values'])
        entry_sub_code.insert(END, l[0])
        entry_sub_name.insert(END, l[1])
        combo_sub_type.set(l[2])


sub_table.bind('<Double-1>', subject_item_select)


def show_sub_table():
    global current_frame
    current_frame.grid_forget()
    current_frame = sub_list_frame
    sub_list_frame.grid(row=0, column=1)
    sub_list_frame.grid_propagate(False)
    sub_table.heading('Subject Code', text='Subject Code')
    sub_table.heading('Subject Name', text='Subject Name')
    sub_table.heading('Subject Type', text='Subject Type')
    sub_table.column('Subject Code', width=170, anchor='center')
    sub_table.column('Subject Name', width=360, anchor='center')
    sub_table.column('Subject Type', width=170, anchor='center')
    sub_table.grid(row=0, column=0,columnspan=3, padx=5, pady=20)

    sub_table.delete(*sub_table.get_children())

    c = 0
    for i, j in sub_names.items():
        sub_table.insert(parent='', index=c, values=(i, j[0], j[1]))
        c=c+1

    lbl_sub_code.grid(row=1,column=0,pady=3, padx=5,sticky='w')
    entry_sub_code.grid(row=1, column=1,pady=3, padx=5,sticky='w')
    lbl_sub_name.grid(row=2,column=0,pady=3, padx=5,sticky='w')
    entry_sub_name.grid(row=2,column=1,pady=3, padx=5,sticky='w')
    lbl_sub_type.grid(row=3, column=0,pady=3, padx=5,sticky='w')
    combo_sub_type.grid(row=3,column=1,pady=3, padx=5,sticky='w')

    sub_insert_btn.grid(row=4, column=0,pady=4,sticky='w',padx=6)
    sub_update_btn.grid(row=4, column=1,pady=4,sticky='w',padx=6)
    sub_delete_btn.grid(row=5, column=0,padx=6, sticky='w', pady=4)
    sub_entry_clear_btn.grid(row=5,column=1, sticky='w', pady=4,padx=6)


# frame1 buttons
empty_lbl = tk.Label(navigation_frame, height=3, bg='white')
empty_lbl.pack()

show_fac_info_btn = tk.Button(navigation_frame, text='FACULTY INFORMATION', command=create_table, width=30)
show_fac_info_btn.pack(pady=10)

show_sub_btn = tk.Button(navigation_frame, text='SUBJECTS', command=show_sub_table, width=30)
show_sub_btn.pack(pady=10)

show_fac_load_btn = tk.Button(navigation_frame, text='FACULTY LOAD', command=show_Load_frame, width=30)
show_fac_load_btn.pack(pady=10)

show_sec_lab_alt_btn = tk.Button(navigation_frame, text='LAB ALLOTMENT', command=show_lab_allotment_frame, width=30)
show_sec_lab_alt_btn.pack(pady=10)

set_btn = tk.Button(navigation_frame, text='START SCHEDULING', command=start_scheduling, width=30)
set_btn.pack(side='bottom')

close_btn = tk.Button(navigation_frame, text='CLOSE', command=close_root, width=30)
close_btn.pack(side='bottom', pady=20)


def close_current_frame(_):
    global current_frame
    current_frame.grid_forget()


root.bind('<Escape>', close_current_frame)

root.resizable(False, False)
root.mainloop()
