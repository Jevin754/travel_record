# travel_record
A simple tool to record your footprint using Django and ClustrMaps

# Requirements
 1. [Django](https://www.djangoproject.com/)  
 Install:
 ```bash
 pip install Django
 ```
 2. [ClustrMaps](https://clustrmaps.com/)  
 Register an account on it. Then Choose `Get Map` to get your script.  
 NOTE: there are two types of scripts of ClustrMaps. But some ICPs only support the second type. So you have try it by youself.

# Install
1. 	Clone this repo to your server:
```bash
	git clone https://github.com/vra/travel_record.git
```
2.	Change the password and script:
   	Including the 7th line in login/views.py:
```bash
# file at REPO_ROOT/login/views.py, line 7
7  your_password = 'put_your_password_here' 
```
   	and 9th line in templates/success.html:
```bash
# file at  REPO_ROOT/templates/success.html, line 10
 9  <!-- put your script here!-->
 10 <!-- end of your script --> 
```
3. 	Run server like this:
```bash
python manage.py runserver 0.0.0.0:8000
```
  	Change the port to your target port.  
   	Then visit the id:port in a broswer, enter your password, and you will see your footprint.
