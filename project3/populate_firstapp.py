import os
import random

import django
from faker import Faker

from firstapp.models import (
    Topic,
    Webpage,
    AccessRecord,
)

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project0.settings")
django.setup()


fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[
            0
        ]

        AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == "__main__":
    print("Start")
    populate(20)
    print("End")
