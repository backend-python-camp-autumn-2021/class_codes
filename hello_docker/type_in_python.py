# generic type
# int
# str
# bool
# List Tuple Set Dict
from datetime import datetime
from typing import List, Tuple, Set, Dict, Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    is_active: Optional[bool] = NotImplemented
    created_time: datetime = datetime.now()


class Account:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self.is_active = is_active


def just_test(name: str, age: int, is_active: bool) -> str:
    if is_active:
        return name + str(age)
    else:
        return "404"


def just_test2(names: List[str]) -> None:
    for name in names:
        print(name.title())


def just_test3(name: str, age: int, is_active: Optional[bool] = None) -> str:
    return name + str(age)


def just_test4(account_obj: Account) -> str:
    return account_obj.name


def just_test5(user: User):
    return user.name


send_data = {
    "name": "ashkan",
    "age": [1, 2]
}

try:
    user = User(**send_data)
    print(user.name)
except ValueError as e:
    print(e.json())
