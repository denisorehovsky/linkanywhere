import mock
import pytest
from nose.tools import eq_
from django_nose.tools import assert_queryset_equal

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_tag__str__():
    tag = f.TagFactory.create()
    eq_(tag.__str__(), tag.name)


def test_link__str__():
    user = f.LinkFactory.create()
    eq_(user.__str__(), '{0}: {1}'.format(user.title, user.url))


def test_link_relation_with_category():
    category_1 = f.CategoryFactory.create()
    link_1 = f.LinkFactory.create(category=category_1)
    link_2 = f.LinkFactory.create(category=category_1)

    eq_(link_1.category, category_1)
    eq_(link_2.category, category_1)


def test_link_and_tag_relation():
    tag_1 = f.TagFactory.create()
    tag_2 = f.TagFactory.create()
    link_1 = f.LinkFactory.create(tags=[tag_1, tag_2])
    link_2 = f.LinkFactory.create(tags=[tag_1])

    assert_queryset_equal(
        link_1.tags.all(),
        [repr(tag_1), repr(tag_2)],
        ordered=False
    )
    assert_queryset_equal(
        link_2.tags.all(),
        [repr(tag_1)],
        ordered=False
    )
    eq_(tag_1.links.count(), 2)
    eq_(tag_2.links.count(), 1)


def test_link_total_likes():
    link_1 = f.LinkFactory.create()
    with mock.patch('linkanywhere.apps.links.models.Link.likes') as likes_mock:
        link_1.total_likes
        likes_mock.count.assert_called()
