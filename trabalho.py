#quantas aulas pode matar de poo

class SistemaFaltas:
    def __init__(self, creditosTotais, creditosFaltados):
        self.creditosTotais = creditosTotais
        self.creditosFaltados = creditosFaltados
    
    def numeroAulasFaltaveis(self):
        return (self.creditosTotais * 0.25) - self.creditosFaltados
        
    def porcentagemMaximaPossivel(self):
        return (self.creditosTotais - self.creditosFaltados) / self.creditosTotais
        
class POO(SistemaFaltas):
    def __init__(self, creditosFaltados, matricula):
        super().__init__(102, creditosFaltados)
        self.matricula = matricula
        
    def verificarAprovacaoPorPresenca(self):
        if (super().porcentagemMaximaPossivel() < 0.75):
            return False
        else:
            return True

alunos = []

def verificarSeJaExisteMatricula(matricula):
    for aluno in alunos:
            if (aluno['matricula'] == matricula):
                return True
        
    return False

while True:
    try:
        opcao = int(input('1 - adicionar aluno \n2 - buscar aluno \n3 - atualizar ficha do aluno \n4 - deletar ficha de aluno \n5 - sair do programa \n'))
        
        if (opcao == 1):
            nome = input('Digite o nome do aluno: ')
            matricula = input('Digite a matricula do aluno: ')
            
            if (verificarSeJaExisteMatricula(matricula)):
                return
            
            numeroDeFaltas = int(input(f'Digite o número de faltas do aluno de matrícula {matricula} até hoje: '))
            alunos.append({'nome': nome, 'matricula': matricula, 'numeroDeFaltas': numeroDeFaltas})
            
        if (opcao == 2):
            matricula = input('Digite a matrícula do aluno que você quer buscar: \n')
            achou = False
            
            for aluno in alunos:
                if (aluno['matricula'] == matricula):
                    print(aluno)
                    achou = True
            
            if (achou == False):
                print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
        
        if (opcao == 3):
            matricula = input('Digite a matrícula do aluno que você quer atualizar a ficha: \n')
            achou = False
            
            for aluno in alunos:
                if (aluno['matricula'] == matricula):
                    print(f'Atualizando a ficha do aluno de matricula {matricula}')
                    nome = input('Digite o nome do aluno: ')
                    matricula = input('Digite a matricula do aluno: ')
                    numeroDeFaltas = int(input(f'Digite o número de faltas do aluno até hoje: '))
                    
                    aluno['nome'] = nome
                    aluno['matricula'] = matricula
                    aluno['numeroDeFaltas'] = numeroDeFaltas
                    
                    achou = True
            
            if (achou == False):
                print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            
    except ValueError:
        print('Você deve digitar um número, não uma letra. Digite o numero 1, 2, 3, 4 ou 5')

numeroFaltasPOO = 2

situacaoPOO = POO(numeroFaltasPOO, '342342342')
print(situacaoPOO.verificarAprovacaoPorPresenca())
