def funcao():
    print("Bloco de código")

def imprime_nome(nome):
    print(f"Nome {nome}")

imprime_nome("Erickson")
imprime_nome("Renan")
imprime_nome("Daniel")



def rep(x):
    for n in range(1,x+1):
        print(str(n) * n)




def uhu(x):
    for n in range(1,x+1):
        for z in range(1,n+1):
            print(z, end= " ")
        print("\n"
