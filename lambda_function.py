import json
import boto3

def lambda_handler(event, context):
  sesClient = boto3.client("ses", region_name="us-east-1")

  emailResponse = sesClient.send_email(
      Destination = {
           "ToAddresses":[
               "arthisuresh0210@gmail.com"
           ],
      },
      Message={
          "Body":{
              "Text":{
                  "Data": "This is my first SES email!"
              }
          },
          "Subject":{
              "Data": "Email from my SES account"
          },
      },
      Source="arthisuresh0210@gmail.com"
      )
