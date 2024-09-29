
"""
- Alta coesão e Baixo acoplamento

COESÃO = RESPONSABILIDADE DE UM MÓDULO
MÓDULO = Class (Classe e arquivo tem o mesmo nome)

IDEAL = ALTA COESÃO (O MINIMO DE RESPONSABILIDADES POR CLASSES)

PlayerDetailView:

1 - Chama o reposório e retornando a resposta
"""







"""
    Tipos de métodos de Classes:

    - Métodos de Instância: Acessam e manipulam dados da instância.
    - Métodos de Classe (classmethod): Operam na classe e podem modificar atributos de classe.
    - Métodos Estáticos (staticmethod): Não acessam nem modificam instâncias ou a classe; são funções que pertencem à classe.

    - Um decorador em Python é uma função que modifica ou estende o comportamento de outra função ou método. 

"""

class Repository:
    model = None

    @classmethod
    def build_from_model(cls, model):
        cls.model = model
        # pode ser acessada pela classe e instancia

    def get_by_id(self, id):
        # pode ser acessada apenas pela instancia
        pass

    @staticmethod
    def get_class_name():
        # pode ser acessada tanto pela classe ou instancia
        # mas não tem acesso aos atributos de classe/instancia
        pass

# --- CLASS VS INSTANCE ---

Repository.build_from_model('Player')

player_repository = Repository.build_from_model('player')
team_repository = Repository.build_from_model('team')
