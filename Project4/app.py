from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tickers.html')
def getTicker():
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile-by-salesnavurl"

    querystring = {"linkedin_url":"https://www.linkedin.com/sales/lead/ACoAAABD0a4B2wblfHunfjGEN-uRLdg2MnWydmk,name,zofi","include_skills":"false","include_certifications":"false","include_publications":"false","include_honors":"false","include_volunteers":"false","include_projects":"false","include_patents":"false","include_courses":"false","include_organizations":"false"}

    headers = {
        "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
        "x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code==200:
        posts_data=response.json()
    else:
        posts_data=[]
    if isinstance(posts_data,list):
        posts=posts_data
    elif isinstance(posts_data,dict) and 'data' in posts_data:
        posts=[posts_data['data']]
    else:
        posts=[]
    return render_template('tickers.html',posts=posts)

@app.route("/profile.html",methods=['GET','POST'])
def profile():
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/google-full-profiles"
    posts=[]
    if request.method=='POST':
        payload = {
        "name": request.form['name'],
        "company_name": request.form['companyname'],
        "job_title": request.form['job_title'],
        "location": request.form['location'],
        "keywords": request.form['keywords'],
        "limit": request.form['limit']
        }
        headers = {
            "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
            "x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code==200:
            posts_data=response.json()
        else:
            print("Not fetched")
            posts_data=[]
        if isinstance(posts_data,list):
            posts=posts_data
        elif isinstance(posts_data,dict) and 'data' in posts_data:
            posts=[posts_data['data']]
        else:
            posts=[]
    return render_template('profile.html',posts=posts)
        
    
if __name__=="__main__":
    app.run(debug=True,port=5001)
