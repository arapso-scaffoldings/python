import time
import random
import uuid
import json

available_event_types = ["WIN", "CLICK"]
available_campaign_ids = ["111", "222", "333", "444", "555"]
available_creative_ids = ["12" , "22", "32", "42", "52"]
available_device_categories = ["m", "d", "t"]


def event_type_gen():
    return random.choice(available_event_types)

def bid_id_gen():
    return str(uuid.uuid4())

def timestamp_gen():
    return int(time.time())

def campaign_id_gen():
    return random.choice(available_campaign_ids)

def creative_id_gen():
    return random.choice(available_creative_ids)

def device_category_gen():
    return random.choice(available_device_categories)

def device_id_gen():
    return str(uuid.uuid4())

def generate_event():
        temp = {"event": event_type_gen(),
            "ts": timestamp_gen(),
            "bidId": bid_id_gen(),
            "campaignId": campaign_id_gen(),
            "creativeId": creative_id_gen(),
            "bid": {"price": 3.183, "currency": "USD"},
            "deviceId": device_id_gen(),
            "device": {"category": device_category_gen()}}
        return json.dumps(temp, separators=(",",":"))

def event_content_gen(lines_no=10):
    for x in xrange(lines_no):
        yield generate_event()

if __name__ == "__main__":
    print str(generate_event())