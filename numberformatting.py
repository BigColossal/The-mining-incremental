def format_large_number(num):
    suffixes = [
        "k", "M", "B", "T", "Qd", "Qn", "Sx", "Sp", "Oc", "No",
        "De", "Vt", "Tg", "qg", "Qg", "sg", "Sg", "Og", "Ng",
        "Ce", "Du", "Tr", "Qa", "Qi", "Se", "Si", "Ot", "Ni",
        # Extend as necessary
    ]
    
    magnitude = 0
    while num >= 1000:
        num //= 1000
        magnitude += 1
    
    if magnitude > 10:
        if magnitude > 100:
            magnitude = (magnitude - 3) // 100
            return magnitude

print(format_large_number(int("1" + "0" * 603)))