from fastapi.testclient import TestClient
from main import app
from recreate_bank import test_recreate_table #Função que criei para recriar o banco de dados
from test_01_create_empresa import test_create_empresa #Adiciono empresa


client = TestClient(app)



def test_get_empresa():
    response = client.get(f"/empresas/{1}") #Id da empresa que quer ler
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 200
