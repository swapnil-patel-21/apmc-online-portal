from base import db
from base.com.vo.vehicle_vo import VehicleVO


class VehicleDAO:
    def insert_vehicle(self, vehicle_vo):
        db.session.add(vehicle_vo)
        db.session.commit()

    def search_vehicle(self):
        vehicle_vo_list = VehicleVO.query.all()
        return vehicle_vo_list

    def delete_vehicle(self, vehicle_id):
        vehicle_vo_list = VehicleVO.query.get(vehicle_id)
        db.session.delete(vehicle_vo_list)
        db.session.commit()
        return vehicle_vo_list

    def view_ajax_vehicle(self, vehicle_vo):
        vehicle_vo_list = VehicleVO.query.filter_by(
            vehicle_type=vehicle_vo.vehicle_type).all()
        return vehicle_vo_list
