from app import app
from app import db
from flask import render_template
from app.user.models import User
from app.user.form import FormRegister
from app.sendmail import send_mail

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        token = user.create_confirm_token()
        
        send_mail(sender='Sender@domain.com',
                  recipients=['recipients@domain.com'],
                  subject='Activate your account',
                  template='author/mail/welcome',
                  mailtype='html',
                  user=user,
                  token=token)

        return 'Check Your Email and Activate Your Account'
    return render_template('user/register.html', form=form)

@app.route('/user_confirm/<token>')
def user_confirm(token):
    user = User()
    data = user.validate_confirm_token(token)
    if data:
        user = User.query.filter_by(id=data.get('user_id')).first()
        user.confirm = True
        db.session.add(user)
        db.session.commit()
        return 'Thands For Your Activate'
    else:
        return 'wrong token'