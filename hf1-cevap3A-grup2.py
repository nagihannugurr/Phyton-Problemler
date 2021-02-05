birthDayDict = {
    "Barış Can Kurt":"18/10/1995",
    "Burak Şen":"16/07/1994",
    "Nagihan Uğur":"01/01/99"
}

print(">>>Doğum günü sözlüğüne hoş geldiniz. Bu kişilerin doğum günlerini biliyoruz: ")
for key in birthDayDict:
    print(key)
name = str(input(">>>Hangisinin doğum gününü öğrenmek istersin? \n "))
print(str(name) + "'un doğum günü " + birthDayDict[name] + ".")