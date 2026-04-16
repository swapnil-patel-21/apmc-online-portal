from base import db
from base.com.vo.crop_vo import CropVO


class CropDAO:
    def insert_crop(self, crop_vo):
        db.session.add(crop_vo)
        db.session.commit()

    def search_crop(self):
        crop_vo_list = CropVO.query.all()
        return crop_vo_list

    def delete_crop(self, crop_vo):
        crop_vo_list = CropVO.query.get(crop_vo.crop_id)
        db.session.delete(crop_vo_list)
        db.session.commit()

    def edit_crop(self, crop_vo):
        crop_vo_list = CropVO.query.filter_by(crop_id=crop_vo.crop_id).all()
        return crop_vo_list

    def update_crop(self, crop_vo):
        db.session.merge(crop_vo)
        db.session.commit()
