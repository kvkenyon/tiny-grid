from enum import Enum


class FieldDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATETIME = "DATETIME"
    DOUBLE = "DOUBLE"
    INTEGER = "INTEGER"
    LONG = "LONG"
    TIME = "TIME"
    VARCHAR = "VARCHAR"

    def __str__(self) -> str:
        return str(self.value)
