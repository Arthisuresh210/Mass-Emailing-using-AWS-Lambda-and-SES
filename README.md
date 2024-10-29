# Mass-Emailing-using-AWS-Lambda-and-SES
Do you need a powerful yet cost-effective way to send bulk emails? Look no further than the dynamic duo of AWS Lambda and Simple Email Service (SES)! This guide will equip you with the knowledge to create a serverless mass emailing solution using these robust AWS services.
Get ready to:

Effortlessly send emails to a large audience without managing servers.
Scale seamlessly as your email volume grows.
Reduce costs compared to traditional email sending methods.

Let's dive in and explore how to leverage AWS Lambda and SES for your next mass email campaign!

Prerequisites:

An AWS account
Familiarity with AWS services like IAM, Lambda,SES and Cloud Watch

Architecture Diagram :

![image](https://github.com/user-attachments/assets/45de793b-32fc-49c2-9930-6f701cda33d0) 

1)AWS Lambda:AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers

2)CloudWatch:CloudWatch is a monitoring service that provides data and actionable insights for AWS resources

3)IAM Role: IAM (Identity and Access Management) is a service that helps you securely control access to AWS resources

4)Simple Email Service (SES): send transactional email, marketing messages, or any other type of high-quality content to your customers

Steps:

1. Creating IAM Role

In the AWS console search for IAM in the search bar and select the service
In that select roles and click on Create role
Select use cases as Lambda and click on next
In permission, policies choose CloudWatch full access and SES full access and then click on next
Give a suitable name for the role and click on Create role
The role will be created.

![image](https://github.com/user-attachments/assets/c89349f5-1c57-4fd2-89e2-a6f92bb8c1e3)
![image](https://github.com/user-attachments/assets/619ac5f8-91f7-43bd-886d-00950828a4e3)
![image](https://github.com/user-attachments/assets/13baea7a-aef5-4278-ac47-377382ea2863)

2.Creating Lambda Function

In the AWS console search for Lambda in the search bar and select the service.
Provide the name of the function.
In the position of runtime, we must choose the language that we want. Here, I am choosing Python 3.8 version.
Choose whether to create a new or existing role as the executing role in the following step. 
Rest everything. We can keep it optional
Select Create a Function.
![image](https://github.com/user-attachments/assets/c8a010ed-c4f1-470f-9365-5ff4ff0615fb)
![image](https://github.com/user-attachments/assets/5645a091-e5ed-43ba-9f13-2d701555ac56)
After creating Lambda Function, we need to write a Lambda code for sending the emails.
Before, that we need to assign IAM permissions 
Click on configuration 
![image](https://github.com/user-attachments/assets/6cb895bb-e97c-42e8-a67f-a4e220f0b84c)

Then, click on Role name site it will direct you to the IAM Roles
![image](https://github.com/user-attachments/assets/a52915a7-2ede-4cab-8a0c-50c625d51f3a)
Go to Add permissions and select Create incline policy
In the policy editor choose visual and select a service as SES
Add Sendmail, Sendbulkmail write actions to it
![image](https://github.com/user-attachments/assets/978086da-c650-4f88-af5f-29b54c8d784d)
Click on next and provide the name of policy and click on create policy
![image](https://github.com/user-attachments/assets/7fd6f01c-1598-4225-8f71-880e6fd9b8d3)

. Creating CloudWatch Events:

In the AWS console search for CloudWatch in the search bar and select the service.
In the left navigation pane, select Event in that select rules and then click on create rule.
Next, choose the schedule and click on the Cron expression to set it to a specific time.
Select add target and choose the lambda function I’m choosing the function that I already created in the previous phase.
Click on configure details.
Next, give a name to the rule and rest everything we can keep optional
Click on Create the rule.
![image](https://github.com/user-attachments/assets/e8f08a80-bc34-4a52-a872-a2305724ec38)

Creating identities in Simple Email Service(SES):

In the AWS console search for SES in the search bar and select the service.
In the left side, click on identities and create an identities
In identities details select Email address and provide a valid email -id
Click on create
![image](https://github.com/user-attachments/assets/be5583c9-4c98-4beb-b016-9142523701ac)
![image](https://github.com/user-attachments/assets/8cab6127-08b6-4f18-a49c-c15e3f423054)

Check your mail for the verification ,click on the link sent by Amazon Web Services so that your email id is verified

![image](https://github.com/user-attachments/assets/bf56a814-77c5-4036-89a4-423f2e862f37)
![image](https://github.com/user-attachments/assets/2fcb35f0-ff8d-40cd-bc15-d22059c3cfb9)
Code for Lambda function

Again ,In the AWS console search for Lambda in the search bar and select the service.
Click on the created lambda function, click on code source 
Click on test you will be seeing Configure test event select that and provide an event name and select save

![image](https://github.com/user-attachments/assets/d2de4543-0bf3-4c32-b8cd-1e4b462d09e5)
After creating your test event ,write a code for sending email in the lambda function
Now ,click on deploy and test your code ,if the code has no error then you will be receiving a mail.

![image](https://github.com/user-attachments/assets/c5a6f278-4dba-4393-b0a9-c20e44938a30)
![image](https://github.com/user-attachments/assets/036b003b-500a-4ffb-9d18-a3d728f2ebed)
![image](https://github.com/user-attachments/assets/c46d694b-cb7e-44a8-925e-ca3c6085669a)

Conclusion: Unleash the Power of Serverless Mass Emailing
By harnessing the combined power of AWS Lambda and SES, you've unlocked a world of possibilities for efficient and scalable mass emailing. This serverless approach offers significant advantages:

Reduced Costs: Pay only for the resources you use, eliminating the need for expensive server infrastructure.
Enhanced Scalability: Effortlessly handle high email volumes without worrying about server limitations.
Simplified Management: Focus on crafting compelling content and leave the complex email delivery process to AWS.


















