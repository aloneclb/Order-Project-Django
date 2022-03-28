from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    # Profil için Urller
    # path("profile/", views.profile_view, name="profile"), # private profile
    # path("profile/edit/<int:id>", views.edit_profile, name="editprofile"), # Profil Editleme
    # path("profile/my/blog/<int:id>", views.my_blog_view, name="myblogs"), # Kullanıcının Yazdığı Bloglar
    # path("profile/change/password/<int:id>", views.change_password, name="password_change"), # Parola Değişikliği
    # path("profile/my/likes/post/<int:id>", views.my_likes_post, name="my_likes_post"), # Beğendiğim Postlar
    # path("profile/public/<int:id>", views.public_profile_view, name="public_profile"), # Public Profile
]
