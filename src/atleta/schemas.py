from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Atleta:
    nome: Annotated[str, Field(description="Nome do Atleta", examples="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", examples="10123495735", max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", examples=25, max_length=4)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=63.2, max_length=10)]
    altura: Annotated[PositiveFloat, Field(description="Altura do Atleta", examples=1.83, max_length=10)]
    sexo: Annotated[str, Field(description="Sexo do Atleta", examples="M", max_length=1)]
