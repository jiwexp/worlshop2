# จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้
x = int(input("Enter your scores: "))
if x >= 80:
    print("grade: A")
elif x >= 75:
    print("grade: B+")
elif x >= 70:
    print("grade: B")
elif x >= 65:
    print("grade: C+")
elif x >= 60:
    print("grade: C")
elif x >= 55:
    print("grade: D+")
elif x >= 50:
    print("grade: D")
else:
    print("grade: F")