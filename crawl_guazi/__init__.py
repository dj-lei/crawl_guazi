import re
import time
import json
import redis
import scrapy
import requests
import datetime
import pandas as pd
import codecs
from lxml import etree

from crawl_guazi import settings
from crawl_guazi.conf import global_settings as gl
from sqlalchemy import create_engine
from crawl_guazi.db import db_operate

import os
root_path = os.path.abspath(os.path.dirname(__file__))



