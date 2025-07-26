## 🟢 Model Relationships (OneToOne, ForeignKey, ManyToMany)
In Django, model relationships define how models (tables) connect to each other in a database.


## 🟢 Migrations and ORM
In this chapter, we will cover the basics of migrations and ORM (Object-Relational Mapping)
in Django. We will also cover how to use the ORM to interact with the database.
#### 1. Make changes in models.py
#### 2. Create migration files
```
python manage.py makemigrations
```
#### 3. Apply changes to the DB
```
python manage.py migrate
```

| Function                           | Description                                |
| ---------------------------------- | ------------------------------------------ |
| ```Model.objects.create()```       | Creates and saves a new                    |
| ```Model()` + `.save()```          | Instantiates and saves a model manually    |
| `Model.objects.get_or_create()`    | Gets an object or creates it if not exists |
| `Model.objects.update_or_create()` | Updates or creates an object in one call   |
| `Model.objects.bulk_create()`      | Creates many objects in one query          |
