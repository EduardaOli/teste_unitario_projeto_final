from src.models.restaurant import Restaurant

class TestRestaurant:
    restaurant = Restaurant("Hashi", "Comida Japonêsa")

    def test_abrir_restaurante_fechado(self):
        # Chamar o método open_restaurant para fechar o restaurante
        resultado = self.restaurant.open_restaurant()

        # Verificar se o restaurante está aberto
        assert resultado == "Hashi agora está aberto!"
        assert self.restaurant.open == True

    def test_abrir_restaurante_aberto(self):
        # Definir o restaurante como aberto
        self.restaurant.open = True

        # Chamar o método open_restaurant para abrir o restaurante
        resultado = self.restaurant.open_restaurant()

        # Verificar se o restaurante está aberto
        assert resultado == "Hashi já está aberto!"
        assert self.restaurant.open == True

    def test_fechar_restaurante_aberto(self):
        # Definir o restaurante como aberto
        self.restaurant.open = True

        # Chamar o método close_restaurant para fechar o restaurante
        resultado = self.restaurant.close_restaurant()

        # Verificar se o restaurante está fechado
        assert resultado == "Hashi agora está fechado!"
        assert self.restaurant.open == False

    def test_fechar_restaurante_fechado(self):

        # Chamar o método close_restaurant para fechar o restaurante
        resultado = self.restaurant.close_restaurant()

        # Verificar se o restaurante está fechado
        assert resultado == "Hashi já está fechado!"
        assert self.restaurant.open == False

    def test_describe_restaurant(self):

        self.restaurant.open_restaurant()
        self.restaurant.set_number_served(10)

        resultadoEsperado = self.restaurant.describe_restaurant()

        expected_description = f"Esse restaturante chama {self.restaurant.restaurant_name} e serve {self.restaurant.cuisine_type}."
        expected_description += f"Esse restaturante está servindo {self.restaurant.number_served} consumidores desde que está aberto."
        assert resultadoEsperado == expected_description

    def test_informar_numero_de_pessoas_atendidas_com_restaurante_fechado(self):

        self.restaurant.close_restaurant()
        resultadoEsperado = self.restaurant.set_number_served(10)

        assert resultadoEsperado == "Hashi está fechado!"

    def test_informar_numero_de_pessoas_atendidas_com_restaurante_aberto(self):

        self.restaurant.open_restaurant()
        resultadoEsperado = self.restaurant.set_number_served(10)

        assert resultadoEsperado == "10 clientes atendido até o momento!"

    def test_incrementar_numeros_de_clientes_atendidos_com_resturante_aberto(self):

        self.restaurant.open_restaurant()
        self.restaurant.set_number_served(10)

        resultadoEsperado = self.restaurant.increment_number_served(2)

        assert resultadoEsperado == "12 clientes atendido até o momento agora!"

    def test_incrementar_numeros_de_clientes_atendidos_com_resturante_fechado(self):

        self.restaurant.close_restaurant()
        resultadoEsperado = self.restaurant.increment_number_served(2)

        assert resultadoEsperado == "Hashi está fechado!"
