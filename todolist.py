# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def print_rows(rows_read):
    if not rows_read:
        print('Nothing to do!')
    else:
        count = 0
        for row in rows_read:
            count += 1
            print("{}. {}".format(count, row))


while True:
    option = int(input('''1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit'''))
    if option == 0:
        print()
        print()
        print('Bye!')
        break
    elif option == 1:
        print()
        print()
        today = datetime.today()
        print('Today: {} {}'.format(today.day, today.strftime('%b')))
        rows = session.query(Table).filter(Table.deadline
                                           == today.date()).all()
        print_rows(rows)
        print()
        print()
    elif option == 2:
        print()
        print()
        date = datetime.today()
        n = 0
        week = {0: 'Monday', 1: 'Tuesday',
                2: 'Wednesday', 3: 'Thursday',
                4: 'Friday', 5: 'Saturday',
                6: 'Sunday'}
        while n < 7:
            n += 1
            print('{}: {} {}'.format(week[date.weekday()],
                                     date.day, date.strftime('%b')))
            rows = session.query(Table).filter(Table.deadline
                                               == date.date()).all()
            print_rows(rows)
            date = date + timedelta(days=1)
            print()
            print()
    elif option == 3:
        print()
        print()
        print('All tasks:')
        rows = session.query(Table).order_by(Table.deadline).all()
        print_rows(rows)
        if not rows:
            print('Nothing to do!')
        else:
            count = 0
            for row in rows:
                current_row = rows[count]
                date = current_row.deadline
                count += 1
                print("{}. {}. {} {}".format(count, row,
                                             date.day, date.strftime('%b')))
        print()
        print()
    elif option == 4:
        print()
        print()
        print('Missed tasks:')
        rows = session.query(Table).filter(Table.deadline
                                           < datetime.today().
                                           date()).order_by\
            (Table.deadline).all()
        if not rows:
            print('Nothing is missed!')
        else:
            count = 0
            for row in rows:
                current_row = rows[count]
                date = current_row.deadline
                count += 1
                print("{}. {}. {} {}".format(count, row,
                                             date.day, date.strftime('%b')))
        print()
        print()
    elif option == 5:
        print()
        print()
        new_row = Table(task=input('Enter task'),
                        deadline=datetime.strptime(input('Enter deadline'), '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print('The task has been added!')
        print()
        print()
    elif option == 6:
        print()
        print()
        print('Choose the number of the task you want to delete:')
        rows = session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print('Nothing to delete')
        else:
            count = 0
            for row in rows:
                current_row = rows[count]
                date = current_row.deadline
                count += 1
                print("{}. {}. {} {}".format(count, row,
                                             date.day, date.strftime('%b')))
        session.delete(rows[int(input()) - 1])
        session.commit()
        print('The task has been deleted!')
        print()
        print()
