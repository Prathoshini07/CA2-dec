from flask import Flask,render_template,request
import requests

app=Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/getRecipe')
def get_recipe():
    
    url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

    querystring = {"prefix":"chicken soup"}

    headers = {
        "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    posts_data=response.json()
    if isinstance(posts_data,list):
        posts=posts_data
    elif isinstance(posts_data,dict) and 'results' in posts_data:
        posts=[posts_data['results']]
    else:
        posts=[]
    return render_template('getRecipe.html',posts=posts)

@app.route('/getRecipeList')
def get_recipe_list():
    url = "https://tasty.p.rapidapi.com/recipes/list"

    querystring = {"from":"0","size":"20","tags":"under_30_minutes"}

    headers = {
        "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
        "x-rapidapi-host": "tasty.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    posts_data=response.json()
    if isinstance(posts_data,list):
        posts=posts_data
    elif isinstance(posts_data,dict) and 'results' in posts_data:
        posts=[posts_data['results']]
    else:
        posts=[]
    return render_template('getRecipeList.html',posts=posts)

@app.route('/burgers')
def burgers():
    url = "https://burgers-hub.p.rapidapi.com/burgers"

    headers = {
        "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
        "x-rapidapi-host": "burgers-hub.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    posts_data=response.json()
    print(posts_data)
    if isinstance(posts_data,list):
        posts=posts_data
    elif isinstance(posts_data,dict) and 'results' in posts_data:
        posts=[posts_data['results']]
    else:
        posts=[]
    return render_template('burgers.html',posts=posts)

@app.route('/keto_diet')
def keto_diet():
    url = "https://keto-diet.p.rapidapi.com/"

    headers = {
        "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
        "x-rapidapi-host": "keto-diet.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    posts_data=response.json()
    print(posts_data)
    if isinstance(posts_data,list):
        posts=posts_data
    elif isinstance(posts_data,dict) and 'results' in posts_data:
        posts=[posts_data['results']]
    else:
        posts=[]
    return render_template('keto_diet.html',posts=posts)

@app.route('/get_recipe',methods=['POST','GET'])
def get_recipe1():
    import requests

    url = "https://ai-food-recipe-generator-api-custom-diet-quick-meals.p.rapidapi.com/generate"
    posts_data=[]
    posts=[]
    querystring = {"noqueue":"1"}
    if request.method=='POST':
        payload = {
            "ingredients": ["chicken", "rice", "pepper"],
            "dietary_restrictions": ["gluten_free"],
            "cuisine": request.form['cuisine'],
            "meal_type": request.form['mealtype'],
            "servings": 4,
            "lang": "en"
        }
        headers = {
            "x-rapidapi-key": "0744311d70mshf2a21dd15e4df85p10d75ejsn5eff9af59b2a",
            "x-rapidapi-host": "ai-food-recipe-generator-api-custom-diet-quick-meals.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers, params=querystring)
        posts_data=response.json()
        print(posts_data)
        if isinstance(posts_data,list):
            posts=posts_data
        elif isinstance(posts_data,dict) and 'result' in posts_data:
            posts=[posts_data['result']]
        else:
            posts=[]
    return render_template('get_recipe.html',posts=posts)


if __name__=="__main__":
    app.run(debug=True,port=5001)
