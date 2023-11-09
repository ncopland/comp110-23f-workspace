"""overload, union types, default parameters"""

class Message:
    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool) -> None:
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    
    def __mul__(self, factor: int) -> str:
        """multiplication operator overload"""
        o = self.content
        for x in range(1, factor):
            self.content += " " + o


msg: Message = Message("erin", "Great job!", False)
msg * 100
print(msg)