import os

import redis
import builtins
from dotenv import load_dotenv

load_dotenv()


class ServiceAsync:
    def __init__(self):
        builtins.unicode = str
        self.r = redis.Redis(host=os.environ['REDIS_HOST'], port=int(os.environ['REDIS_PORT']), decode_responses=True)

    def produce_simple_extract(self, _id_resume):
        self.r.publish('simple_extract_resume', _id_resume)

    def produce_bidding_extract(self, _id_temp_bidding):
        self.r.publish('extract_bidding', _id_temp_bidding)

    def produce_bidding_rational(self, _id_bidding):
        self.r.publish('rational_bidding', _id_bidding)
