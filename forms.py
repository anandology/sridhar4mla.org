from web import form

email_regex = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{1,4}'

stay_connected_form = form.Form(
    form.Textbox('name', form.notnull, size='16'),
    form.Textbox('email', form.notnull, form.regexp(email_regex, 'Please enter a valid email'), size='30'),
    form.Textbox('phone', form.notnull, form.regexp(r'^[0-9]{8,10}$', 'Please enter a valid phone number'), size='16'),
    form.Textbox('pin', form.notnull, size='16'),
    form.Checkbox('donate', form.notnull, size='16'),
    form.Textbox('donate_amt', form.notnull, size='16'),
    form.Checkbox('volunteer', form.notnull, size='16')
)