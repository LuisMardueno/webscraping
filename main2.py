from bs4 import BeautifulSoup
import requests
import time

print('ingresa alguna habilidad con la que no estes familiarizado')
unfamiliar_skill = input('>')
print(f'filtrando: {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_= 'sim-posted').text
        if 'today' in publish_date:
            skills = job.find('span', class_='srp-skills').text.replace('  ','')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ','').replace('(More Jobs)', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Required Skill: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                print("archivo guardado")

if __name__ == '__main__':
    while True:
        find_jobs()
        print('waiting')
        time.sleep(600)

