# Django CRUD API

This is a recruitment task, made after hours and in a hurry.
It's CRUD API in Django, using MySQL as a database.

To run the project simply copy the repository to your local machine, and then, inside the main project directory (DjangoApiWithDocker) type:

`docker-compose build`

and then:

`docker-compose up`

Then go to the browser and type 127.0.0.1:8000

---

Disclaimer:

There's a lof of things missing in this project. Some things may include (but may not be limited to):

1. Unit tests
2. Helper methods (for calling external API for example)
3. Validators should be extracted to another class
4. Enums for months
5. Would be nice if February coudn't have more than 29 days, other months's day limits should be taken into account as well
6. Deployment in the cloud
7. 500 return errors should be replaced with correct 4XX errors

I know what you might be thinking. Something like: "oh my god, this guy didn't even do the half of what we asked him to do"
And you'd be right. But it was a new framework for me and I had a lot of fun doing it and seeing how less complex it was from .NET Framework, and if I can do .NET, I can handle this, I think. 
