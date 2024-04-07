from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator

# Define your desired data structure.
class SearchSchema(BaseModel):
    query: str = Field(description="search query")
    results: list[str] = Field(description="search results")

    # You can add custom validation logic easily with Pydantic.
    @validator("query")
    def query_not_empty(cls, field):
        if not field:
            raise ValueError("Query cannot be empty!")
        return field

    @validator("results")
    def results_not_empty(cls, field):
        if not field:
            raise ValueError("Results cannot be empty!")
        return field
