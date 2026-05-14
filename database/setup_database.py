import os
import logging
from sqlalchemy import text
import time 

from database.dummy_builder import seed_data
from database.models import db, Call

logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")

def init_db(app) -> None:

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)

    retries = 5
    while retries > 0:
        try:
            with app.app_context():                
                db.create_all()
                logger.info("Database tables created.")

                if not db.session.query(Call).first():
                    logger.info("No calls found in database. Seeding data.") 
                    seed_data(app)
                else:
                    logger.info("Calls already exist in database. Skipping seeding.")

            break
        except Exception as e:
            logger.error(f"Database connection failed: {str(e)}. Retrying in 5 seconds.")
            retries -= 1

            if retries == 0:
                logger.error("Max retries reached. Could not connect to the database.")
                raise e
            time.sleep(5) 
        
def get_db_session():

    return db.session
    
def check_database_connection() -> bool:

    try:
        db.session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return False