from src.database.core import db

async def exists(uid: int) -> bool:
    """Check for Existence"""
    return bool(await db.fetchone(db.select("1", "users", "uid = $1"), uid))


async def add(uid: int) -> None:
    """Add"""
    await db.execute(db.insert("users", "uid"), uid)


async def info(uid: int) -> dict:
    """Information"""
    return await db.fetchone(db.select("*", "users", "uid = $1"), uid)
