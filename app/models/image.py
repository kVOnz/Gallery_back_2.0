from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.database import Base 

class Image(Base):
    __tablename__ = "images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    is_moderated = Column(Boolean, nullable=False)
    moderation_code = Column(String, nullable=True) # True потому что если все норм, то кода не будет
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    uploaded_id = Column(UUID(as_uuid=True), ForeignKey("user_id"))