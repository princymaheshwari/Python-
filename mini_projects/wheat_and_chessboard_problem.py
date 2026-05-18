# Calculation of the classical wheat and chessboard Problem

def compound_wheat_by_block(base, rate, growth_blocks):

    wheat_per_block = [base]
    for n in range(1, growth_blocks+1):
        base = base * (1+rate)
        wheat_per_block.append(base)

    return wheat_per_block

wheat = compound_wheat_by_block(1, 1, 63)
total_wheat = sum(wheat)
print(total_wheat)

