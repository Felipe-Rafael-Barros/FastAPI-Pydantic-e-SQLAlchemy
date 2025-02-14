from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Importa o Base do database.py


#Configuração tabela empresa
class Empresa(Base):
    __tablename__ = "empresas"
    
    id = Column(Integer, primary_key=True, index=True)  # id: int (PK - Chave primária)
    nome = Column(String, index=True)                  # nome: str
    cnpj = Column(String, unique=True, index=True)     # cnpj: str e único
    endereco = Column(String, index=True)              # endereço: str
    email = Column(String, index=True)                 # e-mail: str
    telefone = Column(String, index=True)              # telefone: str

    # Relacionamento com a tabela "obrigacoes"
    obrigacoes = relationship("Obrigacao", back_populates="empresa")

#Configuração tabela obrigacoes
class Obrigacao(Base):
    __tablename__ = "obrigacoes"

    id = Column(Integer, primary_key=True, index=True)  # id: int (PK - Chave primária)
    nome = Column(String, index=True)                  # nome: str
    periodicidade = Column(String, index=True)         # periodicidade: str
    empresa_id = Column(Integer, ForeignKey("empresas.id"))  # empresa_id: int (FK - Chave estrangeira)

    # Relacionamento com a tabela "empresas"
    empresa = relationship("Empresa", back_populates="obrigacoes")