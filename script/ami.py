#!/usr/bin/python3.5
import os
import boto3
import traceback
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import getpass
import sys
email_id=input("Enter Sender's email address:")
password=getpass.getpass(prompt="Enter the password")
rec_email=input("Enter receiver's email address:")
email=smtplib.SMTP('smtp.gmail.com', 587)

older_age = datetime.datetime.now() - datetime.timedelta(days=30)
time_iso = older_age.isoformat()
print(time_iso)
client=boto3.client('ec2')
respone=client.describe_images(
    Filters=[{'Name':'tag:delete', 'Values':['yes']},
            {'Name':'description', 'Values':['I can be deleted']}
   ])

def send_mail(email_id,password,rec_email,email,subj):
    msg=MIMEMultipart()
    msg['From']=email_id
    msg['To']=rec_email
    msg['Subject']=subj
    body="""Hi Team,
          
 This mail is regarding to 30 days Older AMIs"""
    msg.attach(MIMEText(body, 'plain'))
    attachment=open("/tmp/ami.txt", "rb")
    att=MIMEBase('application', 'octet-stream')
    att.set_payload((attachment).read())
    att.add_header('Content-Disposition', 'attachment', filename='ami.txt')
    encoders.encode_base64(att)
    msg.attach(att)
    email.starttls()
    email.login(email_id,password)
    email.sendmail(email_id,rec_email,msg.as_string())

def ami_del(ami,email_id,password,rec_email,email):
    image_del=[]
    for data in ami["Images"]:
        image_created_time = data["CreationDate"]
        if image_created_time < time_iso:
            image_id=data["ImageId"]
            image_del.append(image_id)
            try: 
                resul=client.deregister_image(ImageId=image_id)
                sys.stdout=open("/tmp/ami.txt","a")
                print(f"AMI ID is :{image_id} and the response is: {resul['ResponseMetadata']['HTTPStatusCode']}")
                sys.stdout.close()
            except:
                err=str(traceback.format_exc()) 
                sys.stdout=open("/tmp/ami.txt","a")
                print(f"AMI ID is :{image_id} and the error is: {err}")
                sys.stdout.close()
                pass
    if len(image_del) > 0:
        subj="30 Days older AMI Deleted"
        send_mail(email_id,password,rec_email,email,subj) 


ami_del(respone,email_id,password,rec_email,email)

