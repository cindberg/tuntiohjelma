from app import db
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime

class Account(db.Model):
    # id
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    # turhat asiat
    username = db.Column(db.String(100))
    password = db.Column(db.Text)
    roletype = db.Column(db.String(100))

    def __init__(self, username, password, roletype):
        self.username = username
        self.password = password
        self.roletype = roletype
    def __str__(self):
        return self.username
    
def create_account(new_username, new_password, new_roletype):

    account = Account(new_username, new_password, new_roletype)

    # lisäätään tämä tietokantaan
    db.session.add(account)

    # tallentaa kaikki muutokset
    db.session.commit()

    return account


if __name__ == "__main__":

    # Aja tämä ohjelma ensin jotta voit luoda tietokantaan pöydät
    print("luo pöytiä...")
    db.create_all()
    print("tehty!")