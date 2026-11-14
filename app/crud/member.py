from sqlalchemy.orm import Session
from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate

def create_member(db:Session, member:MemberCreate):
    db_member = Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def get_all_members(db:Session):
    members = db.query(Member).all
    return members


def get_member_by_id(db:Session, member_id:int):
    member = db.query(Member).filter(Member.id == member_id).first()
    return member


def update_member(db:Session, member_id:int, member_data: MemberUpdate):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        return None
    update_data =member_data.model_dump(exclude_unset=True).items()
    for key, value in update_data:
        setattr(member, key, value)
    db.commit()
    db.refresh(member)
    return member


def delete_member(db:Session, member_id:int):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        return None

    if member.borrowings:
     return None
    
    db.delete(member)
    db.commit()
    return True