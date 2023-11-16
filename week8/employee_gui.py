import csv
from tkinter import filedialog
from employee import Employee
from tkinter import *
from tkinter import messagebox as msb

class EmployeeGUI:
    def __init__(self):
        self.__employees = []
        ## Create the main window
        self.__window = Tk()
        self.__window.title('Employee Management Program')
        self.__window.geometry('500x300')

        self.__create_widgets()

    def run(self):
        ## Start the main loop
        self.__window.mainloop()
    
    def __create_widgets(self):
        # create employee label
        self.__lbl_employee = Label(self.__window, text='Employee:')
        self.__lbl_employee.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=5)
        # create employee listbox
        self.__lst_employee = Listbox(self.__window, width=20)
        self.__lst_employee.grid(row=1, column=0, columnspan=2, rowspan=5, padx=10, pady=5)
        self.__lst_employee.bind('<<ListboxSelect>>', self.__on_select)

        # create name label & entry
        self.__lbl_name = Label(self.__window, text='Name:')
        self.__lbl_name.grid(row=1, column=2, sticky=W, padx=10, pady=5)
        self.__txt_name = Entry(self.__window, width=20)
        self.__txt_name.grid(row=1, column=3, columnspan=3, padx=10, pady=5)

        # create salary label & entry
        self.__lbl_salary = Label(self.__window, text='Salary:')
        self.__lbl_salary.grid(row=2, column=2, sticky=W, padx=10, pady=5)
        self.__txt_salary = Entry(self.__window, width=20)
        self.__txt_salary.grid(row=2, column=3, columnspan=3, padx=10, pady=5)

        # create age label & entry
        self.__lbl_age = Label(self.__window, text='Age:')
        self.__lbl_age.grid(row=3, column=2, sticky=W, padx=10, pady=5)
        self.__txt_age = Entry(self.__window, width=20)
        self.__txt_age.grid(row=3, column=3, columnspan=3, padx=10, pady=5)

        # create buttons
        self.__btn_load = Button(self.__window, text='Load', width=5, command=self.__load)
        self.__btn_load.grid(row=6, column=0, padx=10, pady=5)
        self.__btn_save = Button(self.__window, text='Save', width=5)
        self.__btn_save.grid(row=6, column=1, padx=10, pady=5)
        self.__btn_add = Button(self.__window, text='Add', width=2, command=self.__add)
        self.__btn_add.grid(row=6, column=3, padx=10, pady=5)
        self.__btn_edit = Button(self.__window, text='Edit', width=2)
        self.__btn_edit.grid(row=6, column=4, padx=10, pady=5)
        self.__btn_delete = Button(self.__window, text='Del', width=2)
        self.__btn_delete.grid(row=6, column=5, padx=10, pady=5)

    def __load(self):
        # clean old data
        self.__employees.clear()
        self.__lst_employee.delete(0, END)
        # open file dialog to load new data
        file_name = filedialog.askopenfilename(title='Select a file', 
                                filetypes=(('CSV files', '*.csv'), ('All files', '*.*')))
        f = open(file_name, 'r', encoding='utf-8')
        reader = csv.reader(f)
        next(reader) # skip the header
        for row in reader:
            e = Employee(row[0], row[1], row[2])    # create an employee object from row data
            self.__employees.append(e)              # add employee to the list
            self.__lst_employee.insert(END, e.name) # add employee name to the listbox

    def __on_select(self, event):
        # get the selected employee
        index = self.__lst_employee.curselection()[0]   # get selected index
        e = self.__employees[index]                     # get employee object at index
        # set the values to the entries
        self.__txt_name.delete(0, END)          # clear old text
        self.__txt_name.insert(END, e.name)     # insert name to the entry
        self.__txt_salary.delete(0, END)
        self.__txt_salary.insert(END, str(e.salary))
        self.__txt_age.delete(0, END)
        self.__txt_age.insert(END, str(e.age))
    
    def __add(self):
        # get text from entries
        name = self.__txt_name.get()
        salary = self.__txt_salary.get()
        age = self.__txt_age.get()
        # create employee object
        try:
            e = Employee(name, salary, age)
            # add employee to the list
            self.__employees.append(e)
            # add employee name to the listbox
            self.__lst_employee.insert(END, e.name)
        except ValueError as err:
            msb.showerror('Error', str(err))
# Run program
program = EmployeeGUI()
program.run()