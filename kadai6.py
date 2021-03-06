#!/usr/local/bin/python3 kadai6.py
# kadai6.py : M進数の数字をN進数の数字に変換するプログラム。

#M進数とをうけとってN進数で返す関数
def  radixConv(fnum,frdx,trdx):
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","A", "B", "C", "D", "E", "F"]
    ans = []
    # M進数を10進数に変換
    Decimal_num = int(fnum,base=frdx)
    # Nを10進数に変換
    N_Decimal = int(trdx,base=10)
    while Decimal_num > 0: 
        rem = Decimal_num % N_Decimal
        Decimal_num = Decimal_num//N_Decimal
        rem = code[rem]
        ans.append(rem)
    ans.reverse()
    print(ans)
    ans = "".join(map(str, ans))
    return ans
#inputします。
print("\nM進数の数字(2<=M<=16)を、N進数の数字(1<=N<=16)に変換します")
M = int(input("\n変換元の基数(M(2<=M<=16))を入力してください。 >>"))
get_num = input("\n変換元の数字を入力してください。 >>")
N = input("\n変換後(N(1<=N<=16))の基数を入力してください。 >>")
#10進数をN進数に変換
after_Conv = radixConv(get_num,M,N)
print("\n----変換前----\n\n",M,"進数:",get_num,"\n\n----変換後----\n\n",N,"進数:",after_Conv,"\n")
