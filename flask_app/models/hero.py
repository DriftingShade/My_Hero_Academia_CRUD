from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class Hero:
    DB = "hero_db"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.quirk = data["quirk"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_hero(cls, data):
        query = """INSERT INTO heroes (first_name, last_name, quirk, age, created_at,
        updated_at) VALUES (%(first_name)s, %(last_name)s, %(quirk)s, %(age)s, NOW(),
        NOW())"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        pprint(results)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM heroes;"
        results = connectToMySQL(cls.DB).query_db(query)
        heroes = []
        for hero in results:
            heroes.append(cls(hero))
        return heroes

    @classmethod
    def get_hero_by_id(cls, data):
        query = """SELECT * FROM heroes where id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results[0]

    @classmethod
    def update(cls, data):
        query = """UPDATE heroes 
                SET first_name=%(first_name)s, last_name=%(last_name)s, quirk=%(quirk)s,
                age=%(age)s WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results

    @classmethod
    def delete(cls, data):
        query = """DELETE FROM heroes WHERE id = %(id)s"""
        connectToMySQL(cls.DB).query_db(query, data)
        return
