#quantas aulas pode matar de poo

class SistemaGeralUFSC:
    def __init__(self):
        self.creditosTotais = 102
        self.alunos = []
        
    def acharMatricula(self, matricula):
        achou = False
        
        for aluno in self.alunos:
            if (aluno['matricula'] == matricula):
                return aluno
        
        if (achou == False):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return None
    
    def numeroAulasFaltaveis(self, matricula):
        aluno = self.acharMatricula(matricula)
        aulasFaltaveis = (self.creditosTotais * 0.25) - int(aluno['numeroDeFaltas'])
        
        if (aulasFaltaveis < 0):
            return 'Aluno já foi reprovado por frequência insuficiente'
        
        return aulasFaltaveis
        
    def porcentagemMaximaPossivel(self, matricula):
        aluno = self.acharMatricula(matricula)
        
        return (self.creditosTotais - int(aluno['numeroDeFaltas'])) / self.creditosTotais

class POO(SistemaGeralUFSC):
    def verificarSeJaExisteMatricula(self, matricula):
        for aluno in self.alunos:
                if (aluno['matricula'] == matricula):
                    return True      
        return False
        
    def adicionarAluno(self, matricula, nome, numeroDeFaltas):
        if (self.acharMatricula(matricula) != None):
            print('Já existe um aluno com essa matrícula. Cada aluno deve ter uma matrícula única.')
            return
        
        self.alunos.append({'nome': nome, 'matricula': matricula, 'numeroDeFaltas': numeroDeFaltas})
        
    def atualizarFichaAluno(self, matricula):
        if (self.acharMatricula(matricula) == None):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return
        
        print(f'Atualizando a ficha do aluno de matricula {matricula}')
        nome = input('Digite o nome do aluno: ')
        matricula = input('Digite a matricula do aluno: ')
        numeroDeFaltas = int(input(f'Digite o número de faltas do aluno até hoje: '))
        
        aluno['nome'] = nome
        aluno['matricula'] = matricula
        aluno['numeroDeFaltas'] = numeroDeFaltas
        achou = True
        
        print('Aluno adicionado')
        
    def deletarFichaAluno(self, matricula):
        if (self.acharMatricula(matricula) == None):
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return
        
        index = alunos.index(aluno)
        alunos.pop(index)
        achou = True
        print(f'Aluno de matrícula {matricula} foi deletado')
    

sistemaPOO = POO()

while True:
    try:
        opcao = int(input('1 - adicionar aluno \n2 - buscar aluno \n3 - atualizar ficha do aluno \n4 - deletar ficha de aluno \n5 - Verificar porcentagem máxima possível \n6 - Verificar quantos dias o aluno ainda pode faltar para não reprovar \n7 - sair do programa \n'))
        
        if (opcao == 1):
            nome = input('Digite o nome do aluno: ')
            numeroDeFaltas = input('Digite o número de faltas do aluno: ')
            matricula = input('Digite a matricula do aluno: ')
            
            sistemaPOO.adicionarAluno(matricula, nome, numeroDeFaltas)
            
        if (opcao == 2):
            matricula = input('Digite a matrícula do aluno que você quer buscar: \n')
            
            print(sistemaPOO.acharMatricula(matricula))
        
        if (opcao == 3):
            matricula = input('Digite a matrícula do aluno que você quer atualizar a ficha: \n')
            
            sistemaPOO.atualizarFichaAluno(matricula)
                
        if (opcao == 4):
            matricula = input('Digite a matrícula do aluno que você quer deletar: \n')
            
            sistemaPOO.deletarFichaAluno(matricula)
        
        if (opcao == 5):
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
            
            print(f'{sistemaPOO.porcentagemMaximaPossivel(matricula)*100:.2f}%')
            
        if (opcao == 6):
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
            
            print(sistemaPOO.numeroAulasFaltaveis(matricula), ' dias')
        
        if (opcao == 7):
            break
            
    except ValueError:
        print('Você deve digitar um número, não uma letra. Digite o numero 1, 2, 3, 4 ou 5')

