import requests
import sqllite3

def import_gists_to_database(db, username, commit=True):
    
    query = 'https://api.github.com/gists/{user}'.format(user = username)
    g = requests.get(query, verify=False)
    db_conn = sqlite3.connect('db')
    
    for resp in g.json():
        db_conn.executescript("""INSERT INTO gists (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url) VALUES (resp['id'], resp['url'], resp['git_pull_url'], resp['git_push_url'], resp['commits_url'], resp['forks_url'], resp['public'], resp['created_at'], resp['updated_at'],resp['comments'], resp['comments_url'])"")
        
    if commit:
        db_conn.commit()
                        
    
    
                    
