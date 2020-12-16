# polls
### this is poll app from [django documentation tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) ###


#### Final goal:
+ to convert this app to an API using [Django Rest Framework](https://www.django-rest-framework.org/)


#### What I have done so far :
  + studied django tutorial docs and created the polls app
  + did [Django Rest Framework](https://www.django-rest-framework.org/) tutorial part 1 and got familiar with [Serialization](https://www.django-rest-framework.org/tutorial/1-serialization/)
  + mapped the structure of the serialization to the polls app, it current can show some data in json format on 'polls/api/' path
  + replaced generic views with viewsets
  
  
  
#### Todo:
  + because the viewsets replacement I blew up the html renderer, browsable api is now viewable at root address, but the Polls app html cannot be rendered
  . need to figure out how to unify them in the same url
