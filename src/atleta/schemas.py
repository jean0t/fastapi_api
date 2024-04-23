from typing import Annotated
from pydantic import Field, PositiveFloat
from contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do Atleta", example="João", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="CPF do Atleta", example="10123495735", max_length=11)
    ]
    idade: Annotated[
        int, Field(description="Idade do Atleta", example=25, max_length=4)
    ]
    peso: Annotated[
        PositiveFloat, Field(description="Peso do Atleta", example=63.2, max_length=10)
    ]
    altura: Annotated[
        PositiveFloat,
        Field(description="Altura do Atleta", example=1.83, max_length=10),
    ]
    sexo: Annotated[str, Field(description="Sexo do Atleta", example="M", max_length=1)]
