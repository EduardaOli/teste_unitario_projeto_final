from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:

    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", ["Baunilha", "Chocolate", "Morango"])

    def test_listar_sabores_disponíveis(self):

        # Verifique se o método retorna a lista de sabores disponíveis quando há sabores
        resultadoEsperado = "No momento temos os seguintes sabores de sorvete disponíveis:Baunilha\nChocolate\nMorango\n"
        result = self.ice_cream_stand.flavors_available()

        assert resultadoEsperado == result

    def test_sabores_disponíveis_vazio(self):

        # Verifique se o método retorna a mensagem de estoque vazio quando não há sabores
        self.ice_cream_stand.flavors = []  # Define a lista de sabores como vazia

        resultadoEsperado = self.ice_cream_stand.flavors_available()
        assert resultadoEsperado == "Estamos sem estoque atualmente!"

    def test_encontrar_sabor_disponivel(self):

        # Defina uma lista de sabores disponíveis
        self.ice_cream_stand.flavors = ["Baunilha", "Chocolate", "Morango"]

        resultado = self.ice_cream_stand.find_flavor("Chocolate")

        ResultadoEsperado = "Temos no momento Chocolate!"
        assert resultado == ResultadoEsperado

    def test_encontrar_sabor_indisponivel(self):

        resultado = self.ice_cream_stand.find_flavor("Pistache")

        # Verifique se a mensagem informa que o sabor não está disponível
        assert resultado == "Não temos no momento Pistache!"

    def test_encontrar_sabor_sem_estoque(self):

        # Não defina nenhum sabor disponível (lista vazia)
        self.ice_cream_stand.flavors = []
        # Tente encontrar um sabor
        resultado = self.ice_cream_stand.find_flavor("Baunilha")

        # Verifique se a mensagem informa que não há estoque
        assert resultado == "Estamos sem estoque atualmente!"

    def test_add_sabor_disponivel_duplicado(self):

        # Defina uma lista de sabores disponíveis
        self.ice_cream_stand.flavors = ["Baunilha", "Chocolate", "Morango"]
        # Tente adicionar um sabor que já está na lista
        resultado = self.ice_cream_stand.add_flavor("Chocolate")

        # Verifique se a mensagem informa que o sabor já está disponível
        assert resultado == "Chocolate já está disponível!"

    def test_add_sabor_novo(self):
        self.ice_cream_stand.flavors = []

        # Tente adicionar um sabor que não está na lista
        resultado = self.ice_cream_stand.add_flavor("Pistache")

        # Verifique se a mensagem informa que o sabor foi adicionado ao estoque
        assert resultado == "Pistache foi adicionado ao estoque!"


