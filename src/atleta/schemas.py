from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from contrib.schemas import BaseSchema, OutMixin
from categorias.schemas import CategoriaIn
from centro_treinamento.schemas import CentroTreinamentoAtleta


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
    sexo: Annotated[
        str,
        Field(description="Sexo do Atleta", example="M", max_length=1),
    ]
    categoria: Annotated[
        CategoriaIn,
        Field(description="Categoria do atleta"),
    ]

    centro_treinamento: Annotated[
        CentroTreinamentoAtleta,
        Field(description="Centro de treinamento do atleta"),
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(AtletaIn, OutMixin):
    pass

class AtletaUpdate(BaseSchema):

    nome: Annotated[
        Optional[str], Field(None, description="Nome do Atleta", example="João", max_length=50)
    ]

    idade: Annotated[
        Optional[int], Field(None, description="Idade do Atleta", example=25, max_length=4)
    ]