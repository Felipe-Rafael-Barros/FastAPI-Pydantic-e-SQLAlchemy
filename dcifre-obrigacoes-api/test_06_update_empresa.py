from fastapi.testclient import TestClient
from main import app
from recreate_bank import test_recreate_table #Função que criei para recriar o banco de dados
from test_01_create_empresa import test_create_empresa #função para criar uma nova empresa
from test_05_create_obrigacoes import test_create_obrigacao #Adiciono uma obrigação

# Instância do TestClient para testar a API
client = TestClient(app)


#
def test_update_obrigacao():
    response = client.put(f"/obrigacoes/{1}", 
        json={
            "nome": "Obrigações Update",
            "periodicidade": "anual",
            "empresa_id": 1
        })
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 200
