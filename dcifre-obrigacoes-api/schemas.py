from datetime import date
from pydantic import BaseModel, ConfigDict

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ObrigacaoBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoCreate(ObrigacaoBase):
    pass

class Obrigacao(ObrigacaoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)