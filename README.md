# Twitter(tweepy)_Airflow_Data_Engineering_Project

##### Description:
I used python program to collect the data from Twitter using Tweepy API and store it in an AWS S3 bucket. I also utilized Airflow to create an ETL pipeline that automated the process of collecting and storing data from Twitter.

##### I used the following Python libraries to build the application:

Tweepy - used to connect to Twitter API
S3fs - used to read and store data from S3 bucket
Pandas, JSON, Datetime - used for data manipulation and formatting
Airflow DAG, PythonOperator, Days_Ago - used to automate the ETL pipeline
To deploy the application, I created an EC2 instance on AWS and connected to it using SSH from the command line. Then, I created a storage bucket on S3 and an IAM role to access it. Finally, I executed the code on the Airflow server and stored the downloaded data from Twitter into the S3 bucket.

Tools/ Skills: Python, tweepy, pandas, Airflow, AWS - EC2, S3
