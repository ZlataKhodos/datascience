import os

username = 'zsuiqzjfnryfqt'
password = 'c15b2cf95d4adaf7477b92a3a51224ece7f0906d557f2bbd00c71226895040cb'
host = 'ec2-174-129-32-240.compute-1.amazonaws.com'
port = '5432'
database = 'dcku3qgnh2f0gf'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://zsuiqzjfnryfqt:c15b2cf95d4adaf7477b92a3a51224ece7f0906d557f2bbd00c71226895040cb@ec2-174-129-32-240.compute-1.amazonaws.com:5432/dcku3qgnh2f0gf')