# College Cost API

College Cost is a College budgeting app. It helps students and parents
make responsible financial decisions on where to go to college. The users 
can see a detailed breakdown of how they are spending their money and see the 
full cost of the college. This app was built using React and Django REST to build the API.

## Here is a live demo of college cost 

<a href="https://youtu.be/8ouCEXQfreU" target="_blank"><img src="http://img.youtube.com/vi/8ouCEXQfreU/0.jpg" 
alt="College Cost Demo" width="500" height="280" border="10" /></a>

## Getting Started
Make sure you have Python 3.7 or greater installed.

Clone Client side application and follow instructions. [Here](https://github.com/mmcdevitt1997/collegecostclient)

Clone this repository down in desired location: 

```
git@github.com:mmcdevitt1997/capstonecollegecostapi.git
```

Enter these commands:

```
cd collegecostapi
python -m venv CollegeCostEnv
source ./CollegeCostEnv/bin/activate
```

Then run 

```
python manage.py makemigrations collegecost_api
python manage.py migrate
python manage.py runserver
```

Your sever for college cost is now active!

Run 

```
python manage.py runserver
```
Each time you run college cost 
