import random
import requests
import json
import requests
from bs4 import BeautifulSoup
from bardapi import Bard
import bardapi
import psycopg2
import time
import os

positions = ["Software Engineer", "Front-End Developer", "Back-End Developer", "Data Scientist", "Data Engineer", "Cloud Developer", "IT Support", "Embedded Systems Engineer"]
email_endings = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@icloud.com']
company_list = ['Meta', 'Google', 'Dell', 'IBM', 'Amazon', 'Amazon Web Services', 'NASA', 'Sony', 'Activision', 'Electronic Arts', 'Oracle', 'Twitter', 'SpaceX', '3M', 'Siemens']

def execute_query():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="333666222",
        host="job-application-db-2.com3yqtc5f7q.eu-west-2.rds.amazonaws.com",
        port="5432",
        sslmode="require"
    )
    try:
        sql_query = submission_query
        cur = conn.cursor()
        cur.execute(sql_query, data)
        conn.commit()
        print("Successfuly submitted data to database.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("No success:", error)
    finally:
        if cur is not None:
            cur.close()

random_data_generator_url = "https://random-data-api.com/api/v2/users?size=1&is_xml=true"
response = requests.get(random_data_generator_url)
data = response.text
data = json.loads(data)

address_data_generator_url = "https://random-data-api.com/api/v2/addresses"
response = requests.get(address_data_generator_url)
address_data = response.text
address_data = json.loads(address_data)

#Name
full_name = data['first_name'] + " " + data['last_name']
first_name = data['first_name']
last_name = data['last_name']
print(full_name)

#Email
email = data['email'].split("@")
email_numbering = [str(random.randint(1, 1000)), ""]
email = email[0] + random.choice(email_numbering) + random.choice(email_endings)
dot_or_underscore = random.choice([0, 1])
if dot_or_underscore == 1:
    email = email.replace(".", "_")
print(email)

#Phone
phone_number = data['phone_number']
#phone_number = phone_number.replace(" ", "")
#phone_number = phone_number.replace(".", "")
#phone_number = phone_number.replace("-", "")
#phone_number = phone_number.replace("(", "")
#phone_number = phone_number.replace(")", "")
if phone_number.count("x") != 0:
    phone_number = phone_number.split("x", 1)[0]
print(phone_number)

#Address
address = address_data['street_address']
#address = address_data['street_address'] + ", " + address_data['city']

print(address)

#Country
country = address_data['country']
print(country)

#Poisition
position = random.choice(positions)
company = random.choice(company_list)

#years of experience
years_experience = random.choice(['1', '2', '3', '4', '5+'])

#Paragraph (Applicant details)
token = 'aAgzO4veR1jHt_gFqpwOz9Tkfz1aYc-iHSbmtSZRoIQWBQe_92MLw3tEQvZr8n8ENvi3ig.'
bard = Bard(token=token)
input = "write me a 80 word paragraph to describe your experiences of " + years_experience + "year(s) as a " + position + " at " + company + ""
paragraph = bard.get_answer(input)['content']
paragraph = paragraph.split('\n')[2]
print(paragraph)

#Expected salary
salary = random.randrange(50000, 80001, 500)
print(salary)

#Survey
survey_result = random.choice(['Facebook', 'LinkedIn', 'Glassdoor', 'Other'])
print(survey_result)

#Applied beofore
applied_before = random.choice([True, False])
print(applied_before)

submission_query = """INSERT INTO applicants (first_name, last_name, email, phone_number, address, country, position, years_experience, applicant_details, expected_salary, survey, applied_before) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
data = (first_name, last_name, email, phone_number, address, country, position, years_experience, paragraph, salary, survey_result, applied_before)

execute_query()
time.sleep(random.randint(60, 1800))

    
