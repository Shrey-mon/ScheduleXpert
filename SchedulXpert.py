import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
import threading

import scheduler6
import scheduler7
from scheduler6 import *
from set_info import *
from get_info import *
from win32api import GetSystemMetrics

sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
rootw = int(sw // 1.2)
rooth = int(sh // 1.2)
xco = sw // 12
yco = sh // 15

fac_info = scheduler6.fac_list


class App(tk.Tk):
    def __init__(self, title, width, height, xco, yco):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}+{xco}+{yco}")
        img = tk.PhotoImage(file="LNCT_Bhopal_Logo.png")
        self.iconphoto(self, img)
        self.current_frame = tk.Frame()
        self.columnconfigure(2)
        self.resizable(False, False)
        self.bind('<Escape>', self.close_current_frame)

        # widget section
        self.navFrame = NavFrame(self, rootw * 0.25, rooth * 0.96)
        self.welcomeFrame = WelcomeFrame(self, rootw * 0.75, rooth * 0.96)
        self.footerFrame = FooterFrame(self, rootw, rooth * 0.04)
        self.facInfoFrame = FacInfoFrame(self, rootw * 0.75, rooth * 0.96)
        self.sectionInfoFrame = SectionInfoFrame(self, rootw * 0.75, rooth * 0.96)
        self.facLoadFrame = FacultyLoadFrame(self, rootw * 0.75, rooth * 0.96)
        self.subjectFrame = SubjectFrame(self, rootw * 0.75, rooth * 0.96)
        self.labAllotmentFrame = LabAllotmentFrame(self, rootw * 0.75, rooth * 0.96)
        self.presetFrame = PresetFrame(self, rootw * 0.75, rooth * 0.96)

    def display(self):
        # self.facInfoFrame.table.bind('<Double-1>', self.facInfoFrame.item_select)
        self.mainloop()

    def close_current_frame(self, _):
        self.current_frame.grid_forget()


def close_root():
    root.destroy()


def create_table():
    root.facInfoFrame.show()


def preset_time_tables():
    root.presetFrame.show()


class NavFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        self.config(width=w, height=h, bg='white', border=1, relief='solid', pady=40, padx=20)
        self.grid(row=0, column=0)
        self.pack_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.img1 = tk.PhotoImage(file="LNCT_Bhopal_Logo.png")
        logo = tk.Label(self, bg='white', image=self.img1)
        logo.pack(fill='both')
        lb1 = tk.Label(self, text="SchedulXpert", font=("Times new roman", 22, "bold"), bg='white')
        lb1.pack(fill='both')

        empty_lbl = tk.Label(self, height=1, bg='white')
        empty_lbl.pack()

        show_fac_info_btn = tk.Button(self, text='FACULTY INFORMATION', command=create_table, width=30)
        show_fac_info_btn.pack(pady=8)

        show_section_info_btn = tk.Button(self, text='SECTION INFORMATION', command=self.show_sections, width=30)
        show_section_info_btn.pack(pady=8)

        show_sub_btn = tk.Button(self, text='SUBJECTS', command=self.show_sub_table, width=30)
        show_sub_btn.pack(pady=8)

        show_fac_load_btn = tk.Button(self, text='FACULTY LOAD', command=self.show_Load_frame, width=30)
        show_fac_load_btn.pack(pady=8)

        show_sec_lab_alt_btn = tk.Button(self, text='LAB ALLOTMENT', command=self.show_lab_allotment_frame, width=30)
        show_sec_lab_alt_btn.pack(pady=8)

        preset_tt_btn = tk.Button(self, text='PRESETS', command=preset_time_tables, width=30)
        preset_tt_btn.pack(pady=8)

        set_btn = tk.Button(self, text='START SCHEDULING', command=self.start_scheduling, width=30)
        set_btn.pack(side='bottom')

        close_btn = tk.Button(self, text='CLOSE', command=close_root, width=30)
        close_btn.pack(side='bottom', pady=20)

    def show_sub_table(self):
        root.current_frame.grid_forget()
        root.subjectFrame.show()

    def show_Load_frame(self):
        root.current_frame.grid_forget()
        root.facLoadFrame.show()

    def show_sections(self):
        root.current_frame.grid_forget()
        root.sectionInfoFrame.show()

    def show_lab_allotment_frame(self):
        root.current_frame.grid_forget()
        root.labAllotmentFrame.show()

    def start_scheduling(self):
        answer = messagebox.askyesno("Confirm", "Do you want to start Scheduling")
        if answer:
            messagebox.showinfo("Task Status", "Scheduling Started\nDo not click anywhere!!")
            setTimeTables()
            copy_tt_to_excel()
            set_sheets()
            messagebox.showinfo("Task Completion", "Scheduling Completed")
        else:
            pass


class WelcomeFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.grid(row=0, column=1)
        self.pack_propagate(False)

        self.create_widgets()

    def create_widgets(self):
        welcome_lbl1 = tk.Label(self, text='Welcome To SchedulXpert', font=(None, 40), anchor='center', pady=50)
        welcome_lbl1.pack()

        welcome_lbl2 = tk.Label(self, text='Your Schedule Management Application', font=(None, 15), justify='left',
                                anchor='w')
        welcome_lbl2.pack()

        self.btn_show_existing_tt = tk.Button(self, text='Show Existing Timetables', width=50, command=self.show_tt)
        self.btn_show_existing_tt.pack()

    def show_tt(self):
        pass


class FooterFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        self.config(width=w, height=h, border=1, relief='solid', bg='lightgreen')
        self.grid(row=1, column=0, columnspan=2)
        self.pack_propagate(False)

        self.create_widgets()

    def create_widgets(self):
        credit_lbl = tk.Label(self, bg='light green', text='Made By Swadesh K Sharma', font=(None, 11), anchor='e',
                              height=int(rooth * 0.04))
        credit_lbl.pack(fill='both', side='right')

        version_lbl = tk.Label(self, bg='light green', text='Version: 0.0.1', font=(None, 11), anchor='w',
                               height=int(rooth * 0.04))
        version_lbl.pack(fill='both', side='left')


class FacInfoFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__()
        self.f_phone_entry = None
        self.f_name_entry = None
        self.f_id_entry = None
        self.fac_phone_label = None
        self.fac_id_label = None
        self.entry_frame = None
        self.fac_name_label = None
        parent.current_frame.grid_forget()
        parent.current_frame = self
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.pack_propagate(False)
        self.columnconfigure(3)
        self.table = ttk.Treeview(self, columns=('f_id', 'f_name', 'f_phone'), show='headings', height=8)
        self.table.bind('<Double-1>', self.item_select)
        self.create_widgets()

    def create_widgets(self):
        self.table.pack(fill='both')
        self.table.heading('f_id', text='Faculty ID')
        self.table.heading('f_name', text='Faculty Name')
        self.table.heading('f_phone', text='Phone Number')
        self.table.column('f_id', anchor='center', width=200)
        self.table.column('f_phone', anchor='center', width=240)
        self.table.column('f_name', width=250)

        self.entry_frame = tk.LabelFrame(self, text='Edit Information', height=rooth / 2, width=int(rootw * 0.75),
                                         pady=10, padx=10)
        self.entry_frame.grid_propagate(False)
        self.entry_frame.columnconfigure(3)
        self.entry_frame.pack()

        self.fac_id_label = tk.Label(self.entry_frame, text='Faculty Id', height=2, width=20, anchor='w',
                                     font=(None, 10))
        self.fac_name_label = tk.Label(self.entry_frame, text='Faculty name', height=2, width=20, anchor='w',
                                       font=(None, 10))
        self.fac_phone_label = tk.Label(self.entry_frame, text='Phone Number', height=2, width=20, anchor='w',
                                        font=(None, 10))

        self.f_id_entry = tk.Entry(self.entry_frame, width=50, font=(None, 10))
        self.f_name_entry = tk.Entry(self.entry_frame, width=50, font=(None, 10))
        self.f_phone_entry = tk.Entry(self.entry_frame, width=50, font=(None, 10))

        self.fac_id_label.grid(row=1, column=0)
        self.f_id_entry.grid(row=1, column=1)

        self.fac_name_label.grid(row=3, column=0)
        self.f_name_entry.grid(row=3, column=1)

        self.fac_phone_label.grid(row=5, column=0)
        self.f_phone_entry.grid(row=5, column=1)

        update_btn = tk.Button(self.entry_frame, text='UPDATE', command=self.update_info, width=15)
        update_btn.grid(row=7, column=0)

        add_btn = tk.Button(self.entry_frame, text='ADD FACULTY', command=self.add_fac, width=15)
        add_btn.grid(row=7, column=1)

        clear_btn = tk.Button(self.entry_frame, text='CLEAR', command=self.clear_entry, width=15)
        clear_btn.grid(row=8, column=0)

        delete_btn = tk.Button(self.entry_frame, text='DELETE', command=self.delete_fac, width=15)
        delete_btn.grid(row=8, column=1)

        self.show_entries()

    def item_select(self, _):
        self.f_id_entry.delete(0, END)
        self.f_name_entry.delete(0, END)
        self.f_phone_entry.delete(0, END)
        # table.update()
        for i in self.table.selection():
            l = list(self.table.item(i)['values'])
            self.f_id_entry.insert(END, l[0])
            self.f_name_entry.insert(END, l[1])
            self.f_phone_entry.insert(END, l[2])

    def show_entries(self):
        global fac_info
        self.table.delete(*self.table.get_children())
        for i in range(len(fac_info)):
            fac = fac_info[i]
            self.table.insert(parent='', index=i, values=(fac.getFId(), fac.getFName(), fac.getFPhone()))

    def update_info(self):
        pass

    def add_fac(self):
        pass

    def clear_entry(self):
        self.f_id_entry.delete(0, END)
        self.f_name_entry.delete(0, END)
        self.f_phone_entry.delete(0, END)

    def delete_fac(self):
        pass

    def show(self):
        root.current_frame.grid_forget()
        root.current_frame = self
        self.grid(row=0, column=1)


class SectionInfoFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        parent.current_frame.grid_forget()
        parent.current_frame = self
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.pack_propagate(False)
        self.section_table = ttk.Treeview(self, columns=('Sections', 'Mentor'), show='headings', height=8)
        self.section_table.bind('<Double-1>', self.fill_entry)

        self.entry_frame = tk.LabelFrame(self, text='Edit Information', height=int(rooth * 0.7),
                                         width=int(rootw * 0.72),
                                         padx=20, pady=20)
        # self.entry_frame.grid_propagate(False)

        self.sec_info = get_sections_and_mentors(2)
        self.create_widgets()

    def create_widgets(self):
        # tk.Label(self,text='Sections And Mentors', width=40, font=(None, 20)).pack()
        self.section_table.heading('Sections', text='Sections')
        self.section_table.heading('Mentor', text='Mentor')
        self.section_table.column('Sections', anchor='center', width=200)
        self.section_table.column('Mentor', anchor='w', width=400)
        self.section_table.pack(fill='both')
        self.entry_frame.pack(fill='both')
        self.section_table.delete(*self.section_table.get_children())
        c = 0
        for i, j in self.sec_info.items():
            self.section_table.insert(parent='', index=c, values=(i, j.getFName()))
            c = c + 1

        self.options = []
        # self.fac_dict={}
        for fac in scheduler6.fac_list:
            self.options.append(fac.getFName())
            # self.fac_dict[fac.getFName()]=fac

        self.lbl_enter_section = tk.Label(self.entry_frame, text='Enter Section Name', width=20, anchor='w', padx=2,
                                          pady=2)
        self.enter_section_entry = tk.Entry(self.entry_frame, width=55)

        self.lbl_select_faculty = tk.Label(self.entry_frame, text='Select Faculty', width=20, anchor='w', padx=2,
                                           pady=2)
        self.select_faculty_combo = ttk.Combobox(self.entry_frame, state='readonly', values=self.options, width=50)

        self.insert_btn = tk.Button(self.entry_frame, text='INSERT', command=self.insert_section, width=20)
        self.update_btn = tk.Button(self.entry_frame, text='UPDATE', command=self.update_section, width=20)
        self.delete_btn = tk.Button(self.entry_frame, text='DELETE', command=self.delete_section, width=20)
        self.clear_btn = tk.Button(self.entry_frame, text='CLEAR', command=self.clear_entry, width=20)

        self.lbl_enter_section.grid(row=2, column=0, )
        self.enter_section_entry.grid(row=2, column=1)

        self.lbl_select_faculty.grid(row=3, column=0)
        self.select_faculty_combo.grid(row=3, column=1)

        self.insert_btn.grid(row=4, column=0)
        self.update_btn.grid(row=4, column=1)
        self.delete_btn.grid(row=5, column=0)
        self.clear_btn.grid(row=5, column=1)

    def insert_section(self):
        self.section_table.insert(parent='', index=END, values=(self.enter_section_entry.get(),
                                                                self.select_faculty_combo.get()))
        insert_section(self.enter_section_entry.get(), self.select_faculty_combo.get())

    def update_section(self):
        pass

    def delete_section(self):
        pass

    def clear_entry(self):
        self.enter_section_entry.delete(0, END)
        self.select_faculty_combo.set('')

    def fill_entry(self, _):
        pass

    def show(self):
        root.current_frame.grid_forget()
        root.current_frame = self
        self.grid_propagate(False)
        self.grid(row=0, column=1)


class FacultyLoadFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        parent.current_frame.grid_forget()
        parent.current_frame = self
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.fac_list_label = tk.Label(self, text='Select Faculty', width=20, anchor='w', font=(None, 10), height=1)
        self.fac_dropdown_list = ttk.Combobox(self, state='readonly', width=30)
        self.fac_load_table_frame = tk.LabelFrame(self, text='Load Table', height=int(rooth * 0.7),
                                                  width=int(rootw * 0.72),
                                                  padx=20, pady=20)
        self.fac_load_table_frame.grid_propagate(False)
        self.fac_load_table = ttk.Treeview(self.fac_load_table_frame,
                                           columns=('Section', 'Subject', 'Theory', 'Laboratory'),
                                           show='headings', height=5, )
        self.grid_propagate(False)
        self.fac_load_table.bind('<Double-1>', self.set_load_entry)

        self.unallotted_sub_table = ttk.Treeview(self.fac_load_table_frame, columns=('Subject', 'Section'),
                                                 show='headings', height=5)
        self.unallotted_sub_table.bind('<Double-1>', self.set_unalloted_sub)
        self.unalloted_sub = get_unallotted_sub()
        self.create_widgets()

    def create_widgets(self):
        self.options = []
        for fac in scheduler6.fac_list:
            self.options.append(fac.getFName())
        self.fac_dropdown_list['values'] = self.options
        self.fac_list_label.grid(row=0, column=0, sticky='w')
        self.fac_dropdown_list.grid(row=0, column=1, sticky='w')
        self.fac_load_table.heading('Section', text='Section')
        self.fac_load_table.heading('Subject', text='Subject')
        self.fac_load_table.heading('Theory', text='Theory')
        self.fac_load_table.heading('Laboratory', text='Laboratory')
        self.fac_load_table.column('Section', anchor='center', width=160)
        self.fac_load_table.column('Subject', anchor='center', width=160)
        self.fac_load_table.column('Theory', anchor='center', width=160)
        self.fac_load_table.column('Laboratory', anchor='center', width=160)
        self.fac_dropdown_list.bind('<<ComboboxSelected>>', self.dropdown_selection)

        self.unallotted_sub_table.heading('Section', text='Section')
        self.unallotted_sub_table.heading('Subject', text='Subject')
        self.unallotted_sub_table.column('Subject', anchor='center', width=100)
        self.unallotted_sub_table.column('Section', anchor='center', width=100)

        self.unallotted_sub_table.delete(*self.unallotted_sub_table.get_children())
        for i in range(len(self.unalloted_sub)):
            self.unallotted_sub_table.insert(parent='', index=i,
                                             values=(self.unalloted_sub[i][0], self.unalloted_sub[i][1]))

        self.fac_load_table.grid(row=0, column=0, columnspan=3)
        self.unallotted_sub_table.grid(row=0, column=3, padx=20)

    def dropdown_selection(self, _):
        self.fac_load_table_frame.grid(row=1, column=0, columnspan=20, pady=100, sticky='w')
        self.fac_load_table.delete(*self.fac_load_table.get_children())
        for fac in scheduler7.faculty:
            if fac.getFName() == self.fac_dropdown_list.get():
                c = 0
                load = fac.getFLoad()
                # for i in load:
                #     print(i)
                for section, info in load.items():
                    for j in info:
                        self.fac_load_table.insert(parent='', index=c, values=(section, j[0], j[2], j[3]))
                        c = c + 1
                break
        tk.Label(self.fac_load_table_frame, height=4).grid(row=1, column=0)

        self.lbl_sub_combo = tk.Label(self.fac_load_table_frame, text='Select Subject', width=20, anchor='w', padx=2,
                                      pady=2)
        self.lbl_sec_combo = tk.Label(self.fac_load_table_frame, text='Select Section', width=20, anchor='w', padx=2,
                                      pady=2)
        # self.select_sec_combo = ttk.Combobox(self.fac_load_table_frame, state='readonly',
        #                                      values=scheduler6.section_list, width=30)
        self.sec_list = list(get_sections_and_mentors(1).keys())
        # print(self.sec_list)
        self.select_sec_combo = ttk.Combobox(self.fac_load_table_frame, state='readonly', width=30)
        self.lbl_theory = tk.Label(self.fac_load_table_frame, text='Enter Theory Lectures', width=20, anchor='w',
                                   padx=2, pady=2)
        self.lbl_lab = tk.Label(self.fac_load_table_frame, text='Enter Labs', width=20, anchor='w', padx=2, pady=2)
        self.select_sub_combo = ttk.Combobox(self.fac_load_table_frame, state='readonly',
                                             values=list(get_sub_names().keys()), width=30)
        self.select_sub_combo.bind('<<ComboboxSelected>>', self.sub_select)
        self.theory_entry = tk.Entry(self.fac_load_table_frame, width=33)
        self.lab_entry = tk.Entry(self.fac_load_table_frame, width=33)

        self.load_insert_btn = tk.Button(self.fac_load_table_frame, text='Insert Load', width=20,
                                         command=self.load_insert, pady=3,
                                         padx=3)
        self.load_clear_btn = tk.Button(self.fac_load_table_frame, text='Clear', width=20,
                                        command=self.clear_load_entry, padx=3,
                                        pady=3)
        self.load_delete_btn = tk.Button(self.fac_load_table_frame, text='Delete', width=20, command=self.delete_load,
                                         padx=3, pady=3)

        self.lbl_sub_combo.grid(row=2, column=0, sticky='w')
        self.select_sub_combo.grid(row=2, column=1)
        self.lbl_sec_combo.grid(row=3, column=0, sticky='w')
        self.select_sec_combo.grid(row=3, column=1)
        self.lbl_theory.grid(row=4, column=0, sticky='w')
        self.theory_entry.grid(row=4, column=1)
        self.lbl_lab.grid(row=5, column=0, sticky='w')
        self.lab_entry.grid(row=5, column=1)
        self.load_insert_btn.grid(row=6, column=0)
        self.load_clear_btn.grid(row=6, column=1)
        self.load_delete_btn.grid(row=7, column=0, columnspan=2)

    def sub_select(self, _):
        sub = self.select_sub_combo.get()
        # print(sub)
        if 'CS3' in sub:
            self.select_sec_combo.delete(0, END)
            sub_list = []
            for s in self.sec_list:
                if 'CS' in s and '3' in s:
                    sub_list.append(s)
            # print(sub_list)
            self.select_sec_combo.config(values=sub_list)
        elif 'CS5' in sub:
            self.select_sec_combo.delete(0, END)
            sub_list = []
            for s in self.sec_list:
                if 'CS' in s and '5' in s:
                    sub_list.append(s)
            self.select_sec_combo.config(values=sub_list)
        elif 'CY3' in sub:
            self.select_sec_combo.delete(0, END)
            sub_list = []
            for s in self.sec_list:
                if 'CY' in s and '3' in s:
                    sub_list.append(s)
            self.select_sec_combo.config(values=sub_list)
        elif 'CY5' in sub:
            self.select_sec_combo.delete(0, END)
            sub_list = []
            for s in self.sec_list:
                if 'CY' in s and '5' in s:
                    sub_list.append(s)
            self.select_sec_combo.config(values=sub_list)
        elif 'AL3' in sub:
            self.select_sec_combo.delete(0, END)
            sub_list = []
            for s in self.sec_list:
                if 'AIML' in s and '3' in s:
                    sub_list.append(s)
            # print(sub_list)
            self.select_sec_combo.config(values=sub_list)
        elif 'AL5' in sub:
            self.select_sec_combo.delete(0, END)
            sub_list = []
            for s in self.sec_list:
                if 'AIML' in s and '5' in s:
                    sub_list.append(s)
            # print(sub_list)
            self.select_sec_combo.config(values=sub_list)

    def set_unalloted_sub(self, _):
        self.theory_entry.delete(0, END)
        self.lab_entry.delete(0, END)
        id = self.unallotted_sub_table.selection()
        l = self.unallotted_sub_table.item(id)['values']
        self.select_sub_combo.set(l[0])
        if 'CS3' in l[0]:
            self.select_sec_combo.set('CSE 3' + l[1])
        elif 'AL3' in l[0]:
            self.select_sec_combo.set('AIML 3' + l[1])
        elif 'CY3' in l[0]:
            self.select_sec_combo.set('CY 3' + l[1])
        elif 'CS5' in l[0]:
            self.select_sec_combo.set('CSE 5' + l[1])
        elif 'AL5' in l[0]:
            self.select_sec_combo.set('AIML 5' + l[1])
        elif 'CY5' in l[0]:
            self.select_sec_combo.set('CY 5' + l[1])

    def set_load_entry(self, _):
        self.theory_entry.delete(0, END)
        self.lab_entry.delete(0, END)
        id = self.fac_load_table.selection()
        l = self.fac_load_table.item(id)['values']
        if len(l) == 0:
            return
        self.select_sub_combo.set(l[1])
        self.select_sec_combo.set(l[0])
        self.theory_entry.insert(0, l[2])
        self.lab_entry.insert(0, l[3])

    def load_insert(self):
        sec = self.select_sec_combo.get()
        sub = self.select_sub_combo.get()
        th = self.theory_entry.get()
        lab = self.lab_entry.get()
        if len(sec) == 0 or len(sub) == 0 or len(th) == 0 or len(lab) == 0:
            return
        fac_name = self.fac_dropdown_list.get()
        for fac in scheduler6.fac_list:
            if fac.getFName() == fac_name:
                f_id = fac.getFId()
                fac.setFLoad(sec, [sub, sec[-1], th, lab])
                if fac in scheduler6.av_fac:
                    pass
                else:
                    scheduler6.av_fac.append(fac)

        self.fac_load_table.insert(parent='', index=END, values=(sec, sub, th, lab))
        add_fac_load(f_id, sub, sec[-1], th, lab)

    def clear_load_entry(self):
        self.select_sub_combo.set('')
        self.select_sec_combo.set('')
        self.theory_entry.delete(0, END)
        self.lab_entry.delete(0, END)

    def delete_load(self):
        f_name = self.fac_dropdown_list.get()
        id = self.fac_load_table.selection()

        sub = self.select_sub_combo.get()
        sec = self.select_sec_combo.get()
        # print(sec)
        th = self.theory_entry.get()
        lab = self.lab_entry.get()
        if len(sub) == 0 or len(sec) == 0 or len(th) == 0 or len(lab) == 0:
            return
        # f_id=''
        self.fac_load_table.delete(id)

        for fac in scheduler6.fac_list:
            if fac.getFName() == f_name:
                f_id = fac.getFId()
                load = fac.getFLoad()[sec]
                for i in load:
                    if i[0] == sub:
                        load.remove(i)
                break

        delete_fac_load(f_id, sub, sec[-1], th, lab)

    def show(self):
        root.current_frame.grid_forget()
        root.current_frame = self
        self.grid_propagate(False)
        self.grid(row=0, column=1)


class SubjectFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__()
        parent.current_frame.grid_forget()
        parent.current_frame = self
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.pack_propagate(False)
        self.sub_names = get_sub_names()
        self.sub_table = ttk.Treeview(self, columns=('Subject Code', 'Subject Name', 'Subject Type'), show='headings',
                                      height=8)
        self.sub_table.bind('<Double-1>', self.subject_item_select)
        self.create_widgets()

    def create_widgets(self):
        self.entry_frame = tk.LabelFrame(self, text='Edit Information', height=rooth / 2, width=int(rootw * 0.75),
                                         pady=10, padx=10)
        self.entry_frame.grid_propagate(False)
        self.lbl_sub_code = tk.Label(self.entry_frame, text='Enter Subject Code', height=1, width=20, anchor='w',
                                     font=(None, 10))
        self.entry_sub_code = tk.Entry(self.entry_frame, width=50, font=(None, 10))
        self.lbl_sub_name = tk.Label(self.entry_frame, text='Enter Subject Name', anchor='w', height=1, width=20,
                                     font=(None, 10))
        self.entry_sub_name = tk.Entry(self.entry_frame, width=50, font=(None, 10))
        self.lbl_sub_type = tk.Label(self.entry_frame, text='Select Subject Type', anchor='w', height=1, width=20,
                                     font=(None, 10))
        self.combo_sub_type = ttk.Combobox(self.entry_frame, values=('B', 'L', 'T'), state='readonly', width=55)

        self.sub_insert_btn = tk.Button(self.entry_frame, width=30, text='INSERT', command=self.insert_sub, padx=6)
        self.sub_update_btn = tk.Button(self.entry_frame, width=30, text='UPDATE', command=self.update_sub, padx=6)
        self.sub_delete_btn = tk.Button(self.entry_frame, text='DELETE', width=31, command=self.delete_subject)
        self.sub_entry_clear_btn = tk.Button(self.entry_frame, text='CLEAR', width=31, command=self.clear_entry_1)

        self.sub_table.heading('Subject Code', text='Subject Code')
        self.sub_table.heading('Subject Name', text='Subject Name')
        self.sub_table.heading('Subject Type', text='Subject Type')
        self.sub_table.column('Subject Code', width=170, anchor='center')
        self.sub_table.column('Subject Name', width=360, anchor='w')
        self.sub_table.column('Subject Type', width=170, anchor='center')
        self.sub_table.pack(fill='both')
        self.entry_frame.pack()

        self.sub_table.delete(*self.sub_table.get_children())

        c = 0
        for i, j in self.sub_names.items():
            self.sub_table.insert(parent='', index=c, values=(i, j[0], j[1]))
            c = c + 1

        self.lbl_sub_code.grid(row=0, column=0, pady=3, padx=5, sticky='w')
        self.entry_sub_code.grid(row=0, column=1, pady=3, padx=5, sticky='w')
        self.lbl_sub_name.grid(row=1, column=0, pady=3, padx=5, sticky='w')
        self.entry_sub_name.grid(row=1, column=1, pady=3, padx=5, sticky='w')
        self.lbl_sub_type.grid(row=2, column=0, pady=3, padx=5, sticky='w')
        self.combo_sub_type.grid(row=2, column=1, pady=3, padx=5, sticky='w')

        self.sub_insert_btn.grid(row=3, column=0, pady=4, sticky='w', padx=6)
        self.sub_update_btn.grid(row=3, column=1, pady=4, sticky='w', padx=6)
        self.sub_delete_btn.grid(row=4, column=0, padx=6, sticky='w', pady=4)
        self.sub_entry_clear_btn.grid(row=4, column=1, sticky='w', pady=4, padx=6)

    def insert_sub(self):
        sub_code = self.entry_sub_code.get()
        sub_name = self.entry_sub_name.get()
        sub_type = self.combo_sub_type.get()

        if len(sub_code) == 0:
            return

        add_subject(sub_code, sub_name, sub_type)
        self.sub_names[sub_code] = [sub_name, sub_type]

        index = len(self.sub_names) - 1
        self.sub_table.insert(parent='', index=index, values=[sub_code, sub_name, sub_type])

    def update_sub(self):
        if len(self.entry_sub_code.get()) == 0:
            return

        sub_code = self.entry_sub_code.get()
        sub_name = self.entry_sub_name.get()
        sub_type = self.combo_sub_type.get()

        update_subject(sub_code, sub_name, sub_type)

        c = 0
        for i in self.sub_table.selection():
            if self.sub_table.item(i)['values'][0] == sub_code:
                c = c + 1
                self.sub_table.delete(i)
                self.sub_table.insert(parent='', index=c, values=(sub_code, sub_name, sub_type))

    def delete_subject(self):
        if len(self.entry_sub_code.get()) == 0:
            return

        sub_code = self.entry_sub_code.get()
        sub_name = self.entry_sub_name.get()
        sub_type = self.combo_sub_type.get()

        delete_sub(sub_code)
        for i in self.sub_table.selection():
            if self.sub_table.item(i)['values'][0] == sub_code:
                self.sub_table.delete(i)

    def clear_entry_1(self):
        self.entry_sub_code.delete(0, END)
        self.entry_sub_name.delete(0, END)
        self.combo_sub_type.set('')

    def subject_item_select(self, _):
        self.entry_sub_name.delete(0, END)
        self.entry_sub_code.delete(0, END)
        for i in self.sub_table.selection():
            l = list(self.sub_table.item(i)['values'])
            self.entry_sub_code.insert(END, l[0])
            self.entry_sub_name.insert(END, l[1])
            self.combo_sub_type.set(l[2])

    def show(self):
        root.current_frame.grid_forget()
        root.current_frame = self
        self.pack_propagate(False)
        self.grid(row=0, column=1)


class LabAllotmentFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__(parent)
        parent.current_frame.grid_forget()
        parent.current_frame = self
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.grid_propagate(False)
        self.grid_columnconfigure(5)
        self.tbl_frame = tk.LabelFrame(self, text='Lab Information', height=int(rooth * 0.7), width=int(rootw * 0.72),
                                       padx=20, pady=20)
        self.tbl_frame.grid_propagate(False)
        self.labAllotTable = ttk.Treeview(self.tbl_frame, columns=('Subject', 'Laboratory', 'Faculty'), show='headings',
                                          height=6)
        self.labAvail = ttk.Treeview(self.tbl_frame, columns=('Laboratory', 'Available Slots'), show='headings',
                                     height=6)
        self.labAvail.bind('<Double-1>', self.lab_entry)

        self.create_widgets()

    def create_widgets(self):
        self.lbl_select_section = tk.Label(self, text='Select Section', height=2, width=20, anchor='w', font=(None, 10))
        self.combo_section = ttk.Combobox(self, state='readonly', width=40,
                                          values=list(get_sections_and_mentors(2).keys()))
        self.combo_section.bind('<<ComboboxSelected>>', self.combo_selected)

        self.labAllotTable.heading('Subject', text='Subject')
        self.labAllotTable.heading('Laboratory', text='Laboratory')
        self.labAllotTable.heading('Faculty', text='Faculty')

        self.labAllotTable.column('Subject', anchor='center', width=100, stretch=NO)
        self.labAllotTable.column('Laboratory', anchor='center', width=200, stretch=NO)
        self.labAllotTable.column('Faculty', anchor='center', width=200, stretch=NO)

        self.labAvail.heading('Laboratory', text='Laboratory')
        self.labAvail.heading('Available Slots', text='Available Slots')

        self.labAvail.column('Available Slots', anchor='center', width=100)
        self.labAvail.column('Laboratory', anchor='center', width=200)

        self.lbl_select_section.grid(row=0, column=0)
        self.combo_section.grid(row=0, column=1)

        self.lbl_select_subject = tk.Label(self.tbl_frame, text='Select Subject', height=2, width=20, anchor='w',
                                           font=(None, 10))
        self.combo_select_subject = ttk.Combobox(self.tbl_frame, state='readonly', width=48)
        self.lbl_select_lab = tk.Label(self.tbl_frame, text='Enter Lab', height=2, width=20, anchor='w',
                                       font=(None, 10))
        self.entry_lab = tk.Entry(self.tbl_frame, width=51)

        self.insert_btn = tk.Button(self.tbl_frame, text='INSERT', command=self.insert_lab)

    def combo_selected(self, _):
        self.combo_select_subject.config(values=[])
        self.combo_select_subject.config(values=get_sub_names_by_section(self.combo_section.get()))
        sec = self.combo_section.get()
        fac_dict = get_fac_dict()
        labs = get_labs_by_sec(sec)
        self.labAllotTable.delete(*self.labAllotTable.get_children())
        for i, j in labs.items():
            f = fac_dict[j[1]].getFName()
            self.labAllotTable.insert(parent='', index=END, values=(i, j[0], f))
        c = 0
        self.labAvail.delete(*self.labAvail.get_children())
        for i, j in get_labs().items():
            self.labAvail.insert(parent='', index=c, values=(i, j))
            c = c + 1

        self.tbl_frame.grid(row=1, column=0, columnspan=5)
        self.tbl_frame.grid_columnconfigure(5)
        self.labAllotTable.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.labAvail.grid(row=0, column=2, padx=10, pady=10, )
        self.lbl_select_subject.grid(row=1, column=0)
        self.combo_select_subject.grid(row=1, column=1)
        self.lbl_select_lab.grid(row=2, column=0)
        self.entry_lab.grid(row=2, column=1)
        self.insert_btn.grid(row=3, column=0)

    def lab_entry(self, _):
        self.entry_lab.delete(0, END)
        for i in self.labAvail.selection():
            self.entry_lab.insert(END, self.labAvail.item(i)['values'][0])
            break

    def insert_lab(self):
        global f_id
        sec = self.combo_section.get()
        sub = self.combo_select_subject.get()
        lab = self.entry_lab.get()
        faculty = ''
        for fac in scheduler7.faculty:
            if sec in fac.getFLoad().keys():
                load = fac.getFLoad()[sec]

            else:
                continue
            for i in load:
                if i[0] == sub:
                    f_id = fac.getFId()
                    faculty = fac.getFName()
                    break
        insert_lab(sub, lab, f_id, sec[-1])
        self.labAllotTable.insert(parent='', index=END, values=(sub, lab, faculty))

    def show(self):
        root.current_frame.grid_forget()
        root.current_frame = self
        self.grid_propagate(False)
        self.grid(row=0, column=1)


class PresetFrame(tk.Frame):
    def __init__(self, parent, w, h):
        super().__init__()
        parent.current_frame.grid_forget()
        parent.current_frame = self
        self.config(width=w, height=h, border=1, relief='solid', pady=40, padx=20)
        self.grid_propagate(False)
        self.columnconfigure(3)
        self.presetTable = ttk.Treeview(self, columns=('', '10:30-11:20', '11:20-12:10', '12:10-01:00', '01:00-:01:50',
                                                       '01:50-02:40', '02:40-03:30', '03:30-04:15', '04:15-05:00'),
                                        show='headings', height=6)
        self.presetTable.bind('<ButtonRelease-1>', self.selectItem)
        self.s = ttk.Style()
        self.s.configure('Treeview', rowheight=40, borderwidth=5)
        self.day_dict = {}
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for i in range(len(self.days)):
            self.day_dict[self.days[i]] = i
        self.create_widgets()

    def create_widgets(self):
        self.grid_propagate(False)
        self.tt_type_select_lbl = tk.Label(self, text='Select Timetable Type', height=2, width=20, anchor='w',
                                           font=(None, 10))
        self.tt_entity_select = tk.Label(self, text='Select Entity', height=2, width=20, anchor='w', font=(None, 10))

        self.tt_type_select_combo = ttk.Combobox(self, state='readonly', values=['Faculty', 'Labs', 'Sections'],
                                                 width=40)
        self.tt_type_select_combo.bind('<<ComboboxSelected>>', self.combo_selected)

        self.tt_entity_select_combo = ttk.Combobox(self, state='readonly', width=40)
        self.tt_entity_select_combo.bind('<<ComboboxSelected>>', self.show_tt)

        self.entry_box_lbl = tk.Label(self, text='Entry Box', height=2, width=20, anchor='w', font=(None, 10))
        self.entry_box_entry = tk.Entry(self, width=50, font=(None, 10))

        self.btn_insert = tk.Button(self, text='INSERT', command=self.insert_data, width=40)
        self.btn_clear = tk.Button(self, text='CLEAR', command=self.clear_entry, width=40)

        self.tt_type_select_lbl.grid(row=0, column=0, sticky='w')
        self.tt_type_select_combo.grid(row=0, column=1, sticky='w')

        self.tt_entity_select.grid(row=1, column=0, sticky='w')
        self.tt_entity_select_combo.grid(row=1, column=1, sticky='w')

    def combo_selected(self, _):
        self.tt_entity_select_combo.delete(0, END)
        self.tt_entity_select_combo.config(values=list(scheduler6.all_tt[self.tt_type_select_combo.get()].keys()))

    def show_tt(self, _):
        self.presetTable.heading('', text='')
        self.presetTable.heading('10:30-11:20', text='10:30-11:20')
        self.presetTable.heading('11:20-12:10', text='11:20-12:10')
        self.presetTable.heading('12:10-01:00', text='12:10-01:00')
        self.presetTable.heading('01:00-:01:50', text='01:00-:01:50')
        self.presetTable.heading('01:50-02:40', text='01:50-02:40')
        self.presetTable.heading('02:40-03:30', text='02:40-03:30')
        self.presetTable.heading('03:30-04:15', text='03:30-04:15')
        self.presetTable.heading('04:15-05:00', text='04:15-05:00')

        self.presetTable.column('', anchor='center', width=80, stretch=NO)
        self.presetTable.column('10:30-11:20', anchor='center', width=100, stretch=NO)
        self.presetTable.column('11:20-12:10', anchor='center', width=100, stretch=NO)
        self.presetTable.column('12:10-01:00', anchor='center', width=100, stretch=NO)
        self.presetTable.column('01:00-:01:50', anchor='center', width=100, stretch=NO)
        self.presetTable.column('01:50-02:40', anchor='center', width=100, stretch=NO)
        self.presetTable.column('02:40-03:30', anchor='center', width=100, stretch=NO)
        self.presetTable.column('03:30-04:15', anchor='center', width=100, stretch=NO)
        self.presetTable.column('04:15-05:00', anchor='center', width=100, stretch=NO)

        self.presetTable.grid(row=3, column=0, columnspan=20, pady=80, sticky='w')

        self.entry_box_lbl.grid(row=4, column=0, )
        self.entry_box_entry.grid(row=4, column=1)

        self.btn_insert.grid(row=5, column=0, pady=10)
        self.btn_clear.grid(row=5, column=1, pady=10)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        tt = scheduler6.all_tt[self.tt_type_select_combo.get()][self.tt_entity_select_combo.get()]
        self.presetTable.delete(*self.presetTable.get_children())
        for i in range(len(tt)):
            self.presetTable.insert(parent='', index=i,
                                    values=(days[i], tt[i][0], tt[i][1], tt[i][2], tt[i][3], tt[i][4], tt[i][5],
                                            tt[i][6], tt[i][7]))

    def insert_data(self):
        global tt_row, tt_col
        scheduler6.all_tt[self.tt_type_select_combo.get()][self.tt_entity_select_combo.get()][tt_row][tt_col] = \
            self.entry_box_entry.get()
        self.presetTable.delete(*self.presetTable.get_children())
        tt = scheduler6.all_tt[self.tt_type_select_combo.get()][self.tt_entity_select_combo.get()]
        scheduler6.all_presets[self.tt_type_select_combo.get()].append(
            [tt_row, tt_col, self.tt_entity_select_combo.get(),
             self.entry_box_entry.get()])
        days = self.days
        for i in range(len(tt)):
            self.presetTable.insert(parent='', index=i,
                                    values=(days[i], tt[i][0], tt[i][1], tt[i][2], tt[i][3], tt[i][4], tt[i][5],
                                            tt[i][6], tt[i][7]))

    def clear_entry(self):
        self.entry_box_entry.delete(0, END)

    def selectItem(self, _):
        global tt_row, tt_col
        self.entry_box_entry.delete(0, END)
        curr = self.presetTable.item(self.presetTable.focus())
        col = self.presetTable.identify_column(_.x)
        if col == '#2':
            self.entry_box_entry.insert(END, curr['values'][1])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2
        elif col == '#3':
            self.entry_box_entry.insert(END, curr['values'][2])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2
        elif col == '#4':
            self.entry_box_entry.insert(END, curr['values'][3])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2
        elif col == '#5':
            self.entry_box_entry.insert(END, curr['values'][4])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2
        elif col == '#7':
            self.entry_box_entry.insert(END, curr['values'][6])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2
        elif col == '#8':
            self.entry_box_entry.insert(END, curr['values'][7])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2
        elif col == '#9':
            self.entry_box_entry.insert(END, curr['values'][8])
            tt_row = self.day_dict[curr['values'][0]]
            tt_col = int(str(col)[-1]) - 2

    def show(self):
        root.current_frame.grid_forget()
        root.current_frame = self
        self.grid_propagate(False)
        self.grid(row=0, column=1)


root = App('SchedulXpert', rootw, rooth, xco, yco)
root.display()
