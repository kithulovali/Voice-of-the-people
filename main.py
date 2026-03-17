from __voice.database import engine , Model 
from users.models import  User


def main():
    Model.metadata.create_all(engine)



if __name__ =="__main__" :
    main()