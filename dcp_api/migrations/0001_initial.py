# Generated by Django 3.0.3 on 2020-06-30 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_TimeStamp', models.DateTimeField()),
                ('CompaintDetail', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_name', models.CharField(max_length=64)),
                ('D_dob', models.DateField()),
                ('D_address', models.CharField(max_length=128)),
                ('D_email', models.EmailField(max_length=254)),
                ('D_mobile', models.CharField(max_length=10)),
                ('D_anniversary', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Treatment_Name', models.CharField(max_length=128)),
                ('Treatment_Amount', models.IntegerField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Name', models.CharField(max_length=64)),
                ('P_DOB', models.DateField()),
                ('P_Address', models.CharField(max_length=128)),
                ('P_Email', models.EmailField(max_length=254)),
                ('P_Mobile', models.CharField(max_length=10)),
                ('P_Religion', models.CharField(max_length=100)),
                ('P_Gender', models.CharField(max_length=64)),
                ('P_Family', models.CharField(max_length=200)),
                ('P_MaritalStatus', models.CharField(max_length=200)),
                ('P_Anniversary', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkDoneLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkDone_Time_Stamp', models.DateField()),
                ('Complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.Complaints')),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorProfile')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.PatientProfile')),
                ('Treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorSpecialization')),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Visit_Time_Stamp', models.DateField()),
                ('Details', models.CharField(max_length=1024)),
                ('Advice', models.CharField(max_length=1024)),
                ('Visit_Type', models.CharField(max_length=64)),
                ('Complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.Complaints')),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorProfile')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.PatientProfile')),
                ('Treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorSpecialization')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DrugName', models.CharField(max_length=64)),
                ('Duration', models.CharField(max_length=64)),
                ('Dose', models.CharField(max_length=64)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.PatientProfile')),
                ('Visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.Visits')),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_habbit', models.CharField(max_length=128)),
                ('P_level_of_higgins', models.CharField(max_length=64)),
                ('P_cosmetic_concern', models.CharField(max_length=128)),
                ('P_medical_history', models.CharField(max_length=1024)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.PatientProfile')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorClinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_Name', models.CharField(max_length=64)),
                ('C_Address', models.CharField(max_length=128)),
                ('C_PhoneNumber', models.CharField(max_length=10)),
                ('C_Google_url', models.CharField(max_length=64)),
                ('C_OpenTime', models.DateField()),
                ('C_Closing', models.DateField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorProfile')),
            ],
        ),
        migrations.AddField(
            model_name='complaints',
            name='Doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.DoctorProfile'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp_api.PatientProfile'),
        ),
    ]
