from cProfile import label#вывод статического текста
from tkinter import *
from tkinter import ttk#импорт ткинтер для создания графического приложения
from tkinter.ttk import Combobox #для создание всплывающих окон
from tkinter.ttk import Radiobutton#для создания кнопок
from tkinter import messagebox#для создания окон
from select import select
from tkinter import filedialog

#сoздаем окно
appli=Tk()
#указываем название окна
appli.title('Горбунов Алексей Алексеевич')
appli.geometry('300x180')
tab_control=ttk.Notebook(appli)  # Создаем виджет закладок
tab1=ttk.Frame(tab_control) # фрейм1
tab2=ttk.Frame(tab_control) # фрейм2
tab3=ttk.Frame(tab_control) # фрейм3
#создаем виджеты с названиями
tab_control.add(tab1,text='Первая')
tab_control.add(tab2,text='Вторая')
tab_control.add(tab3,text='Третья')
#tab1 создаем расчет
def calculate():
    try:
        num1 = float(txt1.get())# Получаем значение из первого окна.
        num2 = float(txt2.get())#получаем значение из второго окна
        operation = combo.get()# Получаем выбранную операцию из выпадающего списка.

        if operation == '+':# Проверяем, какая операция была выбрана.
            result = num1 + num2#проводим операцию при задоном знаке
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Деление на ноль!"
            else:
                result = num1 / num2
        else:
            result = "Ошибка операции!"


        result_label.config(text=f"Результат: {result}")# Обновляем метку результата вычисленным результатом.

    except ValueError:  # Обрабатываем исключение возникающие при не числовом ввод.
        result_label.config(text="Ошибка! Введите числа.")

#добавляем виджеты
combo=Combobox(tab1)#создание выпадающего списка
combo['values']=('+','-','*','/')
combo.current=('+')#статичный знак
combo.grid(column=0,row=0,)
combo.place(relx=0.45,rely=0.1,anchor="c", relwidth=0.13, relheight=0.1)#размеры ,расположение
tab_control.pack(expand=1,fill='both')
def clicked():
    lbl.configure(text='=')
txt1=ttk.Entry(tab1,width=10)#поле ввода
txt1.grid(column=4,row=0)#размеры кнопки
txt1.place(relx=0.27,rely=0.1,anchor="c", relwidth=0.2, relheight=0.1)#расположение
txt2=ttk.Entry(tab1,width=10)#2
txt2.grid(column=1,row=0)#2
txt2.place(relx=0.65,rely=0.1,anchor="c", relwidth=0.2, relheight=0.1)#2
calculate_button = ttk.Button(tab1, text="=", command=calculate)#отображение результата
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)#размер
calculate_button.place(relx=0.8,rely=0.1,anchor="c", relwidth=0.1, relheight=0.1)#положение
result_label = ttk.Label(tab1, text="=")#кнопка вычисления
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
result_label.place(relx=0.4,rely=0.6,anchor="c", relwidth=0.6, relheight=0.6)
#tab2 создаем функцию для вывода выбранного чекбокса
def checkbox_button_clicked():#функция для обработки выбора чикбокса
    selected_options = []#создаем массив для хранения заданных опций
    if select1.get():#проверяем выбран ли первый чикбокс
        selected_options.append("Первый")#выводим если выбран
    if select2.get():
        selected_options.append("Второй")
    if select3.get():
        selected_options.append("Третий")
#отсутствие выбора

    if not selected_options:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали.")#выводим если небыло выбора
    else:
        message = "Вы выбрали: " + ", ".join(selected_options)#для обЪединение Слова с выбранной опцией
        messagebox.showinfo("Выбор", message)#ввывод
select1 = IntVar()#для зранения состояния 1 чикбокса
select2 = IntVar()#2
select3 = IntVar()#3

rad1 = Checkbutton(tab2, text="Первый", variable=select1)#создаем 1 чикбокс
rad1.pack(pady=5)#размещение
rad2 = Checkbutton(tab2, text="Второй", variable=select2)#2
rad2.pack(pady=5)#2
rad3 = Checkbutton(tab2, text="Третий", variable=select3)#3
rad3.pack(pady=5)#3

btn= Button(tab2, text="Показать выбор", command=checkbox_button_clicked)#создание кнопки
btn.pack(pady=10)
#третий виджет текстовой редактор

text=Text(tab3,width=50,height=10,bg="white",fg="#B22222",wrap=WORD) #сщздаем поле для текста ,задаем параметры
text.pack()#упорядочить виджеты
def open_file():#функция для обработки открытия файла
    filepath = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=[("Text Files", "txt"), ("All Files")]
    )# Открываем окно для выбора файла выбрать файл.
    if filepath:#проверяем был ли выбран файл
        try:
            with open(filepath) :# Открываем файл в режиме чтения .
                text = f.read()#читаем содержимое
                text.delete("1.0", END)#очищаем существующий текст
                text.insert(tk.END, text)#вставляем текст из редактора
        except Exception as e:
            messagebox.showerror("Ошибка", "Не удалось открыть файл: ")#ВЫВОДИМ СООБЩЕНИЕ О ОШИБКЕ
menubar = Menu(tab3)#созд меню
filemenu = Menu(menubar, tearoff=0)#отдел файл
filemenu.add_command(label="Открыть", command=open_file)#команда открыть
menubar.add_cascade(label="Файл", menu=filemenu)#добавляем файл в меню
appli.config(menu=menubar)#настройка главного окна для использования меню
appli.mainloop()

