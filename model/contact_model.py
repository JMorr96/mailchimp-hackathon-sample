class ContactModel:
    def __init__(self, email_address, status, first_name, last_name):
        self.email_address = email_address
        self.status = status
        self.merge_fields = {
            "FNAME": first_name,
            "LNAME": last_name
        }
