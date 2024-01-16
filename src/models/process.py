from src.extensions import db


class Process(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    sentiment = db.Column(db.String(150))

    def __repr__(self):
        return f'<Process Analysis id: "{self.id}", text "{self.text}", sentiment: "{self.sentiment}">'
