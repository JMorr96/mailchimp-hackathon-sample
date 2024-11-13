import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from model.audience_model import AudienceModel

class AudienceService:
    def __init__(self, api_key, server_prefix):
        self.client = MailchimpMarketing.Client()
        self.client.set_config({
            "api_key": api_key,
            "server": server_prefix
        })

    def create_audience(self, audience: AudienceModel):
        body = {
            "name": audience.name,
            "permission_reminder": audience.permission_reminder,
            "email_type_option": audience.email_type_option,
            "campaign_defaults": audience.campaign_defaults,
            "contact": audience.contact
        }
        try:
            response = self.client.lists.create_list(body)
            print("Audience created:", response)
            return response['id']
        except ApiClientError as error:
            print("Error creating audience:", error.text)
            return None
