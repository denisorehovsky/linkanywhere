import pytest

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_user__str__():
    user = f.UserFactory.create(username='userhere')
    assert user.__str__() == 'userhere'