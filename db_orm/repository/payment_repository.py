from TG_bot.db_orm.session import SessionLocal
from TG_bot.db_orm.models import Order


class PaymentRepository:
    def create_order(user_id: int, payment):
        session = SessionLocal()

        order = Order(
            user_id=user_id,
            telegram_payment_id=payment.telegram_payment_charge_id,
            amount=payment.total_amount,
            currency=payment.currency,
            status="paid"
        )

        session.add(order)
        session.commit()
        session.close()

    def has_active_payment(telegram_id: int) -> bool:
        session = SessionLocal()

        exists = (
                session.query(Order)
                .filter(
                    Order.user_id == telegram_id,
                    Order.status == "paid"
                )
                .first() is not None
        )

        session.close()
        return exists
