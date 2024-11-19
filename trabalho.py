#quantas aulas pode matar de poo

class SistemaGeralUFSC:
    def __init__(self):
        self.alunos = []
        
    def acharMatricula(self, matricula):
        achou = False
        
        for aluno in self.alunos:
            if (aluno['matricula'] == matricula):
                return aluno
        
        if (achou == False):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return None
        
    def adicionarAluno(self, matricula, nome, numeroDeFaltas):
        if (self.acharMatricula(matricula) != None):
            print('Já existe um aluno com essa matrícula. Cada aluno deve ter uma matrícula única.')
            return
        
        self.alunos.append({'nome': nome, 'matricula': matricula, 'numeroDeFaltas': numeroDeFaltas})
        
    def atualizarFichaAluno(self, matricula):
        aluno = self.acharMatricula(matricula)
        iftricula = input('Digite a matricula do aluno: ')
        numeroDeFaltas = int(input(f'Digite o número de faltas do aluno até hoje: '))
        
        aluno['nome'] = nome
        aluno['matricula'] = matricula
        aluno['numeroDeFaltas'] = int(numeroDeFaltas)
        achou = True
        
        print('Aluno adicionado')
        
    def deletarFichaAluno(self, matricula):
        aluno = self.acharMatricula(matricula)
        if (aluno == None):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return
        
        index = self.alunos.index(aluno)
        self.alunos.pop(index)

        print(f'Aluno de matrícula {matricula} foi deletado')
    
    def numeroAulasFaltaveis(self, numeroDeFaltas):
        aulasFaltaveis = (self.creditosTotais * 0.25) - numeroDeFaltas
        
        if (aulasFaltaveis < 0):
            return 'Aluno já foi reprovado por frequência insuficiente'
        
        return f'{aulasFaltaveis} dias'


class SistemaPOO(SistemaGeralUFSC):
    def __init__(self):
        super().__init__()
        self.creditosTotais = 102
        
    def porcentagemMaximaPossivel(self, numeroDeFaltas):
        
        return (self.creditosTotais - numeroDeFaltas) / self.creditosTotais
    
class SistemaFMI(SistemaGeralUFSC):
    def __init__(self):
        super().__init__()
        self.creditosTotais = 72
        
    def numeroAulasFaltaveis(self, numeroDeFaltas):
        aulasFaltaveis = self.creditosTotais - numeroDeFaltas
        
        return f'Você pode faltar {aulasFaltaveis} dias (todas as aulas), desde que sua média final não seja menor que 6, caso passar direto, ou menor do que 3, em caso de recuperação'
        
    def porcentagemMaximaPossivel(self, numeroDeFaltas):
        
        return (self.creditosTotais - numeroDeFaltas) / self.creditosTotais
    

SistemaGeralUFSC = SistemaGeralUFSC()
SistemaPOO = SistemaPOO()
SistemaFMI = SistemaFMI()

