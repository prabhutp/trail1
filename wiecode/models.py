from django.db import models

# Create your models here.
class participants(models.Model):
    #teamNumber = models.IntegerField('teamNumber',unique=True,primary_key=True)
    # TeamNo = models.AutoField('TeamNo',null=False)
    # teamName = models.CharField('teamName',max_length=30,null=True)
    M1MailId = models.EmailField('M1MailId', max_length=30, primary_key=True)
    M1Name = models.CharField('M1Name', max_length=30, null=True)
    M1College = models.CharField('M1College', max_length=30, null=True)
    M1Phone = models.CharField('M1Phone', max_length=15, null=True)
    #M1Phone = models.ForeignKey(domains,null=True,max_length=15,blank=True,on_delete=models.SET_NULL)

    M2MailId = models.EmailField('M2MailId', max_length=30, null=True)
    M2Name = models.CharField('M2Name', max_length=30, null=True)
    M2College = models.CharField('M2College', max_length=30, null=True)
    M2Phone = models.CharField('M2Phone', max_length=15, null=True)

    M3MailId = models.EmailField('M3MailId', max_length=30, null=True)
    M3Name = models.CharField('M3Name', max_length=30, null=True)
    M3College = models.CharField('M3College', max_length=30, null=True)
    M3Phone = models.CharField('M3Phone', max_length=15, null=True)

    M4MailId = models.EmailField('M4MailId', max_length=20, null=True)
    M4Name = models.CharField('M4Name', max_length=30, null=True)
    M4College = models.CharField('M4College', max_length=30, null=True)
    M4Phone = models.CharField('M4Phone', max_length=15, null=True)

# class domains(models.Model):
#     ProjectNo = models.AutoField('ProjectNo',primary_key=True)
#     #M1MailId = models.ForeignKey(participants,max_length=30,null=True,on_delete=models.SET_NULL)
#     M1MailId = models.EmailField('M1MailId',max_length=30,null=True)
#     domainName = models.CharField('domainName',null=True,max_length=30)
#     abstract = models.FileField(upload_to="domain_abstracts",null=True,default=None)