import psutil as psu
import cpuinfo as cpui
import os, time

###FUNCOES###

#MENU
def menu():
    os.system("cls")

    print("""
    1 - VER INFORMACOES DO CPU
    2 - SAIR
    """)

    op = input("OPCAO >> ")
    return op


#INFOS DO CPU
def cpu():
    cpus = psu.cpu_count() #conta cores do cpu

    nome = cpui.get_cpu_info() #obter nome do cpu

    try:
        while True:
        
            percentagens = psu.cpu_percent(interval=1, percpu=True)
            total = sum(percentagens) / len(percentagens)

            os.system('cls')
            print("***********************\n")
            print ("[INFORMACOES DO CPU]\n")
            print(f"CPU >", nome['brand_raw']) #brand_raw obtem a marca do cpu e o modelo
            print(F"\nCORES/THREADS > {int(cpus/2)}/{cpus}") #cpus devolve cores e threads juntos entao /2 para obter cores


            print("\n***********************")
            print(f"[PERCENTAGEM / CORE]:")
            for i, p in enumerate (percentagens):
                print(f"CPU {i:<2} --> {p}%")
            print("\n***********************")
            print(f"\nUTILIZACAO TOTAL > {total:.1f}%")

        
            time.sleep(1)


    except KeyboardInterrupt:
        print("\nA voltar...")
        time.sleep(0.5)        
        menu()


#######
#######
#######
#######

###MAIN###
while True:
    op = menu()

    if (op == "1"):
        cpu()
    elif(op == "2"):
        exit()
    else:
        print("OPCAO INVALIDA!")
        print("PRESSIONA ENTER PARA CONTINUAR....")