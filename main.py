import sys
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo, askyesno
import tkinter.scrolledtext as scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Functions
import Window
import random
import collections

class App(tkinter.Tk):
    KrzywaEliptyczna = collections.namedtuple('KrzywaEliptyczna', 'name a b p g n h')
    krzywa = KrzywaEliptyczna(
    'secp256k1',
    # Parametry krzywej
    a=0,
    b=7,
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    # Generator
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    # Porządek podgrupy
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    # Kofaktor podgrupy
    h=1)

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        parent.protocol('WM_DELETE_WINDOW', self.Exit)
        self.parent = parent
        Window.create_widgets(self)

    def Exit(self):
        answer = askyesno(title='Zamykanie programu', message='Czy chcesz zamknąć program?')
        if answer:
            sys.exit()

    def fun_tab1_1(self):
        try:
            a = float(self.par_a_var_tab1_1.get())
            b = float(self.par_b_var_tab1_1.get())

            fig, ax = plt.subplots(dpi=100)
            y, x = np.ogrid[self.slider_1_tab1_1.get():self.slider_2_tab1_1.get():100j, self.slider_1_tab1_1.get():self.slider_2_tab1_1.get():100j]
            plt.contour(x.ravel(), y.ravel(), y ** 2 - Functions.ecc_r(x, a, b), [0])
            plt.grid(True, linestyle='--')

            Functions.plot_r(plt, a, b)

            self.canvas_tab1_1 = FigureCanvasTkAgg(fig, master=self.tab1_1)
            self.canvas_tab1_1.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a i b.')

    def fun_tab1_2(self):
        try:
            a = float(self.par_a_var_tab1_2.get())
            b = float(self.par_b_var_tab1_2.get())
            p_x = float(self.P_x_tab1_2.get())
            q_x = float(self.Q_x_tab1_2.get())

            fig, ax = plt.subplots(dpi=100)
            y, x = np.ogrid[self.slider_1_tab1_2.get():self.slider_2_tab1_2.get():100j, self.slider_1_tab1_2.get():self.slider_2_tab1_2.get():100j]
            plt.contour(x.ravel(), y.ravel(), y ** 2 - Functions.ecc_r(x, a, b), [0])
            plt.grid(True, linestyle='--')
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b oraz punkty P, Q.')
            if True:
                return None

        # Punkty P i Q
        if Functions.ecc_r(p_x, a, b) <= 0:
            showinfo(
                title='Informacja',
                message='Punkt P nie należy do krzywej eliptycznej.')
            return None
        else:
            P = np.array((p_x, np.sqrt(Functions.ecc_r(p_x, a, b))))
            if Functions.ecc_r(q_x, a, b) <= 0:
                showinfo(
                    title='Informacja',
                    message='Punkt Q nie należy do krzywej eliptycznej.')
                return None
            else:
                Q = np.array((q_x, np.sqrt(Functions.ecc_r(q_x, a, b))))

                if p_x != q_x:
                    m = (P[1] - Q[1]) / (P[0] - Q[0])
                else:
                    m = (3 * pow(P[0],2) + a) / (2 * P[1])

                r_x = pow(m,2) - P[0] - Q[0]
                r_y = -1 * (P[1] + m * (r_x - P[0]))

                R = np.array((r_x, -r_y))

                self.P_y_var_tab1_2.set(round(P[1], 4))
                self.Q_y_var_tab1_2.set(round(Q[1], 4))
                self.R_x_var_tab1_2.set(round(r_x, 4))
                self.R_y_var_tab1_2.set(round(r_y, 4))

                ax.scatter(*P)
                ax.annotate('P', (P[0]+0.25, P[1]+0.25), c='b')
                ax.scatter(*Q)
                ax.annotate('Q', (Q[0]+0.25, Q[1]+0.25), c='b')

                # Linia przechodząca przez punkty P i Q oraz przecinająca krzywą eliptyczną
                t = np.arange(-3, 3, 0.001)
                line = np.array([(Q-P) * t_i + P for t_i in t])
                ax.plot(line[:,0], line[:,1], linestyle='--', c='yellow', linewidth=1)

                # Pionowa linia przechodząca przez punkt przecinający krzywą oraz nowy punkt będący sumą P+Q
                ax.axvline(R[0], linestyle='--', c='red', linewidth=1)
                ax.scatter(R[0], -R[1])
                ax.annotate('R = P+Q', (R[0]+0.25, -R[1]+0.25), c='b')

                Functions.plot_r(plt, a, b)
                self.canvas_tab1_2 = FigureCanvasTkAgg(fig, master=self.tab1_2)
                self.canvas_tab1_2.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)

    def fun_tab1_3(self):
        try:
            a = float(self.par_a_var_tab1_3.get())
            b = float(self.par_b_var_tab1_3.get())
            n = int(self.n_var_tab1_3.get())
            p_x = float(self.P_x_tab1_3.get())

            fig, ax = plt.subplots(dpi=100)
            y, x = np.ogrid[self.slider_1_tab1_3.get():self.slider_2_tab1_3.get():100j, self.slider_1_tab1_3.get():self.slider_2_tab1_3.get():100j]
            plt.contour(x.ravel(), y.ravel(), y ** 2 - Functions.ecc_r(x, a, b), [0])
            plt.grid(True, linestyle='--')
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b, n oraz punkt P.')
            if True:
                return None

        if Functions.ecc_r(p_x, a, b) <= 0:
            Functions.plot_r(plt, a, b)
            self.canvas_tab1_3 = FigureCanvasTkAgg(fig, master=self.tab1_3)
            self.canvas_tab1_3.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)
            showinfo(
                title='Informacja',
                message='Punkt P nie należy do krzywej eliptycznej.')
            return None
        else:
            if n <= 0:
                showinfo(
                title='Informacja',
                message='Nieprawidłowa wartość n.')
                return None
            else:
                # Punkt P i Q = n*P
                P = np.array((p_x, np.sqrt(Functions.ecc_r(p_x, a, b))))
                Q = np.array(Functions.double_and_add_r(n, P, a))

                ax.scatter(*P)
                ax.annotate('P', (P[0]+0.25, P[1]+0.25), c='b')
                ax.scatter(*Q)
                ax.annotate('Q = n*P', (Q[0]+0.25, Q[1]+0.25), c='b')

                self.P_y_var_tab1_3.set(round(P[1], 4))
                self.Q_x_var_tab1_3.set(round(Q[0], 4))
                self.Q_y_var_tab1_3.set(round(Q[1], 4))

                Functions.plot_r(plt, a, b)
                self.canvas_tab1_3 = FigureCanvasTkAgg(fig, master=self.tab1_3)
                self.canvas_tab1_3.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)

    def fun_tab2_1(self):
        try:
            a = float(self.par_a_var_tab2_1.get())
            b = float(self.par_b_var_tab2_1.get())
            p = int(self.par_p_var_tab2_1.get())

            if not Functions.czy_pierwsza(p):
                showinfo(
                    title='Informacja',
                    message='Liczba p nie jest liczbą pierwszą.')
                return None

            x = np.array(range(0, p))
            y2 = Functions.ecc_f(x, p, a, b)

            y = Functions.sqrt_f(x, y2, p)

            # Liczba punktów +1 dla punktu w nieskończoności
            ile_punktow = len(sum([p_y[1:] for p_y in y], ())) + 1

            self.ile_punktow_label_tab2_1 = scrolledtext.ScrolledText(self.tab2_1, font=(12), height=20, width=50)
            self.ile_punktow_label_tab2_1.grid(row=2, column=27, columnspan= 10, rowspan= 1000, sticky='nw', padx=10, pady=10)

            self.ile_punktow_label_tab2_1.insert(INSERT,'Krzywa eliptyczna posiada {ile} punktów \n(wliczając punkt w nieskończoności).\n' \
                                                    'Punkty:\n' .format(ile=ile_punktow))

            fig = plt.figure(dpi=100)
            for p_y in y:
                [plt.scatter(p_y[0], i, c='b') for i in p_y[1:]]
                for i in range(1, len(p_y)):
                    self.ile_punktow_label_tab2_1.insert(INSERT, '(x: {}, y: {}), \n'.format(p_y[0], p_y[i]))
                #self.ile_punktow_label_tab2_1.insert(INSERT, '(x: {}, y: {}), \n'.format(p_y[0], p_y[1:]))
            plt.grid(True, linestyle='--')
            self.ile_punktow_label_tab2_1['state'] = 'disabled'

            Functions.plot_f(plt, a, b, p)
            self.canvas_tab2_1 = FigureCanvasTkAgg(fig, master=self.tab2_1)
            self.canvas_tab2_1.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b oraz p.')

    def fun_tab2_2(self):
        try:
            a = float(self.par_a_var_tab2_2.get())
            b = float(self.par_b_var_tab2_2.get())
            p = int(self.par_p_var_tab2_2.get())
            p_x = int(self.P_x_tab2_2.get())
            p_y = int(self.P_y_tab2_2.get())
            q_x = int(self.Q_x_tab2_2.get())
            q_y = int(self.Q_y_tab2_2.get())

            if not Functions.czy_pierwsza(p):
                showinfo(
                    title='Informacja',
                    message='Liczba p nie jest liczbą pierwszą.')
                return None

            P = np.array((p_x, p_y))
            Q = np.array((q_x, q_y))

            x = np.array(range(0, p))
            y2 = Functions.ecc_f(x, p, a, b)
            y = Functions.sqrt_f(x, y2, p)

            if Functions.czy_nalezy(P,y):
                if Functions.czy_nalezy(Q, y):
                    r_x, r_y = Functions.point_add(P, Q, a, p)
                    R = np.array((r_x, r_y))
                    self.R_x_var_tab2_2.set(r_x)
                    self.R_y_var_tab2_2.set(r_y)
                else:
                    showinfo(
                        title='Informacja',
                        message='Punkt Q nie należy do krzywej eliptycznej.')
                    return None
            else:
                showinfo(
                    title='Informacja',
                    message='Punkt P nie należy do krzywej eliptycznej.')
                return None

            fig = plt.figure(dpi=100)
            for p_y in y:
                [plt.scatter(p_y[0], i, c='b') for i in p_y[1:]]
            plt.grid(True, linestyle='--')
            plt.scatter(*P, c='r')
            plt.annotate('P', (P[0]+0.75, P[1]+0.75), c='r', size=12)
            plt.scatter(*Q, c='r')
            plt.annotate('Q', (Q[0]+0.75, Q[1]+0.75), c='r', size=12)
            plt.scatter(*R, c='r')
            plt.annotate('R = P + Q', (R[0]+0.75, R[1]+0.75), c='r', size=12)

            Functions.plot_f(plt, a, b, p)
            self.canvas_tab2_2 = FigureCanvasTkAgg(fig, master=self.tab2_2)
            self.canvas_tab2_2.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b, p oraz punkty P i Q.')

    def fun_tab2_3(self):
        try:
            a = int(self.par_a_var_tab2_3.get())
            b = int(self.par_b_var_tab2_3.get())
            p = int(self.par_p_var_tab2_3.get())
            P = (int(self.P_x_tab2_3.get()), int(self.P_y_tab2_3.get()))
            n = int(self.par_n_tab2_3.get())

            if not Functions.czy_pierwsza(p):
                showinfo(
                    title='Informacja',
                    message='Liczba p nie jest liczbą pierwszą.')
                return None

            x = np.array(range(0, p))
            y2 = Functions.ecc_f(x, p, a, b)
            y = Functions.sqrt_f(x, y2, p)

            if Functions.czy_nalezy(P,y):
                if Functions.scalar_mult(n, P, a, p) != None:
                    r_x, r_y = Functions.scalar_mult(n, P, a, p)
                    R = (r_x, r_y)
                    self.R_x_var_tab2_3.set(r_x)
                    self.R_y_var_tab2_3.set(r_y)
                else:
                    R = None
                    self.R_x_var_tab2_3.set('Inf')
                    self.R_y_var_tab2_3.set('Inf')
            else:
                showinfo(
                    title='Informacja',
                    message='Punkt P nie należy do krzywej eliptycznej.')
                return None

            # Liczba punktów +1 dla punktu w nieskończoności
            ile_punktow = len(sum([p_y[1:] for p_y in y], ())) + 1
            order=1

            for i in range(1, ile_punktow +1):
                if Functions.scalar_mult(i, P, a, p) != None:
                    order = order + 1
                else:
                    break

            self.ile_punktow_label_tab2_3 = scrolledtext.ScrolledText(self.tab2_3, font=(12), height=20, width=45)
            self.ile_punktow_label_tab2_3.grid(row=2, column=27, columnspan= 10, rowspan= 1000, sticky='nw', padx=10, pady=10)

            self.ile_punktow_label_tab2_3.insert(INSERT,'Krzywa eliptyczna posiada {ile} punktów \n(wliczając punkt w nieskończoności).\n\n' \
                                                    'Porządek podgrupy wyznaczonej przez punkt P: {order}\n\n' \
                                                    'Podgrupa wygenerowana przez punkt P:\n'.format(ile=ile_punktow, order=order))

            for i in range(1, order + 1):
                if Functions.scalar_mult(i, P, a, p) == None:
                    self.ile_punktow_label_tab2_3.insert(INSERT, '{} * P = (x: Inf, y: Inf), \n'.format(i))
                else:
                    temp_x, temp_y = Functions.scalar_mult(i, P, a, p)
                    self.ile_punktow_label_tab2_3.insert(INSERT, '{} * P = (x: {}, y: {}), \n'.format(i, temp_x, temp_y))

            fig = plt.figure(dpi=100)
            for p_y in y:
                [plt.scatter(p_y[0], i, c='b') for i in p_y[1:]]
            plt.grid(True, linestyle='--')
            plt.scatter(*P, c='r')
            plt.annotate('P', (P[0]+0.75, P[1]+0.75), c='r', size=12)
            if R != None:
                plt.scatter(*R, c='r')
                plt.annotate('R = n * P', (R[0]+0.75, R[1]+0.75), c='r', size=12)
            self.ile_punktow_label_tab2_3['state'] = 'disabled'
            Functions.plot_f(plt, a, b, p)
            self.canvas_tab2_3 = FigureCanvasTkAgg(fig, master=self.tab2_3)
            self.canvas_tab2_3.get_tk_widget().grid(row=2, column=10, rowspan= 1000,columnspan=10, sticky='ew', padx=10, pady=10)
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b, p, n oraz punkt P.')

    def fun_tab3_1_1(self):
        try:
            a = int(self.par_a_var_tab3_1.get())
            b = int(self.par_b_var_tab3_1.get())
            p = int(self.par_p_var_tab3_1.get())
            P = (int(self.P_x_tab3_1.get()), int(self.P_y_tab3_1.get()))
            Secret_key = int(self.par_secret_tab3_1.get())
            E = (int(self.E_x_tab3_1.get()), int(self.E_y_tab3_1.get()))

            if not Functions.czy_pierwsza(p):
                showinfo(
                    title='Informacja',
                    message='Liczba p nie jest liczbą pierwszą.')
                return None

            x = np.array(range(0, p))
            y2 = Functions.ecc_f(x, p, a, b)
            y = Functions.sqrt_f(x, y2, p)

            if Functions.czy_nalezy(P,y):
                if Functions.czy_nalezy(E,y):
                    if Functions.scalar_mult(Secret_key, P, a, p) != None:
                        Public_x, Public_y = Functions.scalar_mult(Secret_key, P, a, p)
                        Public_key = (Public_x, Public_y)
                        Random_key = random.getrandbits(128)
                        while Functions.scalar_mult(Random_key, P, a, p) == None:
                            Random_key = random.getrandbits(128)
                        K = Functions.scalar_mult(Random_key, P, a, p)
                        C = Functions.scalar_mult(Random_key, Public_key, a, p)
                        C = Functions.point_add(C, E, a, p)
                        self.szyfruj_label_tab3_1 = scrolledtext.ScrolledText(self.tab3_1, font=12, height=9, width=65)
                        self.szyfruj_label_tab3_1.grid(row=4, column=6, columnspan= 100, rowspan= 100, sticky='nw', padx=10, pady=10)

                        self.szyfruj_label_tab3_1.insert(INSERT,'Parametry krzywej eliptycznej a: {a}, b: {b}, p: {p}\n'\
                                                    'Generator: {P}\n'\
                                                    'Szyfrowany punkt: {E} \nKlucz prywatny: {Secret_key}\n'\
                                                    'Klucz publiczny: {Public_key}\n'\
                                                    'Klucz losowy: {Random_key}\n\n'\
                                                    'Zaszyfrowana widomość K: {K}, C: {C}\n'.format(a = a, b = b, p = p, P = P, E = E, Secret_key = Secret_key,
                                                                                                    Random_key = Random_key, Public_key = Public_key, K = K, C = C))
                        self.szyfruj_label_tab3_1['state'] = 'disabled'
                    else:
                        showinfo(
                        title='Informacja',
                        message='Proszę podać inną wartość klucza prywatnego.')
                else:
                    showinfo(
                        title='Informacja',
                        message='Punkt do zaszyfrowania nie należy do krzywej eliptycznej.')
                    return None
            else:
                showinfo(
                    title='Informacja',
                    message='Generator nie należy do krzywej eliptycznej.')
                return None
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b, p oraz generator, punkt do zaszyfrowania i klucz prywatny.')

    def fun_tab3_1_2(self):
        try:
            a2 = int(self.par_a2_var_tab3_1.get())
            b2 = int(self.par_b2_var_tab3_1.get())
            p2 = int(self.par_p2_var_tab3_1.get())
            K = (int(self.K_x_tab3_1.get()), int(self.K_y_tab3_1.get()))
            C = (int(self.C_x_tab3_1.get()), int(self.C_y_tab3_1.get()))
            Secret_key2 = int(self.par_secret2_tab3_1.get())

            if not Functions.czy_pierwsza(p2):
                showinfo(
                    title='Informacja',
                    message='Liczba p nie jest liczbą pierwszą.')
                return None

            x = np.array(range(0, p2))
            y2 = Functions.ecc_f(x, p2, a2, b2)
            y = Functions.sqrt_f(x, y2, p2)

            if Functions.czy_nalezy(K,y):
                if Functions.czy_nalezy(C,y):
                    D_x, D_y = Functions.scalar_mult(Secret_key2, K, a2, p2)
                    S = (D_x , D_y)
                    S = Functions.point_neg(S, p2)
                    D = Functions.point_add(C, S, a2, p2)
                    self.deszyfruj_label_tab3_1 = scrolledtext.ScrolledText(self.tab3_1, font=(12), height=9, width=65)
                    self.deszyfruj_label_tab3_1.grid(row=14, column=6, columnspan= 100, rowspan= 100, sticky='nw', padx=10, pady=10)

                    self.deszyfruj_label_tab3_1.insert(INSERT,'Parametry krzywej eliptycznej a: {a2}, b: {b2}, p: {p2}\n' \
                                                'Zaszyfrowana widomość K: {K}, C: {C}\n'
                                                'Klucz prywatny: {Secret_key2}\n\n' \
                                                'Odszyfrowany punkt: {D}\n'.format(a2 = a2, b2 = b2, p2 = p2, K = K, C = C, Secret_key2 = Secret_key2, D = D))
                    self.deszyfruj_label_tab3_1['state'] = 'disabled'
                else:
                    showinfo(
                        title='Informacja',
                        message='Nieprawidłowy punkt C.')
                    return None
            else:
                showinfo(
                    title='Informacja',
                    message='Nieprawidłowy punkt K.')
                return None
        except:
            showinfo(
                title='Informacja',
                message='Proszę podać prawidłowe parametry a, b, p oraz punkty K, C i klucz prywatny.')

    def fun_tab3_2_1(self):
        private, public = Functions.make_keypair(self.krzywa)
        msg = self.par_message_tab3_2.get()
        msg2 = msg.encode('UTF-8')
        signature = Functions.sign_message(private, msg2, self.krzywa)

        self.podpisz_label_tab3_2 = scrolledtext.ScrolledText(self.tab3_2, height=7, width=90)
        self.podpisz_label_tab3_2.grid(row=9, column=2, columnspan= 100, rowspan= 8, sticky='nw', padx=10, pady= 10)
        self.podpisz_label_tab3_2.insert(INSERT,'Wiadomość: {}\n'.format(msg))
        self.podpisz_label_tab3_2.insert(INSERT,'Klucz prywatny: {}\n'.format(hex(private)))
        self.podpisz_label_tab3_2.insert(INSERT,'Klucz publiczny x: {}\n'.format(hex(public[0])))
        self.podpisz_label_tab3_2.insert(INSERT,'Klucz publiczny y: {}\n'.format(hex(public[1])))
        self.podpisz_label_tab3_2.insert(INSERT,'Podpis x: {}\n'.format(hex(signature[0])))
        self.podpisz_label_tab3_2.insert(INSERT,'Podpis y: {}\n'.format(hex(signature[1])))
        self.podpisz_label_tab3_2['state'] = 'disabled'

    def fun_tab3_2_2(self):
        try:
            public = (int(self.par_public_x_tab3_2.get(), 16), int(self.par_public_y_tab3_2.get(), 16))
            signature = (int(self.par_signature_x_tab3_2.get(), 16), int(self.par_signature_y_tab3_2.get(), 16))
            msg = self.par_message2_tab3_2.get()
            msg2 = msg.encode('UTF-8')
            if Functions.verify_signature(public, msg2, signature, self.krzywa):
                self.label19_tab3_2['text'] = 'Podpis prawidłowy.'
                self.label19_tab3_2.config(fg="green")
            else:
                self.label19_tab3_2['text'] = 'Podpis nieprawidłowy.'
                self.label19_tab3_2.config(fg="red")
        except:
            showinfo(
                title='Informacja',
                message='Nieprawidłowa wartość klucza publicznego lub podpisu.')

if __name__ == '__main__':
   main_window = tkinter.Tk()
   run = App(main_window)
   main_window.mainloop()
