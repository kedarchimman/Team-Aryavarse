from sqlalchemy import text
from fastapi import HTTPException


def create_user_in_db(db, name, email, phone, keycloak_id, is_email_verified=False):
    try:
        print(f"\n📝 create_user_in_db: email={email}, phone={phone}, keycloak_id={keycloak_id}")

        db.execute(text("""
            INSERT INTO public.users (
                name, email, phone, user_type, keycloak_id, is_email_verified, is_deleted
            ) VALUES (
                :name, :email, :phone, :user_type, :keycloak_id, :is_email_verified, :is_deleted
            )
        """), {
            "name":              name,
            "email":             email,
            "phone":             phone,
            "user_type":         "customer",
            "keycloak_id":       keycloak_id,
            "is_email_verified": is_email_verified,
            "is_deleted":        False,
        })
        db.commit()

        result = db.execute(
            text("SELECT id, name, email, phone, keycloak_id, user_type, is_email_verified, created_at FROM public.users WHERE keycloak_id = :kid LIMIT 1"),
            {"kid": keycloak_id}
        ).fetchone()

        if not result:
            raise HTTPException(status_code=500, detail="User inserted but not retrievable")

        return _row_to_user(result)

    except HTTPException:
        raise
    except Exception as e:
        import traceback; traceback.print_exc()
        db.rollback()
        raise HTTPException(status_code=500, detail=f"DB insert error: {str(e)}")


def get_user_by_keycloak_id(db, keycloak_id: str):
    try:
        result = db.execute(
            text("SELECT id, name, email, phone, keycloak_id, user_type, is_email_verified, created_at FROM public.users WHERE keycloak_id = :kid LIMIT 1"),
            {"kid": keycloak_id}
        ).fetchone()
        return _row_to_user(result) if result else None
    except Exception as e:
        print(f"⚠️ get_user_by_keycloak_id error: {e}")
        return None


def get_user_by_phone(db, phone: str):
    """
    Used for phone-based login identifier resolution and forgot-password flow.
    """
    try:
        result = db.execute(
            text("SELECT id, name, email, phone, keycloak_id, user_type, is_email_verified, created_at FROM public.users WHERE phone = :phone AND is_deleted = FALSE LIMIT 1"),
            {"phone": phone}
        ).fetchone()
        return _row_to_user(result) if result else None
    except Exception as e:
        print(f"⚠️ get_user_by_phone error: {e}")
        return None


def get_user_by_email(db, email: str):
    try:
        result = db.execute(
            text("SELECT id, name, email, phone, keycloak_id, user_type, is_email_verified, created_at FROM public.users WHERE email = :email AND is_deleted = FALSE LIMIT 1"),
            {"email": email}
        ).fetchone()
        return _row_to_user(result) if result else None
    except Exception as e:
        print(f"⚠️ get_user_by_email error: {e}")
        return None


def _row_to_user(row):
    if not row:
        return None
    return User(
        id=row[0], name=row[1], email=row[2], phone=row[3],
        keycloak_id=row[4], user_type=row[5],
        is_email_verified=row[6], created_at=row[7],
    )


class User:
    def __init__(self, id, name, email, phone, keycloak_id,
                 user_type, is_email_verified, created_at):
        self.id               = id
        self.name             = name
        self.email            = email
        self.phone            = phone
        self.keycloak_id      = keycloak_id
        self.user_type        = user_type
        self.is_email_verified = is_email_verified
        self.created_at       = created_at

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"