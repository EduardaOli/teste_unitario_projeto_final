from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        # Melhoria no codigo para retornar as mensagens para validações dos testes
        if self.flavors:
            message = "No momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                message += f"{flavor}\n"
            return message
        else:
            # retornando mensagem para validação
            return ("Estamos sem estoque atualmente!")

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                # BUG não precisa retonar todos os sabores 'self.flavors' apenas se tem o sabor que foi informando 'flavor'
                # retornando mensagem para validação
                return (f"Temos no momento {flavor}!")
            else:
                # retornando mensagem para validação
                return (f"Não temos no momento {flavor}!")
        else:
            # retornando mensagem para validação
            return ("Estamos sem estoque atualmente!")

    def add_flavor(self, flavor):
        """Adicione o sabor informado ao estoque e retorne uma mensagem."""
        # BUG Removido o if que verifica de existe algum sabor no estoque pq caso não existe não vai para o proximo if
        # e logo não add o novo sabor
        if flavor in self.flavors:
            # retornando mensagem para validação
            return f"{flavor} já está disponível!"
        else:
            self.flavors.append(flavor)
            # retornando mensagem para validação
            return f"{flavor} foi adicionado ao estoque!"
