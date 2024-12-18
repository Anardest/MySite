def attendance(tabels):
    absence = 0
    late = 0
    for tabel in tabels:
        if tabel == 'A':
            absence += 1
        elif tabel == 'L':
            late += 0
            if late == 3 and absence != 0:
                return False
        else:
            late = 0
    return True
# На вход программе подается массив чисел и число n.
# Массив содержит 0 и 1, где 0 означает пустую клетку, а 1 означает клетку с цветком.
# Выведите True, если n цветов можно посадить на клумбу, не нарушая правила, и False, если этого сделать нельзя.

def flowers_pot(garden, n):
    count = 0
    lenght = len(garden)
    for i in garden:
        if garden[i] == 0:
            if (i == 0 or garden[i - 1] == 0) and (i == lenght - 1 or garden[i + 1] == 0):
                count += 1
                garden[i] = 1
        if count >= n:
            return True
    return count >= n
def max_multi(numbers):
    result = 1
    for i in range(3):
        result *= max(numbers)
        numbers.remove(max(numbers))
        if len(numbers) == 0:
            break
    print(result)
