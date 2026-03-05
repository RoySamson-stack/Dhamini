from sqlalchemy import (
    Column,
    String,
    Numeric,
    DateTime,
    Integer,
    ForeignKey,
    Enum as SQLEnum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.database import Base
import enum


class MandateStatus(str, enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    PAUSED = "paused"
    REVOKED = "revoked"
    EXPIRED = "expired"


class DeductionStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"
    RETRY = "retry"


class Mandate(Base):
    __tablename__ = "mandates"

    id = Column(String, primary_key=True)
    borrower_id = Column(String, nullable=False, index=True)
    lender_id = Column(String, nullable=False, index=True)
    bank_account = Column(String, nullable=False)
    bank_code = Column(String, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    frequency = Column(String, nullable=False)
    status = Column(SQLEnum(MandateStatus), default=MandateStatus.PENDING)
    signed_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    deductions = relationship("Deduction", back_populates="mandate")


class Deduction(Base):
    __tablename__ = "deductions"

    id = Column(String, primary_key=True)
    mandate_id = Column(String, ForeignKey("mandates.id"), nullable=False, index=True)
    amount = Column(Numeric(12, 2), nullable=False)
    scheduled_date = Column(DateTime(timezone=True), nullable=False)
    processed_at = Column(DateTime(timezone=True))
    status = Column(SQLEnum(DeductionStatus), default=DeductionStatus.PENDING)
    retry_count = Column(Integer, default=0)
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    mandate = relationship("Mandate", back_populates="deductions")


class Lender(Base):
    __tablename__ = "lenders"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String)
    kyc_status = Column(String, default="pending")
    cbk_license = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Borrower(Base):
    __tablename__ = "borrowers"

    id = Column(String, primary_key=True)
    national_id = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    email = Column(String, index=True)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
