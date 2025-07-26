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
##### Create (Insert)
| Function                           | Description                                |
| ---------------------------------- | ------------------------------------------ |
| ```Model.objects.create()```       | Creates and saves a new                    |
| ```Model()` + `.save()```          | Instantiates and saves a model manually    |
| `Model.objects.get_or_create()`    | Gets an object or creates it if not exists |
| `Model.objects.update_or_create()` | Updates or creates an object in one call   |
| `Model.objects.bulk_create()`      | Creates many objects in one query          |

##### Read

| Function / Method             | Description                                  |
| ----------------------------- | -------------------------------------------- |
| `Model.objects.all()`         | Returns all objects                          |
| `Model.objects.filter()`      | Filters and returns matching objects         |
| `Model.objects.get()`         | Returns a single object (or error)           |
| `Model.objects.first()`       | Returns the first object (or None)           |
| `Model.objects.last()`        | Returns the last object (or None)            |
| `Model.objects.exclude()`     | Excludes objects from the result             |
| `Model.objects.count()`       | Counts total objects                         |
| `Model.objects.exists()`      | Checks if any object exists (True/False)     |
| `Model.objects.order_by()`    | Orders the QuerySet by given field(s)        |
| `Model.objects.values()`      | Returns QuerySet of dictionaries             |
| `Model.objects.values_list()` | Returns QuerySet of tuples                   |
| `Model.objects.distinct()`    | Removes duplicates from QuerySet             |
| `Model.objects.aggregate()`   | Returns summarized values (Count, Avg, etc.) |
| `Model.objects.annotate()`    | Adds calculated fields to each result        |
| `Model.objects.in_bulk()`     | Returns a dict of objects keyed by ID        |
| `Model.objects.raw()`         | Executes raw SQL and maps to model instances |
| `Model.objects.only()`        | Fetches only selected fields                 |
| `Model.objects.defer()`       | Defers selected fields (lazy load)           |
| `Model.objects.latest()`      | Returns latest object by date field          |
| `Model.objects.earliest()`    | Returns earliest object by date field        |

##### Update

| Function                             | Description                              |
| ------------------------------------ | ---------------------------------------- |
| `obj.save()`                         | Saves changes to a single object         |
| `Model.objects.filter(...).update()` | Bulk update matching objects             |
| `Model.objects.bulk_update()`        | Updates many model instances efficiently |
| `Model.objects.update_or_create()`   | Updates or creates object                |
| `Model.objects.get_or_update()`      | Updates or creates object                |

##### Delete

| Function                             | Description             |
| ------------------------------------ | ----------------------- |
| `obj.delete()`                       | Deletes a single object |
| `Model.objects.filter(...).delete()` | Bulk delete             |
| `Model.objects.all().delete()`       | Delete all objects      |
| `Model.objects.filter(...).delete()` | Delete matching objects |


