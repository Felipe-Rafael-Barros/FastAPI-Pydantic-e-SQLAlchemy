from fastapi.testclient import TestClient
from main import app
from recreate_bank import test_recreate_table #Função que criei para recriar o banco de dados
from test_01_create_empresa import test_create_empresa #função para criar uma nova empresa


# Instância do TestClient para testar a API
client = TestClient(app)


# criar obrigação para empresa de id=1
def test_create_obrigacao():
    response = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": 1
        }
    )
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 200
