def leggi_file(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = f



def main():
    leggi_file("GCB2023.csv")

if __name__ == '__main__':
    main()