while True:
    try:
        opcao = int(input('1 - adicionar aluno \n2 - buscar aluno \n3 - atualizar ficha do aluno \n4 - deletar ficha de aluno \n5 - Verificar porcentagem máxima possível \n6 - Verificar quantos dias o aluno ainda pode faltar para não reprovar \n7 - sair do programa \n'))
        
        if (opcao == 1):
            nome = input('Digite o nome do aluno: ')
            numeroDeFaltas = input('Digite o número de faltas do aluno: ')
            matricula = input('Digite a matricula do aluno: ')
            
            SistemaGeralUFSC.adicionarAluno(matricula, nome, numeroDeFaltas)
            
        if (opcao == 2):
            matricula = input('Digite a matrícula do aluno que você quer buscar: \n')
            
            print(SistemaGeralUFSC.acharMatricula(matricula))
        
        if (opcao == 3):
            matricula = input('Digite a matrícula do aluno que você quer atualizar a ficha: \n')
            
            SistemaGeralUFSC.atualizarFichaAluno(matricula)
                
        if (opcao == 4):
            matricula = input('Digite a matrícula do aluno que você quer deletar: \n')
            
            SistemaGeralUFSC.deletarFichaAluno(matricula)
        
        if (opcao == 5):
            opcaoMateria = input('Digite 1 para verificar POO e 2 para verificar FMI: \n')
            
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
                
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            
            if (aluno == None):
                print (f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            
            elif (opcaoMateria == '1'):
                porcentagemMaximaPossivel = SistemaPOO.porcentagemMaximaPossivel(int(aluno["numeroDeFaltas"]))*100
                print(f'{porcentagemMaximaPossivel:.2f}%')
            
            elif (opcaoMateria == '2'):
                porcentagemMaximaPossivel = SistemaPOO.porcentagemMaximaPossivel(int(aluno["numeroDeFaltas"]))*100
                print(f'{porcentagemMaximaPossivel:.2f}%')
            
            else:
                print('Você deve digitar ')
   
            
        if (opcao == 6):
            opcaoMateria = input('Digite 1 para verificar POO e 2 para verificar FMI: \n')
            
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
            
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            
            if (aluno == None):
                print (f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            
            elif (opcaoMateria == '1'):
                numeroAulasFaltaveis = SistemaPOO.numeroAulasFaltaveis(int(aluno["numeroDeFaltas"]))
                print(numeroAulasFaltaveis)
            
            elif (opcaoMateria == '2'):
                numeroAulasFaltaveis = SistemaFMI.numeroAulasFaltaveis(int(aluno["numeroDeFaltas"]))
                print(numeroAulasFaltaveis)
            
            else:
                print('AAAAAAAAAAAAAAAAAAAAA')
            
        
        if (opcao == 7):
            break
            
    except ValueError:
        print('Você deve digitar um número, não uma letra. Digite o numero 1, 2, 3, 4 ou 5') (aluno == None):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return
        
        print(f'Atualizando a ficha do aluno de matricula {matricula}')
        nome = input('Digite o nome do aluno: ')
        matricula = input('Digite a matricula do aluno: ')
        numeroDeFaltas = int(input(f'Digite o número de faltas do aluno até hoje: '))
        
        aluno['nome'] = nome
        aluno['matricula'] = matricula
        aluno['numeroDeFaltas'] = int(numeroDeFaltas)
        achou = True
        
        print('Aluno adicionado')
        
    def deletarFichaAluno(self, matricula):
        aluno = self.acharMatricula(matricula)
        if (aluno == None):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return
        
        index = self.alunos.index(aluno)
        self.alunos.pop(index)

        print(f'Aluno de matrícula {matricula} foi deletado')
    
    def numeroAulasFaltaveis(self, numeroDeFaltas):
        aulasFaltaveis = (self.creditosTotais * 0.25) - numeroDeFaltas
        
        if (aulasFaltaveis < 0):
            return 'Aluno já foi reprovado por frequência insuficiente'
        
        return f'{aulasFaltaveis} dias'


class SistemaPOO(SistemaGeralUFSC):
    def __init__(self):
        super().__init__()
        self.creditosTotais = 102
        
    def porcentagemMaximaPossivel(self, numeroDeFaltas):
        
        return (self.creditosTotais - numeroDeFaltas) / self.creditosTotais
    
class SistemaFMI(SistemaGeralUFSC):
    def __init__(self):
        super().__init__()
        self.creditosTotais = 72
        
    def numeroAulasFaltaveis(self, numeroDeFaltas):
        aulasFaltaveis = self.creditosTotais - numeroDeFaltas
        
        return f'Você pode faltar {aulasFaltaveis} dias (todas as aulas), desde que sua média final não seja menor que 6, caso passar direto, ou menor do que 3, em caso de recuperação'
        
    def porcentagemMaximaPossivel(self, numeroDeFaltas):
        
        return (self.creditosTotais - numeroDeFaltas) / self.creditosTotais
    

SistemaGeralUFSC = SistemaGeralUFSC()
SistemaPOO = SistemaPOO()
SistemaFMI = SistemaFMI()

while True:
    try:
        opcao = int(input('1 - adicionar aluno \n2 - buscar aluno \n3 - atualizar ficha do aluno \n4 - deletar ficha de aluno \n5 - Verificar porcentagem máxima possível \n6 - Verificar quantos dias o aluno ainda pode faltar para não reprovar \n7 - sair do programa \n'))
        
        if (opcao == 1):
            nome = input('Digite o nome do aluno: ')
            numeroDeFaltas = input('Digite o número de faltas do aluno: ')
            matricula = input('Digite a matricula do aluno: ')
            
            SistemaGeralUFSC.adicionarAluno(matricula, nome, numeroDeFaltas)
            
        if (opcao == 2):
            matricula = input('Digite a matrícula do aluno que você quer buscar: \n')
            
            print(SistemaGeralUFSC.acharMatricula(matricula))
        
        if (opcao == 3):
            matricula = input('Digite a matrícula do aluno que você quer atualizar a ficha: \n')
            
            SistemaGeralUFSC.atualizarFichaAluno(matricula)
                
        if (opcao == 4):
            matricula = input('Digite a matrícula do aluno que você quer deletar: \n')
            
            SistemaGeralUFSC.deletarFichaAluno(matricula)
        
        if (opcao == 5):
            opcaoMateria = input('Digite 1 para verificar POO e 2 para verificar FMI: \n')
            
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
                
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            
            if (aluno == None):
                print (f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            
            elif (opcaoMateria == '1'):
                porcentagemMaximaPossivel = SistemaPOO.porcentagemMaximaPossivel(int(aluno["numeroDeFaltas"]))*100
                print(f'{porcentagemMaximaPossivel:.2f}%')
            
            elif (opcaoMateria == '2'):
                porcentagemMaximaPossivel = SistemaPOO.porcentagemMaximaPossivel(int(aluno["numeroDeFaltas"]))*100
                print(f'{porcentagemMaximaPossivel:.2f}%')
            
            else:
                print('ERRO: Você deve digitar 1 ou 2')
   
            
        if (opcao == 6):
            opcaoMateria = input('Digite 1 para verificar POO e 2 para verificar FMI: \n')
            
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
            
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            
            if (aluno == None):
                print (f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            
            elif (opcaoMateria == '1'):
                numeroAulasFaltaveis = SistemaPOO.numeroAulasFaltaveis(int(aluno["numeroDeFaltas"]))
                print(numeroAulasFaltaveis)
            
            elif (opcaoMateria == '2'):
                numeroAulasFaltaveis = SistemaFMI.numeroAulasFaltaveis(int(aluno["numeroDeFaltas"]))
                print(numeroAulasFaltaveis)
            
            else:
                print('AAAAAAAAAAAAAAAAAAAAA')
            
        
        if (opcao == 7):
            break
            
    except ValueError:
        print('Você deve digitar um número, não uma letra. Digite o numero 1, 2, 3, 4 ou 5')
