# corewatch/mongo_config.py
import mongoengine

mongoengine.connect(
    db='corewatch_db',
    host='localhost',
    port=27017
)
