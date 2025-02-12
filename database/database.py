#(©)CodeXBotz
#recoded by @Its_Oreki_Hotarou


import pymongo
import asyncio
from config import DB_URI, DB_NAME, FORCE_CHANNEL, FORCE_CHANNEL2

# Connect to MongoDB and select database
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

# Define collections for user and admin data
user_data = database['users']
admin_data = database['admins']
channel_data = database['channels']
channel_data2 = database['channels2']

# Function to check if a user exists
async def present_user(user_id: int):
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, user_data.find_one, {'_id': user_id})
    return bool(found)

# Function to add a new user
async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

# Function to retrieve all users
async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
    return user_ids

# Function to delete a user
async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

# Function to check if an admin exists
async def present_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, admin_data.find_one, {'_id': admin_id})
    return bool(found)

# Function to add a new admin
async def add_admin(admin_id: int):
    admin_data.insert_one({'_id': admin_id})
    return

# Function to retrieve all admins
async def full_adminbase():
    admin_docs = admin_data.find()
    admin_ids = []
    for doc in admin_docs:
        admin_ids.append(doc['_id'])
    return admin_ids

# Function to delete an admin
async def del_admin(admin_id: int):
    admin_data.delete_one({'_id': admin_id})
    return


    
# Function to check if a channel exists
async def present_channel():
    try:
        config = channel_data.find_one({})
        return config.get('force_sub_channel_1', FORCE_CHANNEL)
    except Exception as e:
        print(f"Failed to get force subscribe channels: {e}")
        return FORCE_CHANNEL

async def add_1(channel1: int):
    try:
        await channel_data.update_one({}, {'$set': {'force_sub_channel_1': channel1}}, upsert=True)
        print(f"Force subscribe channel 1 set successfully: {channel1}")
    except Exception as e:
        print(f"Failed to set force subscribe channel 1: {e}")


# Function to check if a channel exists
async def present_channel2():
    try:
        config = channel_data2.find_one({})
        return config.get('force_sub_channel_2', FORCE_CHANNEL2)
    except Exception as e:
        print(f"Failed to get force subscribe channels: {e}")
        return FORCE_CHANNEL2

async def add_2(channel1: int):
    try:
        await channel_data2.update_one({}, {'$set': {'force_sub_channel_2': channel1}}, upsert=True)
        print(f"Force subscribe channel 2 set successfully: {channel1}")
    except Exception as e:
        print(f"Failed to set force subscribe channel 1: {e}")
        

