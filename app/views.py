from app import app
from flask import render_template
from models import Category, Item

@app.context_processor
def add_template_helpers():
	category_sidebar = Category.query.all()
	return dict(category_sidebar=category_sidebar)

@app.route('/')
def index():
	items = Item.query.all()
	return render_template('index.html', items=items) 

@app.route('/category')
def category_index():
	categories = Category.query.all()
	return render_template('categories.html', categories=categories)

@app.route('/category/<category_name>')
def category(category_name):
	category = Category.query.filter_by(slug_name=category_name).first_or_404()
	items = category.items
	return render_template('category.html', category=category, items=items)

@app.route('/item')
def item_index():
	categories = Category.query.all()
	return render_template('items.html', categories=categories)

@app.route('/item/<item_name>')
def item(item_name):
	item = Item.query.filter_by(slug_name=item_name).first_or_404()
	return render_template('item.html', )