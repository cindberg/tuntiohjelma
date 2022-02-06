from app import db


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
    


if __name__ == "__main__":

    # Aja tämä ohjelma ensin jotta voit luoda tietokantaan pöydät
    print("luo pöytiä...")
    db.create_all()
    print("tehty!")