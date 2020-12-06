from control import Produto
import os
produto = Produto()

class OutputConsole():
    def __init__(self):
        self.telaIinicial()
        self.escolha = 0

    def banner(self):
        self.clear()
        l = '='*108+'\n'
        n = '='*40+'    Controle De Produtos    '+'='*40+'\n'
        banner = str(l+l+n+l+l)
        print(banner)

    def telaIinicial(self):
        produto.organizarLista()
        self.banner()
        print(' Adicionar Produto [1]'+' '*9+
            'Remover Produto [2]'+' '*9+
            'Editar Produto [3]'+' '*9+
            'Consultar Produto [4]'
            )
        self.escolha = input('>')
        self.switch(self.escolha)

    def switch(self, escolha):
        if escolha == '1':
            self.telaAdicionar()
        elif escolha == '2':
            self.telaRemover()
        elif escolha == '3':
            self.telaEditar()
        elif escolha == '4':
            self.telaConsulta()
        elif escolha == 'exit':
            pass
        else:
            print('A escolha não é valida')
            self.continuar()
            self.telaIinicial()

    def continuar(self):
        i = input('pronto aperte enter')
        print(i)
        self.telaIinicial()

    def telaAdicionar(self):
        self.banner()
        nome = input('Nome: ')
        qtde = input('Quantidade: ')
        valor = input('Valor: R$')
        produto.adicionar(nome,qtde,valor)
        self.continuar()

    def telaRemover(self):
        self.banner()
        nome = input('Produto a ser deletado: ')
        produto.remover(nome)
        self.continuar()

    def telaEditar(self):
        self.banner()
        nome = input('Produto a se editar: ')
        print('nome - qtde - valor')
        while True:
            inf = input('>')
            if inf in ['id','nome','qtde','valor']:
                texto = input('Editar: ')
                produto.editar(nome,inf,texto)
                break
            else: print('entrada invalida\nnome - qtde - valor')
        self.continuar()

    def telaConsulta(self):
        self.banner()
        nome = input('Buscar: ')
        if nome == 'all':
            print(produto.verTudo())
        else:
            retorno = produto.buscar(nome)
            if not retorno == 'Produto não encontrado ou inexistente':
                retorno = retorno.split(',')
                print('{nome}\nqtde: {qtde}\nValor: R${valor}\nID -> {id}'.format(nome = retorno[1], qtde = retorno[2], valor = retorno[3],id = retorno[0]))
            else:
                print(retorno)
        self.continuar()

    def clear(self):
        os.system('cls') or None

if __name__ == '__main__':
    OutputConsole()
