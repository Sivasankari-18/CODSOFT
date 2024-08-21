import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#FFFFFF')  # Background changed to white
root.resizable(width=False, height=False)

ent_field = tk.Entry(root, bg='#FFFFFF', fg='#000000', font=('Arial', 25),  # Changed entry field colors
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=10, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')

class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(self.current)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Rad(self):
        try:
            self.result = False
            self.current = math.radians(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Exp(self):
        try:
            self.result = False
            self.current = math.exp(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Fact(self):
        try:
            self.result = False
            self.current = math.factorial(int(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Sinh(self):
        try:
            self.result = False
            self.current = math.sinh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Cosh(self):
        try:
            self.result = False
            self.current = math.cosh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Tanh(self):
        try:
            self.result = False
            self.current = math.tanh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Ln(self):
        try:
            self.result = False
            self.current = math.log(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Log_10(self):
        try:
            self.result = False
            self.current = math.log10(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Log_2(self):
        try:
            self.result = False
            self.current = math.log2(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_2(self):
        try:
            self.result = False
            self.current = int(ent_field.get())**2
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_3(self):
        try:
            self.result = False
            self.current = int(ent_field.get())**3
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_10_n(self):
        try:
            self.result = False
            self.current = 10**int(ent_field.get())
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def One_div_x(self):
        try:
            self.result = False
            self.current = 1 / float(ent_field.get())
            self.Entry(self.current)
        except (ValueError, ZeroDivisionError, SyntaxError):
            self.Entry('Error')

    def Abs(self):
        try:
            self.result = False
            self.current = abs(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

# Define button colors
btn_fg = "#FFFFFF"
btn_bg = "#4B4B4B"
highlight_bg = '#2E2E2E'

numberpad = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg=btn_fg, bg=btn_bg, width=6, height=2,
                                highlightbackground=highlight_bg, highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='nsew', padx=10, pady=10)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1

btn_CE = tk.Button(root, text='CE', command=lambda: sc_app.Clear_Entry(),
                   font=FONT, height=2, fg=btn_fg, bg=btn_bg,
                   highlightbackground=highlight_bg, highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2,
            sticky='nsew', padx=10, pady=10)

btn_sqr = tk.Button(root, text='\u221A', command=lambda: sc_app.SQ_Root(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_sqr.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                  font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                  highlightbackground=highlight_bg, highlightthickness=2)
btn_0.grid(row=5, column=0, columnspan=2,
           sticky='nsew', padx=10, pady=10)

btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                      font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                      highlightbackground=highlight_bg, highlightthickness=2)
btn_point.grid(row=5, column=2, sticky='nsew', padx=10, pady=10)

btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                      highlightbackground=highlight_bg, highlightthickness=2)
btn_equal.grid(row=5, column=3, sticky='nsew', padx=10, pady=10)

btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_add.grid(row=2, column=3, sticky='nsew', padx=10, pady=10)

btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_sub.grid(row=3, column=3, sticky='nsew', padx=10, pady=10)

btn_mult = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                     font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                     highlightbackground=highlight_bg, highlightthickness=2)
btn_mult.grid(row=4, column=3, sticky='nsew', padx=10, pady=10)

btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_div.grid(row=5, column=4, sticky='nsew', padx=10, pady=10)

btn_exp = tk.Button(root, text='Exp', command=lambda: sc_app.Exp(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_exp.grid(row=1, column=4, sticky='nsew', padx=10, pady=10)

btn_pi = tk.Button(root, text='π', command=lambda: sc_app.Pi(),
                   font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                   highlightbackground=highlight_bg, highlightthickness=2)
btn_pi.grid(row=1, column=5, sticky='nsew', padx=10, pady=10)

btn_e = tk.Button(root, text='e', command=lambda: sc_app.E(),
                  font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                  highlightbackground=highlight_bg, highlightthickness=2)
btn_e.grid(row=1, column=6, sticky='nsew', padx=10, pady=10)

btn_sin = tk.Button(root, text='sin', command=lambda: sc_app.Sin(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_sin.grid(row=2, column=4, sticky='nsew', padx=10, pady=10)

btn_cos = tk.Button(root, text='cos', command=lambda: sc_app.Cos(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_cos.grid(row=2, column=5, sticky='nsew', padx=10, pady=10)

btn_tan = tk.Button(root, text='tan', command=lambda: sc_app.Tan(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_tan.grid(row=2, column=6, sticky='nsew', padx=10, pady=10)

btn_sinh = tk.Button(root, text='sinh', command=lambda: sc_app.Sinh(),
                     font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                     highlightbackground=highlight_bg, highlightthickness=2)
btn_sinh.grid(row=3, column=4, sticky='nsew', padx=10, pady=10)

btn_cosh = tk.Button(root, text='cosh', command=lambda: sc_app.Cosh(),
                     font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                     highlightbackground=highlight_bg, highlightthickness=2)
btn_cosh.grid(row=3, column=5, sticky='nsew', padx=10, pady=10)

btn_tanh = tk.Button(root, text='tanh', command=lambda: sc_app.Tanh(),
                     font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                     highlightbackground=highlight_bg, highlightthickness=2)
btn_tanh.grid(row=3, column=6, sticky='nsew', padx=10, pady=10)

btn_log = tk.Button(root, text='log', command=lambda: sc_app.Log_10(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_log.grid(row=4, column=4, sticky='nsew', padx=10, pady=10)

btn_ln = tk.Button(root, text='ln', command=lambda: sc_app.Ln(),
                   font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                   highlightbackground=highlight_bg, highlightthickness=2)
btn_ln.grid(row=4, column=5, sticky='nsew', padx=10, pady=10)

btn_abs = tk.Button(root, text='|x|', command=lambda: sc_app.Abs(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_abs.grid(row=4, column=6, sticky='nsew', padx=10, pady=10)

btn_deg = tk.Button(root, text='deg', command=lambda: sc_app.Deg(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_deg.grid(row=5, column=5, sticky='nsew', padx=10, pady=10)

btn_rad = tk.Button(root, text='rad', command=lambda: sc_app.Rad(),
                    font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                    highlightbackground=highlight_bg, highlightthickness=2)
btn_rad.grid(row=5, column=6, sticky='nsew', padx=10, pady=10)

btn_pow2 = tk.Button(root, text='x²', command=lambda: sc_app.Pow_2(),
                     font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                     highlightbackground=highlight_bg, highlightthickness=2)
btn_pow2.grid(row=2, column=7, sticky='nsew', padx=10, pady=10)

btn_pow3 = tk.Button(root, text='x³', command=lambda: sc_app.Pow_3(),
                     font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                     highlightbackground=highlight_bg, highlightthickness=2)
btn_pow3.grid(row=3, column=7, sticky='nsew', padx=10, pady=10)

btn_pow10n = tk.Button(root, text='10^x', command=lambda: sc_app.Pow_10_n(),
                       font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                       highlightbackground=highlight_bg, highlightthickness=2)
btn_pow10n.grid(row=4, column=7, sticky='nsew', padx=10, pady=10)

btn_1divx = tk.Button(root, text='1/x', command=lambda: sc_app.One_div_x(),
                      font=FONT, width=6, height=2, fg=btn_fg, bg=btn_bg,
                      highlightbackground=highlight_bg, highlightthickness=2)
btn_1divx.grid(row=5, column=7, sticky='nsew', padx=10, pady=10)

sc_app = SC_Calculator()

root.mainloop()
