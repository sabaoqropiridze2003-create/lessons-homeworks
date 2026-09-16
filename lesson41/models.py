from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    description: Mapped[str | None] = mapped_column(String(500), default=None)
    rating: Mapped[float | None] = mapped_column(Float, default=None) #new field for rating

    def __str__(self):
        return f"{self.id}.{self.name} - {self.price}"