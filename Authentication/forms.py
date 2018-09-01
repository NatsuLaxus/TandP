from django import forms 

branch_choices = (
        ('-','---SELECT---'),
        ('CSE','Computer Science & Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('MECH','Mechanical Engineering'),
        ('MME','Metallurgy Engineering'),
        ('CHE','Chemical Engineering'),
        ('CIVIL','Civil Engineering'),
        ('EEE','Electrical and Electronics Engineering'),
        ('BIO','Biotechnology'),
	)
course_choices = (
        ('BTech','B.Tech'),
        ('MTech','M.Tech'),
        ('MCA','MCA'),
        ('MBA','MBA'),
        ('PHD','Phd'),
    )

class UserRegistrationForm(forms.Form):

	username = forms.CharField(
		required = True,
		label = 'Username',
		max_length = 32,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	first_name = forms.CharField(
		required = True,
		label = 'First Name',
		max_length = 32,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	last_name = forms.CharField(
		required = True,
		label = 'Last Name',
		max_length = 32,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	email = forms.CharField(
		required = True,
		label = 'Email id',
		max_length = 32,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	contact = forms.CharField(
		required = True,
		label = 'contact',
		max_length = 100,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	regnum = forms.CharField(
		required = True,
		label = 'Registration number',
		max_length = 32,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	password = forms.CharField(
		required = True,
		label = 'password',
		max_length = 32,
		widget = forms.PasswordInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	cnfm_password = forms.CharField(
		required = True,
		label = 'Confirm Password',
		max_length = 32,
		widget = forms.PasswordInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	branch = forms.CharField(
		required = True,
		label = 'Branch',
		max_length = 32,
		
		widget = forms.Select(
			choices = branch_choices,
			attrs={
			"class": "form-control",
			}
		)
	)

	course = forms.CharField(
		required = True,
		label = 'Course',
		max_length = 32,
		
		widget = forms.Select(
			choices = course_choices,
			attrs={
			"class": "form-control",
			}
		)
	)

	def clean_cnfm_password(self):
		password = self.cleaned_data.get("password")
		pass2 = self.cleaned_data.get("cnfm_password")
		if password != pass2:
			raise forms.ValidationError("Passwords dont match!!")

		return password

class UserLoginForm(forms.Form):
	

	username = forms.CharField(
		max_length=100,
		label=' Username ',
		required = True,
		widget = forms.TextInput(
			attrs={
			"class": "form-control",
			}
		)
	)

	password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 100,
        widget = forms.PasswordInput(
            attrs={
            "class": "form-control",
            }
        )
    )

