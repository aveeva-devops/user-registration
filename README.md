# Use below commands if docker-compose setup gives trouble

$ virtualenv -p python3 venv
$ source venv/bin/activate

(venv)$ pip install Flask-PyMongo

(venv)$ python mongo-1.py

Ref: https://www.youtube.com/watch?v=DsgAuceHha4

Next steps:
1. Check if image inserted in database - via command line
2. Create endpoint to retrieve the image
3. Insert other data


Pardeeps-MBP:~ pardeepchahal$ docker ps 
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                    NAMES
406f1182accd   user-registration_web   "python registerUser…"   16 seconds ago   Up 15 seconds   0.0.0.0:5001->5001/tcp   user-registration_web_1
ae86b3895120   user-registration_db    "docker-entrypoint.s…"   2 days ago       Up 16 seconds   27017/tcp                user-registration_db_1
Pardeeps-MBP:~ pardeepchahal$ docker inspect user-registration_db_1 -f "{{json .NetworkSettings.Networks }}"
{"user-registration_default":{"IPAMConfig":null,"Links":null,"Aliases":["ae86b3895120","db"],"NetworkID":"c3f5a7695ea3b1524f943caae0c190f63d9123462a006a1df0cb792e1ecf0fa8","EndpointID":"6e779dc5f7d9c2217cfb915f633f7948dfd7502b0c31cf692cf8fd87125acc4a","Gateway":"172.19.0.1","IPAddress":"172.19.0.2","IPPrefixLen":16,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:13:00:02","DriverOpts":null}}
Pardeeps-MBP:~ pardeepchahal$ docker inspect user-registration_web_1 -f "{{json .NetworkSettings.Networks }}"
{"user-registration_default":{"IPAMConfig":null,"Links":["user-registration_db_1:db","user-registration_db_1:db_1","user-registration_db_1:user-registration_db_1"],"Aliases":["406f1182accd","web"],"NetworkID":"c3f5a7695ea3b1524f943caae0c190f63d9123462a006a1df0cb792e1ecf0fa8","EndpointID":"d22a0b58fa748a49394d23c3ee06d33202462436f6ea96267308e38f242b5606","Gateway":"172.19.0.1","IPAddress":"172.19.0.3","IPPrefixLen":16,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:13:00:03","DriverOpts":null}}
Pardeeps-MBP:~ pardeepchahal$ 