from bs4 import BeautifulSoup
import requests

urls = ['https://apps.grad.illinois.edu/fellowship-finder/?action=main.search&grp1=11&grp3=21&grp3=22&grp3=23&grp3=24&grp4=31&grp5=32&grp5=15&grp5=13&q=',
        'https://www.careeronestop.org/Toolkit/Training/find-scholarships.aspx?curPage=1&pagesize=500&studyLevelfilter=Graduate%20Degree&studyplacefilter=US&requiredafffilter=Native%20American',
        'https://www.careeronestop.org/Toolkit/Training/find-scholarships.aspx?curPage=1&pagesize=500&studyLevelfilter=Graduate%20Degree&studyplacefilter=US&requiredafffilter=African%20American',
        'https://www.careeronestop.org/Toolkit/Training/find-scholarships.aspx?curPage=1&pagesize=500&studyLevelfilter=Graduate%20Degree&studyplacefilter=US&requiredafffilter=Hispanic%20American',
        'https://www.careeronestop.org/Toolkit/Training/find-scholarships.aspx?curPage=1&pagesize=500&studyLevelfilter=Graduate%20Degree&studyplacefilter=US&requiredafffilter=Asian%20American',
        'https://www.careeronestop.org/Toolkit/Training/find-scholarships.aspx?curPage=1&pagesize=500&studyLevelfilter=Graduate%20Degree&studyplacefilter=US&requiredafffilter=Veteran']

keywords = ['black', 'African-American', 'gay', "Hispanic", "Latino", "Latinx", "Asian", "Native", "LGBT",
            "disabled", "women", "trans", "Hawaiian", "African-American women", "Hispanic women", "military", "veteran"]

for url in urls:

    req = requests.get(url)
    content = req.text
    soup = BeautifulSoup(content, 'html.parser')

    for keyword in keywords:

        matches = soup.find_all(string=lambda x: keyword in x)
        print(f'{len(matches)} instances of {keyword} found.')
