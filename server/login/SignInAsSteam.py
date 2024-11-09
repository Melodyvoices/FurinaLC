from limbus.requests import Cs, ReqSignInAsSteam
from limbus.responses import Sc, RspSignInAsSteam
from limbus.formats import UserAuthFormat, AccountInfoFormat
from database.user import check_user
from utils import get_date_time


async def handle(req: Cs[ReqSignInAsSteam]):
    token = bytes.fromhex(req.parameters.steamToken).decode("utf-8")
    user_id = check_user(token, "steam")
    auth = UserAuthFormat(
        last_update_date=get_date_time(),
        last_login_date=get_date_time(),
        uid=user_id,
        public_id=user_id,
        data_version=16,
        db_id=0,
        auth_code="furinalc",
    )
    rsp = RspSignInAsSteam(
        userAuth=auth,
        accountInfo=AccountInfoFormat(uid=user_id),
        walletCurrency="IDR",
    )

    return Sc[RspSignInAsSteam](result=rsp)
