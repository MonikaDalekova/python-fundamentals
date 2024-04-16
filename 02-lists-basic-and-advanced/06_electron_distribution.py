number_of_electrons = int(input())
filled_shells = []
for shell in range(1, number_of_electrons + 1):
    current_electrons = 2*shell**2
    if number_of_electrons >= current_electrons:
        filled_shells.append(current_electrons)
        number_of_electrons -= current_electrons
        if current_electrons == 0:
            break
    else:
        filled_shells.append(number_of_electrons)
        break
print(filled_shells)