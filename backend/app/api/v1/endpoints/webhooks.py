from fastapi import APIRouter, Request, HTTPException, status
from svix.webhooks import Webhook, WebhookVerificationError
from app.core.config import settings
from app.db.session import AsyncSessionLocal
from app.models.user import User, UserRole
from app.schemas.user import UserCreate
from sqlalchemy.future import select
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/clerk", status_code=status.HTTP_200_OK)
async def clerk_webhook(request: Request):
    payload = await request.body()
    headers = request.headers
    svix_id = headers.get("svix-id")
    svix_timestamp = headers.get("svix-timestamp")
    svix_signature = headers.get("svix-signature")

    if not all([svix_id, svix_timestamp, svix_signature]):
        raise HTTPException(status_code=400, detail="Missing Svix headers")

    webhook = Webhook(settings.CLERK_WEBHOOK_SECRET)
    
    try:
        event = webhook.verify(payload, headers)
    except WebhookVerificationError:
        raise HTTPException(status_code=400, detail="Invalid Webhook Signature")

    event_type = event.get("type")
    data = event.get("data")

    if event_type == "user.created":
        async with AsyncSessionLocal() as session:
            # Check if user exists
            stmt = select(User).where(User.clerk_id == data["id"])
            result = await session.execute(stmt)
            existing_user = result.scalar_one_or_none()

            if not existing_user:
                email = data["email_addresses"][0]["email_address"]
                # Default role is student, logic can be enhanced
                new_user = User(
                    clerk_id=data["id"],
                    email=email,
                    role=UserRole.STUDENT.value
                )
                session.add(new_user)
                await session.commit()
                logger.info(f"Created user {data['id']} from webhook")
            else:
                logger.info(f"User {data['id']} already exists")
    
    return {"status": "ok"}
