from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///mars_explorer.db")
Base.metadata.create_all(engine)
