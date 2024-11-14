import hashlib
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from model.contact_model import ContactModel

class ContactService:
    def __init__(self, api_key, server_prefix):
        self.client = MailchimpMarketing.Client()
        self.client.set_config({
            "api_key": api_key,
            "server": server_prefix
        })

    def add_contact(self, list_id, contact: ContactModel):
        member_info = {
            "email_address": contact.email_address,
            "status": contact.status,
            "merge_fields": contact.merge_fields
        }
        try:
            response = self.client.lists.add_list_member(list_id, member_info)
            print("Contact added:", response)
            return response
        except ApiClientError as error:
            print("Error adding contact:", error.text)
            return None

    def check_subscription_status(self, list_id, email_address):
        member_email_hash = hashlib.md5(email_address.encode('utf-8').lower()).hexdigest()
        try:
            response = self.client.lists.get_list_member(list_id, member_email_hash)
            print("Subscription status:", response['status'])
            return response['status']
        except ApiClientError as error:
            print("Error checking subscription status:", error.text)
            return None

    def get_members_in_list(self, list_id):
        try:
            response = self.client.lists.get_list_members_info(list_id)
            print("Members in list:", response['members'])
            return response['members']
        except ApiClientError as error:
            print("Error retrieving members:", error.text)
            return None

    def tagged(self, list_id):
        members = self.get_members_in_list(list_id)
        if members:
            for member in members:
                email = member['email_address']
                if "interested" in email:
                    member_hash = hashlib.md5(email.encode('utf-8').lower()).hexdigest()
                    try:
                        tag_response = self.client.lists.update_list_member_tags(list_id, member_hash, {
                            "tags": [{"name": "interested", "status": "active"}]
                        })
                        print(f"Tag 'interested' added to {email}. Response: {tag_response}")
                    except ApiClientError as error:
                        print(f"Error tagging {email}: {error.text}")
