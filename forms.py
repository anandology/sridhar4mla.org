from web import form

email_regex = r'(|[\w\.-]+@[\w\.-]+\.[a-zA-Z]{1,4})'

def donation_check(i):
    if 'donate' in i:
        print i.donate, i.donate_amt
        return bool(i.donate_amt)
    return True

stay_connected_form = form.Form(
    form.Textbox('name', form.notnull, size='16'),
    form.Textbox('email', form.regexp(email_regex, 'Please enter a valid email'), size='30'),
    form.Textbox('phone', form.regexp(r'^(|[0-9]{8,10})$', 'Please enter a valid phone number'), size='16'),
    form.Textbox('pin', form.regexp(r'^(|[0-9]{6})$', 'Please enter a valid PIN'), size='16'),
    form.Checkbox('donate', size='16'),
    form.Textbox('donate_amt', form.regexp(r'^(|[0-9]{1,5})$', 'Please enter a valid amount'), size='16'),
    form.Checkbox('volunteer', size='16'),
    validators = [form.Validator("Please let us know your phone or e-mail.", lambda i: i.email or i.phone),
        form.Validator("Please let us know the amount that you'd like to donate.", donation_check)
    ]
)