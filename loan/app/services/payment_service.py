# from sqlalchemy import select
# from app.models.payment import Payment
#
#
# async def get_or_create_payment(db, payload):
#     q = await db.execute(select(Payment).where(Payment.idempotency_key == payload.idempotency_key))
#     existing = q.scalar_one_or_none()
#     if existing:
#         return existing
#
#     payment = Payment(**payload.model_dump())
#     db.add(payment)
#     await db.commit()
#     await db.refresh(payment)
#     return payment
