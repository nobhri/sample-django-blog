import pytest
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone
from django.urls import reverse


@pytest.fixture
def user_create():
    User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")


@pytest.mark.django_db
def test_user_count(user_create):
    assert User.objects.count() == 1


@pytest.fixture
def post_create():
    Post.objects.create(
        author=User.objects.get(username="john"),
        title="about guitar",
        text="I like playing the guitar",
        created_date=timezone.now(),
        published_date=timezone.now(),
    )


@pytest.mark.django_db
def test_post_count(user_create, post_create):
    # assert Post.was_published_recently() is True
    assert Post.objects.count() == 1


@pytest.mark.parametrize("view_name", ["post_list", "about", "music"])
@pytest.mark.django_db
def test_view(client, view_name):
    url = reverse(view_name)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_post_detail(user_create, post_create, client):
    post = Post.objects.get(title="about guitar")
    url = reverse("post_detail", kwargs={"pk": post.pk})
    response = client.get(url)
    assert response.status_code == 200
