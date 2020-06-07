from .models import Gist

def search_gists(db_connection, **kwargs):
    result = []
    if github_id is None and created_at is None:
        query = 'select * from gists'
    elif github_id is not None and created_at is None:
        query = 'select * from gists where github_id = :github_id'
    elif github_id is not None and created_at is not None:
        query = 'select * from gists where github_id = :github_id and created_at = :created_at'
    else:
        query = 'select * from gists where created_at = :created_at'
        
     cursor = db_connect.execute(query)
     for g in cursor.fetchall():
       result.append(g)
    
     return(result)
