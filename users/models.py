from __voice.database import Model 
from sqlalchemy.orm import Mapped , mapped_column 
from sqlalchemy import String ,Integer , Boolean ,DateTime
import datetime 


# user table 
class User(Model):

    __tablename__ ="users"

    user_id :Mapped[str] = mapped_column(Integer ,primary_key=True)
    user_name :Mapped[str] = mapped_column(String(32),index=True) 
    user_reg_number:Mapped[str]= mapped_column(String(32),index=True)
    user_password : Mapped[str]= mapped_column(String(32),index=True) 

    is_admin : Mapped[bool] = mapped_column(Boolean, default=False)
    is_voter : Mapped[bool]  = mapped_column(Boolean , default=True) 
    created_at : Mapped[datetime.datetime] = mapped_column(DateTime) 
    
    def __rept__(self):
        return f"user {self.user_name} created at {self.created_at}"