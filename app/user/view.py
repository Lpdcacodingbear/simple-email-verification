from app import app
from app import db
from flask import render_template
from app.user.models import User
from app.user.form import FormRegister

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
        
        send_mail(sender='Sender@domain.com',
                  recipients=['recipients@domain.com'],
                  subject='Activate your account',
                  template='author/mail/welcome',
                  mailtype='html',
                  user=user)

        return 'Check Your Email and Activate Your Account'
    return render_template('user/register.html', form=form)