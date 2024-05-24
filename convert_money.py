#3 convert money 

cn_yuan = int(input("what do you have left in yuan? : "))
jp_yen = int(input("what do you have left in yen? : "))
kr_won = int(input("what do you have keft in won? : "))
usd = cn_yuan * 0.139 + jp_yen * 0.007 + kr_won * 0.001
print(usd)
