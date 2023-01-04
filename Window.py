from tkinter import ttk
import tkinter
from tkinter import *

def create_widgets(self):
    # okno glowne
    self.parent.title('Zastosowanie krzywych eliptycznych w kryptografii - Karol Budzyński')
    self.parent.state("zoomed")

    # notatnik
    self.notebook = ttk.Notebook(self.parent)
    self.notebook.pack(expand=True, fill="both")

    # zakladki
    self.tab1 = ttk.Frame(self.notebook)
    self.notebook1 = ttk.Notebook(self.tab1)
    self.notebook1.pack(expand=True, fill="both")
    self.tab1_1 = ttk.Frame(self.notebook1)
    self.tab1_2 = ttk.Frame(self.notebook1)
    self.tab1_3 = ttk.Frame(self.notebook1)

    self.tab2 = ttk.Frame(self.notebook)
    self.notebook2 = ttk.Notebook(self.tab2)
    self.notebook2.pack(expand=True, fill="both")
    self.tab2_1 = ttk.Frame(self.notebook2)
    self.tab2_2 = ttk.Frame(self.notebook2)
    self.tab2_3 = ttk.Frame(self.notebook2)

    self.tab3 = ttk.Frame(self.notebook)
    self.notebook3 = ttk.Notebook(self.tab3)
    self.notebook3.pack(expand=True, fill="both")
    self.tab3_1 = ttk.Frame(self.notebook3)
    self.tab3_2 = ttk.Frame(self.notebook3)

    # dodanie zakladek do notatnika
    self.notebook.add(self.tab1, text='Krzywe eliptyczne nad liczbami rzeczywistymi R')
    self.notebook1.add(self.tab1_1, text='Wykres')
    self.notebook1.add(self.tab1_2, text='Dodawanie punktów')
    self.notebook1.add(self.tab1_3, text='Mnożenie punktów')
    self.notebook.add(self.tab2, text='Krzywe eliptyczne nad ciałami skończonymi F(p)')
    self.notebook2.add(self.tab2_1, text='Wykres')
    self.notebook2.add(self.tab2_2, text='Dodawanie punktów')
    self.notebook2.add(self.tab2_3, text='Mnożenie punktów')
    self.notebook.add(self.tab3, text='Krzywe eliptyczne w kryptografii')
    self.notebook3.add(self.tab3_1, text='ElGamal - Punkty')
    self.notebook3.add(self.tab3_2, text='Podpis cyfrowy ECDSA')

    # ---------------------------------------------------------------------------
    # tab1_1 - Krzywe eliptyczne nad liczbami rzeczywistymi - Wykres
    # ---------------------------------------------------------------------------
    self.par_a_var_tab1_1 = tkinter.StringVar()
    self.par_b_var_tab1_1 = tkinter.StringVar()

    self.label1_tab1_1 = tkinter.Label(self.tab1_1, text='Krzywe eliptyczne nad liczbami rzeczywistymi', font=("Helvetica", 16))
    self.label1_tab1_1.grid(row=0, column=6, columnspan=10, sticky='w')

    self.photo_tab1_1 = tkinter.PhotoImage(file='assets/python.PNG')
    self.photo_label_tab1_1 = tkinter.Label(self.tab1_1, image=self.photo_tab1_1)
    self.photo_label_tab1_1.grid(row=0, column=16, columnspan=10, sticky='w', padx=15)

    self.par_a_label_tab1_1 = tkinter.Label(self.tab1_1, text="Parametr a:")
    self.par_a_label_tab1_1.grid(row=3, column=3, sticky='new', pady=2)

    self.par_b_label_tab1_1 = tkinter.Label(self.tab1_1, text="Parametr b:")
    self.par_b_label_tab1_1.grid(row=4, column=3, sticky='new', pady=2)

    self.button_rysuj_tab1_1 = tkinter.Button(self.tab1_1, text='Rysuj', command=self.fun_tab1_1)
    self.button_rysuj_tab1_1.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab1_1 = tkinter.Entry(self.tab1_1, textvariable=self.par_a_var_tab1_1)
    self.par_a_tab1_1.grid(row=3, column=4, sticky='new', pady=2)

    self.par_b_tab1_1 = tkinter.Entry(self.tab1_1, textvariable=self.par_b_var_tab1_1)
    self.par_b_tab1_1.grid(row=4, column=4, sticky='new', pady=2)

    self.zakr_od_label_tab1_1 = tkinter.Label(self.tab1_1, text="Zakres od:")
    self.zakr_od_label_tab1_1.grid(row=5, column=3, sticky='new', pady=2)

    self.zakr_do_label_tab1_1 = tkinter.Label(self.tab1_1, text="Zakres do:")
    self.zakr_do_label_tab1_1.grid(row=6, column=3, sticky='new', pady=2)

    self.slider_1_tab1_1 = Scale(self.tab1_1, from_=-100, to=-1, orient=HORIZONTAL)
    self.slider_1_tab1_1.set(-5)
    self.slider_1_tab1_1.grid(row=5, column=4, sticky='n', pady=2)

    self.slider_2_tab1_1 = Scale(self.tab1_1, from_=1, to=100, orient=HORIZONTAL)
    self.slider_2_tab1_1.set(5)
    self.slider_2_tab1_1.grid(row=6, column=4, sticky='n', pady=2)

    # ---------------------------------------------------------------------------
    # tab1_2 - Krzywe eliptyczne nad liczbami rzeczywistymi - Dodawanie punktów
    # ---------------------------------------------------------------------------
    self.par_a_var_tab1_2 = tkinter.StringVar()
    self.par_b_var_tab1_2 = tkinter.StringVar()
    self.P_x_var_tab1_2 = tkinter.StringVar()
    self.P_y_var_tab1_2 = tkinter.StringVar()
    self.Q_x_var_tab1_2 = tkinter.StringVar()
    self.Q_y_var_tab1_2 = tkinter.StringVar()
    self.R_x_var_tab1_2 = tkinter.StringVar()
    self.R_y_var_tab1_2 = tkinter.StringVar()

    self.label1_tab1_2 = tkinter.Label(self.tab1_2, text='Dodawanie punktów na krzywej eliptycznej', font=("Helvetica", 16))
    self.label1_tab1_2.grid(row=0, column=6, columnspan=10, sticky='w')

    self.photo_tab1_2 = tkinter.PhotoImage(file='assets/python.PNG')
    self.photo_label_tab1_2 = tkinter.Label(self.tab1_2, image=self.photo_tab1_2)
    self.photo_label_tab1_2.grid(row=0, column=16, columnspan=10, sticky='w', padx=15)

    self.par_a_label_tab1_2 = tkinter.Label(self.tab1_2, text="Parametr a:")
    self.par_a_label_tab1_2.grid(row=4, column=3, sticky='new', pady=2)

    self.par_b_label_tab1_2 = tkinter.Label(self.tab1_2, text="Parametr b:")
    self.par_b_label_tab1_2.grid(row=5, column=3, sticky='new', pady=2)

    self.button_oblicz_tab1_2 = tkinter.Button(self.tab1_2, text='Oblicz', command=self.fun_tab1_2)
    self.button_oblicz_tab1_2.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.par_a_var_tab1_2)
    self.par_a_tab1_2.grid(row=4, column=4, sticky='new', pady=2)

    self.par_b_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.par_b_var_tab1_2)
    self.par_b_tab1_2.grid(row=5, column=4, sticky='new', pady=2)

    self.zakr_od_label_tab1_2 = tkinter.Label(self.tab1_2, text="Zakres od:")
    self.zakr_od_label_tab1_2.grid(row=6, column=3, sticky='new', pady=2)

    self.zakr_do_label_tab1_2 = tkinter.Label(self.tab1_2, text="Zakres do:")
    self.zakr_do_label_tab1_2.grid(row=7, column=3, sticky='new', pady=2)

    self.slider_1_tab1_2 = Scale(self.tab1_2, from_=-100, to=-1, orient=HORIZONTAL)
    self.slider_1_tab1_2.set(-5)
    self.slider_1_tab1_2.grid(row=6, column=4, sticky='n', pady=2)

    self.slider_2_tab1_2 = Scale(self.tab1_2, from_=1, to=100, orient=HORIZONTAL)
    self.slider_2_tab1_2.set(5)
    self.slider_2_tab1_2.grid(row=7, column=4, sticky='n', pady=2)

    self.P_x_label_tab1_2 = tkinter.Label(self.tab1_2, text="Punkt P  x:")
    self.P_x_label_tab1_2.grid(row=8, column=3, sticky='new', pady=2)

    self.P_y_label_tab1_2 = tkinter.Label(self.tab1_2, text="Punkt P  y:")
    self.P_y_label_tab1_2.grid(row=9, column=3, sticky='new', pady=2)

    self.P_x_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.P_x_var_tab1_2)
    self.P_x_tab1_2.grid(row=8, column=4, sticky='new', pady=2)

    self.P_y_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.P_y_var_tab1_2, state="disabled")
    self.P_y_tab1_2.grid(row=9, column=4, sticky='new', pady=2)

    self.Q_x_label_tab1_2 = tkinter.Label(self.tab1_2, text="Punkt Q  x:")
    self.Q_x_label_tab1_2.grid(row=10, column=3, sticky='new', pady=2)

    self.Q_y_label_tab1_2 = tkinter.Label(self.tab1_2, text="Punkt Q  y:")
    self.Q_y_label_tab1_2.grid(row=11, column=3, sticky='new', pady=2)

    self.Q_x_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.Q_x_var_tab1_2)
    self.Q_x_tab1_2.grid(row=10, column=4, sticky='new', pady=2)

    self.Q_y_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.Q_y_var_tab1_2, state="disabled")
    self.Q_y_tab1_2.grid(row=11, column=4, sticky='new', pady=2)

    self.R_x_label_tab1_2 = tkinter.Label(self.tab1_2, text="Punkt R = P + Q  x:")
    self.R_x_label_tab1_2.grid(row=12, column=3, sticky='new', pady=2)

    self.R_y_label_tab1_2 = tkinter.Label(self.tab1_2, text="Punkt R = P + Q  y:")
    self.R_y_label_tab1_2.grid(row=13, column=3, sticky='new', pady=2)

    self.R_x_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.R_x_var_tab1_2, state="disabled")
    self.R_x_tab1_2.grid(row=12, column=4, sticky='new', pady=2)

    self.R_y_tab1_2 = tkinter.Entry(self.tab1_2, textvariable=self.R_y_var_tab1_2, state="disabled")
    self.R_y_tab1_2.grid(row=13, column=4, sticky='new', pady=2)

    # ---------------------------------------------------------------------------
    # tab1_3 - Krzywe eliptyczne nad liczbami rzeczywistymi - Mnożenie punktów
    # ---------------------------------------------------------------------------
    self.par_a_var_tab1_3 = tkinter.StringVar()
    self.par_b_var_tab1_3 = tkinter.StringVar()
    self.P_x_var_tab1_3 = tkinter.StringVar()
    self.P_y_var_tab1_3 = tkinter.StringVar()
    self.n_var_tab1_3 = tkinter.StringVar()
    self.Q_x_var_tab1_3 = tkinter.StringVar()
    self.Q_y_var_tab1_3 = tkinter.StringVar()

    self.label1_tab1_3 = tkinter.Label(self.tab1_3, text='Mnożenie punktów na krzywej eliptycznej', font=("Helvetica", 16))
    self.label1_tab1_3.grid(row=0, column=6, columnspan=10, sticky='w')

    self.photo_tab1_3 = tkinter.PhotoImage(file='assets/python.PNG')
    self.photo_label_tab1_3 = tkinter.Label(self.tab1_3, image=self.photo_tab1_3)
    self.photo_label_tab1_3.grid(row=0, column=16, columnspan=10, sticky='w', padx=15)

    self.par_a_label_tab1_3 = tkinter.Label(self.tab1_3, text="Parametr a:")
    self.par_a_label_tab1_3.grid(row=4, column=3, sticky='new', pady=2)

    self.par_b_label_tab1_3 = tkinter.Label(self.tab1_3, text="Parametr b:")
    self.par_b_label_tab1_3.grid(row=5, column=3, sticky='new', pady=2)

    self.button_oblicz_tab1_3 = tkinter.Button(self.tab1_3, text='Oblicz', command=self.fun_tab1_3)
    self.button_oblicz_tab1_3.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.par_a_var_tab1_3)
    self.par_a_tab1_3.grid(row=4, column=4, sticky='new', pady=2)

    self.par_b_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.par_b_var_tab1_3)
    self.par_b_tab1_3.grid(row=5, column=4, sticky='new', pady=2)

    self.zakr_od_label_tab1_3 = tkinter.Label(self.tab1_3, text="Zakres od:")
    self.zakr_od_label_tab1_3.grid(row=6, column=3, sticky='new', pady=2)

    self.zakr_do_label_tab1_3 = tkinter.Label(self.tab1_3, text="Zakres do:")
    self.zakr_do_label_tab1_3.grid(row=7, column=3, sticky='new', pady=2)

    self.slider_1_tab1_3 = Scale(self.tab1_3, from_=-100, to=-1, orient=HORIZONTAL)
    self.slider_1_tab1_3.set(-5)
    self.slider_1_tab1_3.grid(row=6, column=4, sticky='n', pady=2)

    self.slider_2_tab1_3 = Scale(self.tab1_3, from_=1, to=100, orient=HORIZONTAL)
    self.slider_2_tab1_3.set(5)
    self.slider_2_tab1_3.grid(row=7, column=4, sticky='n', pady=2)

    self.P_x_label_tab1_3 = tkinter.Label(self.tab1_3, text="Punkt P  x:")
    self.P_x_label_tab1_3.grid(row=8, column=3, sticky='new', pady=2)

    self.P_y_label_tab1_3 = tkinter.Label(self.tab1_3, text="Punkt P  y:")
    self.P_y_label_tab1_3.grid(row=9, column=3, sticky='new', pady=2)

    self.P_x_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.P_x_var_tab1_3)
    self.P_x_tab1_3.grid(row=8, column=4, sticky='new', pady=2)

    self.P_y_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.P_y_var_tab1_3, state="disabled")
    self.P_y_tab1_3.grid(row=9, column=4, sticky='new', pady=2)

    self.n_label_tab1_3 = tkinter.Label(self.tab1_3, text="Mnożnik n:")
    self.n_label_tab1_3.grid(row=10, column=3, sticky='new', pady=2)

    self.n_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.n_var_tab1_3)
    self.n_tab1_3.grid(row=10, column=4, sticky='new', pady=2)

    self.Q_x_label_tab1_3 = tkinter.Label(self.tab1_3, text="Punkt Q = n * P  x:")
    self.Q_x_label_tab1_3.grid(row=11, column=3, sticky='new', pady=2)

    self.Q_y_label_tab1_3 = tkinter.Label(self.tab1_3, text="Punkt Q = n * P  y:")
    self.Q_y_label_tab1_3.grid(row=12, column=3, sticky='new', pady=2)

    self.Q_x_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.Q_x_var_tab1_3, state="disabled")
    self.Q_x_tab1_3.grid(row=11, column=4, sticky='new', pady=2)

    self.Q_y_tab1_3 = tkinter.Entry(self.tab1_3, textvariable=self.Q_y_var_tab1_3, state="disabled")
    self.Q_y_tab1_3.grid(row=12, column=4, sticky='new', pady=2)

    # ---------------------------------------------------------------------------
    # tab2_1 - Krzywe eliptyczne nad dowolnym ciałem - Wykres
    # ---------------------------------------------------------------------------
    self.par_a_var_tab2_1 = tkinter.StringVar()
    self.par_b_var_tab2_1 = tkinter.StringVar()
    self.par_p_var_tab2_1 = tkinter.StringVar()

    self.label1_tab2_1 = tkinter.Label(self.tab2_1, text='Krzywe eliptyczne nad dowolnym ciałem', font=("Helvetica", 16))
    self.label1_tab2_1.grid(row=0, column=6, columnspan=10, sticky='w')

    self.photo_tab2_1 = tkinter.PhotoImage(file='assets/python2.PNG')
    self.photo_label_tab2_1 = tkinter.Label(self.tab2_1, image=self.photo_tab2_1)
    self.photo_label_tab2_1.grid(row=0, column=16, columnspan=10, sticky='w', padx=15)

    self.par_a_label_tab2_1 = tkinter.Label(self.tab2_1, text="Parametr a:")
    self.par_a_label_tab2_1.grid(row=3, column=3, sticky='new', pady=2)

    self.par_b_label_tab2_1 = tkinter.Label(self.tab2_1, text="Parametr b:")
    self.par_b_label_tab2_1.grid(row=4, column=3, sticky='new', pady=2)

    self.button_oblicz_tab2_1 = tkinter.Button(self.tab2_1, text='Rysuj', command=self.fun_tab2_1)
    self.button_oblicz_tab2_1.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab2_1 = tkinter.Entry(self.tab2_1, textvariable=self.par_a_var_tab2_1)
    self.par_a_tab2_1.grid(row=3, column=4, sticky='new', pady=2)

    self.par_b_tab2_1 = tkinter.Entry(self.tab2_1, textvariable=self.par_b_var_tab2_1)
    self.par_b_tab2_1.grid(row=4, column=4, sticky='new', pady=2)

    self.p_label_tab2_1 = tkinter.Label(self.tab2_1, text="Pole p:")
    self.p_label_tab2_1.grid(row=5, column=3, sticky='new', pady=2)

    self.par_p_tab2_1 = tkinter.Entry(self.tab2_1, textvariable=self.par_p_var_tab2_1)
    self.par_p_tab2_1.grid(row=5, column=4, sticky='new', pady=2)

    # ---------------------------------------------------------------------------
    # tab2_2 - Krzywe eliptyczne nad dowolnym ciałem - Dodawanie punktów
    # ---------------------------------------------------------------------------
    self.par_a_var_tab2_2 = tkinter.StringVar()
    self.par_b_var_tab2_2 = tkinter.StringVar()
    self.par_p_var_tab2_2 = tkinter.StringVar()
    self.P_x_var_tab2_2 = tkinter.StringVar()
    self.P_y_var_tab2_2 = tkinter.StringVar()
    self.Q_x_var_tab2_2 = tkinter.StringVar()
    self.Q_y_var_tab2_2 = tkinter.StringVar()
    self.R_x_var_tab2_2 = tkinter.StringVar()
    self.R_y_var_tab2_2 = tkinter.StringVar()

    self.label1_tab2_2 = tkinter.Label(self.tab2_2, text='Dodawanie punktów na krzywej eliptycznej', font=("Helvetica", 16))
    self.label1_tab2_2.grid(row=0, column=6, columnspan=10, sticky='w')

    self.photo_tab2_2 = tkinter.PhotoImage(file='assets/python2.PNG')
    self.photo_label_tab2_2 = tkinter.Label(self.tab2_2, image=self.photo_tab2_2)
    self.photo_label_tab2_2.grid(row=0, column=16, columnspan=10, sticky='w', padx=15)

    self.par_a_label_tab2_2 = tkinter.Label(self.tab2_2, text="Parametr a:")
    self.par_a_label_tab2_2.grid(row=4, column=3, sticky='new', pady=2)

    self.par_b_label_tab2_2 = tkinter.Label(self.tab2_2, text="Parametr b:")
    self.par_b_label_tab2_2.grid(row=5, column=3, sticky='new', pady=2)

    self.button_oblicz_tab2_2 = tkinter.Button(self.tab2_2, text='Oblicz', command=self.fun_tab2_2)
    self.button_oblicz_tab2_2.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.par_a_var_tab2_2)
    self.par_a_tab2_2.grid(row=4, column=4, sticky='new', pady=2)

    self.par_b_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.par_b_var_tab2_2)
    self.par_b_tab2_2.grid(row=5, column=4, sticky='new', pady=2)

    self.p_label_tab2_2 = tkinter.Label(self.tab2_2, text="Pole p:")
    self.p_label_tab2_2.grid(row=6, column=3, sticky='new', pady=2)

    self.par_p_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.par_p_var_tab2_2)
    self.par_p_tab2_2.grid(row=6, column=4, sticky='new', pady=2)

    self.P_x_label_tab2_2 = tkinter.Label(self.tab2_2, text="Punkt P  x:")
    self.P_x_label_tab2_2.grid(row=7, column=3, sticky='new', pady=2)

    self.P_y_label_tab2_2 = tkinter.Label(self.tab2_2, text="Punkt P  y:")
    self.P_y_label_tab2_2.grid(row=8, column=3, sticky='new', pady=2)

    self.P_x_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.P_x_var_tab2_2)
    self.P_x_tab2_2.grid(row=7, column=4, sticky='new', pady=2)

    self.P_y_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.P_y_var_tab2_2)
    self.P_y_tab2_2.grid(row=8, column=4, sticky='new', pady=2)

    self.Q_x_label_tab2_2 = tkinter.Label(self.tab2_2, text="Punkt Q  x:")
    self.Q_x_label_tab2_2.grid(row=9, column=3, sticky='new', pady=2)

    self.Q_y_label_tab2_2 = tkinter.Label(self.tab2_2, text="Punkt Q  y:")
    self.Q_y_label_tab2_2.grid(row=10, column=3, sticky='new', pady=2)

    self.Q_x_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.Q_x_var_tab2_2)
    self.Q_x_tab2_2.grid(row=9, column=4, sticky='new', pady=2)

    self.Q_y_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.Q_y_var_tab2_2)
    self.Q_y_tab2_2.grid(row=10, column=4, sticky='new', pady=2)

    self.R_x_label_tab2_2 = tkinter.Label(self.tab2_2, text="Punkt R = P + Q  x:")
    self.R_x_label_tab2_2.grid(row=11, column=3, sticky='new', pady=2)

    self.R_y_label_tab2_2 = tkinter.Label(self.tab2_2, text="Punkt R = P + Q  y:")
    self.R_y_label_tab2_2.grid(row=12, column=3, sticky='new', pady=2)

    self.R_x_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.R_x_var_tab2_2, state="disabled")
    self.R_x_tab2_2.grid(row=11, column=4, sticky='new', pady=2)

    self.R_y_tab2_2 = tkinter.Entry(self.tab2_2, textvariable=self.R_y_var_tab2_2, state="disabled")
    self.R_y_tab2_2.grid(row=12, column=4, sticky='new', pady=2)

    # ---------------------------------------------------------------------------
    # tab2_3 - Krzywe eliptyczne nad dowolnym ciałem - Mnożenie punktów
    # ---------------------------------------------------------------------------
    self.par_a_var_tab2_3 = tkinter.StringVar()
    self.par_b_var_tab2_3 = tkinter.StringVar()
    self.par_p_var_tab2_3 = tkinter.StringVar()
    self.P_x_var_tab2_3 = tkinter.StringVar()
    self.P_y_var_tab2_3 = tkinter.StringVar()
    self.par_n_var_tab2_3 = tkinter.StringVar()
    self.R_x_var_tab2_3 = tkinter.StringVar()
    self.R_y_var_tab2_3 = tkinter.StringVar()

    self.label1_tab2_3 = tkinter.Label(self.tab2_3, text='Mnożenie punktów na krzywej eliptycznej', font=("Helvetica", 16))
    self.label1_tab2_3.grid(row=0, column=6, columnspan=10, sticky='w')

    self.photo_tab2_3 = tkinter.PhotoImage(file='assets/python2.PNG')
    self.photo_label_tab2_3 = tkinter.Label(self.tab2_3, image=self.photo_tab2_3)
    self.photo_label_tab2_3.grid(row=0, column=16, columnspan=10, sticky='w', padx=15)

    self.par_a_label_tab2_3 = tkinter.Label(self.tab2_3, text="Parametr a:")
    self.par_a_label_tab2_3.grid(row=4, column=3, sticky='new', pady=2)

    self.par_b_label_tab2_3 = tkinter.Label(self.tab2_3, text="Parametr b:")
    self.par_b_label_tab2_3.grid(row=5, column=3, sticky='new', pady=2)

    self.button_oblicz_tab2_3 = tkinter.Button(self.tab2_3, text='Oblicz', command=self.fun_tab2_3)
    self.button_oblicz_tab2_3.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.par_a_var_tab2_3)
    self.par_a_tab2_3.grid(row=4, column=4, sticky='new', pady=2)

    self.par_b_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.par_b_var_tab2_3)
    self.par_b_tab2_3.grid(row=5, column=4, sticky='new', pady=2)

    self.p_label_tab2_3 = tkinter.Label(self.tab2_3, text="Pole p:")
    self.p_label_tab2_3.grid(row=6, column=3, sticky='new', pady=2)

    self.par_p_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.par_p_var_tab2_3)
    self.par_p_tab2_3.grid(row=6, column=4, sticky='new', pady=2)

    self.P_x_label_tab2_3 = tkinter.Label(self.tab2_3, text="Punkt P  x:")
    self.P_x_label_tab2_3.grid(row=7, column=3, sticky='new', pady=2)

    self.P_y_label_tab2_3 = tkinter.Label(self.tab2_3, text="Punkt P  y:")
    self.P_y_label_tab2_3.grid(row=8, column=3, sticky='new', pady=2)

    self.P_x_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.P_x_var_tab2_3)
    self.P_x_tab2_3.grid(row=7, column=4, sticky='new', pady=2)

    self.P_y_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.P_y_var_tab2_3)
    self.P_y_tab2_3.grid(row=8, column=4, sticky='new', pady=2)

    self.par_n_label_tab2_3 = tkinter.Label(self.tab2_3, text="Mnożnik n:")
    self.par_n_label_tab2_3.grid(row=9, column=3, sticky='new', pady=2)

    self.par_n_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.par_n_var_tab2_3)
    self.par_n_tab2_3.grid(row=9, column=4, sticky='new', pady=2)

    self.R_x_label_tab2_3 = tkinter.Label(self.tab2_3, text="Punkt R = n * P  x:")
    self.R_x_label_tab2_3.grid(row=10, column=3, sticky='new', pady=2)

    self.R_y_label_tab2_3 = tkinter.Label(self.tab2_3, text="Punkt R = n * P  y:")
    self.R_y_label_tab2_3.grid(row=11, column=3, sticky='new', pady=2)

    self.R_x_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.R_x_var_tab2_3, state="disabled")
    self.R_x_tab2_3.grid(row=10, column=4, sticky='new', pady=2)

    self.R_y_tab2_3 = tkinter.Entry(self.tab2_3, textvariable=self.R_y_var_tab2_3, state="disabled")
    self.R_y_tab2_3.grid(row=11, column=4, sticky='new', pady=2)

    # ---------------------------------------------------------------------------
    # tab3_1 - Krzywe eliptyczne w kryptografii - ElGamal - Punkty
    # ---------------------------------------------------------------------------
    self.par_a_var_tab3_1 = tkinter.StringVar()
    self.par_b_var_tab3_1 = tkinter.StringVar()
    self.par_p_var_tab3_1 = tkinter.StringVar()
    self.P_x_var_tab3_1 = tkinter.StringVar()
    self.P_y_var_tab3_1 = tkinter.StringVar()
    self.par_secret_var_tab3_1 = tkinter.StringVar()
    self.E_x_var_tab3_1 = tkinter.StringVar()
    self.E_y_var_tab3_1 = tkinter.StringVar()

    self.par_a2_var_tab3_1 = tkinter.StringVar()
    self.par_b2_var_tab3_1 = tkinter.StringVar()
    self.par_p2_var_tab3_1 = tkinter.StringVar()
    self.K_x_var_tab3_1 = tkinter.StringVar()
    self.K_y_var_tab3_1 = tkinter.StringVar()
    self.C_x_var_tab3_1 = tkinter.StringVar()
    self.C_y_var_tab3_1 = tkinter.StringVar()
    self.par_secret2_var_tab3_1 = tkinter.StringVar()

    self.label1_tab3_1 = tkinter.Label(self.tab3_1, text='Szyfrowanie ElGamal z wykorzystaniem krzywych eliptycznych', font=("Helvetica", 16))
    self.label1_tab3_1.grid(row=0, column=6, columnspan=10, sticky='w')

    self.par_a_label_tab3_1 = tkinter.Label(self.tab3_1, text="Parametr a:")
    self.par_a_label_tab3_1.grid(row=4, column=3, sticky='new', pady=2)

    self.par_b_label_tab3_1 = tkinter.Label(self.tab3_1, text="Parametr b:")
    self.par_b_label_tab3_1.grid(row=5, column=3, sticky='new', pady=2)

    self.button_oblicz_tab3_1 = tkinter.Button(self.tab3_1, text='Szyfruj', command=self.fun_tab3_1_1)
    self.button_oblicz_tab3_1.grid(row=2, column=4, sticky='new', pady=2)

    self.par_a_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_a_var_tab3_1)
    self.par_a_tab3_1.grid(row=4, column=4, sticky='new', pady=2)

    self.par_b_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_b_var_tab3_1)
    self.par_b_tab3_1.grid(row=5, column=4, sticky='new', pady=2)

    self.p_label_tab3_1 = tkinter.Label(self.tab3_1, text="Pole p:")
    self.p_label_tab3_1.grid(row=6, column=3, sticky='new', pady=2)

    self.par_p_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_p_var_tab3_1)
    self.par_p_tab3_1.grid(row=6, column=4, sticky='new', pady=2)

    self.P_x_label_tab3_1 = tkinter.Label(self.tab3_1, text="Generator x:")
    self.P_x_label_tab3_1.grid(row=7, column=3, sticky='new', pady=2)

    self.P_y_label_tab3_1 = tkinter.Label(self.tab3_1, text="Generator y:")
    self.P_y_label_tab3_1.grid(row=8, column=3, sticky='new', pady=2)

    self.P_x_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.P_x_var_tab3_1)
    self.P_x_tab3_1.grid(row=7, column=4, sticky='new', pady=2)

    self.P_y_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.P_y_var_tab3_1)
    self.P_y_tab3_1.grid(row=8, column=4, sticky='new', pady=2)

    self.E_x_label_tab3_1 = tkinter.Label(self.tab3_1, text="Punkt do zaszyfrowania x:")
    self.E_x_label_tab3_1.grid(row=9, column=3, sticky='new', pady=2)

    self.E_y_label_tab3_1 = tkinter.Label(self.tab3_1, text="Punkt do zaszyfrowania y:")
    self.E_y_label_tab3_1.grid(row=10, column=3, sticky='new', pady=2)

    self.E_x_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.E_x_var_tab3_1)
    self.E_x_tab3_1.grid(row=9, column=4, sticky='new', pady=2)

    self.E_y_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.E_y_var_tab3_1)
    self.E_y_tab3_1.grid(row=10, column=4, sticky='new', pady=2)

    self.par_secret_label_tab3_1 = tkinter.Label(self.tab3_1, text="Klucz prywatny:")
    self.par_secret_label_tab3_1.grid(row=11, column=3, sticky='new', pady=2)

    self.par_secret_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_secret_var_tab3_1)
    self.par_secret_tab3_1.grid(row=11, column=4, sticky='new', pady=2)

    self.par_odstep_label_tab3_1 = tkinter.Label(self.tab3_1, text="    ")
    self.par_odstep_label_tab3_1.grid(row=12, column=3, sticky='new', pady=2)

    self.par_a2_label_tab3_1 = tkinter.Label(self.tab3_1, text="Parametr a:")
    self.par_a2_label_tab3_1.grid(row=14, column=3, sticky='new', pady=2)

    self.par_b2_label_tab3_1 = tkinter.Label(self.tab3_1, text="Parametr b:")
    self.par_b2_label_tab3_1.grid(row=15, column=3, sticky='new', pady=2)

    self.button_deszyfruj_tab3_1 = tkinter.Button(self.tab3_1, text='Deszyfruj', command=self.fun_tab3_1_2)
    self.button_deszyfruj_tab3_1.grid(row=13, column=4, sticky='new', pady=2)

    self.par_a2_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_a2_var_tab3_1)
    self.par_a2_tab3_1.grid(row=14, column=4, sticky='new', pady=2)

    self.par_b2_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_b2_var_tab3_1)
    self.par_b2_tab3_1.grid(row=15, column=4, sticky='new', pady=2)

    self.p2_label_tab3_1 = tkinter.Label(self.tab3_1, text="Pole p:")
    self.p2_label_tab3_1.grid(row=16, column=3, sticky='new', pady=2)

    self.par_p2_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_p2_var_tab3_1)
    self.par_p2_tab3_1.grid(row=16, column=4, sticky='new', pady=2)

    self.K_x_label_tab3_1 = tkinter.Label(self.tab3_1, text="Punkt K x:")
    self.K_x_label_tab3_1.grid(row=17, column=3, sticky='new', pady=2)

    self.K_y_label_tab3_1 = tkinter.Label(self.tab3_1, text="Punkt K y:")
    self.K_y_label_tab3_1.grid(row=18, column=3, sticky='new', pady=2)

    self.K_x_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.K_x_var_tab3_1)
    self.K_x_tab3_1.grid(row=17, column=4, sticky='new', pady=2)

    self.K_y_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.K_y_var_tab3_1)
    self.K_y_tab3_1.grid(row=18, column=4, sticky='new', pady=2)

    self.C_x_label_tab3_1 = tkinter.Label(self.tab3_1, text="Punkt C x:")
    self.C_x_label_tab3_1.grid(row=19, column=3, sticky='new', pady=2)

    self.C_y_label_tab3_1 = tkinter.Label(self.tab3_1, text="Punkt C y:")
    self.C_y_label_tab3_1.grid(row=20, column=3, sticky='new', pady=2)

    self.C_x_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.C_x_var_tab3_1)
    self.C_x_tab3_1.grid(row=19, column=4, sticky='new', pady=2)

    self.C_y_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.C_y_var_tab3_1)
    self.C_y_tab3_1.grid(row=20, column=4, sticky='new', pady=2)

    self.par_secret2_label_tab3_1 = tkinter.Label(self.tab3_1, text="Klucz prywatny:")
    self.par_secret2_label_tab3_1.grid(row=21, column=3, sticky='new', pady=2)

    self.par_secret2_tab3_1 = tkinter.Entry(self.tab3_1, textvariable=self.par_secret2_var_tab3_1)
    self.par_secret2_tab3_1.grid(row=21, column=4, sticky='new', pady=2)

