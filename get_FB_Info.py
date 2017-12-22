import os
import json
import facebook
import requests

if __name__ == '__main__':
	token = os.environ.get("FACEBOOK_TEMP_TOKEN")

	# this will get the location of the user
	graph = facebook.GraphAPI(token)
	# profile = graph.get_object('me', fields='name, location{location}')
	# print(json.dumps(profile, indent=4))

	#this will get a list of friends who have agreed to allow access to the app
	# user = graph.get_object('me')
	# friends = graph.get_connections(user['id'], 'friends')
	# print(json.dumps(friends, indent=4))

	#get all posts
	# posts = graph.get_connections('me', 'posts') 
 
 #  	while True:  # keep paginating 
	#     try: 
	#      	with open('my_posts.json', 'a') as f: 
	#         	for post in posts['data']: 
	#           		f.write(json.dumps(post)+"\n") 
	#         # get next page 
	#         posts = requests.get(posts['paging']['next']).json() 
	#     except KeyError: 
	#       # no more pages, break the loop 
	#       	break 
	
	#get detailed information about posts
	
	all_fields = [ 
	    'message', 
	    'created_time', 
	    'description', 
	    'caption', 
	    'link', 
	    'place', 
	    'status_type' 
	  ] 
  	all_fields = ','.join(all_fields) 
 	posts = graph.get_connections('me', 'posts', fields=all_fields) 
 
  	while True:  
  		try: 
  			with open('my_posts2.json', 'a') as f: 
  				for post in posts['data']: 
  					f.write(json.dumps(post) + "\n")  
        			posts = requests.get(posts['paging']['next']).json() 
		except KeyError: 	 
			break

