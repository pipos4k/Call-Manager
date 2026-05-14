import random
from faker import Faker
from database.models import db, Call, Notes
import logging

logger = logging.getLogger(__name__)
fake = Faker()

def seed_data(app):
    with app.app_context():
        logger.info("Seeding database.")
        
        all_calls = []
        for _ in range(50):
            new_call = Call(
                direction=random.choice(["inbound", "outbound"]),
                caller=fake.msisdn(),
                callee=fake.msisdn(),
                call_duration=random.randint(10, 3600),
                is_archived=random.choice([True, False]),
                call_type=random.choice(["missed", "answered", "voicemail"])
            )
            db.session.add(new_call)
            all_calls.append(new_call)
        
        db.session.flush()

        for _ in range(10):
            random_call = random.choice(all_calls)
            new_note = Notes(
                content= fake.sentence(),
                created_at= fake.date_time_this_year(),
                call_id= random_call.call_id
            )
            db.session.add(new_note)

        try:
            db.session.commit()
            logger.info(f"Successfully added 50 calls and 10 notes to the database.")

        except Exception as e:
            db.session.rollback()
            logger.error(f"Error seeding data: {e}") 
        