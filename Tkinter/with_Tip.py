class CustomObject:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Entering the context for {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting the context for {self.name}")


# 使用 with 语句来管理 CustomObject 的上下文
with CustomObject("lys") as obj:
    print(f"Inside the context for {obj.name}")
