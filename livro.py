class Livro:
    def __init__(self, autor, capitulo):
        self.autor = autor
        self.capitulo = capitulo
    
    def mostrar_autor(self):
        print("Autor:", self.autor)
    
    def passar_capitulo(self):
        if self.capitulo < total_capitulos:
            self.capitulo += 1
            print("Você está no capítulo", self.capitulo)
        else:
            print("Você já está no último capítulo.")

# Defina o número total de capítulos do livro
total_capitulos = 20  

# Crie uma instância da classe Livro
meu_livro = Livro("João Amado", 1)

# Chame os métodos da classe Livro
meu_livro.mostrar_autor()
meu_livro.passar_capitulo()
