from flask import render_template, redirect, url_for, request
from application import db, app, bcrypt
from application.models import Posts, Users, Products
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateStoreForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
      return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        password=hash_pw)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#posts
@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            title = form.title.data,
            content = form.content.data,
            author = current_user
 )
        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('post.html', title='Post', form=form)

@app.route('/home')
def home():
    postdata=Posts.query.all()
    return render_template('home.html', title='Home', form=postdata)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


#STORE____________________________________________________________________
#add
@app.route('/store', methods=['GET', 'POST'])
@login_required
def store():
   form = UpdateStoreForm()
   if form.validate_on_submit():
       productcode = Products(productcode=form.productcode.data)
       productname = Products(productname=form.productname.data)
       productdescription = Products(productdescription=form.productdescription.data)
       price = Products(price=form.price.data)
       db.session.add(productcode, productname, productvendor, productdescription, price)
       db.session.commit()
       return render_template("store.html", title='store', form=form)

#update
@app.route('/store/update', methods=['GET', 'POST'])
@login_required
def store_update():
    form = UpdateStoreForm()
    if form.validate_on_submit():
        current_user.productname = form.productname.data
        current_user.productvendor = form.productvendor.data
        current_user.productdescription = form.productdescription.data
        current_user.price = form.price.data
        db.session.commit()
        return redirect(url_for('store'))
    elif request.method == 'GET':
        form.productname.data = current_user.productname
        form.productvendor.data = current_user.productvendor
        form.productdescription.data = current_user.productdescription
        form.price = current_user.price
    return render_template('store.html', title='Store', form=form)

#delete
@app.route('/store/delete', methods=["GET", "POST"])
@login_required
def store_delete():
    form = product()
    product = request.form.get("productname")
    product = products.query.filter_by(productcode=form).first()
    db.session.delete(product)
    db.session.commit()
    return render_template('store.html', title='store', form=form)


#ACCOUNT ___________________________________________________________


#update
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

#delete account
@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))



