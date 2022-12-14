from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp, Range, And

# Create Saving Model 
class Saving(db.Model):
    __tablename__ = 'savings'

    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String)
    current_amount = db.Column(db.Float, nullable=False)
    date_updated = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='saving')

# Create Saving Schema 
class SavingSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'id'])
    # Validate entries for current amount
    current_amount = fields.Float(required=True, validate=Range(min=0.0, error='Amount must be greater than 0'))

    class Meta:
        fields = ('id', 'bank_name', 'current_amount', 'date_updated', 'user_id')
        ordered = True
