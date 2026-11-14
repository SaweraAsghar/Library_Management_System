from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.member import MemberCreate,MemberResponse, MemberUpdate
from app.crud.member import create_member,get_all_members,get_member_by_id,update_member,delete_member 


router = APIRouter(
    prefix="/member"
)

@router.get("/", response_model=list[MemberResponse])
def read_member(db:Session=Depends(get_db)):
    return get_all_members(db)

@router.get("/{member_id}", response_model=MemberResponse)
def read_member_by_id(member_id:int, db:Session=Depends(get_db)):
    member = get_member_by_id(db, member_id)
    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )
    return member

@router.post("/", response_model=MemberResponse)
def post_member_by_id(member:MemberCreate , db:Session=Depends(get_db)):
    return create_member(db, member)

@router.put("/{member_id}", response_model=MemberResponse)
def put_member(member_id:int,member_data:MemberUpdate ,db:Session=Depends(get_db)):
    member = update_member(db,member_data ,member_id)
    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )
    return member

@router.delete("/{member_id}")
def remove_member(member_id:int, db:Session=Depends(get_db)):
    member = get_member_by_id(db, member_id)
    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )
    result = delete_member(db, member_id)
    if not result:
        raise HTTPException(
            status_code= 400,
            detail="Cannot delete member because this member has borrowing history" )
    return {"message": "member deleted successfully"}
            