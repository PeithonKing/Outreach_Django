
# Niser Outreach Page

A web page made with the help of python, Django, to be used by the Outreach Community of NISER.


## Author
* Aritra Mukhopadhyay
    * Email: [amukherjeeniser@gmail.com](mailto:amukherjeeniser@gmail.com)

  
## Installations
  *For actual server deployment, refer to [Django Documentation](https://docs.djangoproject.com/en/3.2/howto/deployment/).*
  
  Apart from that, for development purposes, to setup a local version we should do this:

**Step 1:** Install Python (make sure you have pip along with that)


**Step 2:** Make a Virtual Environment (if you don't have virtual environment library of python, do `pip install virtualenv`).\
Make a virtual environment with the command `virtualenv venv` and activate it with `.\venv\Scripts\activate`.

**Step 3:** Clone this repository:
```
git clone https://github.com/PeithonKing/Outreach_Django.git
```

**Step 4:**
* While still in the virtual environment, navigate to the cloned directory.
```
cd Outreach_Django
```

* Install Requirements
```
pip install -r requirements.txt
```

* Make the migrations and apply them:
```
python manage.py makemigrations
python manage.py migrate
```

* Create the Super-User:
```
python manage.py createsuperuser
```
This pas
Having a strong Password is highly recommended.\
(While deploying for the server, Provide this username and Password to the user, Outreach Committee)

* Populate the database:
```
python populate.py
```

* Run the server:
```
python manage.py runserver
```
# How To Use

1. The `static\gallery` folder contains all the actual images which will not go to the page.
The `static\sgallery` folder contains all the images which will be actually shown on the page. When someone clicks on this image, the actual image will be served from `static\gallery`.

2. **To add some new images or to remove images from the existing pages,** just keep/delete the image in appropriate place under the `static\gallery`. The image will automatically go to the appropriate place. Remember to keep/delete the reduced version of the same file **with the same name** in the `static\sgallery` folder.


    **Note:** Only file with the extensions `.jpg`, `.jepg`, `.png` and `.jfif` will be hosted on the page. If you have an image file with some different extensions they wont be shown. In such cases, there are two ways out:
    - Change the `images()` function in `main\views.py` file
    - Convert the file to any of the above extensions. Remember to change the file in both the `gallery` and `sgallery` folders. The filenames should be same including the **extension**.

3. **To make a new page:**
    - Make that page and keep it in appropriate places under the `templates` directory.
    - Have its URL listed in the `main\urls.py` file.
    - Write its view in the `main\views.py` file.

4. **To add new**
    - news,
    - webinars, 
    - or Student coordinators
        
        **or to edit them,** go to the admin section of the page.
