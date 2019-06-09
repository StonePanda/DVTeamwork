# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comments(models.Model):
    value = models.CharField(max_length=100, blank=True, null=True)
    useful_count = models.CharField(max_length=100, blank=True, null=True)
    authorname = models.CharField(max_length=100, blank=True, null=True)
    authoravatar = models.CharField(max_length=100, blank=True, null=True)
    subject_id = models.CharField(max_length=100)
    content = models.CharField(max_length=350, blank=True, null=True)
    created_at = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Keywords(models.Model):
    mvid = models.CharField(primary_key=True, max_length=10)
    stars = models.CharField(max_length=5)
    value = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'keywords'
        unique_together = (('mvid', 'stars', 'keyword', 'value'),)


class Keywords5(models.Model):
    mvid = models.CharField(primary_key=True, max_length=15)
    star_1_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_1 = models.CharField(max_length=10, blank=True, null=True)
    star_1_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_2 = models.CharField(max_length=10, blank=True, null=True)
    star_1_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_3 = models.CharField(max_length=10, blank=True, null=True)
    star_1_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_4 = models.CharField(max_length=10, blank=True, null=True)
    star_1_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_5 = models.CharField(max_length=10, blank=True, null=True)
    star_2_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_1 = models.CharField(max_length=10, blank=True, null=True)
    star_2_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_2 = models.CharField(max_length=10, blank=True, null=True)
    star_2_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_3 = models.CharField(max_length=10, blank=True, null=True)
    star_2_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_4 = models.CharField(max_length=10, blank=True, null=True)
    star_2_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_5 = models.CharField(max_length=10, blank=True, null=True)
    star_3_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_1 = models.CharField(max_length=10, blank=True, null=True)
    star_3_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_2 = models.CharField(max_length=10, blank=True, null=True)
    star_3_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_3 = models.CharField(max_length=10, blank=True, null=True)
    star_3_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_4 = models.CharField(max_length=10, blank=True, null=True)
    star_3_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_5 = models.CharField(max_length=10, blank=True, null=True)
    star_4_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_1 = models.CharField(max_length=10, blank=True, null=True)
    star_4_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_2 = models.CharField(max_length=10, blank=True, null=True)
    star_4_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_3 = models.CharField(max_length=10, blank=True, null=True)
    star_4_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_4 = models.CharField(max_length=10, blank=True, null=True)
    star_4_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_5 = models.CharField(max_length=10, blank=True, null=True)
    star_5_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_1 = models.CharField(max_length=10, blank=True, null=True)
    star_5_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_2 = models.CharField(max_length=10, blank=True, null=True)
    star_5_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_3 = models.CharField(max_length=10, blank=True, null=True)
    star_5_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_4 = models.CharField(max_length=10, blank=True, null=True)
    star_5_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_5 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords5'


class MvstarsCopy(models.Model):
    mvid = models.CharField(primary_key=True, max_length=100)
    number_1num = models.CharField(db_column='1num', max_length=100, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2num = models.CharField(db_column='2num', max_length=100, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3num = models.CharField(db_column='3num', max_length=100, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4num = models.CharField(db_column='4num', max_length=100, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5num = models.CharField(db_column='5num', max_length=100, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'mvstars_copy'


class Rankmovies(models.Model):
    rank = models.CharField(max_length=100, blank=True, null=True)
    cover_url = models.CharField(max_length=100, blank=True, null=True)
    mvid = models.CharField(primary_key=True, max_length=100)
    types1 = models.CharField(max_length=100, blank=True, null=True)
    regions = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.CharField(max_length=100, blank=True, null=True)
    vote_count = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=100, blank=True, null=True)
    types2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rankmovies'


class View1(models.Model):
    type = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    mvid = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'view_1'
        unique_together = (('mvid', 'type'),)


class View11(models.Model):
    type = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    mvid = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'view_1_1'
        unique_together = (('mvid', 'type'),)


class View12(models.Model):
    type = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    mvid = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'view_1_2'
        unique_together = (('mvid', 'type'),)


class View2(models.Model):
    mvid = models.CharField(primary_key=True, max_length=15)
    score = models.CharField(max_length=10)
    star_1 = models.CharField(max_length=10, blank=True, null=True)
    star_2 = models.CharField(max_length=10, blank=True, null=True)
    star_3 = models.CharField(max_length=10, blank=True, null=True)
    star_4 = models.CharField(max_length=10, blank=True, null=True)
    star_5 = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_1 = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_2 = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_3 = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_4 = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_5 = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_1 = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_2 = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_3 = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_4 = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_5 = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_1 = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_2 = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_3 = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_4 = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_5 = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_1 = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_2 = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_3 = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_4 = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_5 = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_1 = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_2 = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_3 = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_4 = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_5 = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_1_kw_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_2_kw_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_3_kw_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_4_kw_5_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_1_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_2_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_3_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_4_name = models.CharField(max_length=10, blank=True, null=True)
    star_5_kw_5_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_2'


class Yy(models.Model):
    url = models.CharField(max_length=100)
    mvid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yy'
        unique_together = (('mvid', 'url'),)


class Yyaward(models.Model):
    year = models.CharField(max_length=4)
    award = models.CharField(max_length=100)
    rurl = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'yyaward'
        unique_together = (('rurl', 'award', 'year'),)
