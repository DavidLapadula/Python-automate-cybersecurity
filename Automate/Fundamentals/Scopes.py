toast = 'Toast'

def spam():
    eggs = 99
    print(toast)
    bacon()
    print(eggs)
    print(toast)

def bacon():
    global toast
    toast = 'Toast Toast'
    ham = 101
    eggs = 0

spam()