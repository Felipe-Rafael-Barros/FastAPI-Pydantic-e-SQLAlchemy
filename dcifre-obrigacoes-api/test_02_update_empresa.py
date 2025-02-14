from fastapi.testclient import TestClient
from main import app
import random
import string
from recreate_bank import test_recreate_table #Função que desenvolvi para recriar o banco de dados
from test_01_create_empresa import test_create_empresa #Criar empresa

# Função para simular um cnpj
def generate_cnpj(): 
    return str(random.randint(10**11, 10**12 - 1))  


# Função para gerar um e-mail
def generate_email():
    """Gera um e-mail aleatório válido."""
    domains = ["gmail.com", "outlook.com", "yahoo.com", "empresa.com.br"]
    name = "".join(random.choices(string.ascii_lowercase, k=8))
    return str(f"{name}@{random.choice(domains)}")

# Função para gerar um nome de empresa
def generate_company_name():
    """Gera um nome de empresa aleatório."""
    prefixes = ["Tech", "Global", "Solutions", "Smart", "Digital", "Future"]
    suffixes = ["Corp", "LTDA", "S.A.", "Enterprises", "Indústria", "Comércio"]
    return str(f"{random.choice(prefixes)} {random.choice(suffixes)}")

#Função para gerar um número de telefone
def generate_phone():
    """Gera um número de telefone aleatório no formato brasileiro."""
    ddd = random.randint(11, 99)
    first_part = random.randint(90000, 99999)  # Garante um número válido (9 dígitos no Brasil)
    second_part = random.randint(1000, 9999)
    return str(f"({ddd}) {first_part}-{second_part}")

# Função para gerar um endereço de rua

def generate_address():
    """Gera um endereço de rua aleatório."""
    street_types = ["Rua", "Avenida", "Travessa", "Alameda"]
    names = ["Central", "das Flores", "dos Andradas", "da Liberdade", "Brasil", "Paulista"]
    number = random.randint(1, 9999)
    return str(f"{random.choice(street_types)} {random.choice(names)}, {number}")




# Instância do TestClient para testar a API
client = TestClient(app)



def test_update_empresa():
    response = client.put(f"/empresas/{1}", #Id da empresa que quer atualizar
                          json={
            "nome": "Empresa Atualizada: "+ generate_company_name(),
            "cnpj": generate_cnpj(),
            "endereco": generate_address(),
            "email": generate_email(),
            "telefone": generate_phone()
        })
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 200

