import tkinter as tk
root = tk.Tk()

# 進数変換関数
def  radixConv(fnum,frdx,trdx):
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","A", "B", "C", "D", "E", "F"]
    ans = []
    Decimal_num = int(fnum,base=int(frdx))
    N_Decimal = int(trdx,base=10)
    while Decimal_num > 0: 
        rem = Decimal_num % N_Decimal
        Decimal_num = Decimal_num//N_Decimal
        rem = code[rem]
        ans.append(rem)
    ans.reverse()
    ans = "".join(map(str, ans))
    return ans

# クリックされたときの関数
def onClick():
    label2 = tk.Label( root, text=m.get()+"進数 : ")
    label2.pack()
    label3 = tk.Label( root, text=n.get()+"進数 : ")

    label3.pack()
    label = tk.Label( root, text="------------------")
    label.pack()
    after_conv = radixConv(get_num.get(),m.get(),n.get())
    label2.config(text =m.get()+"進数 : "+get_num.get())
    label3.config(text =n.get()+"進数 : "+after_conv)

# 配置とかの初期化
labelNum = tk.Label( root, text='変換元の数字')
labelNum.pack()

get_num = tk.Entry( root )
get_num.pack()

labelM = tk.Label( root, text='変換元基数(2進数~16進数)')
labelM.pack()

m = tk.Entry( root )
m.pack()

labelN = tk.Label( root, text='変換後基数(2進数~16進数)')
labelN.pack()

n = tk.Entry( root )
n.pack()


button = tk.Button(root, text='変換', command=onClick)
button.pack()


root.mainloop()