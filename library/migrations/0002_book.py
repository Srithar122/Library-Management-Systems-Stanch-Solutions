from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),  # Adjusted max_length to 100
                ('isbn', models.PositiveIntegerField()),  # Removed default value for ISBN
                ('author', models.CharField(max_length=100)),  # Adjusted max_length to 100
                ('Average_Rating', models.FloatField()),  # Removed max_length for FloatField
                ('Number_of_Pages', models.PositiveIntegerField()),  # Removed default value for Number_of_Pages
                ('Ratings_Count', models.PositiveIntegerField()),  # Removed default value for Ratings_Count
                ('Text_Reviews_Count', models.PositiveIntegerField()),  # Removed default value for Text_Reviews_Count
                ('Language_Code', models.CharField(max_length=10)),  # Adjusted max_length to 10 for language code
                ('isbn13', models.PositiveIntegerField()),  # Removed default value for isbn13
                ('Book_ID', models.PositiveIntegerField()),  # Removed default value for Book_ID
                ('Publication_Date', models.DateField()),  # Changed to DateField for publication date
                ('publisher', models.CharField(max_length=100)),  # Adjusted max_length to 100
                ('category', models.CharField(choices=[
                    ('education', 'Education'),
                    ('entertainment', 'Entertainment'),
                    ('comics', 'Comics'),
                    ('biography', 'Biography'),  # Corrected 'Biographie' to 'Biography'
                    ('history', 'History')
                ], default='education', max_length=30)),
            ],
        ),
    ]
