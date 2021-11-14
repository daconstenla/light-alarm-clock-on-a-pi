from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Alarm(db.Model):
    __tablename__ = 'alarms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    time = db.Column(db.Time)
    repeat = db.Column(db.Boolean) # if the alarm will be repeated
    days = db.Column(db.Integer) # binary alike day selection encoding 1000000 (monday only)
    nextTrigger = db.Column(db.DateTime) # to be used later
    lastTrigger = db.Column(db.DateTime) # to be used later

    @property
    def serialize(self):
        return {
            'id':  self.id,
            'name': self.name,
            'time': self.time,
            'repeat': self.repeat,
            'days': self.days,
            'nextTrigger': self.nextTrigger,
            'lastTrigger': self.lastTrigger,
        }

    def __repr__(self):
        return '<Alarm %r>' % self.name