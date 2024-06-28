import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import create_engine, inspect, Column, Integer, String, ForeignKey, select, func

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(String(9))
    endereco = Column(String(50))

    contas = relationship('Conta', back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(20), nullable=False)
    agencia = Column(Integer, nullable=False)
    numero = Column(Integer, nullable=False)
    valor = Column(Integer, nullable=False)  # Adicionando o campo valor
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="contas")

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.numero}, valor={self.valor})"

print(Cliente.__tablename__)
print(Cliente.__table__)

# Conexão com banco de dados
engine = create_engine("sqlite://")

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

inspector = inspect(engine)
print(inspector.has_table("cliente"))
print(inspector.get_table_names())
print(inspector.default_schema_name)

# Inserindo dados de exemplo
with Session(engine) as session:
    maria = Cliente(
        nome="Carlos",
        cpf="123456789",
        endereco="Rua A, 123",
        contas=[Conta(tipo='Corrente', agencia=1, numero=123, valor=1000), 
                Conta(tipo='Poupança', agencia=1, numero=456, valor=500)]
    )
    joao = Cliente(
        nome="Joao",
        cpf="987654321",
        endereco="Avenida B, 456",
        contas=[Conta(tipo='Corrente', agencia=2, numero=789, valor=1500)]
    )
    ana = Cliente(
        nome="Pedro",
        cpf="456789123",
        endereco="Rua C, 789",
    )
    
    # Enviando para o BD (persistência de dados)
    session.add_all([maria, joao, ana])
    session.commit()

# Recuperando dados
with Session(engine) as session:
    stmt = select(Cliente).where(Cliente.nome.in_(['Carlos', 'Joao']))
    print("Recuperando clientes a partir de condições de filtragem")
    for cliente in session.scalars(stmt):
        print(cliente)

    stmt_conta = select(Conta).where(Conta.cliente_id == 1)
    print("\nRecuperando contas de Maria")
    for conta in session.scalars(stmt_conta):
        print(conta)

    stmt_order = select(Cliente).order_by(Cliente.nome.desc())
    print("\nRecuperando info de maneira ordenada")
    for result in session.scalars(stmt_order):
        print(result)

    stmt_join = select(Cliente.nome, Conta.tipo, Conta.agencia, Conta.numero, Conta.valor).join(Conta)
    for result in session.execute(stmt_join):
        print(result)

    stmt_count = select(func.count('*')).select_from(Cliente)
    print("\nTotal de instâncias em Cliente")
    total_clientes = session.scalar(stmt_count)
    print(total_clientes)


