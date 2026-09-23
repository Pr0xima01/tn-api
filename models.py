from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    rank = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    trade = Column(String)
    is_active = Column(Boolean, default=True)