from app import db


class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(180), index = True, unique = True)
	slug_name = db.Column(db.String(250), index = True, unique = True)
	description = db.Column(db.Text)
	items = db.relationship('Item', backref = 'category') 

	def __repr__(self):
		return '<Category %r>' % self.name


class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(180), nullable = False, index = True)
	slug_name = db.Column(db.String(250), index = True, unique = True)
	description = db.Column(db.Text)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

	def __repr__(self):
		return '<Item %r>' % self.name