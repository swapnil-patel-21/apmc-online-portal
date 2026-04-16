from base import db


class VehicleVO(db.Model):
    __tablename__ = 'vehicle_table'
    vehicle_id = db.Column('vehicle_id', db.Integer, nullable=False, primary_key=True, autoincrement=True)
    vehicle_type = db.Column('vehicle_type', db.String(255), nullable=False)
    vehicle_number = db.Column('vehicle_number', db.String(255), nullable=False)
    vehicle_charge = db.Column('vehicle_charge', db.Integer, nullable=False)
    vehicle_image_name = db.Column('vehicle_image_name', db.String(100), nullable=False)
    vehicle_image_path = db.Column('vehicle_image_path', db.String(100), nullable=False)

    def as_dict(self):
        return {
            'vehicle_id': self.vehicle_id,
            'vehicle_type': self.vehicle_type,
            'vehicle_number': self.vehicle_number,
            'vehicle_charge': self.vehicle_charge,
            'vehicle_image_name': self.vehicle_image_name,
            'vehicle_image_path': self.vehicle_image_path
        }


# db.create_all()
