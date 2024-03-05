from client.base_client import BaseClient
from constants.api_constants import UrlApiConstants
from model.user_credentials_model import UserCredentials
from model.user_model import User
from model.user_token import UserToken


class UserClient(BaseClient):
    def create_user(self, user: User):
        return self.post(f'{UrlApiConstants.USER_URL}/register', user.__dict__)

    def login_user(self, user_credentials: UserCredentials):
        return self.post(f'{UrlApiConstants.USER_URL}/login', user_credentials.__dict__)

    def delete_user(self, token: UserToken):
        return self.delete(url=f'{UrlApiConstants.USER_URL}/user', headers=token.to_dict())
