class Error(Exception):
    def __init__():
        pass

class Control_error(Error):
    def __init__(self,message):
        self.message = message

class Arquivo():
    def __init__(self, nome):
        self.nome = nome
        self.abrir()
        self.organizar()

    def abrir(self):
        try:
            arquivo = open(self.nome,'r')
            leitura = arquivo.read()
            return leitura
            arquivo.close()
        except FileNotFoundError:
            return 'O arquivo não existe'

    def organizar(self):
        i = 0
        lista = self.abrir()
        lista = lista.split('\n')
        for x in lista:
            if x == '':
                lista.pop(i)
            i += 1
        lista = sorted(lista)
        arquivo = open(self.nome, 'w')
        for x in lista:
            arquivo.write(x+'\n')
        arquivo.close()


    def buscar(self, busca):
        try:
            indice = 0
            indiceInter = 0
            leitura = self.abrir()
            leitura = leitura.split('\n')
            for x in leitura:
                leituraInter = leitura[indice]
                leituraInter = leituraInter.split(',')
                for i in leituraInter:
                    if i == busca:
                        return leitura[indice]
                        break
                    indiceInter += 1
                indice += 1
            raise Control_error('Produto não encontrado ou inexistente')
        except Control_error as ex:
            return str(ex)

    def adicionar(self, texto):
        arquivo = open(self.nome, 'a')
        arquivo.write(texto+'\n')
        arquivo.close()

    def delete(self,produto):
        i = 0
        leitura = self.abrir()
        leitura = leitura.split('\n')
        dados = self.buscar(produto)
        for x in leitura:
            if x == dados:
                leitura.pop(i)
                break
            i += 1
        arquivo = open(self.nome, 'w')
        for x in leitura:
            arquivo.write(x+'\n')
        arquivo.close()

    def editar(self, produto, inf, texto):
        try:
            dicionario = {'id':0,'nome':1,'qtde':2,'valor':3}
            i = dicionario[inf]
            dados = self.buscar(produto)
            if dados == 'Produto não encontrado ou inexistente':
                raise Control_error('Produto não encontrado ou inexistente, impossive editar')
            listaDados = dados.split(',')
            listaDados[i] = texto
            dados = ''
            for x in listaDados:
                dados += (x+',')
            l = list(dados)
            del(l[-1])
            dados = "".join(l)
            self.delete(produto)
            self.adicionar(dados)
        except Control_error as ex:
            return str(ex)

class Produto():
    def __init__(self):
        self.arquivo = Arquivo('listaProdutos.txt')

    def getId(self):
        leitura = self.arquivo.abrir()
        leitura = leitura.split('\n')
        id = len(leitura)
        return id

    def verTudo(self):
        leitura = self.arquivo.abrir()
        leitura = leitura.split('\n')
        saida = ''
        for x in leitura:
            if not x == '':
                x = x.split(',')
                saida += 'Nome: '+x[1]+'  ID: '+x[0]+'\n'
        return  saida

    def adicionar(self, nome, qtde, valor):
        id = self.getId()
        produto = (str(id) + ',' + nome + ',' + qtde + ',' + valor)
        self.arquivo.adicionar(produto)

    def remover(self, produto):
        self.arquivo.delete(produto)

    def editar(self, produto, inf, texto):
        self.arquivo.editar(produto,inf,texto)

    def buscar(self,produto):
        return self.arquivo.buscar(produto)

    def organizarLista(self):
        self.arquivo.organizar()

if __name__ == '__main__':
    pass
