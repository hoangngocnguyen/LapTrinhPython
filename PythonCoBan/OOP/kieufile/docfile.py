with open("dulieu.txt", encoding="utf-8") as file:
    st = file.readlines()
    st = [x.strip() for x in st]
    for x in st:
        print(x)



