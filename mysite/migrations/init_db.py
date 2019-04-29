# Generated by Django 2.1.3 on 2019-04-01 05:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mysite.models

def load_sql(filename):
    f = open(filename)
    sql_statements = f.read()
    f.close()
    return sql_statements

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True, null=True, verbose_name='username')),
                ('email', models.CharField(max_length=150, unique=True, null=True, verbose_name='email')),
                ('password', models.CharField(max_length=150, null=True, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('is_company', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', null=True, verbose_name='staff status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', null=True, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', null=True, verbose_name='active')),
                ('is_mail', models.BooleanField(default=False, null=True, verbose_name='mail status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, null=True, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('image', models.CharField(max_length=150, null=True, verbose_name='image')),
                ('fab_selection_id', models.CharField(max_length=45, null=True, verbose_name='fab selection id')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'mysite_user',
            },
            managers=[
                ('objects', mysite.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.IntegerField(null=True, verbose_name='company id')),
                ('customer', models.IntegerField(null=True, verbose_name='customer')),
                ('article_name', models.CharField(max_length=150, null=True, verbose_name='article name')),
                ('comments', models.CharField(max_length=150, null=True, verbose_name='comments')),
                ('article_image', models.CharField(max_length="255", null=True, verbose_name='article image')),
                ('room_images_id', models.CharField(max_length=150, null=True, verbose_name='room images id')),
                ('address_number', models.CharField(max_length=45, null=True, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=150, null=True, verbose_name='address')),
                ('rent', models.CharField(max_length=150, null=True, verbose_name='rent')),
                ('park', models.CharField(max_length=150, null=True, verbose_name='park')),
                ('initial_cost', models.CharField(max_length=150, null=True, verbose_name='initial cost')),
                ('floor_plan', models.CharField(max_length=150, null=True, verbose_name='floor plan')),
                ('common_service_expense', models.CharField(max_length=150, null=True, verbose_name='common service expense')),
                ('term_of_contract', models.CharField(max_length=150, null=True, verbose_name='term of contract')),
                ('floor_number', models.CharField(max_length=150, null=True, verbose_name='floor number')),
                ('column', models.TextField(null=True, verbose_name='column')),
                ('live_flag_id', models.CharField(max_length=45, null=True, verbose_name='live flag id')),
                ('map_url', models.TextField(null=True, verbose_name='map url')),
                ('map_url_air', models.TextField(null=True, verbose_name='map url air')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('published_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='published at')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Article_request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True, verbose_name='user_id')),
                ('article_image', models.CharField(max_length=255, null=True, verbose_name='建物イメージ画像')),
                ('article_name', models.CharField(max_length=45, null=True, verbose_name='建物名')),
                ('address', models.CharField(max_length=45, null=True, verbose_name='住所')),
                ('map', models.TextField(null=True, verbose_name='マップURL')),
                ('comments', models.CharField(max_length=255, null=True, verbose_name='その他')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'article_request',
            },
        ),
        migrations.CreateModel(
            name='ArticleFloor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('floor_id', models.CharField(max_length=45, null=True, verbose_name='floor id')),
            ],
            options={
                'db_table': 'sample_floor',
            },
        ),
        migrations.CreateModel(
            name='ArticleLive',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('article_id', models.IntegerField(null=True, verbose_name='article id')),
                ('vacancy_info', models.CharField(max_length=45, null=True, verbose_name='vacancy live')),
                ('vacancy_live', models.CharField(max_length=45, null=True, verbose_name='vacancy live')),
                ('start_date', models.CharField(max_length=45, null=True, verbose_name='start date')),
                ('update_date', models.CharField(max_length=45, null=True, verbose_name='update date')),
                ('cancel_date', models.CharField(max_length=45, null=True, verbose_name='cancel date')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'article live',
                'verbose_name_plural': 'article live',
                'db_table': 'article_live',
            },
        ),
        migrations.CreateModel(
            name='ArticleRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_id', models.CharField(max_length=45, null=True, verbose_name='room id')),
                ('room_live_id', models.CharField(max_length=45, null=True, verbose_name='room live id')),
            ],
            options={
                'db_table': 'sample_room',
            },
        ),
        migrations.CreateModel(
            name='Chat_room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.IntegerField(null=True, verbose_name='企業ID')),
                ('user_id', models.IntegerField(null=True, verbose_name='ユーザーID')),
                ('article_id', models.IntegerField(null=True, verbose_name='物件ID')),
                ('chat', models.CharField(max_length=255, null=True, verbose_name='メッセージ')),
                ('to_person', models.CharField(max_length=45, null=True, verbose_name='送信相手')),
                ('from_person', models.CharField(max_length=45, null=True, verbose_name='送信主')),
                ('img', models.CharField(max_length=255, null=True, verbose_name='アイコン')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'db_table': 'chat_room',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=255, null=True, verbose_name='ストライプID')),
                ('stripe_subscription_id', models.CharField(max_length=255, null=True, verbose_name='stripe_subscriotion_id')),
                ('plan_name', models.CharField(max_length=255, null=True, verbose_name='plan_name')),
                ('is_company', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', null=True, verbose_name='staff status')),
                ('user_id', models.IntegerField(null=True, verbose_name='user_id')),
                ('company_name', models.CharField(max_length=150, verbose_name='会社名')),
                ('address_number', models.CharField(max_length=45, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=150, verbose_name='住所')),
                ('update_count', models.CharField(max_length=45, null=True, verbose_name='免許更新回数')),
                ('license', models.CharField(max_length=45, unique=True, verbose_name='免許番号')),
                ('email', models.EmailField(max_length=45, null=True, verbose_name='Email')),
                ('web', models.CharField(max_length=45, null=True, verbose_name='Webサイト')),
                ('tel_number', models.CharField(max_length=150, null=True, verbose_name='電話番号')),
                ('company_image', models.TextField(null=True, verbose_name='イメージ画像')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'company',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Fab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('article_id', models.IntegerField(null=True)),
                ('flag', models.IntegerField(null=True)),
                ('message_send_flag', models.BooleanField(default=False, null=True,verbose_name='message send flag')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'fab',
                'verbose_name_plural': 'fab',
                'db_table': 'fab',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('license', models.CharField(max_length=45, null=True, verbose_name='免許番号')),
            ],
            options={
                'db_table': 'license',
            },
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(max_length=45, null=True, verbose_name='article id')),
                ('comment', models.CharField(max_length=150, null=True, verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'others',
                'verbose_name_plural': 'others',
                'db_table': 'others',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stripe_plan_id', models.CharField(max_length=255, null=True, verbose_name='stripe_plan_id')),
                ('product_name', models.CharField(max_length=255, null=True, verbose_name='サービス名')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='プラン名')),
                ('namespace', models.CharField(max_length=255, null=True, verbose_name='Namespace')),
                ('amount', models.IntegerField(null=True, verbose_name='プラン料金')),
                ('detail', models.CharField(max_length=255, null=True, verbose_name='プラン詳細')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, )),
            ],
            options={
                'db_table': 'plans',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(max_length=45, null=True, verbose_name='floor number')),
                ('image', models.TextField(null=True, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'images',
                'verbose_name_plural': 'images',
                'db_table': 'images',
            },
        ),

        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/article.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/company.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/article_live.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/images.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/license.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/user.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/plan.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/sample_floor.sql')),
        migrations.RunSQL(load_sql('/var/www/roomii/mysite/migrations/csv/sample_room.sql')),
    ]

