with open("futbolcular.txt", "r", encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()

    for a in file:
        a=a[:-1]
        print(a)

        takım_adları=list()
        takım_adları=a.split(",")
        if takım_adları[1]=="Fenerbahçe":
            fb.append(a+"\n")

        elif takım_adları[1] =="Galatasaray":
            gs.append(a+"\n")


        elif takım_adları[1] =="Beşiktaş":
            bjk.append(a+"\n")

    with open("fb.txt", "w", encoding="utf-8") as file1:
        for i in fb:
            file1.write(i)

    with open("gs.txt", "w", encoding="utf-8") as file2:
        for a in gs:
            file2.write(a)

    with open("bjk.txt", "w", encoding="utf-8") as file3:
        for c in bjk:
            file3.write(c)

    