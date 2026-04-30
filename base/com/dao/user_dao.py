from base import db
from base.com.vo.user_vo import UserVO
from base.com.vo.login_vo import LoginVO


class UserDAO:
    def insert_user(self, register_vo):
        db.session.add(register_vo)
        db.session.commit()

    def search_user(self):
        user_vo_list = db.session.query(UserVO, LoginVO) \
            .join(LoginVO, UserVO.user_login_id == LoginVO.login_id) \
            .all()
        return user_vo_list

    # def edit_crop(self, crop_vo):
    #     crop_vo_list = CropVO.query.filter_by(crop_id=crop_vo.crop_id).all()
    #     return crop_vo_list
    #
    # def update_crop(self, crop_vo):
    #     db.session.merge(crop_vo)
    #     db.session.commit()

    def find_login_user_fname_lname(self, user_vo):
        user_vo_list = UserVO.query.filter_by(user_login_id=user_vo.user_login_id).all()
        login_user_fname_lname = f"{user_vo_list[0].user_firstname} {user_vo_list[0].user_lastname}"
        return login_user_fname_lname
