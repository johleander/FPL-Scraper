import os
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime

import config
from jsonParser import readFromJson

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']


def create_items(container):
    print('\nCreating Items\n')
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, f"./output")
    
    try:
        for filename in os.listdir(path):
            f = os.path.join(path,filename)
            if os.path.isfile(f):
                print(f)
                data = readFromJson(f)
                container.create_item(body=data)
                print('\nFinished\n' + data["id"])
    except:
        print("Error")



def read_item(container, id, iid):
    print('\nReading Item by Id\n')

    # We can do an efficient point read lookup on partition key and id
    response = container.read_item(item=id, partition_key=iid)

    print(response)

def read_items(container):
    print('\nReading all items in a container\n')

    # NOTE: Use MaxItemCount on Options to control how many items come back per trip to the server
    #       Important to handle throttles whenever you are doing operations such as this that might
    #       result in a 429 (throttled request)
    item_list = list(container.read_all_items(max_item_count=10))

    print('Found {0} items'.format(item_list.__len__()))

    for doc in item_list:
        print('Item Id: {0}'.format(doc.get('id')))


def query_items(container, account_number):
    print('\nQuerying for an  Item by Partition Key\n')

    # Including the partition key value of account_number in the WHERE filter results in a more efficient query
    items = list(container.query_items(
        query="SELECT * FROM r WHERE r.partitionKey=@account_number",
        parameters=[
            { "name":"@account_number", "value": account_number }
        ]
    ))

    print('Item queried by Partition Key {0}'.format(items[0].get("id")))


def replace_item(container, doc_id, account_number):
    print('\nReplace an Item\n')

    read_item = container.read_item(item=doc_id, partition_key=account_number)
    read_item['subtotal'] = read_item['subtotal'] + 1
    response = container.replace_item(item=read_item, body=read_item)

    print('Replaced Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))


def upsert_item(container, id):


    read_item = container.read_item(item=id, partition_key=id)
    read_item['subtotal'] = read_item['subtotal'] + 1
    response = container.upsert_item(body=read_item)

    print('Upserted Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))


def delete_item(container, id, iid):
    print('\nDeleting Item by Id\n')

    response = container.delete_item(item=id, partition_key=iid)

    print('Deleted item\'s Id is {0}'.format(id))



def setupOrAccessContainer():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="Football", user_agent_overwrite=True)
    try:
        # setup database for this sample
        try:
            db = client.create_database(id=DATABASE_ID)
            print('Database with id \'{0}\' created'.format(DATABASE_ID))

        except exceptions.CosmosResourceExistsError:
            db = client.get_database_client(DATABASE_ID)
            print('Database with id \'{0}\' was found'.format(DATABASE_ID))

        # setup container for this sample
        try:
            container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/id'))
            print('Container with id \'{0}\' created'.format(CONTAINER_ID))

        except exceptions.CosmosResourceExistsError:
            container = db.get_container_client(CONTAINER_ID)
            print('Container with id \'{0}\' was found'.format(CONTAINER_ID))
    except exceptions.CosmosHttpResponseError as e:
        print('\nrun_sample has caught an error. {0}'.format(e.message))

    finally:
            print("\nrun_sample done")

    return container

def run_sample():
   

        #scale_container(container)
        #create_items(container)
        read_item(container, 'SalesOrder1', 'Account1')
        read_items(container)
        query_items(container, 'Account1')
        replace_item(container, 'SalesOrder1', 'Account1')
        upsert_item(container, 'SalesOrder1', 'Account1')
        delete_item(container, 'SalesOrder1', 'Account1')

        # cleanup database after sample
        #try:
        #client.delete_database(db)

        #except exceptions.CosmosResourceNotFoundError:
        #    pass

    


if __name__ == '__main__':
    #run_sample()
    container = setupOrAccessContainer()
    #read_item(container, "159a0515-a1e2-4af4-a4a6-41dc021ddc03", "194634")
    #read_items(container)
    #delete_item(container, "159a0515-a1e2-4af4-a4a6-41dc021ddc03", "194634")
    create_items(container)
    
