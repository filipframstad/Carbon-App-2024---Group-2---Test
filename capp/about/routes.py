from flask import render_template, Blueprint

about=Blueprint('about',__name__)

@about.route('/about')
def about_home():
  return render_template('about.html')