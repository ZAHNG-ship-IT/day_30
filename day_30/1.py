from pathlib import Path
import json
def greet_user():
    ##问候
    path = Path("user_name")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        user_name = input("请输入你的名字：")
        contents = json.dumps(user_name)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {user_name}!")

greet_user()

###成！！！功