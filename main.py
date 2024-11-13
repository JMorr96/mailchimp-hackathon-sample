from service.audience_service import AudienceService
from service.contact_service import ContactService
from service.lead_generator_service import LeadGeneratorService
from model.audience_model import AudienceModel

# Mailchimp API configuration
API_KEY = "YOUR_API_KEY"
SERVER_PREFIX = "YOUR_SERVER_PREFIX"

def main():
    # Initialize services
    audience_service = AudienceService(API_KEY, SERVER_PREFIX)
    contact_service = ContactService(API_KEY, SERVER_PREFIX)
    lead_generator = LeadGeneratorService()

    # Define the Afrotech Hackathon audience
    afrotech_audience = AudienceModel(
        name="Afrotech Hackathon - Houston",
        permission_reminder="You signed up for updates on our website",
        email_type_option=False,
        from_name="Mailchimp",
        from_email="freddie@mailchimp.com",
        subject="Afrotech Hackathon",
        language="EN_US",
        company="Mailchimp",
        address1="405 N Angier Ave NE",
        city="Atlanta",
        state="GA",
        zip="30308",
        country="US"
    )

    # Create audience and get the list ID
    list_id = audience_service.create_audience(afrotech_audience)
    if list_id:
        print(f"Audience created with list ID: {list_id}")

        # Add only InterestedMember to the audience
        interested_member = lead_generator.get_interested_member()
        if interested_member:
            print("Adding InterestedMember to the audience.")
            contact_service.add_contact(list_id, interested_member)
        else:
            print("InterestedMember not found.")

        # Check subscription status for all contacts
        for contact in lead_generator.get_contacts():
            status = contact_service.check_subscription_status(list_id, contact.email_address)
            print(f"Subscription status for {contact.email_address}: {status}")

if __name__ == "__main__":
    main()
