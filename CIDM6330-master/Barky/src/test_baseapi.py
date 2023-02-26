from abc import ABC, abstractmethod
from barkylib.api.baseapi import AbstractBookMarkAPI
def test_AbstractBookMarkAPI():
    class TestBookMarkAPI(AbstractBookMarkAPI):
        def one(self, id):
            return {"id": id}

        def first(self, property, value):
            return {"property": property, "value": value}

        def many(self, property, value, sort):
            return {"property": property, "value": value, "sort": sort}

        def add(self, bookmark):
            return {"bookmark": bookmark}

        def delete(self, bookmark):
            return {"bookmark": bookmark}

        def update(self, bookmark):
            return {"bookmark": bookmark}

    bookmark_api = TestBookMarkAPI()

    # Test one method
    assert bookmark_api.one(1) == {"id": 1}

    # Test first method
    assert bookmark_api.first("url", "http://www.google.com") == {"property": "url", "value": "http://www.google.com"}

    # Test many method
    assert bookmark_api.many("category", "python", "date_added") == {"property": "category", "value": "python", "sort": "date_added"}

    # Test add method
    assert bookmark_api.add("http://www.google.com") == {"bookmark": "http://www.google.com"}

    # Test delete method
    assert bookmark_api.delete("http://www.google.com") == {"bookmark": "http://www.google.com"}

    # Test update method
    assert bookmark_api.update("http://www.google.com") == {"bookmark": "http://www.google.com"}
