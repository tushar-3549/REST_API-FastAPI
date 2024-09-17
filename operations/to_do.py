
import sys
sys.path.append('./')

from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode


# create a todo
def create_to_do(todo: str) -> dict:
    try:
        req = Todo(todo)
        db_session.add(req)
        db_session.commit()
        return {
            'status': 'ok',
            'message': 'Created new todo'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

def get_all():
    try:
        res = db_session.query(Todo).all()
        docs = decode.decode_todos(res)
        return {
            'status': 'ok',
            'data': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# get one todo
def get_one(_id: int):
    try:
        res = db_session.query(Todo).filter_by(_id=_id).one_or_none()
        if res is not None:
            return {
                'status': 'ok',
                'data': decode.decode_todo(res)
            }
        else:
            return {
                'status': 'error',
                'message': f'Record with id {_id} not found.'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

# update todo
def update_todo(_id: int, title: str):
    try:
        # todo_item = db_session.query(Todo).filter_by(_id=_id).one_or_none()
        criteria = {'_id': _id}
        todo_item = db_session.query(Todo).filter_by(**criteria).one_or_none()

        if todo_item is not None:
            todo_item.todo = title
            db_session.commit()

            return {
                'status': 'ok',
                'message': f'Todo with id {_id} updated successfully.'
            }
        else:
            return {
                'status': 'error',
                'message': f'Todo with id {_id} not found.'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

#delete todo 
def delete_todo(_id: int):
    try:
        # todo_item = db_session.query(Todo).filter_by(_id=_id).one_or_none()
        criteria = {'_id': _id}
        todo_item = db_session.query(Todo).filter_by(**criteria).one_or_none()

        if todo_item is not None:
            db_session.delete(todo_item)
            db_session.commit()

            return {
                'status': 'ok',
                'message': f'Todo with id {_id} deleted successfully.'
            }
        else:
            return {
                'status': 'error',
                'message': f'Todo with id {_id} not found.'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }



# res = create_to_do("Creating JS course")
# res = create_to_do("Creating Python course")
# print(res)

# res = get_all()
# print(res)

# res = get_one(2)
# print(res)

# res = update_todo(1, "Updated JS course")
# print(res)

res = delete_todo(1)
print(res)