# ---------------------------------------------------------------------------
    # tab3_2 - Krzywe eliptyczne w kryptografii - ElGamal - Punkty
    # ---------------------------------------------------------------------------

    self.par_message_var_tab3_2 = tkinter.StringVar()
    self.par_message2_var_tab3_2 = tkinter.StringVar()
    self.par_public_x_var_tab3_2 = tkinter.StringVar()
    self.par_public_y_var_tab3_2 = tkinter.StringVar()
    self.par_signature_x_var_tab3_2 = tkinter.StringVar()
    self.par_signature_y_var_tab3_2 = tkinter.StringVar()

    self.label1_tab3_2 = tkinter.Label(self.tab3_2, text='Podpis cyfrowy ECDSA {}'.format(self.krzywa.name), font=("Helvetica", 16))
    self.label1_tab3_2.grid(row=0, column=3, columnspan=10, sticky='w', padx= 10)

    self.label2_tab3_2 = tkinter.Label(self.tab3_2, text='Krzywa eliptyczna: {} (wykorzystywana w szyfrowaniu Bitcoin)'.format(self.krzywa.name))
    self.label2_tab3_2.grid(row=1, column=2, columnspan=10, sticky='w', padx= 10)

    self.label3_tab3_2 = tkinter.Label(self.tab3_2, text='Parametry krzywej:')
    self.label3_tab3_2.grid(row=2, column=2, columnspan=10, sticky='w', padx= 10)

    self.label4_tab3_2 = tkinter.Label(self.tab3_2, text='a: {}'.format(self.krzywa.a))
    self.label4_tab3_2.grid(row=3, column=2, columnspan=10, sticky='w', padx= 10)

    self.label5_tab3_2 = tkinter.Label(self.tab3_2, text='b: {}'.format(self.krzywa.b))
    self.label5_tab3_2.grid(row=4, column=2, columnspan=10, sticky='w', padx= 10)

    self.label6_tab3_2 = tkinter.Label(self.tab3_2, text='p: {}'.format(self.krzywa.p))
    self.label6_tab3_2.grid(row=5, column=2, columnspan=10, sticky='w', padx= 10)

    self.label7_tab3_2 = tkinter.Label(self.tab3_2, text='Generator x: {}'.format(self.krzywa.g[0]))
    self.label7_tab3_2.grid(row=6, column=2, columnspan=10, sticky='w', padx= 10)

    self.label8_tab3_2 = tkinter.Label(self.tab3_2, text='Generator y: {}'.format(self.krzywa.g[1]))
    self.label8_tab3_2.grid(row=7, column=2, columnspan=10, sticky='w', padx= 10)

    self.par_message_label_tab3_2 = tkinter.Label(self.tab3_2, text="Wiadomość do podpisania:")
    self.par_message_label_tab3_2.grid(row=8, column=1, sticky='new', padx=10)

    self.par_message_tab3_2 = tkinter.Entry(self.tab3_2, textvariable=self.par_message_var_tab3_2)
    self.par_message_tab3_2.grid(row=8, column=2, columnspan=10, sticky='new', padx=10)

    self.button_podpisz_tab3_2 = tkinter.Button(self.tab3_2, text='Podpisz', command=self.fun_tab3_2_1)
    self.button_podpisz_tab3_2.grid(row=8, column=13, sticky='e', padx=10)

    self.label9_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label9_tab3_2.grid(row=9, column=1, columnspan=10, sticky='w', padx= 10)
    self.label10_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label10_tab3_2.grid(row=10, column=1, columnspan=10, sticky='w', padx= 10)
    self.label11_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label11_tab3_2.grid(row=11, column=1, columnspan=10, sticky='w', padx= 10)
    self.label12_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label12_tab3_2.grid(row=12, column=1, columnspan=10, sticky='w', padx= 10)
    self.label13_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label13_tab3_2.grid(row=13, column=1, columnspan=10, sticky='w', padx= 10)
    self.label14_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label14_tab3_2.grid(row=14, column=1, columnspan=10, sticky='w', padx= 10)
    self.label15_tab3_2 = tkinter.Label(self.tab3_2, text='')
    self.label15_tab3_2.grid(row=15, column=1, columnspan=10, sticky='w', padx= 10)

    self.label19_tab3_2 = tkinter.Label(self.tab3_2, text='Weryfikacja podpisu:')
    self.label19_tab3_2.grid(row=16, column=1, columnspan=10, sticky='w', padx= 10)

    self.par_message2_label_tab3_2 = tkinter.Label(self.tab3_2, text="Podpisana wiadomość:")
    self.par_message2_label_tab3_2.grid(row=17, column=1, sticky='w', padx=10)

    self.par_message2_tab3_2 = tkinter.Entry(self.tab3_2, textvariable=self.par_message2_var_tab3_2)
    self.par_message2_tab3_2.grid(row=17, column=2, columnspan=10, sticky='new', padx=10)

    self.par_public_x_label_tab3_2 = tkinter.Label(self.tab3_2, text="Klucz publiczny x:")
    self.par_public_x_label_tab3_2.grid(row=18, column=1, sticky='w', padx=10)

    self.par_public_x_tab3_2 = tkinter.Entry(self.tab3_2, textvariable=self.par_public_x_var_tab3_2)
    self.par_public_x_tab3_2.grid(row=18, column=2, columnspan=10, sticky='new', padx=10)

    self.par_public_y_label_tab3_2 = tkinter.Label(self.tab3_2, text="Klucz publiczny y:")
    self.par_public_y_label_tab3_2.grid(row=19, column=1, sticky='w', padx=10)

    self.par_public_y_tab3_2 = tkinter.Entry(self.tab3_2, textvariable=self.par_public_y_var_tab3_2)
    self.par_public_y_tab3_2.grid(row=19, column=2, columnspan=10, sticky='new', padx=10)

    self.par_signature_x_label_tab3_2 = tkinter.Label(self.tab3_2, text="Podpis x:")
    self.par_signature_x_label_tab3_2.grid(row=20, column=1, sticky='w', padx=10)

    self.par_signature_x_tab3_2 = tkinter.Entry(self.tab3_2, textvariable=self.par_signature_x_var_tab3_2)
    self.par_signature_x_tab3_2.grid(row=20, column=2, columnspan=10, sticky='new', padx=10)

    self.par_signature_y_label_tab3_2 = tkinter.Label(self.tab3_2, text="Podpis y:")
    self.par_signature_y_label_tab3_2.grid(row=21, column=1, sticky='w', padx=10)

    self.par_signature_y_tab3_2 = tkinter.Entry(self.tab3_2, textvariable=self.par_signature_y_var_tab3_2)
    self.par_signature_y_tab3_2.grid(row=21, column=2, columnspan=10, sticky='new', padx=10)

    self.button_weryfikuj_tab3_2 = tkinter.Button(self.tab3_2, text='Weryfikuj', command=self.fun_tab3_2_2)
    self.button_weryfikuj_tab3_2.grid(row=21, column=13, sticky='e', padx=10)

    self.label19_tab3_2 = tkinter.Label(self.tab3_2, text='', font=10)
    self.label19_tab3_2.grid(row=22, column=2, columnspan=10, sticky='w', padx= 10)
