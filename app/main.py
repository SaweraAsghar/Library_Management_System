from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from app.models.member import Member
from app.models.borrowing import Borrowing
from app.models.fine import Fine
from fastapi import FastAPI
from app.routers import book, author, member,borrowing,category,fine

from app.database import engine, Base

app = FastAPI()
app.include_router(book.router)
app.include_router(author.router)
app.include_router(member.router)
app.include_router(borrowing.router)
app.include_router(category.router)
app.include_router(fine.router)




Base.metadata.create_all(bind=engine)
