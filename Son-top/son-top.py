import random
def son_top(x=10):
    """pc son oylaydi siz esa uni topishingiz kerak boladi. necha marta uringaningizni ham korsatadi"""
    son = random.randint(1, x)
    while True:
        taxmin = int(input('men son oyladm sen top: '))
        if taxmin>son:
            print('men oylagan son bundan kichikroq')
        elif taxmin<son:
            print('men oylagan son bundan kattaroq')
        else:
            print('sen topding yutding tabrik')
            break

son_top()
