from app import db
from app.models.User import User


db.create_all()
print('\n')


def add_user(name, pwd):
    try:
        user = User(username=name, password=pwd)
        db.session.add(user)
        db.session.commit()
        print("Add user (%s) success!!"%name)
    except Exception as e:
        print(e)
        print("Add user (%s) faild!!"%name)

def select_all(db_name):
    try:
        results = db_name.query.all()
        for item in results:
            print("username: {}\t password: {}".format(item.username, item.password))        
    except Exception as e:
        print(e)
        print("select_all user faild!!")

def select_user(name):
    try:
        results = User.query.filter_by(username=name).all()
        print(results)
        for item in results:
            print("username: {}\t password: {}".format(item.username, item.password))       
    except Exception as e:
        print(e)
        print("select_user faild!!")

def update_user(name, pwd):
    user = User.query.filter_by(username=name).first()
    user.password = pwd
    try:
        db.session.add(user)
        db.session.commit()
        print("Update user (%s) success!!"%name)            
    except Exception as e:
        print(e)
        print("Update user (%s) faild!!"%name)

def delete_user(name):
    user = User.query.filter_by(username=name).first()
    try:
        db.session.delete(user)
        db.session.commit()  
        print("delete user (%s) success!!"%name)       
    except Exception as e:
        raise e
        print("delete user (%s) faild!!"%name)
   

if __name__ == '__main__':
    name = "test"
    pwd  = "123456"
    # add_user(name, pwd)

    # select_all(User)
    # select_user("test")
    # update_user("test", pwd="test123456")
    # delete_user("test")
