from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.clint


def get_index(index_name = 'products'):
    client = get_client()
    index =client.init_index(index_name)
    
    
    return index

def perform_search (query , **kwargs):
    index = get_index()
    return index.search(query)