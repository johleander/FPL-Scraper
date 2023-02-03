import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://johleander-db.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'CegvJVmJlTJym9R1l802bUxFLFirPItKX3OeiR5zgefywYPQu5V3QgzGeF1UF9W1Ezfpp0mLYdHXfDra9OFA2A=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'FootballDB'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'FootballContainer'),
}