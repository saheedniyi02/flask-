from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,ValidationError,TextAreaField,SubmitField
from wtforms.validators import Length,Email,DataRequired,EqualTo
from flask_wtf.file import FileAllowed,FileField
from flask_login import current_user
from blog.models import User




class RegisterForm(FlaskForm):
	username=StringField("username",validators=[Length(min=3,max=15),DataRequired()])
	email=StringField("email",validators=[Length(min=7,max=40),DataRequired(),Email()])
	password=PasswordField("password",validators=[Length(min=6,max=15),DataRequired()])
	confirm_password=PasswordField("Confirm Password",validators=[Length(min=6,max=15),DataRequired(),EqualTo("password")])
	submit=SubmitField("Sign up")
	
	
	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("That email is taken!!! Kindly choose another one")
	
	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("That username is taken!!! Kindly choose another one")
			
			
class LoginForm(FlaskForm):
	username=StringField("Username",validators=[DataRequired(),Length(min=3,max=20)])
	password=PasswordField("password",validators=[DataRequired(),Length(min=6,max=15)])
	remember=BooleanField("remember me?")
	submit=SubmitField("Sign in")
	
	
class UpdateProfile(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=15)])
    picture=FileField("Profile Picture",validators=[FileAllowed(["png","jpg"])])
    email=StringField("email",validators=[Length(min=7,max=40),DataRequired()])
    information=TextAreaField("About me")
    twitter=StringField("Twitter username")
    linkedin=StringField("Linkedin username")
    instagram=StringField("Instagram username")
    submit=SubmitField("Update Profile")
    
    def validate_username(self,username):
    	if username.data!=current_user.username:
    		user=User.query.filter_by(username=username.data).first()
    		if user:
    			raise ValidationError("That username has been chosen, Kindly choose another one")
    		
    def validate_email(self,email):
    	if email.data!=current_user.email:
    		user=User.query.filter_by(email=email.data).first()
    		if user:
    			raise ValidationError("That Email has been chosen, Kindly choose another one")
    	
    	


class RequestResetForm(FlaskForm):
	email=StringField('email',validators=[DataRequired(),Email()])
	submit=SubmitField("Rquest Reset password")
	
	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		
		if not user:
			raise ValidationError("There is no account registered with this email, kindly check your email.")
	
	
class ResetPasswordForm(FlaskForm):
	password=PasswordField("the password",validators=[DataRequired()])
	confirm_password=PasswordField("the confirm password",validators=[DataRequired(),EqualTo("password")])
	submit=SubmitField("Reset password")
	

