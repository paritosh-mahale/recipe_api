# Recipe Api

An rest api for managing your recipes. 
This application is build using Django

## API List
1) Register User
2) Login User
3) Create Recipe
4) Get recipe by id
5) Update recipe
6) Delete recipe
7) Get all recipes







### Register User: 

**Method** : POST

**URL** : /user/

**Body** : username, first_name, last_name, password



### Login User: 

**Method** : POST

**URL** : /user/login/

**Body** : username, password



### Create Recipe: 

**Method** : POST

**Header** : Token

**URL** : /recipe

**Body** : recipe_name, description, Image


### Get Recipe by id: 

**Method** : GET

**Header** : Token

**URL** : /recipe/<id>


### Update Recipe: 

**Method** : PUT

**Header** : Token

**URL** : /recipe/<id>

**Body** : recipe_name, description, Image


### Delete Recipe: 

**Method** : DELETE

**Header** : Token

**URL** : /recipe/<id>

**Body** : recipe_name, description, Image



### Get all Recipe: 

**Method** : GET

**Header** : Token

**URL** : /recipe/
