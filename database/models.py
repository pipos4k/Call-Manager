from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from typing import Dict, Any
import uuid

db = SQLAlchemy()

class Call(db.Model):

    __tablename__ = "calls"

    call_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    direction = db.Column(db.String, nullable=False)
    caller = db.Column(db.String(20), nullable=False)
    callee = db.Column(db.String(20), nullable=False)
    call_duration = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_archived = db.Column(db.Boolean, default=False)
    call_type = db.Column(db.String, nullable=False)

    notes = db.relationship("Notes", backref="call", lazy="dynamic", 
                            cascade="all, delete-orphan", passive_deletes=True)

    __table_args__ = (
        db.CheckConstraint(direction.in_(["inbound", "outbound"]), name="check_direction"),
        db.CheckConstraint(call_type.in_(["missed", "answered", "voicemail"]), name="check_call_type")
    )


    def to_dict(self) -> Dict[str, Any]:
        return {
            "call_id": self.call_id,
            "caller": self.caller,
            "callee": self.callee,
            "direction": self.direction,
            "call_duration": self.call_duration,
            "created_at": self.created_at.isoformat(),
            "is_archived": self.is_archived,
            "call_type": self.call_type,
            "notes": [note.to_dict() for note in self.notes]
        }


    def __repr__(self):
        return f"<Call {self.call_id} - {self.direction} - {self.caller} to {self.callee}>"


class Notes(db.Model):

    __tablename__ = "notes"

    note_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    call_id = db.Column(db.String(36), db.ForeignKey("calls.call_id", ondelete="CASCADE"), nullable=False)


    def to_dict(self) -> Dict[str, Any]:
        return {
            "note_id": self.note_id,
            "call_id": self.call_id,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }


    def __repr__(self):
        return f"<Note {self.note_id} for Call {self.call_id}>"