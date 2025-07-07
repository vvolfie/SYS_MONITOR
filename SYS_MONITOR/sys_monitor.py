import psutil as psu
import cpuinfo as cpui
import GPUtil as gpui
import os, time

###FUNCOES###

#MENU
def menu():
    os.system("cls")

    print("""
    1 - CPU
    2 - DISCO
    3 - GPU
    0 - SAIR
    """)

    op = input("OPCAO >> ")
    return op


#INFOS DO CPU
def cpu():

    # ATUALIZA VALORES EM TEMPO REAL

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
            print("***********************")
            print(f"\nUTILIZACAO TOTAL > {total:.1f}%")

        
            time.sleep(1)


    except KeyboardInterrupt:
        print("\n[INFO] A voltar...")
        time.sleep(0.5)
        return

#INFOS DISCO
def disco():
    particoes = psu.disk_partitions() # Obtem as particoes do disco
    os.system('cls')
    try:
        print(f"[PARTICOES]")
        for particao in particoes:
            print(particao)

        print(f"\n\n[UTILIZACAO]")

        for particao in particoes:
            espaco = psu.disk_usage(particao.mountpoint) # Busca a utilizacao da particao
            print(f"{particao.mountpoint} --> {espaco.percent}% ocupado") #imprime a utilizacao

        input()
    except KeyboardInterrupt:
        print("\n[INFO] A voltar...")
        time.sleep(0.5)
        return

#INFOS GPU
def gpu():

    #ATUALIZA VALORES EM TEMPO REAL

    gpus = gpui.getGPUs()

    os.system('cls')

    try:

        print(f"[GPUS]")

        if not gpus:
            print("[INFO] Nao existem GPUs no sistema.")
        else:
            for i, gpu in enumerate(gpus):
                print(f"\nGPU {i+1:<2} --> {gpu.name}")
            
            op = input("\n Escolha uma GPU para ver mais detalhes (CRTL+C para voltar): ")

            if op.isdigit() and 0 < int(op) <= len(gpus): # Ver, se a input esta dentro do intervalo de gpus
                indice = int(op) - 1
                try:
                    while True:
                        gpus = gpui.getGPUs()  # Atualiza a lista de GPUs a cada iteração
                        gpu = gpus[indice]
                        os.system('cls')
                        print(f"\n[INFORMACOES DA GPU {indice+1} EM TEMPO REAL]\n")
                        print(f"GPU           > {gpu.name}")
                        print(f"Memoria Total > {gpu.memoryTotal} MB")
                        print(f"Memoria Livre > {gpu.memoryFree} MB")
                        print(f"Temperatiura  > {gpu.temperature} (C)")
                        print("\nPressiona CTRL+C para voltar ao menu...")
                        time.sleep(1)

                except KeyboardInterrupt:
                    print("\n[INFO] A voltar...")
                    time.sleep(0.5)
                    return
            
        
    except KeyboardInterrupt:
        print("\n[INFO] A voltar...")
        time.sleep(0.5)
        return

###MAIN###

while True:
    op = menu()

    if (op == "1"):
        print("[INFO] A carregar informacoes do CPU...")
        cpu()
    elif(op == "2"):
        disco()
    elif(op == "3"):
        gpu()
    elif(op == "0"):
        print("[INFO] A sair...")
        time.sleep(0.5)
        exit()
    else:
        print("[INFO] OPCAO INVALIDA!")
        print("PRESSIONA ENTER PARA CONTINUAR....")