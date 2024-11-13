class AudienceModel:
    def __init__(self, name, permission_reminder, email_type_option, from_name, from_email, subject, language, company, address1, city, state, zip, country):
        self.name = name
        self.permission_reminder = permission_reminder
        self.email_type_option = email_type_option
        self.campaign_defaults = {
            "from_name": from_name,
            "from_email": from_email,
            "subject": subject,
            "language": language
        }
        self.contact = {
            "company": company,
            "address1": address1,
            "city": city,
            "state": state,
            "zip": zip,
            "country": country
        }
