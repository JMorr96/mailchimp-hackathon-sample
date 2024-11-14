from model.contact_model import ContactModel

class LeadGeneratorService:
    def __init__(self):
        # Generate five contacts with sample data
        self.contacts = [
            ContactModel("prudence.mcvankab@jakt.com", "subscribed", "Prudence", "McVankab"),
            ContactModel("james.smith@jakt.com", "subscribed", "James", "Smith"),
            ContactModel("susan.lee@jakt.com", "subscribed", "Susan", "Lee"),
            ContactModel("michael.brown@jakt.com", "subscribed", "Michael", "Brown"),
            ContactModel("interested.member@jakt.com", "subscribed", "Interested", "Member")
        ]

    def get_contacts(self):
        return self.contacts

    def get_interested_member(self):
        # Return the designated contact for adding to the audience
        return next((contact for contact in self.contacts if contact.email_address == "interested.member@jakt.com"), None)
