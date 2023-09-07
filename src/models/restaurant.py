class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #BUG {self.restaurant_name} pq indica o nome do restaurante
        #ajustando 'and serve' para 'e serve'
        #Melhoria no retorno para realizar a validação das mensagens
        expected_description = f"Esse restaturante chama {self.restaurant_name} e serve {self.cuisine_type}."
        expected_description += f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."
        return expected_description

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            #BUG Alteração para 'True' pq se entrar no if indica que está fechado e logo deve abrir
            self.open = True
            #BUG Alterado o number para zero pq nenhum cliente foi atendido pq abriu agora
            self.number_served = 0
            #retornando mensagem para validação
            return (f"{self.restaurant_name} agora está aberto!")
        else:
            #retornando mensagem para validação
            return (f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            #retornando mensagem para validação
            return (f"{self.restaurant_name} agora está fechado!")
        else:
            #retornando mensagem para validação
            return (f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            #Adicionada mensagem
            return (f"{self.number_served} clientes atendido até o momento!")
        else:
            return (f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            # Bug adicionado o + para incrementar com o que já tinha no number served
            self.number_served += more_customers
            return (f"{self.number_served} clientes atendido até o momento agora!")
        else:
            return(f"{self.restaurant_name} está fechado!")
