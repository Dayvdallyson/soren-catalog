from email.message import EmailMessage

class EmailBuilder:
  def __init__(self):
    self._message = EmailMessage()

  def from_(self, address: str) -> "EmailBuilder":
    self._message["From"] = address
    return self

  def to(self, address: str) -> "EmailBuilder":
    self._message["To"] = address
    return self

  def subject(self, text: str) -> "EmailBuilder":
    self._message["Subject"] = text
    return self

  def body(self, text: str) -> "EmailBuilder":
    self._message["Body"] = text
    return self

  def build(self) -> EmailMessage:
    return self._message
