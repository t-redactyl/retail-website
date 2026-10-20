from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict


class Product(BaseModel):
    # DEMO 1: Use this to set up the code completion suggestions for PY-90108
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    # DEMO 1: Use this to set up the code completion suggestions for PY-90108
    # DEMO 2: Use this to set up the base validation rules for the product name in PY-90015
    name: str = Field(validation_alias="productName", min_length=2, max_length=80)
    price: float = Field(gt=0, lt=10_000)
    sku: str = "UNASSIGNED"
    category: str = "general"
    description: str = ""
    currency: str = "USD"
    stock_quantity: int = 0
    weight_kg: float | None = None
    supplier_id: str | None = None
    brand: str | None = None
    tags: list[str] = Field(default_factory=list)
    is_active: bool = True
    is_featured: bool = False
    tax_rate: float = 0.0
    shipping_class: str = "standard"
    warehouse_location: str | None = None
    published_at: datetime | None = None
    notes: str | None = None

    # DEMO 3: Cmd-click "price" below to jump back up to price: float for PY-90014
    @field_validator("price")
    @classmethod
    def price_must_be_in_whole_cents(cls, value: float) -> float:
        # A custom rule beyond the simple Field(gt=0, lt=10_000) constraints.
        if round(value, 2) != value:
            raise ValueError("Price must be specified in whole cents")
        return value

if __name__ == "__main__":
    # DEMO 1: Use this to set up the code completion suggestions for PY-90108
    print(Product(name="Book", price=12.50))
    print(Product(productName="Notebook", price=7.25))

    # DEMO 2: Use this to show the warning when violating the base validation rules in PY-90015
    print(Product(productName="C", price=-100))

