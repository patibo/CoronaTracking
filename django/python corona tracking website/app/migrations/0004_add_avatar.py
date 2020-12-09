

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_make_birthday_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
