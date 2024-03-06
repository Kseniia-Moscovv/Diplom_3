import pytest

from client.user_client import UserClient
from model.user_model import User
from model.user_credentials_model import UserCredentials
from model.user_token import UserToken


@pytest.fixture(scope='function')
def prepare_user():
    user_client = UserClient()

    user_token = {}

    def _prepare_user(data: User, driver):
        nonlocal user_token

        user_client.create_user(data)
        (login_response, _) = user_client.login_user(UserCredentials(data.email, data.password))

        user_token = UserToken(login_response['accessToken'], login_response['refreshToken'])

        driver.execute_script(f'window.localStorage.setItem("accessToken", "{user_token.access}");')
        driver.execute_script(f'window.localStorage.setItem("refreshToken", "{user_token.refresh}");')

    yield _prepare_user

    user_client.delete_user(user_token)
