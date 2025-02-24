from sqlalchemy import create_engine,text
engine =  create_engine("sqlite:///Maji_Ndogo_farm_survey_small.db")  # Maji_Ndogo_farm_survey_small.db

with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    print(result.all())
