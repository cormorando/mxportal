## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python >= 3.7
* Django >= 2.2
* Celery >= 4.3
* Elasticsearch Docker image == 5.5.3
* RabbitMQ Docker image >= 3.7

### Installing

Install dependencies

```
pip install -r requirements.txt
```

Create Facebook and Twitter apps for accounts purposes and fill in your credentials in mxportal/settings.py

```
# facebook
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

# twitter
SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''
```

### Running

Run Docker images

```
docker run -d -e RABBITMQ_DEFAULT_USER=rabbit -e RABBITMQ_DEFAULT_PASS=rabbit -p 5672:5672 rabbitmq
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:5.5.3
```

Run Celery

```
celery -A mxportal worker -l info
```

Run "dumb” SMTP server that receives the emails locally (if you want)

```
python -m smtpd -n -c DebuggingServer localhost:1025
```

Run the app

```
./mange.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Celery](http://www.celeryproject.org/)
* [Elasticsearch](https://www.elastic.co/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Django Suit](https://djangosuit.com/)
* [Django Compressor](https://django-compressor.readthedocs.io/en/stable/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
* [Django Meta](https://django-meta.readthedocs.io/en/latest/)
* [Django Impersonate](https://bitbucket.org/petersanchez/django-impersonate/src/default/)
* [Django Haystack](https://django-haystack.readthedocs.io/en/master/)
* [Django Widget Tweaks](https://github.com/jazzband/django-widget-tweaks)
* [Django Celery Email](https://github.com/pmclanahan/django-celery-email)
* [RAKE NLTK](https://github.com/csurfer/rake-nltk)

## Author

By **Konrad Pluta**, [@github](https://github.com/cormorando).

(Ends)
