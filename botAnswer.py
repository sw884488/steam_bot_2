

def botAnswer(l, s, discount):
    print(l, s)
    st = ""
    if discount == True:
        st += "Скидка уже есть\n\n"
        c = -1
        for key, value in l.items():
            c += 1
            st+= key
            st += "\n"
            st += "Скидка:  "
            st+= s[c]
            st += "\n"
            st += "Цена - "
            st+= value
            st+="\n\n"
    else:
        return "Скидки пока нет"
    return st

