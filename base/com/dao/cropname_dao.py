from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.cropname_vo import CropNameVO


class CropNameDAO:
    def insert_crop_name(self, crop_name_vo):
        db.session.add(crop_name_vo)
        db.session.commit()

    def search_crop_name(self):
        croprequest_vo_list = db.session.query(CropNameVO, CropVO) \
            .join(CropVO, CropNameVO.crop_type_id == CropVO.crop_id) \
            .all()
        return croprequest_vo_list

    def delete_crop_name(self, crop_name_vo):
        crop_vo_list = CropNameVO.query.get(crop_name_vo.crop_name_id)
        db.session.delete(crop_vo_list)
        db.session.commit()

    def edit_crop_name(self, crop_name_vo):
        crop_vo_list = CropNameVO.query.filter_by(crop_name_id=crop_name_vo.crop_name_id).all()
        return crop_vo_list

    def update_crop_name(self, crop_vo):
        db.session.merge(crop_vo)
        db.session.commit()

    def view_ajax_cropname(self, cropname_vo):
        cropname_vo_list = CropNameVO.query.filter_by(
            crop_type_id=cropname_vo.crop_type_id).all()
        return cropname_vo_list
