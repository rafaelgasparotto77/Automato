class AutomatoPedido:
    def __init__(self):
        self.estados_finais = {'S3', 'S5', 'S7', 'S8', 'S9'}
        self.transicoes = {
            'S0': {'Quero': 'S1', 'Gostaria': 'S1', 'Vou querer': 'S1'},
            'S1': {'uma': 'S2', 'um': 'S2'},
            'S2': {'hambúrguer': 'S3', 'pizza': 'S3', 'salada': 'S3'},
            'S3': {'com': 'S4', 'sem': 'S4', 'mais': 'S6', 'menos': 'S6', 'FINAL': 'S3'},
            'S4': {'queijo': 'S5', 'tomate': 'S5', 'cebola': 'S5', 'e': 'S4'},
            'S5': {'FINAL': 'S5', 'com': 'S4', 'sem': 'S4', 'mais': 'S6', 'menos': 'S6'},
            'S6': {'queijo': 'S7', 'tomate': 'S7', 'cebola': 'S7'},
            'S7': {'FINAL': 'S8', 'e': 'S6'},
            'S8': {'FINAL': 'S9'}
        }
        self.estado_atual = 'S0'

    def processar_token(self, token):
        if token in self.transicoes[self.estado_atual]:
            self.estado_atual = self.transicoes[self.estado_atual][token]
        else:
            self.estado_atual = 'ERRO'

    def reconhecer_pedido(self, tokens):
        self.estado_atual = 'S0'
        for token in tokens:
            self.processar_token(token)
            if self.estado_atual == 'ERRO':
                return "Frase inválida"
        
        if self.estado_atual in self.estados_finais:
            return "Frase válida"
        else:
            return "Frase incompleta"

# Função para executar o reconhecimento interativo
def executar_reconhecimento():
    automato = AutomatoPedido()
    
    while True:
        frase = input("Digite uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == 'sair':
            break
        
        tokens = frase.split()
        resultado = automato.reconhecer_pedido(tokens)
        print(f"Resultado: {resultado}")

# Executar o reconhecimento interativo
executar_reconhecimento()