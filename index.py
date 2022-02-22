from app import db
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime


class Account(db.Model):
    # We always need an id
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    # A dessert comes with calories
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

    # Add this to the db
    db.session.add(account)

    # Saves changes to db
    db.session.commit()

    return account


class Calender(db.Model):
    __tablename__ = 'calender'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship("Account", backref="calender")
    planned_date = db.Column(DateTime)
    schedule_date = db.Column(DateTime(timezone=True), default=func.now())
    end_date = db.Column(DateTime)
    hours = db.Column(db.Text)
    task_name = db.Column(db.Text)
    task_description = db.Column(db.Text)

    def __init__(self, account_id, account, planned_date, schedule_date, end_date, hours, task_name, task_description):
        self.account_id = account_id
        self.account = account
        self.planned_date = planned_date
        self.schedule_date = schedule_date
        self.end_date = end_date
        self.hours = hours
        self.task_name = task_name
        self.task_description = task_description

    def __str__(self):
        return self.task_name

    @staticmethod
    def create_account(account_id, account, planned_date, schedule_date, end_date, hours, task_name, task_description):
        calender = Calender(account_id, account, planned_date, schedule_date, end_date, hours, task_name,
                            task_description)

        # Adds to the db
        db.session.add(calender)

        # Save all changes to db
        db.session.commit()

        return calender


if __name__ == "__main__":

    # We should run this file directly to create the database tables
    print("Creating tables...")
    db.create_all()
    print("Done!")