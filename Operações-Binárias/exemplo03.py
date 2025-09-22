
binNumA = bin(intNumA)
binNumB = bin(intNumB)

resultadoAND = int(binNumA) & int(binNumB)

print(f'\nNúmero A: {bin(intNumA):>16} ({int(bin(intNumA), 2)})\n')
print(f'\nNúmero B: {bin(intNumB):>16} ({int(bin(intNumB), 2)})\n')
print(f'\n AND: {bin(resultadoAND):>16} ({int(intNumA, 2)})\n')

#-------------------------------------------------------------


binNumA = bin(150)
binNumB = bin(120)


print(f'\nNúmero A: {binNumA:>16} ({int(binNumA, 2)})\n')
print(f'\nNúmero B: {binNumB:>16} ({int(binNumB, 2)})\n')
print(f'\n AND: {resultadoAND:>16} ({int(binNumA, 2)})\n')