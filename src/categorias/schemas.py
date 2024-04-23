from contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field, UUID4


class Categoria(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da Categoria", example="Scale", max_length=10)
    ]


class CategoriaIn(Categoria):
    pass


class CategoriaOut(Categoria):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
